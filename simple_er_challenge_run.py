# a basic challenge run creator

import random

soul_level_1 = "no"
soul_level_cap = ""
class_type = ""

region_lock = "random"
class_weapon = ""

sl_caps = ["1", "69", "75", "90", "120", "150", "300"]
master_class_list = ["Astrologer", "Bandit", "Confessor", "Hero", "Prisoner", "Prophet", "Samurai", "Vagabond", "Warrior", "Wretch"]
melee_class_list = ["Bandit", "Hero", "Prisoner", "Prophet", "Samurai", "Vagabond", "Warrior", "Wretch"]
caster_class_list = ["Astrologer", "Confessor", "Prophet", "Warrior", "Wretch"]
ranged_class_list = ["Astrologer", "Bandit", "Hero", "Prisoner", "Prophet", "Samurai", "Warrior", "Wretch"]

melee_weapon_list = [
    "Colossal", 
    "Fist", 
    "Straight Sword", 
    "Curved Sword",
    "Axe", 
    "Hammers", 
    "Flails", 
    "Great Hammers", 
    "Great Sword", 
    "Great Axe", 
    "Halberd", 
    "Claws", 
    "Curved Great Swords", 
    "Twinblades", 
    "Katanas",
    "Daggers",
    "Thrusting Swords",
    "Heavy Thrusting Swords",
    "Spears", 
    "Great Spears",
    "Reapers", 
    "Whips", 
    "Shield" 
    ]
caster_type_list = [
    "Raya Lucaria", 
    "Carian Royal", 
    "Sellian Sigil", 
    "Gravity", 
    "Volcano Manor", 
    "Prince of Death", 
    "Giants Flames and Flame Sigil", 
    "Two Fingers", 
    "Erdtree Sigil and Ancient Erdtree", 
    "Golden Order", 
    "Clawmark", 
    "Ancient Dragon and Dragon Communion", 
    "Godskin Sigil",
    "Lord of Blood", 
    "Scarlet Wings", 
    "Three Fingers"
    ]
ranged_weapon_list = [
    "Light Bows",
    "Bows",
    "Greatbows", 
    "Crossbows", 
    "Ballistas", 
    ]

def main(class_type):

    soul_level_cap = is_sl1(soul_level_1)
    character_class = get_class_type(class_type)
    region_locked = is_region_locked(region_lock).decode('utf-8', 'ignore')
    class_weapon_to_use = get_weapon_type(class_type)
    print(f"{soul_level_cap} your class will be {character_class} and {class_weapon_to_use}. {region_locked}")

    

def is_sl1(soul_level_1):
    if soul_level_1 == "yes":
        soul_level_cap = b"For this run you will be locked to SL1"
        return soul_level_cap
    else:
        level_cap = random.choice(sl_caps)
        soul_level_cap = f"For this run you will be capped at SL{level_cap}".encode('utf-8')
        return soul_level_cap

def get_class_type(class_type):
    if class_type == "melee":
        character_class = random.choice(melee_class_list)
        return character_class
    elif class_type == "ranged":
        character_class = random.choice(ranged_class_list)
        return character_class
    elif class_type == "caster":
        character_class = random.choice(caster_class_list)
        return character_class
    else:
        character_class = random.choice(master_class_list)
        return character_class
    
def get_weapon_type(class_type):
    if class_type == "melee":
        class_weapon_type = random.choice(melee_weapon_list)
        class_weapon_to_use = f"your weapon type will be: {class_weapon_type}".encode('utf-8')
        return class_weapon_to_use
    elif class_type == "ranged":
        class_weapon_type = random.choice(ranged_weapon_list)
        class_weapon_to_use = f"your weapon type will be: {class_weapon_type}".encode('utf-8')
        return class_weapon_to_use
    elif class_type == "caster":
        class_weapon_type = random.choice(caster_type_list)
        class_weapon_to_use = f"your spell school will be: {class_weapon_type}".encode('utf-8')
        return class_weapon_to_use
    else:
        class_weapon_type_1 = random.choice(melee_weapon_list)
        class_weapon_type_2 = random.choice(ranged_weapon_list)
        class_weapon_type_3 = random.choice(caster_type_list)
        class_weapon_to_use = f"your weapon type is a choice of one of these three: {class_weapon_type_1}, {class_weapon_type_2}, {class_weapon_type_3}".encode('utf-8')
        return class_weapon_to_use
    
def is_region_locked(region_locked):
    if region_locked == "yes":
        region_locked = b"This run is region locked."
        return region_locked
    elif region_locked == "no":
        region_locked = b"This run is not region locked."
        return region_locked
    else:
        random_lock = [b"This run is region locked.", b"This run is not region locked."]
        region_locked = random.choice(random_lock)
        return region_locked


if __name__ == "__main__":
    main()