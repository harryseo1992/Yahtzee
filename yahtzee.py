import random
import re


def SMALL_STRAIGHT_POINTS():
    return 30


def LARGE_STRAIGHT_POINTS():
    return 40


def FULL_HOUSE_POINTS():
    return 25


def TOP_HALF_MINIMUM_POINTS_FOR_BONUS():
    return 63


def TOP_HALF_BONUS():
    return 35


def NO_SCORE():
    return -1


def YAHTZEE_SCORE():
    return 50


def YAHTZEE_BONUS_SCORE():
    return 100


def DISPLAY_DICE() -> list:
    return [1, 4, 3, 2, 5]


def print_scoreboard(score: dict):
    print(f"=================\t{score['username']}\t=======================")
    print(f"One:\t{score['1']}\t\tThree of a kind:\t{score['three of a kind']}\tChance:\t{score['chance']}")
    print(f"Two:\t{score['2']}\t\tFour of a kind:\t\t{score['four of a kind']}\tTotal:\t{score['total']}")
    print(f"Three:\t{score['3']}\t\tFull House:\t\t\t{score['full house']}")
    print(f"Four:\t{score['4']}\t\tSmall Straight:\t\t{score['small straight']}")
    print(f"Five:\t{score['5']}\t\tLarge Straight:\t\t{score['large straight']}")
    print(f"Six:\t{score['6']}\t\tYAHTZEE:\t\t\t{score['yahtzee']}")
    print(f"Bonus:\t{score['top half bonus']}\t\tYahtzee counter:\t{score['yahtzee counter']}")


def get_username() -> str:
    """Ask users for their name to be used to create unique scoreboards.

    :return:                A string that represents the user's name.
    """
    user_name = input("Type in your name: ")
    return user_name


def user_scoreboard(user_name: str) -> dict:
    """Form user scoreboard initialized with -1 in all points.

    It forms a yahtzee user scoreboard in dictionary form with all values as -1 to be changed into
    points as game progresses.

    :param user_name:       Name inputted by the user
    :return:                A yahtzee scoreboard in dictionary form
    """
    return {"username": user_name, "1": NO_SCORE(), "2": NO_SCORE(), "3": NO_SCORE(), "4": NO_SCORE(),
            "5": NO_SCORE(), "6": NO_SCORE(), "top half bonus": NO_SCORE(), "three of a kind": NO_SCORE(),
            "four of a kind": NO_SCORE(), "full house": NO_SCORE(), "small straight": NO_SCORE(),
            "large straight": NO_SCORE(), "yahtzee": NO_SCORE(), "yahtzee counter": NO_SCORE(), "chance": NO_SCORE(),
            "total": 0}


# This will be a behemoth of a function with lots of helper functions -> Do I unit test this??
def round_of_yahtzee(scoreboard: dict):
    """Play a round of yahtzee.

    It simulates a round of yahtzee with a maximum of three rolls and options for user to save die,
    release die, and even choose to score mid-session without finishing 3 rolls.

    :param scoreboard:      Scoreboard of a user in dictionary form.
    """
    dice_list = dice_roll(DISPLAY_DICE())
    saved_list = []
    roll_count = 1
    while roll_count < 3:
        print(f"\n=========\t{scoreboard['username']}'s turn\t=============\n")
        print(f"\nCurrent roll count = {roll_count}\n")
        print(f"\nCurrent dice hand: {dice_list}\n")
        print(f"\nCurrent saved dice: {saved_list}\n")
        print("Option (put dice values instead of variables!)================")
        print("roll / save w x y z / release w x y z / submit")
        user_input = input("Type here: ")

        command_input = user_input.split()[0]
        chosen_dice = ''.join(user_input.split()[1:])

        if command_input == 'save':
            dice_list, saved_list = round_of_yahtzee_save(chosen_dice, dice_list, saved_list)

        elif command_input == 'release':
            dice_list, saved_list = round_of_yahtzee_release(chosen_dice, dice_list, saved_list)

        elif command_input == 'roll':
            dice_list = dice_roll(dice_list)
            roll_count += 1

        elif command_input == 'submit':
            return submit_scores(scoreboard, dice_list, saved_list)

    print(f"\nCurrent dice hand: {dice_list}\n")
    print(f"\nCurrent saved dice: {saved_list}\n")
    return submit_scores(scoreboard, dice_list, saved_list)


