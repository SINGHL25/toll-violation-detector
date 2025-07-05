# Detect violations based on rules
### 🔹 logic/detect_violation.py
```python
import pandas as pd
from logic.compare_axle_vs_class import compare_class_vs_axle


def detect_violation():
    df_passage = pd.read_csv("data/passage_log.csv")
    df_axle = pd.read_csv("data/axle_data.csv")

    df = pd.merge(df_passage, df_axle, on=['vehicle_id', 'timestamp'])
    violations = []

    for _, row in df.iterrows():
        if compare_class_vs_axle(row['class'], row['axle_count']) or row['payment_status'] != 'SUCCESS':
            violations.append(row.to_dict())

    print("⚠️ Violations Detected:", len(violations))
    pd.DataFrame(violations).to_json("data/violations.json", orient='records', indent=2)
```
