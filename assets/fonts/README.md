# Fonts

Self-hosted instead of loading from Google Fonts, so the first paint does not
wait on two extra third-party connections (`fonts.googleapis.com` for the
stylesheet, then `fonts.gstatic.com` for the files).

| Family  | Files | Notes |
| ------- | ----- | ----- |
| Manrope | `manrope-{cyrillic,cyrillic-ext,latin,latin-ext}.woff2` | Variable font, `wght` 200–800. One file per subset covers every weight. |
| Prata   | `prata-{cyrillic,cyrillic-ext,latin}.woff2` | Single weight (400). |

Only the Cyrillic and Latin subsets are kept — the Greek and Vietnamese subsets
Google also ships are not needed for a RU/EN site. Characters outside the
declared `unicode-range`s fall back to the system font, which is the same
behaviour the Google-hosted version had.

The `@font-face` rules live at the top of `assets/css/main.css` and use
stylesheet-relative `url("../fonts/…")` paths, so they keep working if
`baseurl` ever changes. `_layouts/default.html` preloads the two subsets the
current page's language actually needs.

## Updating

Fetch the current CSS with a modern browser User-Agent (Google serves `woff2`
only to browsers that support it), then download the URLs it lists:

    curl -A "Mozilla/5.0 ... Chrome/120 ..." \
      "https://fonts.googleapis.com/css2?family=Manrope:wght@400;600;700&display=swap"
    curl -A "Mozilla/5.0 ... Chrome/120 ..." \
      "https://fonts.googleapis.com/css2?family=Prata&display=swap"

Copy the `unicode-range` values across verbatim — they must match the subset
files or the browser will download a file and then find no glyphs in it.

## Licence

Both families are under the SIL Open Font License 1.1; the full texts are in
`OFL-Manrope.txt` and `OFL-Prata.txt`.

- Manrope — Copyright 2018 The Manrope Project Authors, https://github.com/sharanda/manrope
- Prata — Copyright 2011 The Prata Project Authors, https://github.com/cyrealtype/Prata
