import json, csv, datetime, pathlib
BASE = pathlib.Path(__file__).parent
PROMPTS = BASE / "prompts" / "_generated"
RESULTS = BASE / "results"
RESULTS.mkdir(exist_ok=True)

def fake_response(prompt, model):
    snippet = prompt.splitlines()[-1][:120]
    txt = f"[{model}] {snippet}"
    return {"text": txt, "tokens": len(txt.split()), "version": model + "_stub"}

def run(model="gpt4", samples=2):
    jsonl = RESULTS / f"{model}_responses.jsonl"
    csvf = RESULTS / "summary.csv"
    wrote = not csvf.exists()
    with jsonl.open("w", encoding="utf-8") as jf, csvf.open("a", newline="", encoding="utf-8") as cf:
        writer = csv.DictWriter(cf, fieldnames=["prompt_id","model","tokens"])
        if wrote:
            writer.writeheader()
        for p in PROMPTS.glob("*.txt"):
            for i in range(1, samples+1):
                out = fake_response(p.read_text(), model)
                rec = {
                    "prompt_id": f"{p.stem}_{i:02d}",
                    "model": model,
                    "tokens": out["tokens"],
                    "timestamp": datetime.datetime.utcnow().isoformat()+"Z",
                    "text": out["text"]
                }
                jf.write(json.dumps(rec, ensure_ascii=False)+"\n")
                writer.writerow({"prompt_id": rec["prompt_id"],"model":model,"tokens":out["tokens"]})
                print("→", rec["prompt_id"])

if __name__=="__main__":
    run("gpt4",2)
