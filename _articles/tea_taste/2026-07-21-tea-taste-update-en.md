---
title: "Tea Taste: VK login, a public feed, and an admin panel — a major update"
project: tea_taste
pair: tea-taste-update
platform: VK
type: Technical breakdown
date: 2026-07-21
lang: en
authors:
  - Nikita Konkin
summary: "A breakdown of a major Tea Taste (teaform.ru) update: VK ID sign-in, editable tastings, password recovery, a public feed with author profiles, in-app user feedback, and an admin panel on top of it."
translation_of: 2026-07-21-tea-taste-update.md
links:
  repo: "https://github.com/nikita-konkin/tea-taste-frontend"
tags: [programming, react, nodejs, express, mongodb, product]
featured: true
---

The first version of Tea Taste recorded brewing parameters and sensory ratings per infusion, but a lot around the record itself stayed unfinished: the only way in was an email and password, a saved tasting couldn't be corrected, and the public feed showed cards with no author on them. This update closes exactly those gaps and adds what a public-facing service can't do without for long — user feedback and tools for an administrator.

## Signing in with VK ID

Previously the only way into the service was email/password registration. The backend now implements a full `id.vk.com` OAuth 2.1 flow with PKCE: the server generates a verifier/challenge pair, sends the user to VK for authorization, exchanges the code for a token, and fetches the profile. If the `vkId` from the response is already linked to an account, the user signs in; if not, an account is created or linked to an existing one by email.

On the frontend this is a single receiving page (`VkAuthDone`): it waits for the backend to set the JWT cookie, confirms the profile with a `/profile` request, and does a full-page redirect into the app. A deliberately simple approach instead of a client-side VK SDK — all the OAuth logic stays on the server.

Alongside this, password recovery by email arrived (via `nodemailer`): the `/reset-password` page works in two modes — without a token it requests a reset link, with a token in the query string it accepts a new password.

## Editing a tasting

Before this update, a tasting could only be created and deleted — there was no way to fix a typo in a tea's name or adjust a rating. A new `FormEdit` component opens an already-saved form for editing and saves changes via a `PATCH` request against the same `sessionId`. On the backend this required splitting creation and update into separate, purpose-validated routes instead of the duplicated validation that used to live in `routes/teaforms.js`.

Entering sensory descriptors got an upgrade too: `DescriptorPicker` flattens the aroma-and-taste dictionary (category → subcategory → descriptor) into one searchable list and adds quick-pick chips for frequently used values — no need to walk to the bottom of the tree every time when the category alone is enough.

## The public feed

The section previously labeled "Blog" is now called "Feed" — a more accurate description of its content, which is a stream of published tastings, not editorial posts. A public card (`/blog/:sessionId`) now shows the author's name and avatar — on the backend, `GET /public-forms` started returning the owner's data alongside the tasting itself, not just the brewing parameters.

That required adding avatar uploads to the user model: an endpoint accepts a file via `multer`, caps it at two megabytes and an image MIME type, and serves it back as a plain link. The Profile section can now display and edit the avatar, name, occupation, and a short bio.

## Feedback and an admin panel

The service got an in-app feedback channel for the first time: a "Suggest an improvement" form in the side menu posts text into a new `suggestion` collection tied to its author. This replaces scattered direct messages with a single reviewable list.

Reviewing that list — and managing users — happens in a new admin panel. It adds an `admin` role to the user model and a set of endpoints gated by an `adminOnly` middleware: listing every account, changing a role, deleting a user along with their data, and viewing or deleting suggestions. On the frontend it's one page with a user list and suggestion cards — a dedicated interface becomes unavoidable once a service has users beyond its own author.

## Infrastructure

The update also touched what isn't visible from outside. Both repositories gained test suites (Jest and Supertest on the backend, Testing Library on the frontend) and GitHub Actions workflows that run them on every push. The legacy server-side rendering through `jade` templates was removed — the backend is now a clean API. Dependencies were updated (Express, Mongoose, JWT, Helmet), along with the Docker image configuration.

## Takeaway

If the first version of Tea Taste proved that a tasting could become structured data, this update turns the project into one used by more than its own author: passwordless sign-in, the ability to correct your own record, a public author profile next to each tasting, a feedback channel, and moderation on top of all of it.

- Repository (frontend): [github.com/nikita-konkin/tea-taste-frontend](https://github.com/nikita-konkin/tea-taste-frontend)
- Repository (API): [github.com/nikita-konkin/tea-taste-api](https://github.com/nikita-konkin/tea-taste-api)
- Service: [teaform.ru](https://teaform.ru)
