# TA4: Laptop Troubleshooting Assistant

Two small Python programs that diagnose laptop problems using different AI reasoning approaches.

| File | Approach |
|---|---|
| `TA4A_Coritana_Hizon.py` | Rule-Based Reasoning (RBR) |
| `TA4B_Coritana_Hizon.py` | Case-Based Reasoning (CBR) |

## Part A: Rule-Based Reasoning

Checks a set of facts (power, thermal, display, storage) against IF-THEN rules and prints every action that applies.

- **Knowledge base**: a nested dictionary of laptop facts
- **Rules**: low battery, overheating, loud fan, screen flicker, low storage, no power
- **Inference engine**: runs every rule and collects the ones that fire

```bash
python TA4A_Coritana_Hizon.py
```

Sample output:

```
Rule-Based Reasoning Actions:
- Battery is low - plug in the charger
- Close heavy programs and place the laptop on a cooling pad
- Clean the fan and air vents from dust
- Delete unused files or run Disk Cleanup
```

To test another scenario, edit the `facts` dictionary.

## Part B: Case-Based Reasoning

Asks yes/no questions about the problem, then finds the most similar past case and reuses its solution.

1. **Retrieve**: similarity is the fraction of matching features (5 total)
2. **Reuse**: use the best case's solution
3. **Revise**: optionally edit the suggested solution
4. **Retain**: save the new case to the case base

```bash
python TA4B_Coritana_Hizon.py
```

## Requirements

Python 3, no external libraries.
