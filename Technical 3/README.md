# CBR Disaster Response System

A small Python program that uses **Case-Based Reasoning (CBR)** to recommend an evacuation plan for a new disaster, based on similar past events in the Philippines.

## How It Works

1. **Retrieve**: Scores every past case against the new problem and picks the most similar.
2. **Reuse**: Adapts the best case's solution to the new population size.
3. **Retain**: Saves the new case into the case base.

### Similarity Score (0 to 1)

| Factor | Weight |
|---|---|
| Same disaster type | 0.5 |
| Same area type | 0.3 |
| Population closeness | 0.2 |

### Adaptation

- Evacuees = population × old evacuee %
- Shelters needed = evacuees ÷ shelter capacity (rounded up)
- Urban areas get an added "vertical evacuation and rescue boats" measure

## Case Base

- Typhoon Ursula (2019)
- Typhoon Odette (2021)
- Metro Flood (2012)
- Bohol Earthquake (2013)

## Usage

Requires Python 3 (no external libraries).

```bash
python cbr_disaster.py
```

To test another scenario, edit `new_problem` in `main()`:

```python
new_problem = {"type": "typhoon", "area": "urban", "population": 200000}
```

## Sample Output

```
=== CBR DISASTER RESPONSE SYSTEM ===

SIMILARITY SCORES:
  1. Typhoon Ursula (2019)      0.92
  2. Typhoon Odette (2021)      0.66
  3. Metro Flood (2012)         0.43
  4. Bohol Earthquake (2013)    0.08

MOST SIMILAR CASE: Typhoon Ursula (2019)

ADAPTED FINAL SOLUTION:
  Strategy : Evacuate low-lying barangays to schools and gyms; add vertical evacuation and rescue boats
  Evacuees : 60,000 (30% of population)
  Shelters : 150 (capacity 400 each)
```
