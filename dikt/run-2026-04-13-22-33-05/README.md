# Run: 2026-04-13-22-33-05

## Configuration

| Setting | Value |
| --- | --- |
| Output directory | `dikt/run-2026-04-13-22-33-05` |
| Run count | 13 |
| Temperature | 0.7 |
| Max tokens | None |

### Phase 1 — Poem

| Setting | Value |
| --- | --- |
| Provider | ollama |
| Model | gpt-oss:120b-cloud |
| System prompt | — |

**Prompt:**
```
Lag et kort dikt om noe helt tilfeldig du finner på.
Svar med kun selve diktet.
```

### Phase 2 — Code

| Setting | Value |
| --- | --- |
| Provider | ollama |
| Model | gemma3 |
| System prompt | — |

**Prompt template:**
```
Du får et dikt. Du skal lage en kreativ matematisk representasjon av diktet. Bruk ulike matematiske grafer, flater eller andre visualiseringer som passer diktet.

Skriv KUN gyldig Python-kode som lager en figur med matplotlib.

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
| 13 | 13 | 7 | 0 |

### Per-iteration details

| # | ID | execution_ok | fallback | image_ok | error |
| --- | --- | --- | --- | --- | --- |
| 1 | 2026-04-13-22-33-21 | True | False | True |  |
| 2 | 2026-04-13-22-33-37 | False | True | True | name 'y' is not defined |
| 3 | 2026-04-13-22-33-52 | True | False | True |  |
| 4 | 2026-04-13-22-34-04 | False | True | True | x and y must have same first dimension, but have shapes (100,) and (1,) |
| 5 | 2026-04-13-22-34-24 | True | False | True |  |
| 6 | 2026-04-13-22-34-35 | False | True | True | 'Axes' object has no attribute 'ellipse' |
| 7 | 2026-04-13-22-34-57 | False | True | True | unsupported operand type(s) for -: 'float' and 'str' |
| 8 | 2026-04-13-22-35-13 | True | False | True |  |
| 9 | 2026-04-13-22-35-27 | True | False | True |  |
| 10 | 2026-04-13-22-35-46 | False | True | True | shape mismatch: objects cannot be broadcast to a single shape.  Mismatch is betw |
| 11 | 2026-04-13-22-36-02 | False | True | True | 'float' object is not subscriptable |
| 12 | 2026-04-13-22-36-15 | True | False | True |  |
| 13 | 2026-04-13-22-36-26 | False | True | True | Argument Z must be 2-dimensional. |
