import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set random seed
np.random.seed(42)

# Number of mock records
num_records = 250

# Generate Patient IDs
patient_ids = [f"PT{str(i).zfill(5)}" for i in range(1, num_records + 1)]

# Admission times over a 30-day period
start_date = datetime(2024, 7, 1)
admit_times = [start_date + timedelta(hours=np.random.randint(0, 24*30)) for _ in range(num_records)]

# First order times (1–6 hrs after admission)
first_order_times = [admit + timedelta(hours=np.random.randint(1, 7)) for admit in admit_times]

# Discharge orders (2–6 days after admission)
discharge_order_times = [admit + timedelta(days=np.random.randint(2, 7), hours=np.random.randint(0, 6)) for admit in admit_times]

# Actual discharge times (0–12 hrs after discharge order)
discharge_times = [order + timedelta(hours=np.random.randint(0, 13)) for order in discharge_order_times]

# Charge entry time (0–3 days after discharge)
charge_entry_times = [discharge + timedelta(days=np.random.randint(0, 4), hours=np.random.randint(0, 6)) for discharge in discharge_times]

# Payment post time (0–10 days after charge entry)
payment_times = [charge + timedelta(days=np.random.randint(0, 11), hours=np.random.randint(0, 12)) for charge in charge_entry_times]

# Denial info
denial_flags = np.random.choice(['Yes', 'No'], size=num_records, p=[0.25, 0.75])
denial_reasons = [
    random.choice(['Authorization', 'Missing Documentation', 'Coding Error', 'None']) 
    if denied == 'Yes' else 'None'
    for denied in denial_flags
]

# Units for grouping
units = ['Med/Surg', 'ICU', 'Telemetry', 'Ortho', 'Neuro', 'Oncology']
admit_units = [random.choice(units) for _ in range(num_records)]

# Create DataFrame
df = pd.DataFrame({
    'Patient_ID': patient_ids,
    'Admit_Unit': admit_units,
    'Admit_Time': admit_times,
    'First_Order_Time': first_order_times,
    'Discharge_Order_Time': discharge_order_times,
    'Discharge_Time': discharge_times,
    'Charge_Entry_Time': charge_entry_times,
    'Payment_Posted_Time': payment_times,
    'Denied': denial_flags,
    'Denial_Reason': denial_reasons
})

# Export to CSV
df.to_csv('epic_throughput_revenue_data.csv', index=False)
print("Mock data saved to 'epic_throughput_revenue_data.csv'")
