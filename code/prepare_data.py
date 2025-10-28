from pathlib import Path
import json

raw = Path("../data/raw/book.txt").read_text(encoding="utf-8")
examples = [p.strip() for p in raw.split("\n\n") if p.strip()]

out = Path("../data/processed/dataset.jsonl")
with out.open("w", encoding="utf-8") as f:
    for ex in examples:
        rec = {"input": "", "output": ex}
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
print("Saved", out)