# Class vs axle mismatch logic
### 🔹 logic/compare_axle_vs_class.py
```python
def compare_class_vs_axle(actual_class, axle_count):
    expected_class = {2: 'Car', 3: 'LCV', 4: 'Truck'}.get(axle_count, 'Unknown')
    return actual_class != expected_class
```