def round_of_yahtzee_release(chosen_dice: str, dice_list: list, saved_list: list) -> tuple:
    """Control release action.

    :param chosen_dice:         A series of string that represents chosen dice.
    :param dice_list:           A list of dice that are being rolled.
    :param saved_list:          A list of dice that are being saved.
    :precondition:              The chosen_dice must be in saved_list.
    :postcondition:             It promises to return a tuple of two lists that had the values changed.
    :return:                    A tuple of two lists.
    """
    new_dice_list = release_dice(dice_list, saved_list, chosen_dice)
    dice_list = new_dice_list[0]
    saved_list = new_dice_list[1]
    return dice_list, saved_list


def round_of_yahtzee_save(chosen_dice: str, dice_list: list, saved_list: list) -> tuple:
    """Control save action.

    :param chosen_dice:         A series of string that represents chosen dice.
    :param dice_list:           A list of dice that are being rolled.
    :param saved_list:          A list of dice that are being saved.
    :precondition:              The chosen_dice must be in dice_list.
    :postcondition:             It promises to return a tuple of two lists that had the values changed.
    :return:                    A tuple of two lists.
    """
    new_dice_list = choose_dice_handler(dice_list, saved_list, chosen_dice)
    dice_list = new_dice_list[0]
    saved_list = new_dice_list[1]
    return dice_list, saved_list


def submit_scores(scoreboard: dict, dice_list: list, saved_list: list):
    """Control submit action.

    :param scoreboard:          A scoreboard in dictionary form.
    :param dice_list:           A list of dice that are being rolled.
    :param saved_list:          A list of dice that are being saved.
    """
    new_dice_list = convert_and_sort_dice(dice_list, saved_list)
    category = [keys for keys in scoreboard.keys()]
    input_guard = 0
    while input_guard < 1:
        choose_category = input("Input the category you want to submit your scores: ")
        if choose_category not in category:
            print("That's not a valid category.")
        else:
            input_guard += 1
            return score_adder(scoreboard, new_dice_list, choose_category)


def convert_and_sort_dice(rolled_dice: list, saved_dice: list) -> list:
    """Take dice from both rolled list and saved list and sort them.

    It appends dice from both lists in one list, sorts them, and stringify each element,.

    :param rolled_dice:                     List of rolled dice.
    :param saved_dice:                      List of dice that was saved by the user.
    :return:                                List of string elements.

    >>> rolled_list = [3, 1, 2]
    >>> saved_list = [5, 5]
    >>> convert_and_sort_dice(rolled_list, saved_list)
    ['1', '2', '3', '5', '5']

    >>> rolled_list = [1]
    >>> saved_list = [4, 5, 6, 6]
    >>> convert_and_sort_dice(rolled_list, saved_list)
    ['1', '4', '5', '6', '6']
    """
    all_dice = []
    for die in rolled_dice:
        saved_dice.append(die)
    for die in sorted(saved_dice):
        all_dice.append(str(die))
    return all_dice


def dice_roll(list_of_dice: list) -> list:
    """Roll dice

    It simulates dice roll and returns a list of 5 dice with randomized face values.

    :param list_of_dice:    List of dice.
    :return:                List of dice with randomized rolls.
    """
    new_dice_list = []
    for _ in range(len(list_of_dice)):
        new_dice = random.randint(1, 6)
        new_dice_list.append(new_dice)
    return new_dice_list


