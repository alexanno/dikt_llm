# dikt_llm

**dikt** (Norwegian: *poem*) + **llm** — an AI that writes random Norwegian poems and renders each one as a mathematical visualization.

→ **[View gallery](https://alexanno.github.io/dikt_llm)**

---

## How it works

Each run:
1. Prompts GPT-4o-mini to write a random Norwegian poem *and* Python code that mathematically represents it
2. Executes the generated code to produce a matplotlib plot
3. Saves the poem + visualization as a timestamped HTML/PNG pair in `dikt/`
4. Updates `dikt/registry.json` so the gallery can discover new entries

```
dikt/
  registry.json          ← index of all poems
  2025-03-20-19-44-09.html
  2025-03-20-19-44-09.png
  ...
index.html               ← GitHub Pages gallery
dikt_llm.ipynb           ← generation notebook
```

## Examples

**Frosken kvakker, himmelen lyser** — a frog's journey rendered as a sine wave riding a linear sky:

```
Frosken kvakker, himmelen lyser,
Hopp og plask, naturen fryser.
Fra dam til sky, veien er vid,
En iriserende reise, alltid strid.
```

**Langs en snirklete sti gikk en gammel maur** — an ant's winding path as a parametric Lissajous curve:

```
Langs en snirklete sti gikk en gammel maur,
som bar på en krumme fra gårsdagens bål.
Hver gang stien krummet og vred seg som et buet tau,
hvisket vinden hemmeligheter som kun naturen forstår.
```

## Setup

Requires an Azure OpenAI deployment. Copy `.env.example` to `.env` and fill in your credentials:

```
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_KEY=your-api-key
OPENAI_API_VERSION=2024-02-01
```

Install dependencies:

```bash
pip install openai python-dotenv matplotlib numpy
```

Then open and run `dikt_llm.ipynb`.

## GitHub Pages

The `index.html` gallery loads `dikt/registry.json` at runtime and fetches individual poems on demand — no build step required. Enable Pages on the `main` branch root to publish.

## License

MIT — Alexander Salveson Nossum, 2025
