# TA4: Knowledge Representation, Rule-Based Reasoning and Case-Based Reasoning

This activity builds a **laptop troubleshooting assistant** twice, using two classic AI reasoning approaches on the same domain, so their strengths can be compared.

| File | Part | Approach |
|---|---|---|
| `TA4A_Coritana_Hizon.py` | A | Knowledge Representation + Rule-Based Reasoning (RBR) |
| `TA4B_Coritana_Hizon.py` | B | Case-Based Reasoning (CBR) |

## Part A: Knowledge Representation + RBR

The laptop's state is stored as a **knowledge base**: a nested dictionary of facts grouped into `power`, `thermal`, and `display`.

- **Rules**: six IF-THEN functions (no power, low battery, overheating, loud fan, screen flicker, low storage). Each returns a recommended action if its condition is true.
- **Inference engine (Task 2B)**: loops through the rule base, evaluates every rule against the facts, and collects the actions of all rules that fire into a list.
- **Display output (Task 2C)**: prints the knowledge base, then the inferred actions (or a "no action needed" message).

Sample output for the default facts (battery 12%, CPU 92°C, loud fan, 3 GB free):

```
Rule-Based Reasoning Actions:
- Battery is low - plug in the charger
- Close heavy programs and place the laptop on a cooling pad
- Clean the fan and air vents from dust
- Delete unused files or run Disk Cleanup
```


## Part B: Case-Based Reasoning

Instead of fixed rules, the program solves a new problem by reusing the solution of the most similar past case. It follows the CBR cycle:

1. **Retrieve**: compares the new problem to each stored case using five yes/no features (`wont_turn_on`, `overheating`, `loud_fan`, `slow`, `screen_flicker`). Similarity is the fraction of features that match (0% to 100%).
2. **Reuse**: takes the best case's solution as the suggestion.
3. **Revise**: lets the user keep the suggestion or type an edited solution.
4. **Retain**: saves the new problem and final solution into the case base, so it grows with use.

The case base starts with four cases: won't turn on, overheating, slow, and screen flicker.

Example run (answers: overheating, loud fan, and slow = yes; the rest = no):

```
Most similar case found (similarity: 100%)
Suggested solution: Clean the fan and vents, then use a cooling pad.
Case retained. Case base now has 5 cases.
```


Python 3, no external libraries.
