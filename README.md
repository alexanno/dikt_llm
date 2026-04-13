# dikt_llm

**dikt** (Norwegian: *poem*) + **llm** — an AI that writes random Norwegian poems and renders each one as a mathematical visualization.

→ **[View gallery](https://alexanno.github.io/dikt_llm)**

---

## How it works

Each run:
1. Generates a random Norwegian poem (phase 1)
2. Generates Python/matplotlib code from that poem (phase 2)
3. Executes the generated code locally to render the visualization
4. Saves the result in a timestamped run folder (HTML, PNG, and run metadata)
5. Updates that run folder's `registry.json`
6. Rebuilds `dikt/meta-registry.json` so the gallery can discover all run folders

The current notebook flow is Ollama-only for both phases. You can change models per phase (`POEM_MODEL`, `CODE_MODEL`) and endpoint settings via environment variables.

Note: older run folders may still contain historical outputs produced with other model setups.

```
dikt/
  meta-registry.json     ← index of all run folders + run registries
  gpt-4o-mini/
    registry.json
    2025-03-20-19-44-09.html
    2025-03-20-19-44-09.png
  run-2026-04-13-21-57-51/
    registry.json
    2026-04-13-22-01-28.html
    2026-04-13-22-01-28.png
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

Install dependencies:

```bash
pip install openai python-dotenv matplotlib numpy
```

Then open and run `dikt_llm.ipynb`.

If needed, configure Ollama endpoint/auth via `.env`:

```
OLLAMA_BASE_URL=http://localhost:11434/v1
OLLAMA_API_KEY=ollama
```

## GitHub Pages

The `index.html` gallery loads `dikt/meta-registry.json` and then fetches each run's `registry.json` at runtime.

Because GitHub Pages does not expose folder listings, rebuild `meta-registry.json` before publishing:

```bash
python scripts/generate_meta_registry.py
```

Then commit the updated `dikt/meta-registry.json` file and publish from `main` branch root.

## License

MIT — Alexander Salveson Nossum, 2025
