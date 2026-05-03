class Pitch:
    def __init__(self, pitch_number, exit_velo, description, balls, strikes):
        self.pitch_number = pitch_number
        self.exit_velo = exit_velo
        self.description = description
        self.balls = balls
        self.strikes = strikes

class AtBat:
    def __init__(self, player_name):
        self.player_name = player_name
        self.pitches = []

    def add_pitch(self, pitch):
        self.pitches.append(pitch)

    def pitch_count_score(self):
        n = len(self.pitches)
        if n >= 6:
            return 2
        elif n >= 4:
            return 1
        elif n == 3:
            return 0
        else:
            return -1

    def quality_contact_score(self):
        score = 0
        for pitch in self.pitches:
            if pitch.description in ("foul", "in_play"):
                if pitch.exit_velo > 105:
                    score += 3
                elif pitch.exit_velo > 95:
                    score += 1.5
                elif pitch.exit_velo < 80:
                    score -= 1
        return score

    def count_management_score(self):
        score = 0
        for pitch in self.pitches:
            if pitch.balls > pitch.strikes:
                score += 0
            elif pitch.strikes > pitch.balls:
                score -= 0
    
        # Loop 2 — milestone bonuses, did they reach leverage counts
        for pitch in self.pitches:
            if pitch.balls == 3 and pitch.strikes == 0:
                score += 0  # 3-0, pitcher in trouble
            elif pitch.balls == 3 and pitch.strikes == 1:
                score += 0  # 3-1, still hitter friendly
            elif pitch.balls == 0 and pitch.strikes == 2:
                score -= 0  # 0-2, pitcher dominating  # placeholder so Python doesn't crash
        return score

    def calculate_tor(self):
        score = 50
        score += self.pitch_count_score()
        score += self.quality_contact_score()
        score += self.count_management_score()
        return score
