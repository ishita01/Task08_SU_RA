import json, re, pathlib
BASE = pathlib.Path(__file__).parent
GT = BASE/"data"/"ground_truth.json"
RES = BASE/"results"
ANA = BASE/"analysis"
ANA.mkdir(exist_ok=True)

gt=json.loads(GT.read_text()) if GT.exists() else {}
pat=re.compile(r"(Player [ABC]).*?(\d+)\s+(goals|assists|turnovers|minutes)",re.I)
flags=[]
for f in RES.glob("*_responses.jsonl"):
    for line in f.read_text().splitlines():
        rec=json.loads(line)
        for m in pat.finditer(rec["text"]):
            pl, val, met=m.group(1),int(m.group(2)),m.group(3).lower()
            truth=gt.get(pl,{}).get(met)
            if truth and truth!=val:
                flags.append({"prompt":rec["prompt_id"],"player":pl,"metric":met,"claimed":val,"truth":truth})
out=ANA/"fabrication_flags.json"
out.write_text(json.dumps(flags,indent=2))
print("Mismatches:",len(flags))
