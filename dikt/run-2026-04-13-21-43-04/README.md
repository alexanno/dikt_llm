# Run: 2026-04-13-21-43-04

## Configuration

| Setting | Value |
| --- | --- |
| Output directory | `dikt/run-2026-04-13-21-43-04` |
| Run count | 2 |
| Temperature | 0.7 |
| Max tokens | None |

### Phase 1 — Poem

| Setting | Value |
| --- | --- |
| Provider | ollama |
| Model | gemma3 |
| System prompt | — |

**Prompt:**
```
Lag et kort dikt om noe helt tilfeldig du finner på.
Svar med kun selve diktet. Ikke inkluder labels som TEXT: eller CODE:.
```

### Phase 2 — Code

| Setting | Value |
| --- | --- |
| Provider | ollama |
| Model | gemma3 |
| System prompt | — |

**Prompt template:**
```
Du får et dikt. Skriv KUN gyldig Python-kode som lager en figur med matplotlib.

Krav:
- Returner kun Python-kode, ingen forklaring eller markdown.
- Koden må kunne kjøres direkte.
- Bruk matplotlib og lag minst én figur.
- Lagre figuren med: plt.savefig(output_path)
- Ikke bruk plt.show().

DIKT:
{poem}
```

## Results

| Total | Successful | Fallback used | Failed |
| --- | --- | --- | --- |
| 2 | 2 | 0 | 0 |

### Per-iteration details

| # | ID | execution_ok | fallback | image_ok | error |
| --- | --- | --- | --- | --- | --- |
| 1 | 2026-04-13-21-43-12 | True | False | True |  |
| 2 | 2026-04-13-21-43-18 | True | False | True |  |