def choose_dice_handler(rolled_dice: list, saved_dice: list, chosen_dice: str) -> tuple:
    """Choose which di(c)e to keep by putting it in an empty list to save the rolls.

    It allows the user to save dice on the board by inputting a string length of 1 to 4.

    :param rolled_dice:     A list of dice that the user has rolled.
    :param saved_dice:      A list of dice that the user has saved.
    :param chosen_dice:     A string of chosen di(c)e to be saved into an empty list.
                            The numbers must be their values!
    :precondition:          Chosen_dice must be a length of 4 at most, and it should be their values.
    :postcondition:         Returns a tuple of lists (rolled dice and saved dice).
    :return:                A tuple of sorted lists that represent rolled and saved.

    >>> rolled_list = [2, 6, 4, 4, 3]
    >>> saved_roll = []
    >>> dice_chosen = ""
    >>> choose_dice_handler(rolled_list, saved_roll, dice_chosen)
    ([2, 3, 4, 4, 6], [])

    >>> rolled_list = [2, 6, 4, 4, 3]
    >>> saved_roll = []
    >>> dice_chosen = "23363"
    >>> choose_dice_handler(rolled_list, saved_roll, dice_chosen)
    You can't save more than 4 dice.

    >>> rolled_list = [2]
    >>> saved_roll = [3, 4, 4, 6]
    >>> dice_chosen = "2"
    >>> choose_dice_handler(rolled_list, saved_roll, dice_chosen)
    You have reached the maximum allotted capacity. Cannot save more than what you have.
    """
    allotted_dice_face_values = ['1', '2', '3', '4', '5', '6']
    if chosen_dice == '':
        return sorted(rolled_dice), sorted(saved_dice)
    elif len(chosen_dice) > 4:
        print("You can't save more than 4 dice.")
    elif len(saved_dice) == 4:
        print("You have reached the maximum allotted capacity. Cannot save more than what you have.")
    else:
        # saved list is empty and the chosen input numbers are unique
        return choose_dice(allotted_dice_face_values, chosen_dice, rolled_dice, saved_dice)


def choose_dice(allotted_dice_face_values: list, chosen_dice: str, rolled_dice: list, saved_dice: list) -> tuple:
    """Choose dice from a list of dice.

    It appends dice that match the string input into the saved_dice and removes dice from rolled_dice.

    :param allotted_dice_face_values:           A list of all acceptable face values of a die in yahtzee.
    :param chosen_dice:                         A series of string numbers that represent chosen dice.
    :param rolled_dice:                         A list of dice currently being rolled.
    :param saved_dice:                          A list of dice currently being saved.
    :return:                                    A tuple of lists.

    >>> acceptable_dice_value = ['1', '2', '3', '4', '5', '6']
    >>> rolled_list = [2, 4]
    >>> saved_roll = [3, 4, 6]
    >>> dice_chosen = "3"
    >>> choose_dice(acceptable_dice_value, dice_chosen, rolled_list, saved_roll)
    There are no die or dice of those values available in the rolled hand.

    >>> acceptable_dice_value = ['1', '2', '3', '4', '5', '6']
    >>> rolled_list = [2, 3]
    >>> saved_roll = [4, 4, 6]
    >>> dice_chosen = "3"
    >>> choose_dice(acceptable_dice_value, dice_chosen, rolled_list, saved_roll)
    ([2], [3, 4, 4, 6])
    """
    for string_number in list(chosen_dice):
        if int(string_number) not in rolled_dice:
            print("There are no die or dice of those values available in the rolled hand.")
            break
        elif int(string_number) in rolled_dice:
            for index in range(len(chosen_dice)):
                for dice in rolled_dice:
                    if int(chosen_dice[index]) == dice and chosen_dice[index] in allotted_dice_face_values:
                        saved_dice.append(dice)
                        rolled_dice.remove(dice)
        return sorted(rolled_dice), sorted(saved_dice)


