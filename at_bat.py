class Pitch:
    def __init__(self, pitch_number, exit_velo, description, balls, strikes):
        self.pitch_number = pitch_number
        self.exit_velo = exit_velo
        self.description = description
        self.balls = balls
        self.strikes = strikes

class AtBat:
    def __init__(self, player_name, final_outcome):
        self.player_name = player_name
        self.final_outcome = final_outcome
        self.pitches = []

    def add_pitch(self, pitch):
        self.pitches.append(pitch)

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

    def quality_contact_score(self):
        score = 0
        for pitch in self.pitches:
            if pitch.description in ("foul", "in_play"):
                if pitch.exit_velo > 120:
                    score += 85
                elif pitch.exit_velo > 116:
                    score += 50
                elif pitch.exit_velo > 111:
                    score += 27
                elif pitch.exit_velo > 106:
                    score += 17
                elif pitch.exit_velo > 101:
                    score += 8
                elif pitch.exit_velo > 95:
                    score += 3
                elif pitch.exit_velo > 80:
                    score += 0
                elif pitch.exit_velo < 80:
                    score -= 2
        return score

    def count_management_score(self):
        score = 0
        milestone30 = False
        milestone31 = False
        for pitch in self.pitches:
            if pitch.balls > pitch.strikes:
                score += 0.25
            elif pitch.strikes > pitch.balls:
                score -= 0.25
        # Loop 2 — milestone bonuses, did they reach leverage counts
            if pitch.balls == 3 and pitch.strikes == 0 and not milestone30:
                score += 0.25
                milestone30 = True
            elif pitch.balls == 3 and pitch.strikes == 1 and not milestone30 and not milestone31:
                score += 0.25
                milestone31 = True
        return score            

    def outcome_score(self):
        outcomes = {
            "home_run": 50,
            "triple": 20,
            "double": 12,
            "single": 4,
            "walk": 3,
            "field_out": -2,
            "strikeout": -4
        }
        return outcomes.get(self.final_outcome, 0)
        
    def is_valid_ab(self):
        # List of outcomes that provide zero skill data
        invalid_outcomes = ["hit_by_pitch", "intentional_walk"]
        
        if self.final_outcome in invalid_outcomes:
            return False
        if len(self.pitches) == 0:
            return False
        return True

    def calculate_tor(self):
        if not self.is_valid_ab():
            return 0
        
        score = 50
        score += self.pitch_count_score() *1.2
        score += self.quality_contact_score() * 4.5
        score += self.count_management_score() *1.2
        score += self.outcome_score() * 4
        return score
