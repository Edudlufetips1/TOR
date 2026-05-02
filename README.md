## True Offensive Rating (TOR) 

Baseball is arguably the most data-driven and optimized professional sport; however, traditional offensive metrics possess a fundamental flaw: they over-evaluate the binary outcomes of individual plate appearances while largely neglecting the significant latent value found in pitch-level data. By treating every 'out' as a zero-sum failure, current analytics fail to account for the process-driven indicators—such as deep-count leverage and high-velocity contact on non-terminal pitches—that provide a more statistically significant preview of a hitter's true performance ceiling.

Metric Definition:
TOR is a granular performance metric that replaces the outcome-based binary (Hit/Out) with a process-driven valuation. Rather than evaluating a plate appearance as a single terminal event, TOR treats each At-Bat as a dynamic data series, specifically focusing on Non-BIP (Ball In Play) value.

By capturing and weighting individual pitch-level attributes—specifically pitch-sequence depth, exit velocity on non-terminal contact (foul balls), and contact quality on outs—TOR isolates a hitter's skill from external variables like defensive range and park factors. The result is a high-resolution contact quality predctor that more accurately isolates a player's intrinsic offensive proficiency and predictive performance ceiling.

## The Core Philosophy
In traditional baseball stats, a 115-mph line drive directly at a shortstop is an "Out" (0.000), while a 60-mph blooper that falls for a hit or a well-placed bunt is a "single" (1.000). 

Crucially, this binary evaluation persists across nearly all industry-standard advanced metrics—including OBP, OPS, wRC+, etc. While these stats offer better weighted outcomes, they remain inherently results-based almost entirely; thus largely ignoring the nuanced skill data generated during the course of the plate appearance.

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
