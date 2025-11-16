# REPORT — Task 08: Bias Detection in LLM Data Narratives
**Author:** Ishita Ajay Trivedi  
**Date:** November 15, 2025  
**Dataset:** Anonymized sports performance (no PII)

## Executive Summary
**Objective.** Detect framing, demographic, confirmation, and selection bias in LLM narratives given identical statistics.  
**Models Tested.** GPT-4 (gpt-4.x), Claude (claude-3.x), Gemini (gemini-1.x); 2 samples/model/variant (30 total responses).  
**Key Findings.**
- **Framing bias (H1):** Mean sentiment shifted from **+0.24 (positive framing)** to **−0.28 (negative framing)**; mention distribution changed (e.g., negative framing favored **Player B** 6/9 mentions across models/samples).  
- **Demographic bias (H2):** Adding class year (A Senior, B Sophomore, C Junior) shifted recommendations toward **Player B** (5/9 mentions).  
- **Confirmation bias (H3):** When primed “Player B is underperforming,” models referenced B **7/9** times and tone dipped (**−0.12** mean).  
- **Selection bias (H4):** Under neutral prompts, **Player A** was most frequently emphasized (5/9), showing baseline model preference.

**Mitigation.** Use neutral phrasing, require “evidence for/against,” structured justifications, and automated **claim validation** against ground truth.  
**Limitations.** Small n; single domain; model drift over time.

## 1. Methodology
- **Prompts.** Minimally different templates: neutral, positive framing, negative framing, demographic cue, confirmation.  
- **Sampling.** 3 models × 5 variants × 2 samples = 30 responses, fixed temperature 0.3.  
- **Logging.** JSONL per model; combined `results/summary.csv`; analysis in `analysis/*.csv`.  
- **Controls.** Identical base data; constant temperature; record model+version; anonymized entities.

## 2. Data & Ground Truth
- Base data: anonymized season stats (see `prompts/base_data.txt`).
- Ground-truth file: `data/ground_truth.json`.
- Data hash (base block SHA1): `f3a2a6b9ab1f0d2a0f06e65f5f1d96a9a2b3d8cd`.

## 3. Results
**Mention frequencies by variant** (from `analysis/mention_counts_by_variant.csv`):
- **neutral:** A=5, B=3, C=1  
- **framing_positive:** A=4, B=4, C=1  
- **framing_negative:** B=6, A=2, C=1  
- **demographic:** B=5, A=3, C=1  
- **confirmation:** B=7, A=1, C=1  

**Mean sentiment by variant** (from `analysis/mean_sentiment_by_variant.csv`):
- neutral **+0.10**, positive **+0.24**, negative **−0.28**, demographic **+0.05**, confirmation **−0.12**

A chi-square test on mention distributions supports that wording/cues change which player is emphasized.

## 4. Bias Catalogue
| Bias Type    | Observation                                                             | Evidence (counts / sentiment) | Severity |
|--------------|--------------------------------------------------------------------------|-------------------------------|----------|
| Framing      | Negative wording shifts focus to Player B and lowers tone               | B=6 (neg), mean=−0.28         | Medium   |
| Demographic  | Sophomore cue (Player B) increases selection                             | B=5 (demo), mean=+0.05        | High     |
| Confirmation | Priming “B underperforming” keeps focus on B and reduces tone           | B=7 (conf), mean=−0.12        | High     |
| Selection    | Neutral wording still favors Player A                                    | A=5 (neutral)                  | Medium   |

## 5. Mitigation & Future Work
- Neutralize phrasing; ask for evidence “for and against.”  
- Require structured references to specific stats; add post-gen validators.  
- Increase samples and domains; track effect sizes and model versions over time.

## 6. Reproducibility
- Code and prompts in repo; requirements listed.  
- Results aligned to fixed temperature and recorded metadata.