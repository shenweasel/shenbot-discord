from bs4 import BeautifulSoup
import requests

card_name = ""
card_stats = ""
abiity = ""
agamotto_skill_cards = {
        "windsofwatoomb": "Spell01Agamotto", 
        "temporalmanipulation": "Spell02Agamotto",
        "imagesofikonn": "Spell03Agamotto",
        "boltsofbalthakk": "Spell04Agamotto"    
    }

def main(card_name):
    
    content = get_content(card_name)
    ability = get_card_ability(content).decode('utf-8', 'ignore')
    ability = verify_ability(ability)
    card_stats = get_card_stats(content).decode('utf-8', 'ignore')
    card_name =  prettify_card_name(card_name)

    print(f"{card_name} is {card_stats} and {ability}")
    return card_name, card_stats, ability


def get_card_name(card_name):

    card_name_stripped = card_name.replace(" ", "").replace("'", "").strip().casefold()
    agamotto_skill_cards = {
        "windsofwatoomb": "Spell01Agamotto", 
        "temporalmanipulation": "Spell02Agamotto",
        "imagesofikonn": "Spell03Agamotto",
        "boltsofbalthakk": "Spell04Agamotto"    
    }
    if card_name_stripped in agamotto_skill_cards:
        card_name_stripped = agamotto_skill_cards[card_name_stripped]
    return card_name_stripped

def get_content(card_name):
    url = "https://snap.fan/cards/"
    card_name_stripped = get_card_name(card_name)
    snap_url = (url + card_name_stripped).strip()
    content = requests.get(snap_url)

    if content.status_code != 200:
        card_name = input("Card Name? ").replace(" ", "").strip()
        snap_url = (url + card_name).strip()
    else:
        print(f"Get Request Status code is: {content.status_code} OK.")

    content.encoding = 'utf-8'

    return content
    
def get_card_ability(content):
    soup = BeautifulSoup(content.text, 'lxml')   
    ability_elem = soup.find(class_="d-none d-lg-block")
    if ability_elem:
        ability = ability_elem.get_text().replace("\n", " ").replace("Description", "").strip()
        ability_type = f"{ability}".encode('utf-8')
    else:
        ability_type = b"Ability not found"
    return ability_type

def verify_ability(ability):
    
    exclude_abilities = ("My secret power is that I get things done.", 
                       "Let's move, X-Men.",
                       "It's clobberin' time!",
                       "We've got to save this city.",
                       "Foolish rabble! You are beneath me!",
                       "HULK SMASH!",
                       "I'm gonna blast you!",
            )

    for phrase in exclude_abilities:
        if phrase in ability:
            ability = b"has no ability."
            ability = ability.decode('utf-8', 'ignore')
            return ability
        
    return ability
    
def get_card_stats(content):
    soup = BeautifulSoup(content.text, 'lxml')
    card_stats = b"Stats not found"
    h3_elem = soup.find("h3", class_="mt-3")
    if h3_elem:
        ul_elem = h3_elem.find_next("ul")
        if ul_elem:
            cost = power = None
            for li in ul_elem.find_all("li"):
                text = li.get_text(strip=True)
                if text.startswith("Type: Spell"):
                    type = text.replace("Type: Spell", "Skill").strip()
                elif text.startswith("Type: Character"):
                    type = text.replace("Type: Character", "Character").strip()
                if text.startswith("Cost:"):
                    cost = text
                elif text.startswith("Power:"):
                    power = text
            if type == "Character":
                card_stats = f"a {type} card with {cost} and {power}".encode('utf-8', 'ignore')
            else:
                card_stats = f"a {type} card with {cost}".encode('utf-8', 'ignore')
    return card_stats

def prettify_card_name(card_name):
    card_name_split = card_name.split()
    card_name_upper = [word.capitalize() for word in card_name_split]
    card_name = " ".join(card_name_upper)
    return card_name

if __name__ == "__main__":
    main()