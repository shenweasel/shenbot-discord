# a basic challenge run creator

from random import choice

soul_level_1 = "no"
soul_level_cap = ""
job_type = ""
sote = ""
sote_rule = ""
sote_weapon_rule = ""

region_lock = "either"
class_weapon = ""

sl_caps = ["1", "69", "75", "90", "120", "150", "300"]
master_job_list = ["Astrologer", "Bandit", "Confessor", "Hero", "Prisoner", "Prophet", "Samurai", "Vagabond", "Warrior", "Wretch"]
melee_job_list = ["Bandit", "Hero", "Prisoner", "Prophet", "Samurai", "Vagabond", "Warrior", "Wretch"]
caster_job_list = ["Astrologer", "Confessor", "Prophet", "Warrior", "Wretch"]
ranged_job_list = ["Astrologer", "Bandit", "Hero", "Prisoner", "Prophet", "Samurai", "Warrior", "Wretch"]

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
    "Shield", 
    ]
sote_melee_weapon_list = [
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
    "Shield", 
    "Beast Claws (SoTE) - Use regular claws until SoTE", 
    "Thrusting Shields (SoTE) - Use any shield until SoTE", 
    "Light Greatswords (SoTE) - Use any greatsword until SoTE", 
    "Great Katanas (SoTE) - Use any katana until SoTE", 
    "Backhand Blades (SoTE) - Use any melee weapon until SoTE", 
    "Hand-to-Hand Arts (SoTE) - Use a Fist weapon until SoTE"
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
    "Three Fingers",
    "Cold Sorceries",
    "Thorn Sorceries",
    ]
ranged_weapon_list = [
    "Light Bows",
    "Bows",
    "Greatbows", 
    "Crossbows", 
    "Ballistas", 
    "Tools: Any",
    ]
sote_ranged_weapon_list = [
    "Light Bows",
    "Bows",
    "Greatbows", 
    "Crossbows", 
    "Ballistas", 
    "Tools: Any",
    "Throwing Blades (SoTE) - combine with Tools: Any",
    "Perfume Bottles (SoTE) - combine with Tools: Any",
    ]

def main(job_type):

    soul_level_cap = is_sl1(soul_level_1)
    character_class = get_job_type(job_type)
    region_locked = is_region_locked(region_lock)
    sote_weapon_rule = get_sote_weapon_rule(sote, sote_rule)
    job_weapon_to_use = get_weapon_type(job_type, sote_weapon_rule)
    sote_rule = is_sote(sote)
    print(f"{soul_level_cap} your class will be {character_class} and {job_weapon_to_use}. {region_locked} {sote_rule}")
    

def is_sl1(soul_level_1):
    if soul_level_1 == "yes":
        soul_level_cap = "For this run you will be locked to SL1"
        return soul_level_cap
    else:
        level_cap = choice(sl_caps)
        soul_level_cap = f"For this run you will be capped at SL{level_cap}"
        return soul_level_cap


def get_job_type(job_type):
    if job_type == "melee":
        character_class = choice(melee_job_list)
        return character_class
    elif job_type == "ranged":
        character_class = choice(ranged_job_list)
        return character_class
    elif job_type == "caster":
        character_class = choice(caster_job_list)
        return character_class
    else:
        character_class = choice(master_job_list)
        return character_class


def is_sote(sote):
    if sote == "yes":
        sote_rule = "This run allows Scadu Tree Fragments."
        return sote_rule
    elif sote == "no":
        sote_rule = "This run does not allow Scadu Tree Fragments."
        return sote_rule
    elif sote == "nosote":
        sote_rule = "Shadows of the Erdtree is not included for this run."
        return sote_rule
    else:
        sote_rule = choice(["This run allows Scadu Tree Fragments.", 
                       "This run does not allow Scadu Tree Fragments.", 
                       "Shadows of the Erdtree is not included for this run."
                   ])
        sote_rule = "".join(sote_rule)
        return sote_rule


def get_sote_weapon_rule(sote, sote_rule):
    if sote == "yes" or sote_rule == "no":
        sote_weapon_rule = "yes"
    elif sote == "nosote":
        sote_weapon_rule = "nosote"
    else:
        if sote_rule == "Shadows of the Erdtree is not included for this run.":
            sote_weapon_rule = "nosote"
        else:
            sote_weapon_rule = "yes"
    return sote_weapon_rule


def get_weapon_type(job_type, sote_weapon_rule):
    if sote_weapon_rule == "yes" or sote_weapon_rule == "no":
        sote_weapon_rule = "yes"
    if job_type == "melee" and sote_weapon_rule == "nosote":
        job_weapon_type = choice(melee_weapon_list)
        job_weapon_to_use = f"your weapon type will be: {job_weapon_type}"
        return job_weapon_to_use
    elif job_type == "ranged"and sote_weapon_rule == "nosote":
        job_weapon_type = choice(ranged_weapon_list)
        job_weapon_to_use = f"your weapon type will be: {job_weapon_type}"
        return job_weapon_to_use
    elif job_type == "caster"and sote_weapon_rule == "nosote":
        job_weapon_type = choice(caster_type_list)
        job_weapon_to_use = f"your spell school will be: {job_weapon_type}"
        return job_weapon_to_use
    elif job_type == "melee" and sote_weapon_rule == "yes":
        job_weapon_type = choice(sote_melee_weapon_list)
        job_weapon_to_use = f"your weapon type will be: {job_weapon_type}"
        return job_weapon_to_use
    elif job_type == "ranged" and sote_weapon_rule == "yes":
        job_weapon_type = choice(sote_ranged_weapon_list)
        job_weapon_to_use = f"your weapon type will be: {job_weapon_type}"
        return job_weapon_to_use
    elif job_type == "any" and sote_weapon_rule == "yes":
        job_weapon_type_1 = choice(sote_melee_weapon_list)
        job_weapon_type_2 = choice(sote_ranged_weapon_list)
        job_weapon_type_3 = choice(caster_type_list)
        job_weapon_to_use = f"your weapon type is a choice of one of these three: {job_weapon_type_1}, {job_weapon_type_2}, {job_weapon_type_3}"
        return job_weapon_to_use
    elif job_type == "any" and sote_weapon_rule == "nosote":
        job_weapon_type_1 = choice(melee_weapon_list)
        job_weapon_type_2 = choice(ranged_weapon_list)
        job_weapon_type_3 = choice(caster_type_list)
        job_weapon_to_use = f"your weapon type is a choice of one of these three: {job_weapon_type_1}, {job_weapon_type_2}, {job_weapon_type_3}"
        return job_weapon_to_use

    
def is_region_locked(region_locked):
    if region_locked == "yes":
        region_locked = "This run is region locked."
        return region_locked
    elif region_locked == "no":
        region_locked = "This run is not region locked."
        return region_locked
    else:
        random_lock = ["This run is region locked.", 
                       "This run is not region locked."]
        region_locked = choice(random_lock)
        return region_locked
    


if __name__ == "__main__":
    main()