def release_dice(rolled_dice: list, saved_dice: list, chosen_dice: str) -> tuple:
    """Choose which di(c)e to release.

    It releases a die/dice based on user's input, pop them from saved_dice and puts them inside
    rolled_dice.

    :param rolled_dice:     List of rolled dice.
    :param saved_dice:      List of dice saved by the user.
    :param chosen_dice:     Chosen di(c)e in string format: e.g. "123" -> chose 1st, 2nd, and 3rd dice.
    :return:                A tuple of two lists of dice after releasing from saved_dice and catching from rolled_dice.

    >>> rolled = [1, 2, 3, 5]
    >>> saved = [5]
    >>> chosen = '5'
    >>> release_dice(rolled, saved, chosen)
    ([1, 2, 3, 5, 5], [])

    >>> rolled = [1, 4, 5]
    >>> saved = [4, 5]
    >>> chosen = '45'
    >>> release_dice(rolled, saved, chosen)
    ([1, 4, 4, 5, 5], [])

    >>> rolled = [1, 4]
    >>> saved = [4, 5, 5]
    >>> chosen = '455'
    >>> release_dice(rolled, saved, chosen)
    ([1, 4, 4, 5, 5], [])

    >>> rolled = [1]
    >>> saved = [4, 4, 5, 5]
    >>> chosen = '4455'
    >>> release_dice(rolled, saved, chosen)
    ([1, 4, 4, 5, 5], [])

    >>> rolled = [1, 4, 4, 5, 6]
    >>> saved = []
    >>> chosen = '4'
    >>> release_dice(rolled, saved, chosen)
    There is nothing to release.

    >>> rolled = [1, 5, 6]
    >>> saved = [4, 4]
    >>> chosen = '45'
    >>> release_dice(rolled, saved, chosen)
    ([1, 4, 5, 6], [4])
    """
    allotted_dice_face_values = ['1', '2', '3', '4', '5', '6']
    if not saved_dice:
        print("There is nothing to release.")
    elif chosen_dice == '':
        return sorted(rolled_dice), sorted(saved_dice)
    elif len(chosen_dice) > len(saved_dice):
        print("You are trying to release more than what you have.")
    else:
        for string_number in list(chosen_dice):
            if int(string_number) not in saved_dice:
                print("There are no die or dice of those values available in the saved hand.")
                break
            elif int(string_number) in saved_dice:
                for index in range(len(chosen_dice)):
                    for dice in saved_dice:
                        if int(chosen_dice[index]) == dice and chosen_dice[index] in allotted_dice_face_values:
                            rolled_dice.append(dice)
                            saved_dice.remove(dice)
            return sorted(rolled_dice), sorted(saved_dice)


def is_scoreboard_all_filled_out(scoreboard: dict) -> bool:
    """Check scoreboard to see if all values inside the keys are integers or not.

    It checks to see if the scoreboard has all the values filled out by integers, thereby ending the game.

    :param scoreboard:      Scoreboard of a user in dictionary form
    :return:                Boolean

    >>> score = {"username": "Harry", "1": NO_SCORE(), "2": NO_SCORE(), "3": NO_SCORE()}
    >>> is_scoreboard_all_filled_out(score)
    False

    >>> score = {"username": "Harry", "1": 0, "2": 0, "3": 0}
    >>> is_scoreboard_all_filled_out(score)
    True
    """
    all_values = [values for values in scoreboard.values()]
    if NO_SCORE() not in all_values:
        return True
    else:
        return False


def upper_section_bonus_checker(score: dict) -> bool:
    """Check to see if the points in the upper section add up to 63 or greater.

    A bonus checker for face values that adds up the numbers to see if they are 63 or greater.

    :param score:           Scoreboard of a user in dictionary form.
    :return:                Boolean

    >>> scoreboard = {"username": "Harry", "1": 6, "2": 12, "3": 18, "4": 24, "5": 30}
    >>> upper_section_bonus_checker(scoreboard)
    True

    >>> scoreboard = {"username": "Harry", "1": 0, "2": 0, "3": 0, "4": 0, "5": 0}
    >>> upper_section_bonus_checker(scoreboard)
    False
    """
    upper_half_categories = ['1', '2', '3', '4', '5', '6']
    sum_list = []
    for keys in score.keys():
        if keys in upper_half_categories and score[keys] > 0:
            sum_list.append(score[keys])
    if sum(sum_list) >= TOP_HALF_MINIMUM_POINTS_FOR_BONUS():
        return True
    else:
        return False


def full_house_checker(rolled_dice: list) -> bool:
    """Check if the rolled dice passes the regex for full house.

    It takes the list of rolled dice and sees if it passes the regex check for full house.

    :param rolled_dice:     List of dice that the user has rolled.
    :return:                Boolean

    >>> rolled = ['1', '1', '1', '2', '2']
    >>> full_house_checker(rolled)
    True

    >>> rolled = ['1', '1', '2', '2', '2']
    >>> full_house_checker(rolled)
    True

    >>> rolled = ['1', '1', '1,' '1', '1']
    >>> full_house_checker(rolled)
    False
    """
    rolled_dice_to_string = ''.join(rolled_dice)

    full_house_three_and_two_regex = re.compile(r"^([1-6])\1{2}([1-6])\2$")
    full_house_two_and_three_regex = re.compile(r"^([1-6])\1([1-6])\2{2}$")

    match_full_house_three_and_two = full_house_three_and_two_regex.search(rolled_dice_to_string)
    match_full_house_two_and_three = full_house_two_and_three_regex.search(rolled_dice_to_string)

    if len(set(rolled_dice)) != 1 and (match_full_house_three_and_two or match_full_house_two_and_three):
        return True
    else:
        return False


