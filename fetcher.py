import csv 

def test_read():
    with open('test.csv', mode=r) as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row['player_name'])

        pass