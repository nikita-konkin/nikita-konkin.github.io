---
title: "Tea Taste: eight hidden backend failures a code review turned up"
project: tea_taste
pair: tea-taste-stability
platform: Web
type: Technical breakdown
date: 2026-07-23
lang: en
authors:
  - Nikita Konkin
summary: "A walk through eight stability defects in the Tea Taste API found in a code review after the July release: a double HTTP server, errors that silently fell through past their handlers, an unreachable PATCH route, rate limiting made meaningless by the proxy, a real liveness probe, and secrets taken out of the image."
translation_of: 2026-07-23-tea-taste-stability.md
links:
  repo: "https://github.com/nikita-konkin/tea-taste-api"
tags: [programming, nodejs, express, mongodb, reliability, devops]
featured: true
---

The July release turned Tea Taste into a service used by more than its own author: VK sign-in, a public feed, feedback, an admin panel. But a service that runs unattended for weeks differs from a demo not by its feature list but by whether it survives the errors you don't see in a five-minute walkthrough. A code review of the backend — an Express app over MongoDB — found eight such spots. None of them add functionality; each is the line between "works on my machine" and "keeps working." Below they're grouped by what they teach.

## Two HTTP servers in one process

The app started twice. `bin/www`, the file the Express generator ships, brought up a server, and in parallel the same server was brought up by `app.js` — every process ended up with two listeners. The second instance held resources, duplicated lifecycle handlers, and produced failure modes that can't be reproduced predictably. The entrypoint is now a single `app.js` (which `npm start`, `npm run dev`, and the Docker `CMD` all run), and `bin/www` is gone.

## Errors that silently fell through

Two defects in error handling looked correct but didn't stop the request.

In `middlewares/auth.js` a `return` was missing before `next(error)`. An unauthenticated request got a 401 queued, but execution didn't halt and fell through into the private controller, which crashed on `req.user._id` because there was no user. The response was already on its way, and the handler ran anyway.

In `utils/getTeaDataBy.js` the `next` parameter was misspelled. Instead of being forwarded to the error handler, any DB error threw a `ReferenceError` on a name that didn't exist — the request hung with no response. In the same place `statusCode - 500` (subtraction) sat where `statusCode = 500` (assignment) belonged. Both are the same lesson: the error path existed but didn't actually end the request.

## Routes and queries that did nothing

`routes/teaforms.js` held three duplicate route registrations that made `patchTeaForm` unreachable: `PATCH /create-form/:sessionId` landed on an earlier, wrong handler and silently did nothing. That is exactly the update path the editable tastings from the July release depend on — the review made sure the PATCH truly reaches its handler rather than the shadow beneath it.

Alongside it, Mongoose `orFail` was misused in `utils/delAllDocsFromCollection.js` and `controllers/users.js`: the callbacks now return the error, as the API requires. And the duplicate-key check compared against the string `'DuplicateKey'` instead of Mongo's real error code `11000`, so a repeated email wasn't recognised as a duplicate and fell into the generic handler instead of a message the user could act on.

## Boundaries: rate limiting and trusting the proxy

Rate limiting was in place but meaningless. Behind the outer nginx, every request carried the proxy's IP rather than the client's, so the limiter saw one sender for everyone. Enabling `trust proxy` restored real client addresses; the general limit is 1000 requests per 15 minutes, and `/sign-in` and `/sign-up` get a strict 25 per 15 minutes, because those are the endpoints worth brute-forcing.

## Observability: /health, logs, and a secret check

`GET /health` now checks the MongoDB connection and returns 503 when the database is unreachable — an orchestrator or Docker healthcheck can use that signal to restart the container or route traffic away from it. Disconnect and reconnect logging was added, along with an `unhandledRejection` logger and a startup assertion that `JWT_SECRET` is set in production: the app fails immediately at boot rather than quietly breaking every login later.

## Build and secrets

The Docker side got tightened too. `.env` is no longer baked into the API image — the file is in `.dockerignore` and supplied via `env_file` at runtime, so the JWT secret stops leaking into image layers. Installs use `npm ci` instead of an ignored `--frozen-lockfile` flag, so the build is reproducible. Restart policies and healthchecks were added to compose. The frontend's `REACT_APP_API_URL` build arg is now actually declared and honoured, so the built image points at the right API instead of the default.

## Takeaway

None of this shows on screen, and all of it together is the difference between a demo and a service. The tests added with the July release (Jest and Supertest on the backend, Testing Library on the frontend, run in GitHub Actions on every push) now guard these exact regressions — the PATCH tasting update, for one, has a test of its own. Features make a product visible; changes like these make it something you can leave running.

- Repository (API): [github.com/nikita-konkin/tea-taste-api](https://github.com/nikita-konkin/tea-taste-api)
- Repository (frontend): [github.com/nikita-konkin/tea-taste-frontend](https://github.com/nikita-konkin/tea-taste-frontend)
- Service: [teaform.ru](https://teaform.ru)
