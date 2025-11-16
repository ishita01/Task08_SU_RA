# Task_08_Bias_Detection

This repository implements **Research Task 08 – Bias Detection in LLM Data Narratives**.  
It extends prior work (Task 07) by running a *controlled experiment* to detect **framing**, **demographic**, **confirmation**, and **selection** biases across multiple LLMs (e.g., Claude, GPT-4, Gemini).

## Hypotheses
- **H1 — Framing bias:** wording changes (“struggling” vs “developing”) alter recommendations.  
- **H2 — Demographic bias:** adding class year changes which player is recommended.  
- **H3 — Confirmation bias:** priming with a hypothesis increases supportive language.  
- **H4 — Selection bias:** different models emphasize particular players/metrics disproportionately.

## Repo Structure
├── prompts/                 # Prompt templates
│   └── _generated/          # Created automatically by experiment_design.py
├── results/                 # Model responses (JSONL + summary CSV)
├── analysis/                # Analysis outputs (CSV + flags)
├── data/                    # Ground-truth file (not committed)
├── experiment_design.py
├── run_experiment.py
├── analyze_bias.py
├── validate_claims.py
├── README.md
├── REPORT.md
├── requirements.txt
└── .gitignore