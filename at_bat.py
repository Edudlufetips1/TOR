class Pitch:
    def __init__(self, pitch_number, description, balls, strikes, exit_velo, bat_speed):
        self.pitch_number = pitch_number
        self.description = description
        self.balls = balls
        self.strikes = strikes
        self.exit_velo = exit_velo
        self.bat_speed = bat_speed


class AtBat:
    def __init__(self, player_name, final_outcome):
        self.player_name = player_name
        self.final_outcome = final_outcome
        self.pitches = []

    # ── Pitch Management ──────────────────────────────────────────────────────

    def add_pitch(self, pitch):
        self.pitches.append(pitch)

    # ── Validity ──────────────────────────────────────────────────────────────

    def is_valid_ab(self):
        invalid_outcomes = ["hit_by_pitch", "intentional_walk"]
        if self.final_outcome in invalid_outcomes:
            return False
        if len(self.pitches) == 0:
            return False
        return True

    # ── Scoring Components ────────────────────────────────────────────────────

    def pitch_count_score(self):
        n = len(self.pitches)
        if n >= 6:
            return 4
        elif n >= 4:
            return 2
        elif n == 3:
            return 0
        else:
            return -3

    def count_management_score(self):
        score = 0
        milestone30 = False
        milestone31 = False
        for pitch in self.pitches:
            if pitch.balls > pitch.strikes:
                score += 0.25
            elif pitch.strikes > pitch.balls:
                score -= 0.25
            if pitch.balls == 3 and pitch.strikes == 0 and not milestone30:
                score += 0.25
                milestone30 = True
            elif pitch.balls == 3 and pitch.strikes == 1 and not milestone30 and not milestone31:
                score += 0.25
                milestone31 = True
        return score

    def quality_contact_score(self):
        score = 0
        for pitch in self.pitches:
            if pitch.description in ("foul", "in_play"):
                if pitch.exit_velo > 120:
                    score += 70
                elif pitch.exit_velo > 116:
                    score += 48
                elif pitch.exit_velo > 111:
                    score += 32
                elif pitch.exit_velo > 106:
                    score += 20
                elif pitch.exit_velo > 101:
                    score += 12
                elif pitch.exit_velo > 95:
                    score += 5
                elif pitch.exit_velo > 80:
                    score = 1
                else:
                    score = 0
        return score

    def bat_speed_score(self):
        score = 0
        for pitch in self.pitches:
            if pitch.bat_speed and pitch.description in ("foul", "in_play", "swinging_strike"):
                if pitch.bat_speed > 84:
                    base = 16
                elif pitch.bat_speed > 81:
                    base = 12
                elif pitch.bat_speed > 78:
                    base = 8
                elif pitch.bat_speed > 75:
                    base = 4
                elif pitch.bat_speed > 72:
                    base = 2
                elif pitch.bat_speed > 69:
                    base = 1
                else: 
                    base = 0

                if pitch.description == "in_play":
                    score += base
                elif pitch.description == "foul":
                    score += base * 0.6
                elif pitch.description == "swinging_strike":
                    score += base * 0.1
        return score

    def outcome_score(self):
        outcomes = {
            "home_run": 80,
            "triple":   58,
            "double":   20,
            "single":    5,
            "walk":      3,
            "field_out": 0,
            "strikeout": -1,
        }
        return outcomes.get(self.final_outcome, 0)

    # ── Aggregator ────────────────────────────────────────────────────────────

    def calculate_tor(self):
        if not self.is_valid_ab():
            return 0

        score = 50
        score += self.pitch_count_score()      * 1.1
        score += self.count_management_score() * 1.1
        score += self.bat_speed_score()        * 1.15
        score += self.quality_contact_score()  * 1.6
        score += self.outcome_score()          * 2
        return score