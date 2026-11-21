---
title: "IonoPotok: Stations Within a Radius, Plots for Any Query, and the Hub on a Phone Screen"
project: ict_platform
pair: ict-stancii-grafiki
platform: Web
type: Technical breakdown
date: 2026-11-21
source_from: 9db5061ea92c753199a7ccd542c314ae1141ec8a
source_rev: ae9c38f928de8c490843624a122538551e65a198
lang: en
authors:
  - Nikita Konkin
summary: "A month of work on the things used every day. The offline stations map gains detailed outlines, regional borders and pinch zoom, and a radius can be drawn around a station to open data analysis for that area at once. Data analysis plots any query, the indexer shows the progress of a scan and the expected wait, the hub fits a phone screen, and AbsTEC results are removed in a way that can be undone. Along the way, a path escape out of the data folder and a dozen other bugs were closed."
image: /assets/ict_platform/stations-preview.png
translation_of: 2026-11-21-stancii-i-grafiki.md
links:
  repo: "https://github.com/nikita-konkin/ict-hub"
tags: [programming, python, web, ionosphere, gnss, security]
---

While the [native AbsolTEC and MapTEC converters]({% link _articles/ict_platform/2026-11-21-absoltec-maptec-en.md %}) were in the works, about twenty changes of another kind went into IonoPotok between 9 October and 6 November. They concern the things used every day: the stations map, data analysis, the indexer and the hub's shell itself.

## A stations map without internet

After the [move to OpenStreetMap]({% link _articles/ict_platform/2026-10-12-ict-karty-bystree-en.md %}), the outline map stayed as the option for working offline, but it looked bare: coarse Natural Earth outlines at 1:110 million and not a single name. It is now drawn from 1:50 million data kept in the hub itself, with first-level regional borders (for Russia, the federal subjects) and labels for the nearby regions. Borders and labels are picked by the visible area, and the contrast of land and borders is raised.

Pinch zoom on a trackpad had to be done separately too. Browsers on the WebKit engine report a pinch not as scrolling with Ctrl held, as the others do, but as special gesture events, and Plotly ignored them. The hub now handles those events itself, and both backgrounds gained "+" and "−" buttons.

The main addition is the radius. A station is picked from a list or by clicking its marker, and a circle of the given radius is drawn around it. The map frames the circle, the stations table gains a distance column, and the stations inside the radius are highlighted. A link under the map opens data analysis with that area already set.

{% include screen.html src="/assets/ict_platform/stations-radius-en.webp" wide=true width=1600 height=1942 caption="A radius around a station on the outline map. The stations are made up." alt="The Stations Map page on the outline background: on the left, the filters with centre station ST01, a radius of 150 km and the line “6 stations within 150 km of ST01” with an “Open in Data Analysis” link; on the right, sixteen made-up stations ST01–ST16 over the middle Volga region, regional borders and a circle around ST01; below, the stations table with a “Distance, km” column and the six stations inside the radius highlighted" %}

## Data analysis: areas, dates and plots

The data analysis section talks to a separate TEC statistics service. It now has a "Stations in an area" row: a station code or a "latitude, longitude" pair and a radius find the nearby stations, show the distance to each and the number of days with data, and select those that have data of the needed type. The same parameters can be passed in the page address, and the search then runs at once; that is how the link from the stations map works.

Range queries can now be set not only by year and day numbers but also by calendar dates, including across New Year. On switching, the dates are filled in from the chosen year and day numbers. New range queries cover raw TEC and AbsTEC values, satellites, station availability and the stations map.

{% include screen.html src="/assets/ict_platform/analysis-area-en.webp" wide=true width=922 height=1600 max=420 caption="Data analysis: a range by calendar dates and a search for stations in an area." alt="A query card in Data Analysis: Range by set to “Calendar dates” from 01/01/2026 to 01/01/2026, station st01, the found stations ticked in the stations list, and a “Stations in an area” row with st01, a radius of 150 and a “Find stations” button; below, the line “6 stations within 150 km of st01; 6 with data for this data type” and a table of six stations with distances from 0 to 114.8 km and the number of AbsolTEC and TEC days" %}

Every query whose result can be downloaded can now be viewed as a plot as well. For live answers from the service, the default axes are chosen from the data: empty metadata columns are skipped, and each metadata query gets a categorical axis of its own.

A familiar form bug turned up as well. The significance-level fields had `min="0.001"` and `step="0.01"`, so the browser considered the default value of 0.05 invalid and refused to submit the form. Last time the opacity field broke the same way. Numeric fields now use `step="any"`, and the server still checks the bounds.

## The indexer: scan progress and an honest station count

