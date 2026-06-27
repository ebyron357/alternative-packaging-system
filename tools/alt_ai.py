#!/usr/bin/env python3
"""
ALTERNATIVE(TM) — Claude API toolkit.

One entry point, four tools, all built on the official Anthropic SDK
(`anthropic`) and the `claude-opus-4-8` model.

    python3 tools/alt_ai.py ask "Summarize the brand positioning in 2 lines"
    python3 tools/alt_ai.py chat
    python3 tools/alt_ai.py proof  --flavor "Lychee Sweet Tea" --tier SOCIAL --dose 10
    python3 tools/alt_ai.py compliance --states CA,NY,TX

Auth: set ANTHROPIC_API_KEY in your environment (never hardcode it).
    export ANTHROPIC_API_KEY=sk-ant-...
Get a key at https://console.anthropic.com/.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from typing import List, Optional

try:
    import anthropic
    from pydantic import BaseModel, Field
except ImportError:
    sys.exit(
        "Missing dependency. Install the SDK first:\n"
        "    pip install anthropic\n"
        "(pydantic ships with it)."
    )

MODEL = "claude-opus-4-8"   # latest, most capable Opus-tier model


def make_client() -> "anthropic.Anthropic":
    """Construct the client. Reads ANTHROPIC_API_KEY from the environment."""
    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit(
            "ANTHROPIC_API_KEY is not set.\n"
            "    export ANTHROPIC_API_KEY=sk-ant-...\n"
            "Get a key at https://console.anthropic.com/."
        )
    return anthropic.Anthropic()  # SDK reads the env var automatically


# --------------------------------------------------------------------------
# 1. GENERIC STARTER — one prompt in, streamed answer out
# --------------------------------------------------------------------------
def cmd_ask(client: "anthropic.Anthropic", args: argparse.Namespace) -> None:
    """Send a single prompt and stream the response to stdout."""
    prompt = args.prompt or sys.stdin.read()
    if not prompt.strip():
        sys.exit("Nothing to ask. Pass a prompt or pipe text via stdin.")

    with client.messages.stream(
        model=MODEL,
        max_tokens=16000,
        thinking={"type": "adaptive"},          # Claude decides how much to think
        system=args.system or None,
        messages=[{"role": "user", "content": prompt}],
    ) as stream:
        for text in stream.text_stream:
            print(text, end="", flush=True)
    print()


# --------------------------------------------------------------------------
# 2. CHAT LOOP — interactive, multi-turn conversation
# --------------------------------------------------------------------------
def cmd_chat(client: "anthropic.Anthropic", args: argparse.Namespace) -> None:
    """Hold a streaming conversation. Type 'exit' / Ctrl-D to quit."""
    system = args.system or (
        "You are a concise assistant helping the ALTERNATIVE(TM) beverage team."
    )
    messages: list[dict] = []
    print("ALTERNATIVE(TM) chat — type 'exit' or Ctrl-D to quit.\n")
    while True:
        try:
            user = input("you  > ").strip()
        except EOFError:
            print()
            break
        if user.lower() in {"exit", "quit"}:
            break
        if not user:
            continue
        messages.append({"role": "user", "content": user})

        print("alt  > ", end="", flush=True)
        parts: list[str] = []
        with client.messages.stream(
            model=MODEL,
            max_tokens=16000,
            thinking={"type": "adaptive"},
            system=system,
            messages=messages,
        ) as stream:
            for text in stream.text_stream:
                parts.append(text)
                print(text, end="", flush=True)
        print("\n")
        messages.append({"role": "assistant", "content": "".join(parts)})


# --------------------------------------------------------------------------
# 3. LABEL PROOF GENERATOR — structured output that can feed the build script
# --------------------------------------------------------------------------
class FrontPanelSpec(BaseModel):
    """Structured front-panel copy for one SKU. Maps to build_front.py fields."""
    tagline: str = Field(description="Always 'A NEW STATE OF MIND' unless told otherwise")
    wordmark: str = Field(description="Always 'ALTERNATIVE'")
    product_line: str = Field(description="Tier: SESSION, SOCIAL, RESERVE, or ASCEND")
    thc_strength: str = Field(description="e.g. '10 MG THC PER CAN'")
    flavor: str = Field(description="Flavor name in title or all caps")
    category: str = Field(description="Always 'HEMP-DERIVED THC BEVERAGE'")
    net_contents: str = Field(description="e.g. '12 FL OZ (355 mL)'")
    notes: str = Field(description="One or two lines of art-direction guidance for this SKU")


def cmd_proof(client: "anthropic.Anthropic", args: argparse.Namespace) -> None:
    """Generate a structured front-panel spec for a SKU and print it as JSON."""
    ask = (
        f"Produce the front-panel copy spec for an ALTERNATIVE(TM) SKU.\n"
        f"Tier: {args.tier}\nDose: {args.dose} mg THC per can\nFlavor: {args.flavor}\n"
        f"Net contents: {args.net}\n\n"
        "Follow the locked brand system: tagline 'A NEW STATE OF MIND', wordmark "
        "'ALTERNATIVE', category 'HEMP-DERIVED THC BEVERAGE'. Beverage-first, "
        "premium, restrained. Do not invent claims."
    )
    resp = client.messages.parse(
        model=MODEL,
        max_tokens=8000,
        messages=[{"role": "user", "content": ask}],
        output_format=FrontPanelSpec,
    )
    spec = resp.parsed_output
    out = spec.model_dump()
    text = json.dumps(out, indent=2)
    print(text)
    if args.out:
        with open(args.out, "w") as f:
            f.write(text + "\n")
        print(f"\n[written to {args.out}]", file=sys.stderr)


# --------------------------------------------------------------------------
# 4. COMPLIANCE COPY DRAFTER — structured, flagged for counsel review
# --------------------------------------------------------------------------
class StateWarning(BaseModel):
    state: str = Field(description="Two-letter US state code")
    warning_text: str = Field(description="DRAFT mandatory warning / disclosure text for that state")
    rationale: str = Field(description="Why this language; which rule it maps to (best effort)")


class ComplianceDraft(BaseModel):
    disclaimer: str = Field(description="A prominent note that this is an unreviewed DRAFT")
    per_state: List[StateWarning]


def cmd_compliance(client: "anthropic.Anthropic", args: argparse.Namespace) -> None:
    """Draft per-state warning copy for legal review. NOT legal advice."""
    states = [s.strip().upper() for s in args.states.split(",") if s.strip()]
    if not states:
        sys.exit("Pass one or more states, e.g. --states CA,NY,TX")
    ask = (
        "You are assisting a beverage brand's design team by DRAFTING starting-point "
        "compliance warning copy for a hemp-derived THC beverage, to be reviewed and "
        "corrected by licensed legal counsel before any use. This is not legal advice.\n\n"
        f"Product: ALTERNATIVE(TM) SESSION, 5 mg Delta-9 THC per 12 fl oz can.\n"
        f"Draft mandatory/adult-use warning language for these states: {', '.join(states)}.\n"
        "For each state, give a clearly-labeled DRAFT and note which requirement it maps to. "
        "Where you are uncertain, say so explicitly rather than inventing a citation."
    )
    resp = client.messages.parse(
        model=MODEL,
        max_tokens=16000,
        messages=[{"role": "user", "content": ask}],
        output_format=ComplianceDraft,
    )
    draft = resp.parsed_output
    print("=" * 70)
    print("DRAFT — NOT LEGAL ADVICE — counsel review required before any use")
    print("=" * 70)
    print(draft.disclaimer, "\n")
    for w in draft.per_state:
        print(f"[{w.state}]")
        print(f"  Warning : {w.warning_text}")
        print(f"  Maps to : {w.rationale}\n")
    if args.out:
        with open(args.out, "w") as f:
            f.write(draft.model_dump_json(indent=2) + "\n")
        print(f"[written to {args.out}]", file=sys.stderr)


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------
def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="alt_ai", description="ALTERNATIVE(TM) Claude API toolkit"
    )
    sub = p.add_subparsers(dest="command", required=True)

    a = sub.add_parser("ask", help="Single prompt -> streamed answer")
    a.add_argument("prompt", nargs="?", help="Prompt text (or pipe via stdin)")
    a.add_argument("--system", help="Optional system prompt")
    a.set_defaults(func=cmd_ask)

    c = sub.add_parser("chat", help="Interactive multi-turn chat")
    c.add_argument("--system", help="Optional system prompt")
    c.set_defaults(func=cmd_chat)

    pr = sub.add_parser("proof", help="Generate a structured front-panel SKU spec")
    pr.add_argument("--flavor", required=True)
    pr.add_argument("--tier", default="SESSION", choices=["SESSION", "SOCIAL", "RESERVE", "ASCEND"])
    pr.add_argument("--dose", default="5", help="mg THC per can")
    pr.add_argument("--net", default="12 FL OZ (355 mL)")
    pr.add_argument("--out", help="Write JSON to this path")
    pr.set_defaults(func=cmd_proof)

    co = sub.add_parser("compliance", help="Draft per-state warning copy (for counsel review)")
    co.add_argument("--states", required=True, help="Comma list, e.g. CA,NY,TX")
    co.add_argument("--out", help="Write JSON to this path")
    co.set_defaults(func=cmd_compliance)

    return p


def main() -> None:
    args = build_parser().parse_args()
    client = make_client()
    args.func(client, args)


if __name__ == "__main__":
    main()
