import random
from sentinel_llm.consistency.auditor import ConsistencyAuditor
from sentinel_llm.grounding.auditor   import GroundingAuditor
from sentinel_llm.calibration.auditor import CalibrationAuditor

def demo_llm_query(prompt):
    responses = [
        "Pakistan's capital is Islamabad, established in 1960.",
        "Islamabad is the capital of Pakistan, made capital in 1960.",
        "The capital of Pakistan is Islamabad.",
    ]
    return random.choice(responses)

ca = ConsistencyAuditor(demo_llm_query)
ca.self_consistency_check("What is the capital of Pakistan?", num_runs=5)
print("Consistency:", ca.get_consistency_score())

ga = GroundingAuditor()
ga.keyword_overlap_check(
    "Islamabad is the capital of Pakistan, established in 1960.",
    ["Islamabad", "capital", "Pakistan", "1960"]
)
print("Grounding:", ga.get_grounding_score())

cba = CalibrationAuditor()
cba.confidence_language_check("Islamabad is definitely the capital of Pakistan.", is_correct=True)
print("Calibration:", cba.get_calibration_score())
