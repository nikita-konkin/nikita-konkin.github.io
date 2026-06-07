source "https://rubygems.org"

# Pins the local toolchain to the same stack GitHub Pages runs in production.
# The github-pages gem bundles jekyll-seo-tag, jekyll-sitemap and jekyll-feed,
# which are enabled through the `plugins:` list in _config.yml.
gem "github-pages", group: :jekyll_plugins

# Timezone data and file-watching support for Windows/JRuby local builds.
gem "tzinfo-data", platforms: [:mingw, :mswin, :x64_mingw, :jruby]
# wdm gives faster file-watching on Windows during `jekyll serve`, but the only
# published version (0.1.1) does not compile on Ruby 3.3+. It is optional —
# Jekyll falls back to polling — so it is left out to keep local installs working.
# gem "wdm", "~> 0.1.0", platforms: [:mingw, :mswin, :x64_mingw]
