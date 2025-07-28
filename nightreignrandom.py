import random

numrolls = "2"
allow_dupes = "no"
characters = ""

def main(numrolls):
    numrolls = int(numrolls)

    char = ['Wylder', 'Raider', 'Guardian', 'Duchess', 'Executor', 'Ironeye', 'Revenant', 'Recluse']
    if numrolls > 1:  
        characters = random.sample(char, numrolls)
        characters = " and ".join(characters)
        
        print(f"For {numrolls} players with {allow_dupes} you have been given {characters} to play for this expedition. GL, HF!")
        return characters

    else:
        characters = random.choice(char)
        characters = f"{characters}"
        print(f"For {numrolls} player you have been given {characters} to play for this expedition. GL, HF!")
        
    return characters

if __name__ == "__main__":
    main(numrolls, allow_dupes)