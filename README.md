# UK TRE Glossary

[![Build](https://github.com/manics/uktre-glossary/actions/workflows/hugo.yaml/badge.svg)](https://github.com/manics/uktre-glossary/actions/workflows/hugo.yaml)

**⚠️⚠️⚠️⚠️⚠️ Under development ⚠️⚠️⚠️⚠️⚠️**

## How to modify the current glossary version

TODO: Define the YAML format.

## How to add a new version of the glossary

For example, to create `v1` of the glossary when `v0` already exists:

1. Add the new version of the glossary under `assets/`
2. Create a new directory `content/v1/`
3. Copy `content/v0/_index.md` and `content/v0/_content.gotmpl` to `content/v1`
4. Edit `content/v1/_index.md`: Change `glossary_yaml` to the filename of the new glossary version under `assets/`
5. Edit `content/v1/_content.gotmpl`: Change `$glossary_yaml` to the filename of the new glossary version under `assets/`
