# True Offensive Rating (TOR)

In baseball, traditional offensive metrics evaluate plate appearances as terminal events. A hit, an out, a strikeout — each assigned a fixed value determined entirely by result. While this framework has proven analytically useful, it systematically discards the pitch-level process data from which offensive outcomes emerge.

TOR proposes a complementary framework: decomposing each plate appearance into its underlying sequence of pitch-level events and evaluating offensive quality along both process and outcome dimensions.

---

## Metric Definition

TOR is a process-weighted offensive rating that evaluates the competitive quality of individual plate appearances at pitch resolution.

Each At-Bat is modeled as a dynamic sequence rather than a singular result, scored across the following components:

- **Count Leverage** — progression through favorable and unfavorable count states
- **Pitch Sequence Depth** — plate appearance length and pitcher workload imposed
- **Contact Quality** — exit velocity on all contacted pitches, including non-terminal fouls
- **Terminal Outcome Value** — result-based contribution, dynamically weighted by outcome informativeness

---

## Outcome Weighting Philosophy

TOR does not treat outcome as irrelevant — it treats outcome as *variably informative*.

Certain results carry intrinsic value independent of process: a home run produces runs regardless of how it was generated. Extra-base hits eliminate base-out state uncertainty. These outcomes warrant substantial positive weighting.

Conversely, routine negative outcomes — the weak rollover groundout, the first-pitch popup — are largely uninformative in isolation. A sharply-hit lineout and a weak groundout register identically in conventional statistics despite representing categorically different offensive processes.

TOR therefore applies a sliding outcome weight: increasing emphasis for high-leverage productive events, decreasing emphasis where process-level signal dominates.

---

## Core Philosophy

Conventional statistics flatten plate appearances into binary results, obscuring meaningful within-at-bat variation. A 115-mph line drive caught by the shortstop, a 12-pitch strikeout featuring multiple hard fouls, and a first-pitch popup may register similarly — or identically — across OBP, OPS, and wRC+.

Simultaneously, favorable outcomes can mask process-level vulnerabilities: elevated swing-and-miss tendencies, poor pitch selection, or unsustainable contact profiles that conventional metrics are not designed to surface.

TOR addresses this by evaluating what the hitter *did* across the plate appearance — not merely what resulted from it — with the goal of more accurately estimating:

- **Offensive Threat Quality** — how dangerous the hitter actually was
- **Contact Sustainability** — whether the underlying contact profile is repeatable
- **Pitcher Pressure** — the degree to which the hitter imposed competitive difficulty

---

## Project Structure

- `at_bat.py` — `AtBat` and `Pitch` classes (Core Data Model)
- `scorer.py` — TOR aggregation and player-level rating logic
- `fetcher.py` — *(In Development)* Statcast pitch-level data ingestion
- `main.py` — Simulation entry point and output testing

---

## Tech Stack

- **Language:** Python 3.x
- **Libraries:** Pandas, Matplotlib
- **Environment:** VSCode / WSL
