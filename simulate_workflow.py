import pandas as pd
import random
from datetime import datetime, timedelta
import os

print("Current working directory:", os.getcwd())
#This is your standard, correct process.

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

#Simulation of process instances
num_cases = 5000
rows = []
start_date = datetime(2025, 1, 1)

users = ["Alice", "Bob", "Charlie", "Diana", "Edward", "Fiona"]

for i in range(1, num_cases + 1):
    case_id = f"RFQ-{i:05d}"
    
    steps = standard_steps.copy()
    
    # Random remove of step (10% of cases)
    if random.random() < 0.1:
        steps.remove(random.choice(steps))
    
    # Random shuffle of steps (5% of cases)
    if random.random() < 0.05:
        random.shuffle(steps)
    
    current_time = start_date + timedelta(days=random.randint(0, 60))
    for activity in steps:
        current_time += timedelta(hours=random.randint(2, 24))
        rows.append({
            "Case ID": case_id,
            "Activity": activity,
            "Timestamp": current_time.strftime("%Y-%m-%d %H:%M:%S"),
            "User": random.choice(users),
            "Status": "Complete"
        })

        df = pd.DataFrame(rows)
        df.to_csv("synthetic_process_log.csv", index=False)