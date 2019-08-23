from typing import List, Optional, Dict
from yatzyapi import YatzyApi
import random

REROLLS = 3
NUMBER_OF_DICE = 5

def roll_dice(number_of_dice:int=NUMBER_OF_DICE) -> List[int]:
    return[random.randint(1,6) for _ in range(0,number_of_dice)]




UPPER_SEC=["ones","twos","threes","fours","fives","sixes","_bonus"]
LOWER_SEC=[
    "one_pair",        
    "two_pairs",       
    "three_of_a_kind", 
    "four_of_a_kind",  
    "small_straight",  
    "large_straight",  
    "full_house",      
    "chance",          
    "yatzy",
]

def print_scoreboard(scores):
    global LOWER_SEC
    global UPPER_SEC
    print("----------------------------------------")
    for player in scores:
        print(f'PLAYER: {player["name"]}')
        for name in UPPER_SEC:
            print(f'{name}: {player["upper_section"][name]}')
        print("----------------------------------------")
        print(f'total score: {player["upper_section"]["total_score"]}')
        print("----------------------------------------")
        for name in LOWER_SEC:
            print(f'{name}: {player["lower_section"][name]}')
        print("----------------------------------------")
        print(f'total score: {player["lower_section"]["total_score"]}')
        print("----------------------------------------")
        print("========================================")
        print(f'Total Score: {player["total_score"]}')
        print("****************************************")
        print("****************************************")

def print_scoreboard_matrix(scores):
    global LOWER_SEC
    global UPPER_SEC
    rows= {name:[] for name in [*LOWER_SEC,*UPPER_SEC]}
    rows["name"]=[]
    rows["total_score_upper"]=[]
    rows["total_score_lower"]=[]
    rows["total_score_final"]=[]
    for idx, player in enumerate(scores):
        rows["name"].append(player["name"])
        for name in UPPER_SEC:
            val = player["upper_section"][name]
            rows[name].append(str(val) if val is not None else "[ ]")
        rows["total_score_upper"].append(str(player["upper_section"]["total_score"]))
        for name in LOWER_SEC:
            val = player["lower_section"][name]
            rows[name].append(str(val) if val is not None else "[ ]")
        rows["total_score_lower"].append(str(player["lower_section"]["total_score"]))
        rows["total_score_final"].append(str(player["total_score"]))
    
    out = [["Score Type",*rows["name"]]]
    for name in UPPER_SEC:
        out.append([name,*rows[name]])
    out.append(["total_score", *rows["total_score_upper"]])
    for name in LOWER_SEC:
        out.append([name,*rows[name]])
    out.append(["total_score",*rows["total_score_lower"]])
    out.append(["total_score", *rows["total_score_final"]])

    col_width = max(len(word) for row in out for word in row) + 2  # padding
    num_cols = len(out[0])
    cnt = 0
    print("".join(["-" for _ in range(col_width*num_cols)]))
    for row in out:
        if row[0] == "total_score":
            cnt += 1
            if cnt <3:
                print("".join(["-" for _ in range(col_width*num_cols)]))
            else:
                print("".join(["=" for _ in range(col_width*num_cols)]))
        print("".join(word.ljust(col_width) for word in row))
        if row[0] == "total_score" and cnt <3:
            print("".join(["-" for _ in range(col_width*num_cols)]))

    print("".join(["-" for _ in range(col_width*num_cols)]))


def choose_viable_number(max_val:int):
    ans: Optional[int] = None
    while ans is None:
        try:
            user_ans = int(input("Choose option number: "))
        except ValueError:
            print("You need to input a valid number")
            continue
        if user_ans >= 0 and user_ans <= max_val:
            ans= user_ans
            break
        else:
            print(f"Choose a number between 0 and {max_val}")
    return ans


def choose_from_options(options:Dict[str,int], order:List[str]):
    print("Your options are")
    print("Option number: option name - points")
    ordered_options: List[str] = []
    cnt = 0
    for name in order:
        if name in options.keys():
            ordered_options.append(name)
            print(f'option {cnt}: {name} - {options[name]}')
            cnt += 1
    
    option_number = choose_viable_number(cnt-1)
    return ordered_options[option_number]


def print_dice(dice:List[int]):
    for idx, die in enumerate(dice):
        print(f'{idx}: {die}')

def should_do_reroll() -> bool:
    ans: Optional[bool] = None
    while ans is None:
        do_reroll = input("Do you want to reroll anything?[y/n]: ")
        if do_reroll.lower().strip() in ["no","n"]:
            ans = False
        elif do_reroll.lower().strip() in ["yes","y"]:
            ans = True
        else:
            print(f'{do_reroll} is not a valid answer')
    return ans


if __name__ == "__main__":
    api = YatzyApi("http://10.46.52.103:5000")

    player_names_str = input("Add player names seperated with space: ")
    player_names: List[str] = []
    for name in player_names_str.split():
        player_names.append(name.strip())
    
    print(f"Creating game with players: {player_names}")
    game_data = api.new_game(player_names)
    if game_data is None:
        print("Could not create a new game")
        print("Exiting...")
        exit(-1)

    game_id = int(game_data["game_id"])
    print("Game created successfully")

    current_player = api.start_game(game_id)

    while current_player is not None:
        print(f"Current Player: {current_player}")
        dice: List[int] = []
        for i in range(REROLLS):
            dice.extend(roll_dice(NUMBER_OF_DICE-len(dice)))
            print_dice(dice)
            if i < REROLLS -1:
                if not should_do_reroll():
                    break
                
                accaptable_keep_dice = False
                while not accaptable_keep_dice:
                    keep_dice_str = input("keep dice, give indices seperated by space: ")
                    keep_dice_indices = list(map(int, keep_dice_str.split()))
                    if not [keep_dice_idx for keep_dice_idx in keep_dice_indices if keep_dice_idx >=NUMBER_OF_DICE and keep_dice_idx >=0]:
                        accaptable_keep_dice= True
                    else:
                        print(f"Values must be less than {NUMBER_OF_DICE}")

                print(f'Keeping dice: {keep_dice_indices}')
                dice = [dice[idx] for idx in keep_dice_indices]

        print(f'Your final dice are: {dice}')

        chosen_option = choose_from_options(api.get_options(game_id,current_player, dice), [*LOWER_SEC, *UPPER_SEC])
        print(f'You choosed {chosen_option}')
        current_player, scores = api.submit_decision(game_id, current_player,dice, chosen_option)
        print_scoreboard_matrix(scores)