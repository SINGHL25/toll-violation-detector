### 🔹 dashboard/streamlit_app.py
```python
import streamlit as st
import pandas as pd
import json

st.title("🚧 Toll Violation Dashboard")

with open("data/violations.json") as f:
    violations = json.load(f)

if violations:
    df = pd.DataFrame(violations)
    st.dataframe(df)
else:
    st.info("✅ No violations found.")
```