def small_straight_checker(rolled_dice: list) -> bool:
    """Check if the rolled dice passes the regex for small straight.

    It takes the list of rolled dice and sees if it passes the regex check for small straight.

    :param rolled_dice:     List of dice that the user has rolled.
    :return:                Boolean

    >>> rolled = ['1', '2', '3', '4', '6']
    >>> small_straight_checker(rolled)
    True

    >>> rolled = ['1', '3', '4', '5', '6']
    >>> small_straight_checker(rolled)
    True

    >>> rolled = ['1', '2', '2', '3', '4']
    >>> small_straight_checker(rolled)
    True

    >>> rolled = ['1', '2', '3', '4', '5']
    >>> small_straight_checker(rolled)
    True
    """
    first_three_string = ''.join(rolled_dice[:3])
    last_three_string = ''.join(rolled_dice[1:4])
    set_string = ''.join(sorted(set(rolled_dice)))

    small_straight_parameter = '123456'

    small_straight_first_three_regex = re.compile(first_three_string)
    small_straight_last_three_regex = re.compile(last_three_string)
    small_straight_set_string_regex = re.compile(set_string)

    match_small_straight_first_three = small_straight_first_three_regex.search(small_straight_parameter)
    match_small_straight_last_three = small_straight_last_three_regex.search(small_straight_parameter)
    match_small_straight_set_string = small_straight_set_string_regex.search(small_straight_parameter)

    if len(set(rolled_dice)) != 1 and \
            (match_small_straight_first_three or match_small_straight_last_three or match_small_straight_set_string):
        return True
    else:
        return False


def large_straight_checker(rolled_dice: list) -> bool:
    """Check if the rolled dice passes the regex for large straight.

    It takes the list of rolled dice and sees if it passes the regex check for large straight.

    :param rolled_dice:     List of dice that the user has rolled.
    :return:                Boolean

    >>> rolled = ['1', '2', '3', '4', '5']
    >>> large_straight_checker(rolled)
    True

    >>> rolled = ['2', '3', '4', '5', '6']
    >>> large_straight_checker(rolled)
    True

    >>> rolled = ['1', '2', '3', '4', '6']
    >>> large_straight_checker(rolled)
    False

    >>> rolled = ['1', '1', '1', '1', '1']
    >>> large_straight_checker(rolled)
    False
    """
    rolled_dice_to_string = ''.join(rolled_dice)

    large_straight_parameter = '123456'

    large_straight_regex = re.compile(rolled_dice_to_string)

    match_large_straight = large_straight_regex.search(large_straight_parameter)

    if match_large_straight:
        return True
    else:
        return False


def yahtzee_checker(rolled_dice: list) -> bool:
    """Check if the rolled dice passes the regex for yahtzee.

    It takes the list of rolled dice and sees if it passes the regex check for yahtzee.

    :param rolled_dice:     List of dice that the user has rolled.
    :return:                Boolean

    >>> rolled = ['1', '1', '1', '1', '1']
    >>> yahtzee_checker(rolled)
    True

    >>> rolled = ['1', '1', '1', '1', '2']
    >>> yahtzee_checker(rolled)
    False
    """
    rolled_dice_to_string = ''.join(rolled_dice)

    yahtzee_regex = re.compile(r"^([1-6])\1{4}$")

    match_yahtzee = yahtzee_regex.search(rolled_dice_to_string)

    if match_yahtzee:
        return True
    else:
        return False


