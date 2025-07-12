import pandas as pd

standard_steps = [
    "Issuance of RFQ",
    "Technical Evaluation",
    "Commercial Evaluation",
    "PO Creation",
    "Supplier Confirmation",
    "Goods Dispatch",
    "Goods Receipt",
    "Inspection & Approval",
    "Invoice Generation",
    "Payment to Supplier"
]

df = pd.read_csv("synthetic_process_log.csv")

# Identify breaches in the process
breach_missing = []
for case_id, group in df.groupby("Case ID"):
    activities = list(group["Activity"])
    missing_steps = [step for step in standard_steps if step not in activities]
    if missing_steps:
        breach_missing.append({
            "Case ID": case_id,
            "Breach Type": "Missing Steps",
            "Details": ", ".join(missing_steps)
        })

# Identify breaches in the order of steps
breach_order = []
for case_id, group in df.groupby("Case ID"):
    activities = list(group.sort_values("Timestamp")["Activity"])
    try:
        indices = [standard_steps.index(step) for step in activities]
        if indices != sorted(indices):
            breach_order.append({
                "Case ID": case_id,
                "Breach Type": "Out of Order",
                "Details": "Steps executed out of order"
            })
    except ValueError:
        continue

# Combine breaches
breach_records = breach_missing + breach_order
breach_df = pd.DataFrame(breach_records)

# Save breaches to CSV
breach_df.to_csv("breach_analysis.csv", index=False)
print("Breach detection complete ! Saved to breach_cases.csv")
