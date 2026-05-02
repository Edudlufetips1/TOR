# TOR: True Offensive Rating ⚾

**True Offensive Rating (TOR)** 

Baseball is one of the most data-driven professional sports, yet traditional offensive metrics suffer from a critical flaw: they overemphasize binary plate appearance outcomes (Hit/Out) while ignoring the latent value in pitch-level process data. By treating every out as a zero-sum failure, conventional analytics overlook key indicators—such as deep-count leverage and high-velocity foul contact—that better reflect a hitter's true skill and future performance potential. 

TOR is a granular, process-driven metric that redefines offensive evaluation. Instead of focusing solely on terminal outcomes, TOR analyzes each at-bat as a dynamic sequence of pitches, emphasizing Non-BIP (Ball In Play) value.  By weighting pitch-level attributes—count depth, exit velocity on foul balls, and contact quality on outs—TOR isolates a hitter’s intrinsic offensive ability, minimizing noise from defense, luck, and park effects. The result is a higher-resolution predictor of offensive proficiency and performance ceiling.

## The Core Philosophy
In traditional baseball statistics, a 115-mph line drive caught by a shortstop counts as an "Out" (0.000), while a 60-mph bloop single counts as a "Hit" (1.000). This binary framework persists across most advanced metrics like OBP, OPS, and wRC+, which, while improved, remain fundamentally outcome-based. 

**TOR** aims to bridge this gap by analyzing Statcast data at the pitch level to reward:
*   **Deep Counts:** High pitches-per-plate-appearance.
*   **Quality of Contact:** High exit velocities, even on foul balls or "unlucky" outs.
*   **Aggressive Discipline:** Rewarding hitters who force pitchers to work.

## Project Structure
- `at_bat.py`: Contains the `AtBat` and `Pitch` classes (The Data Model).
- `scorer.py`: Logic for aggregating TOR across multiple games or players.
- `fetcher.py`: (In Development) Module for ingesting Statcast CSV/API data.
- `main.py`: The entry point for running the analysis.

## Tech Stack
- **Language:** Python 3.x
- **Libraries:** (Planned) Pandas, Matplotlib, Seaborn
- **Development Environment:** Fedora Linux (KDE) / WSL