def three_of_a_kind_checker(rolled_dice: list) -> bool:
    """Check if the rolled dice passes the regex for three of a kind.

    It takes the list of rolled dice and sees if it passes the regex check for three of a kind.

    :param rolled_dice:     List of dice that the user has rolled.
    :return:                Boolean

    >>> rolled = ['1', '1', '1', '2', '2']
    >>> three_of_a_kind_checker(rolled)
    True

    >>> rolled = ['1', '1', '1', '1', '2']
    >>> three_of_a_kind_checker(rolled)
    True

    >>> rolled = ['2', '3', '4', '4', '4']
    >>> three_of_a_kind_checker(rolled)
    True
    """
    rolled_dice_to_string = ''.join(rolled_dice)

    three_of_a_kind_regex = re.compile(r"([1-6])\1{2}")

    match_three_of_a_kind = three_of_a_kind_regex.search(rolled_dice_to_string)

    if match_three_of_a_kind:
        return True
    else:
        return False


def four_of_a_kind_checker(rolled_dice: list) -> bool:
    """Check if the rolled dice passes the regex for four of a kind.

    It takes the list of rolled dice and sees if it passes the regex check for four of a kind.

    :param rolled_dice:     List of dice that the user has rolled.
    :return:                Boolean

    >>> rolled = ['1', '1', '1', '2', '2']
    >>> four_of_a_kind_checker(rolled)
    False

    >>> rolled = ['1', '1', '1', '1', '2']
    >>> four_of_a_kind_checker(rolled)
    True

    >>> rolled = ['2', '4', '4', '4', '4']
    >>> four_of_a_kind_checker(rolled)
    True
    """
    # Step 1: Same as three of a kind but should be a regex for 4 repeats
    rolled_dice_to_string = ''.join(rolled_dice)

    four_of_a_kind_regex = re.compile(r"([1-6])\1{3}")

    match_four_of_a_kind = four_of_a_kind_regex.search(rolled_dice_to_string)

    if match_four_of_a_kind:
        return True
    else:
        return False


def score_adder(scoreboard: dict, rolled_dice: list, user_input_for_category: str):
    """Add up scores on the scoreboard.

    It takes the list of rolled dice and category input to see if it passes the regex checks and
    adds up the scores on the scoreboard.

    :param scoreboard:                  Scoreboard of a user in dictionary form.
    :param rolled_dice:                 List of dice that the user has rolled.
    :param user_input_for_category:     Category input in string that has been entered by the user.
    :precondition:                      The category input must be written in correct format.
    :return:                            Scoreboard of a user with the points updated.
    """
    if small_straight_checker(rolled_dice) and user_input_for_category == 'small straight':
        scoreboard['small straight'] = SMALL_STRAIGHT_POINTS()

    elif large_straight_checker(rolled_dice) and user_input_for_category == 'large straight':
        scoreboard['large straight'] = LARGE_STRAIGHT_POINTS()

    elif full_house_checker(rolled_dice) and user_input_for_category == 'full house':
        scoreboard['full house'] = FULL_HOUSE_POINTS()

    elif three_of_a_kind_checker(rolled_dice) and user_input_for_category == 'three of a kind':
        scoreboard['three of a kind'] = sum_all_dice(rolled_dice)

    elif four_of_a_kind_checker(rolled_dice) and user_input_for_category == 'four of a kind':
        scoreboard['four of a kind'] = sum_all_dice(rolled_dice)

    elif yahtzee_checker(rolled_dice) and user_input_for_category == 'yahtzee':
        scoreboard = yahtzee_point_adder(scoreboard)

    elif not yahtzee_checker(rolled_dice) and user_input_for_category == 'yahtzee':
        scoreboard['yahtzee'] = 0
        scoreboard['yahtzee counter'] = 0

    elif user_input_for_category in ['1', '2', '3', '4', '5', '6']:
        scoreboard = top_half_adder(scoreboard, rolled_dice, user_input_for_category)

    elif user_input_for_category == 'chance':
        scoreboard['chance'] = sum_all_dice(rolled_dice)

    return total_point_compiler(scoreboard)


