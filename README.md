# Sentinel-LLM

### Hallucination & Confidence Audit Toolkit for LLMs

Sentinel-LLM checks any LLM's output across three dimensions — Consistency, Grounding, and Calibration — and returns a unified Hallucination Trust Score.

## Quick Start

```bash
git clone https://github.com/Zaira-Shahid/sentinel-llm.git
cd sentinel-llm
pip install -r requirements.txt
python example.py
```

## What it checks

| Module | What it does |
|--------|---------------|
| Consistency | Sends the same prompt multiple times, measures answer drift |
| Grounding | Compares the answer against known facts you supply |
| Calibration | Flags confident language paired with wrong answers |

## Trust Score

| Grade | Score | Meaning |
|-------|-------|---------|
| A | 90-100 | Highly Reliable |
| B | 75-89  | Reliable |
| C | 60-74  | Use With Caution |
| D | 45-59  | High Hallucination Risk |
| F | 0-44   | Critical Risk |

## License
MIT
