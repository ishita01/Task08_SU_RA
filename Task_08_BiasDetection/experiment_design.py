import datetime, hashlib, pathlib

BASE = pathlib.Path(__file__).parent
PROMPTS = BASE / "prompts"
OUT = PROMPTS / "_generated"
OUT.mkdir(exist_ok=True)

def sha1(s): return hashlib.sha1(s.encode()).hexdigest()

base = (PROMPTS / "base_data.txt").read_text()
for p in PROMPTS.glob("*.txt"):
    if p.name == "base_data.txt": continue
    text = p.read_text().replace("{{base_data}}", base)
    out = OUT / p.name
    out.write_text(text)
    print(f"Generated {out.name} hash={sha1(text)[:8]} at {datetime.datetime.utcnow()}Z")