def total_point_compiler(scoreboard: dict):
    """Compile all valid points into total.

    It takes the scoreboard, scrapes all the scores from valid categories, and add up to the total.

    :param scoreboard:          A yahtzee scoreboard in dictionary form.

    >>> score = {"username": "Harry", "1": -1, "2": -1, "3": -1, "4": -1, \
"5": -1, "6": -1, "top half bonus": -1, "three of a kind": -1, \
"four of a kind": -1, "full house": -1, "small straight": -1, \
"large straight": -1, "yahtzee": 50, "yahtzee counter": 1, "chance": -1, \
"total": 0}
    >>> total_point_compiler(score) # doctest: +NORMALIZE_WHITESPACE
    =================	Harry	=======================
    One:	-1		Three of a kind:	-1	Chance:	-1
    Two:	-1		Four of a kind:		-1	Total:	50
    Three:	-1		Full House:			-1
    Four:	-1		Small Straight:		-1
    Five:	-1		Large Straight:		-1
    Six:	-1		YAHTZEE:			50
    Bonus:	-1		Yahtzee counter:	1
    """
    categories_that_count_in_total = ['1', '2', '3', '4', '5', '6', 'full house', 'three of a kind', 'four of a kind',
                                      'small straight', 'large straight', 'bonus', 'yahtzee', 'chance']
    total_point = 0
    for keys in scoreboard.keys():
        if keys in categories_that_count_in_total and scoreboard[keys] != NO_SCORE():
            total_point += scoreboard[keys]
    scoreboard['total'] = total_point
    return print_scoreboard(scoreboard)


def sum_all_dice(rolled_dice: list) -> int:
    """Sum up all dice values.

    It sums up all dice values for three of a kind, four of a kind, and chance.

    :param rolled_dice:     A list of 5 dice.
    :postcondition:         Return a sum of integers.
    :return:                An integer that represents the sum of all dice values.

    >>> list_of_dice = ['1', '2', '3', '4', '5']
    >>> sum_all_dice(list_of_dice)
    15
    """
    sum_list = []
    for die in rolled_dice:
        sum_list.append(int(die))
    return sum(sum_list)


def top_half_adder(scoreboard: dict, rolled_dice: list, user_input_for_face_value: str) -> dict:
    """Add up scores on the scoreboard.

    It takes the list of rolled dice and face value input to pass through a regex check for each sides
    and adds up the scores on the scoreboard.

    :param scoreboard:                  Scoreboard of a user in dictionary form.
    :param rolled_dice:                 List of dice that the user has rolled.
    :param user_input_for_face_value:   Face value input in string that has been entered by the user.
    :precondition:                      The face value input must be written in correct format.
    :return:                            Scoreboard of a user with points added up.

    >>> score = {"username": "Harry", "1": NO_SCORE(), "2": NO_SCORE(), "3": NO_SCORE()}
    >>> rolled = ['1', '1', '1', '2', '2']
    >>> user_input = '1'
    >>> top_half_adder(score, rolled, user_input)
    {'username': 'Harry', '1': 3, '2': -1, '3': -1}

    >>> score = {"username": "Harry", "1": 0, "2": NO_SCORE(), "3": NO_SCORE()}
    >>> rolled = ['1', '1', '1', '2', '2']
    >>> user_input = '1'
    >>> top_half_adder(score, rolled, user_input)
    {'username': 'Harry', '1': 0, '2': -1, '3': -1}
    """
    score_list = []
    if scoreboard[user_input_for_face_value] >= 0:
        scoreboard[user_input_for_face_value] = scoreboard[user_input_for_face_value]
    else:
        for die in rolled_dice:
            if die == user_input_for_face_value and scoreboard[user_input_for_face_value] == NO_SCORE():
                score_list.append(int(die))
        scoreboard[user_input_for_face_value] = sum(score_list)
    return scoreboard


