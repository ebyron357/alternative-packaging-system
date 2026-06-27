# ALTERNATIVE™ — Claude API toolkit (`alt_ai.py`)

A small Python tool that connects to the Claude API (official `anthropic` SDK,
model `claude-opus-4-8`) with four commands.

## 1. Install

```bash
pip install anthropic
```

## 2. Set your API key

Get one at https://console.anthropic.com/, then:

```bash
export ANTHROPIC_API_KEY=sk-ant-...
```

The code reads this from the environment — the key is never hardcoded.

## 3. Run

```bash
# Single prompt, streamed answer
python3 tools/alt_ai.py ask "Summarize the ALTERNATIVE brand positioning in 2 lines"
echo "long text..." | python3 tools/alt_ai.py ask          # or pipe via stdin

# Interactive chat (type 'exit' or Ctrl-D to quit)
python3 tools/alt_ai.py chat

# Structured front-panel spec for a SKU -> JSON (optionally written to a file)
python3 tools/alt_ai.py proof --flavor "Lychee Sweet Tea" --tier SOCIAL --dose 10 \
    --out products/social-10mg-lychee/front_spec.json

# DRAFT per-state compliance copy (for legal counsel review — NOT legal advice)
python3 tools/alt_ai.py compliance --states CA,NY,TX --out scratch/compliance_draft.json
```

## Notes

- `ask` and `chat` use streaming + adaptive thinking.
- `proof` and `compliance` use **structured outputs** (`messages.parse` + Pydantic),
  so you get validated JSON, not free text.
- `proof` output maps to the fields in `scratchpad/build_front.py`, so it can feed
  proof generation for new SKUs.
- `compliance` output is explicitly a **draft for counsel** — it never substitutes
  for legal review.
