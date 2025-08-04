from random import sample, choices

numrolls = 2
allow_dupes = "no"
characters = ""

nightfarers = ['Wylder', 'Raider', 'Guardian', 'Duchess', 'Executor', 'Ironeye', 'Revenant', 'Recluse']

def main(numrolls, allow_dupes):
    numrolls = int(numrolls)

    if allow_dupes == "yes":
        characters = dupe_is_allowed(allow_dupes)
        print(f"For {numrolls} players with duplicates allowed you have been given {characters} to play for this expedition. GL, HF!")
        return characters
    
    else:
        characters = no_dupe_allowed(allow_dupes)
        print(f"For {numrolls} player(s) you have been given {characters} to play for this expedition. GL, HF!")
        return characters
    
def dupe_is_allowed(allow_dupes):

    if allow_dupes == "yes":
        characters = random.choices(nightfarers, k=numrolls)
        characters = " and ".join(characters)
        return characters
    
def no_dupe_allowed(allow_dupes):

    if allow_dupes == "no":
        characters = random.sample(nightfarers, numrolls)
        characters = " and ".join(characters)
        return characters

if __name__ == "__main__":
    main(numrolls)