def yahtzee_point_adder(scoreboard: dict) -> dict:
    """Add point for yahtzee.

    After passing yahtzee regex check, it looks at the scoreboard and looks at the yahtzee counter
    to decide how many points to add.

    :param scoreboard:          Scoreboard of a user in dictionary form.
    :return:                    Scoreboard of a user in dictionary form with yahtzee point and counter added.

    >>> score = {"username": "Harry", "yahtzee": NO_SCORE(), "yahtzee counter": NO_SCORE()}
    >>> yahtzee_point_adder(score)
    {'username': 'Harry', 'yahtzee': 50, 'yahtzee counter': 1}

    >>> score = {"username": "Harry", "yahtzee": 0, "yahtzee counter": 0}
    >>> yahtzee_point_adder(score)
    {'username': 'Harry', 'yahtzee': 0, 'yahtzee counter': 0}

    >>> score = {"username": "Harry", "yahtzee": 50, "yahtzee counter": 1}
    >>> yahtzee_point_adder(score)
    {'username': 'Harry', 'yahtzee': 150, 'yahtzee counter': 2}
    """
    if scoreboard['yahtzee counter'] < 0 and scoreboard['yahtzee'] < 0:
        scoreboard['yahtzee counter'] = 1
        scoreboard['yahtzee'] = YAHTZEE_SCORE()
    elif scoreboard['yahtzee counter'] == 0:
        scoreboard['yahtzee counter'] = 0
        scoreboard['yahtzee'] = 0
    else:
        scoreboard['yahtzee counter'] += 1
        scoreboard['yahtzee'] += YAHTZEE_BONUS_SCORE()
    return scoreboard


def menu():
    """Display menu and options for the user to choose.

    ========================================================
    Welcome to Yahtzee! Choose your options!

    1. Let's Yahtzee!
    2. Let's not!
    """
    print("========================================================")
    print("Welcome to Yahtzee! Choose your options!\n")
    print("1. Let's Yahtzee!")
    print("2. Let's not!")
    user_choice = input("What will it be? ")
    execute_order_66 = False
    while not execute_order_66:
        if user_choice == '1':
            game_engine()
        elif user_choice == '2':
            execute_order_66 = True
        else:
            print("You must have typed the wrong option. Please choose between 1 and 2.")
    if execute_order_66 is True:
        quit()


def game_engine():
    """Control the turn order of yahtzee.
    """
    user1_name = get_username()
    user2_name = get_username()
    user1_scoreboard = user_scoreboard(user1_name)
    user2_scoreboard = user_scoreboard(user2_name)
    user1_turn = True
    while True:
        while user1_turn is True:
            round_of_yahtzee(user1_scoreboard)
            user1_turn = user1_turn_controller(user1_scoreboard, user1_turn, user2_scoreboard)
        while user1_turn is False:
            round_of_yahtzee(user2_scoreboard)
            user1_turn = True


def user1_turn_controller(user1_scoreboard: dict, user1_turn: bool, user2_scoreboard: dict) -> bool:
    """Control user 1 turn.

    :param user1_scoreboard:    A scoreboard in dictionary format for user 1.
    :param user1_turn:          A sentinel value that determines the turn.
    :param user2_scoreboard:    A scoreboard in dictionary format for user 2.
    :postcondition:             It will return a boolean to help guide the turns.
    :return:                    A boolean.
    """
    if not is_scoreboard_all_filled_out(user1_scoreboard) and not is_scoreboard_all_filled_out(user2_scoreboard):
        user1_turn = False
    elif is_scoreboard_all_filled_out(user1_scoreboard) and not is_scoreboard_all_filled_out(user2_scoreboard):
        user1_turn = False
    elif not is_scoreboard_all_filled_out(user1_scoreboard) and is_scoreboard_all_filled_out(user2_scoreboard):
        user1_turn = True
    return user1_turn


def user2_turn_controller(user1_scoreboard, user1_turn, user2_scoreboard):
    """Control user 2 turn.

    :param user1_scoreboard:    A scoreboard in dictionary format for user 1.
    :param user1_turn:          A sentinel value that determines the turn.
    :param user2_scoreboard:    A scoreboard in dictionary format for user 2.
    :postcondition:             It will return a boolean to help guide the turns.
    :return:                    A boolean.
    """
    if not is_scoreboard_all_filled_out(user1_scoreboard) and not is_scoreboard_all_filled_out(user2_scoreboard):
        user1_turn = True
    elif is_scoreboard_all_filled_out(user1_scoreboard) and not is_scoreboard_all_filled_out(user2_scoreboard):
        user1_turn = False
    elif not is_scoreboard_all_filled_out(user1_scoreboard) and is_scoreboard_all_filled_out(user2_scoreboard):
        user1_turn = True
    return user1_turn


def main():
    """Drive the program.
    """
    menu()


if __name__ == '__main__':
    main()