A full scan of a large data tree takes minutes, and all that time the lists of years, days and stations loaded slowly or came back empty with no explanation. The indexer now tracks running scans and records the duration of each one per data root. Every page of the hub shows a bar with the scan's progress, and the expected time comes from the previous scan of the same root. The page polls the state every 5 seconds while a scan runs and every 30 seconds otherwise. Scans shorter than 5 seconds are not shown, so cache refreshes do not make the bar flicker.

{% include screen.html src="/assets/ict_platform/indexer-progress-en.webp" wide=true width=1600 height=503 caption="The scan progress bar with the elapsed and expected time." alt="The top of the Indexed data page with a “Data index is updating” box: a note that year, day and station lists may load slowly or look incomplete until it finishes, the RINEX root demo-rescan, a progress bar and “5 s of about 10 s”" %}

The RINEX day listing counted the number of `.zip` archives as "stations". Stations that deliver hourly or session files produce many archives a day, so 1 January 2025 showed 2,398 stations instead of 224. The count is now of distinct four-character site codes, which begin both short file names and long RINEX 3 names. It is fixed on the stations map, in the indexed data section and on the TEC-Suite run page.

The indexer now skips damaged archives instead of abandoning the whole scan because of one. The geodetic height calculation no longer divides by the cosine of latitude, which broke at the pole.

## The hub on a phone screen

The hub had no layout for narrow screens: the 220-pixel side menu stayed in place, covering the page and the language and theme buttons. On screens narrower than 900 pixels the menu now slides off the edge and opens with a button, and it closes on the darkened backdrop, the Escape key or a link. Wide tables scroll inside their own block instead of widening the page. The language and theme buttons share one row, forms reflow by width, and the run panels stack on screens narrower than 700 pixels.

{% include screen.html src="/assets/ict_platform/phone-menu-en.webp" width=540 height=1169 max=300 caption="The open menu on a phone screen." alt="The hub on a phone screen: the side menu open over the darkened IonMaps page, with the Overview, Indexed roots and Converters sections and the admin user pinned at the bottom" %}

The menu also needed scrolling on short laptop screens. It took the full height of the window and ran past its bottom edge, taking the converter and administration sections with it. The menu is now as tall as the window, the logo and the user stay fixed, and only the list of sections scrolls.

## A removal that can be undone

An administrator can remove AbsTEC results for chosen stations, in both DAT and Parquet. The hub first shows which folders will be affected, then moves them to a `.ionflow-trash` folder inside the same data root. That frees no disk space, but a mistake can be fixed by moving the folders back. If a folder is mounted read-only, the hub explains this and suggests how to grant write access.

{% include screen.html src="/assets/ict_platform/trash-preview-en.webp" wide=true width=1600 height=814 caption="A preview of moving results to the trash. Synthetic data." alt="The Remove AbsTEC output data page: DAT and Parquet, year 2026, day 1, stations st01, st02 and st03; under the Preview selection button, the list “Folders to remove (6)” with the DAT and PARQUET folders of each station, a note that they will be moved to .ionflow-trash, and a Remove listed folders button" %}

## Bugs that stay invisible until they happen

- **An escape out of the data folder.** The TEC map took a station name as given, and a name like `../x` read Parquet files outside the data root. Only plain station codes are accepted now.
- **A job's event stream.** On reconnecting, the stream of an already finished job spun in a loop without waiting and blocked the server's event loop. It now sends "done" again and closes.
- **Dates and times.** Day 366 of a common year is now a 400 error rather than 1 January of the next year; snapshot times are accepted as "HH:MM" and range-checked; a deleted file of a finished animation is a 404, not a 500.
- **Feedback.** The XML export of feedback strips invalid characters: terminal colour codes made the file unreadable.
- **The stations map.** Indexer errors reach the page instead of turning into an empty "0 stations" map.
- **The browser console.** The Cross-Origin-Opener-Policy header is sent only over HTTPS, and map labels no longer request an icon from a third-party server: the hub serves its own transparent one.

Small things for daily work: a batch AbsTEC run can be limited to chosen stations, the log of a finished job opens again, and a dry run is off by default. The documentation gained Mermaid sequence diagrams: the life cycle of a converter job, browsing data through the indexer, and the snapshot and animation jobs of TEC maps.

## Conclusions

1. A wait without an explanation looks like a breakdown. A progress bar with an estimate from the previous run is cheap and settles the question.
2. Counting files is not counting objects. One station can produce dozens of archives a day, so the count has to be of site codes.
3. Any name from a request that becomes part of a file path must be checked against its expected form, or `../` leads outside the data.
4. The `min` and `step` attributes of a numeric field are enforced by the browser, not the server. A default value that is not a multiple of the step silently blocks the form.

## Availability

- Source code: [github.com/nikita-konkin/ict-hub](https://github.com/nikita-konkin/ict-hub)
