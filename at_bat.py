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

    def calculate_tor(self):
        """
        The 'Secret Sauce' formula. 
        Starts at a base of 50 and adjusts based on process.
        """
        score = 50 
        return score
        