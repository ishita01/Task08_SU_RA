import json, pathlib, pandas as pd
BASE = pathlib.Path(__file__).parent
RES = BASE / "results"
ANA = BASE / "analysis"
ANA.mkdir(exist_ok=True)

players = ["Player A","Player B","Player C"]

def mentions(txt):
    hits=[p for p in players if p.lower() in txt.lower()]
    return hits or ["None"]

def main():
    rows=[]
    for f in RES.glob("*_responses.jsonl"):
        for line in f.read_text().splitlines():
            rows.append(json.loads(line))
    df=pd.DataFrame(rows)
    df["mentions"]=df["text"].apply(mentions)
    df=df.explode("mentions")
    counts=df.groupby(["mentions"]).size().reset_index(name="n")
    counts.to_csv(ANA/"mention_counts.csv",index=False)
    print(counts)

if __name__=="__main__":
    main()
