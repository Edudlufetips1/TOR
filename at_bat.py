class Pitch:
    def __init__(self, pitch_number, exit_velo, description):
        self.pitch_number = pitch_number
        self.exit_velo = exit_velo
        self.description = description


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
        return 0  # placeholder so Python doesn't crash

    def calculate_tor(self):
        score = 50
        score += self.pitch_count_score()
        score += self.quality_contact_score()
        score += self.count_management_score()
        return score