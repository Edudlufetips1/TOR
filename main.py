from at_bat import AtBat, Pitch


def main():
    print("Welcome to TOR: True Offensive Rating")

    ab = AtBat("Aaron Judge")

    ab.add_pitch(Pitch(1, 0, "ball", 1, 0))
    ab.add_pitch(Pitch(2, 98, "foul", 1, 1))
    ab.add_pitch(Pitch(3, 107, "in_play", 1, 2))

    print(f"Player: {ab.player_name}")
    print("Pitch Count Score:", ab.pitch_count_score())
    print("Quality Contact Score:", ab.quality_contact_score())
    print("Count Management Score:", ab.count_management_score())
    print("TOR:", ab.calculate_tor())


if __name__ == "__main__":
    main()