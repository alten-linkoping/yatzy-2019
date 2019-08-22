from typing import List, Optional, Dict
from yatzyapi import YatzyApi
import random

REROLLS = 3

def roll_dice(number_of_dice:int=5) -> List[int]:
    return[random.randint(1,6) for _ in range(0,number_of_dice)]




UPPER_SEC=["once","twos","threes","fours","fives","sixes","_bonus"]
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
    for player in scores:
        print(f'PLAYER: {player["name"]}')
        for name in UPPER_SEC:
            print(f'{name}: {player["upper_section"][name]}')
        print("----------------------------------------")
        for name in LOWER_SEC:
            print(f'{name}: {player["lower_section"][name]}')
        print("========================================")
        print(f'Total Score: {player["total_score"]}')
        print("****************************************")
        print("****************************************")



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
            dice.extend(roll_dice(5-len(dice)))
            print_dice(dice)
            if i < REROLLS -1:
                if not should_do_reroll():
                    break

                keep_dice_str = input("keep dice, give indenes seperated by space: ")
                keep_dice = list(map(int, keep_dice_str.split()))
                print(f'Keeping dice: {keep_dice}')
                dice = [dice[idx] for idx in keep_dice]

        print(f'Your final dice are: {dice}')

        chosen_option = choose_from_options(api.get_options(game_id,current_player, dice), [*LOWER_SEC, *UPPER_SEC])
        print(f'You choosed {chosen_option}')
        current_player, scores = api.submit_decision(game_id, current_player,dice, chosen_option)
        print_scoreboard(scores)