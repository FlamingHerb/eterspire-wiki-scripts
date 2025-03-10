import json
import math
import sys

if __name__ == '__main__':

    
    # Check if arguments are lacking.
    if not len( sys.argv ) == 3:
        sys.exit("""
        WARNING: LACKING ARGUMENT INPUTS!
        Input NUMERICAL MIN_TARGET_LEVEL and MAX_TARGET_LEVEL!
            
        e.g.: python monster_parser.py 42 69
                """)
        
    # Check if both arguments are int
    if sys.argv[1].isdigit() == False or sys.argv[2].isdigit() == False:
        sys.exit("""
        WARNING: ARGUMENTS ARE NOT NUMBERS!
        Input NUMERICAL values in MIN_TARGET_LEVEL and MAX_TARGET_LEVEL!!
            
        e.g.: python monster_parser.py 42 69
        """)

    # Check if min level is greater than max level
    if int(sys.argv[1]) >= int(sys.argv[2]):
        sys.exit("""
        WARNING: MINIMUM LEVEL IS GREATER THAN OR EQUAL TO MAX LEVEL
        Input a lower MIN_TARGET_LEVEL than MAX_TARGET_LEVEL!!
            
        e.g.: python monster_parser.py 42 69
        """)

    target_minimum_level: int = int(sys.argv[1])
    target_maximum_level: int = int(sys.argv[2])

    icons = {
        "Poison": "[[File:Icon-poison.jpg|center|50x50px]][[Status Effects|Poison]]",
        "Slow": "[[File:Icon-slow.jpg|center|50x50px]][[Status Effects|Slow]]",
        "Stun": "[[File:Icon-stun.jpg|center|50x50px]][[Status Effects|Stun]]",
        "Blind": "[[File:Icon-blind.jpg|center|50x50px]][[Status Effects|Blind]]",        
    }

    misc_items = {
        "Bug": [
            "Mandible Pieces",
            "Larva",
            "Rotten Egg"
        ],
        "Animal": [
            "Game Meat",
            "Beast Pelt",
            "Beast Bone"
        ],
        "Mushroom": [
            "Flamecap Fungi",
            "Trumpet Spore",
            "Ghostcap Shroom"
        ],
        "Crab": [
            "Old Coins",
            "Coral Bloom",
            "Seaweed",
        ],
        "Fairy": [
            "Fairy Dust",
            "Fae Gems",
            "Fairy Wings"
        ],
        "Undead": [
            "Skeletal Remnants",
            "Necrotic Ooze",
            "Mourner's Pouch"
        ],
        "Demon": [
            "Demon Blood",
            "Infernal Orbs",
            "Demonic Bracelet"
        ],
        "Reptile": [
            "Fang",
            "Scales",
            "Violet Gemstone"
        ],
        "Rock": [
            "Coin Bag",
            "Blue Gemstone",
            "Red Gemstone"
        ]
    }

    familiars_img = [
        "Magical Familiar 1",
        "Magical Familiar 2 transparent",
        "Magical Familiar 3 transparent",
        "Magical Familiar 4 transparent",
        "Magical Familiar 5 transparent",
        "Magical Familiar Transparent 6",
        "Magical Familiar Transparent 7",
        "Magical Familiar Transparent 8",
        "Magical Familiar Transparent 9",
        "Magical Familiar Transparent 10",
        "Magical Familiar Transparent 11",
        "Magical Familiar Transparent 12",
        "Magical Familiar Transparent 13",
        "Magical Familiar Transparent 14",
        "Magical Familiar Transparent 15",
        "Magical Familiar Transparent 16",
        "Magical Familiar Transparent 17",
        "Magical Familiar Transparent 18",
        "Magical Familiar Transparent 19",
        "Magical Familiar Transparent 20",
    ]

    with open('wikistuff_2.json') as f:
        d = json.load(f)
        text_file = open('new_table.txt', 'w+')
        
        text_file.write('<!-- === START: MONSTER TABLE AREA === -->\n')
        text_file.write('{| class="wikitable" style="border: none; text-align: center; width: 100%; table-layout: fixed;"\n|+\n\n')
        
        for monster in d["monsters"]:
            if monster["name"] == "": continue;
            if not (target_minimum_level <= monster["level"] <= target_maximum_level) : continue;
            
            print(f"Printing {monster['name']} (Level {monster['level']})")
            
            ability_string = ""
            
            if "Stun" in monster["abilities"]: ability_string += icons["Stun"]
            if "Slow" in monster["abilities"]: ability_string += icons["Slow"]
            if "Poison" in monster["abilities"]: ability_string += icons["Poison"]
            if "Blind" in monster["abilities"]: ability_string += icons["Blind"]
            
            if ability_string == "": ability_string = "None"
            
            text_file.write(f"""
<!-- ========== START: Monster Row ========== -->
! rowspan='4' style="background-color: #8A412E; color: white; font-family: 'Verdana'; font-weight: 900; font-size: 14px; text-shadow: black 2px 2px; paint-order: stroke fill; -webkit-text-stroke: 2px black; border: 1px solid black; width: 175px;" |  {monster['img']} {monster['name']} <br/> <small>(Lvl. {monster['level']})</small>
|-
! style='height: 75px;' | Damage
| style='text-align: center; background-color: #f5524b' | {monster['damage']}
! Abiltiies
| colspan='3' style='text-align: center;' | {ability_string}
|-
! Experience
| style='text-align: center; background-color: #9cf54b;' | {monster['exp']} EXP
! Misc.
| style='border-style: solid none; background-color: #E2F3FF;' | [[File:{misc_items[monster['misc']][0]}.png|center|50x50px]][[Miscellaneous Items|{misc_items[monster['misc']][0]} <br/><small>(Level {math.floor(monster['level']/10)*10})</small>]]
| style='border-style: solid none; background-color: #E2F3FF;' | [[File:{misc_items[monster['misc']][1]}.png|center|50x50px]][[Miscellaneous Items|{misc_items[monster['misc']][1]} <br/><small>(Level {math.floor(monster['level']/10)*10})</small>]]
| style='border-left-style: none; background-color: #E2F3FF;' | [[File:{misc_items[monster['misc']][2]}.png|center|50x50px]][[Miscellaneous Items|{misc_items[monster['misc']][2]} <br/><small>(Level {math.floor(monster['level']/10)*10})</small>]]
|-
! Location
| style='text-align: center' | [[Zone: {monster['location']}|{monster['location']}]]
! Familiar
| colspan='3' style='border-left-style: none; background-color: #E2F3FF; text-align: center;' | [[File:{familiars_img[monster['familiar']-1]}.png|center|50x50px]][[Magical Familiar|Magical Familiar #{monster['familiar']}]]
<!-- ========== END: Monster Row ========== -->

<!-- ========== BLANK SPACE ========== -->
|-
| colspan='7' style='background-color: white; border: none; height: 50px;'|
|-
<!-- ========== BLANK SPACE ========== -->
""")
            
        text_file.write('|}\n')
        text_file.write('<!-- === END: MONSTER TABLE AREA === -->')
        
    print("\nTable printed, check out new_table.txt!")