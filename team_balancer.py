from constants import TEAMS
import copy
import random


def balance_teams(teams, cleaned_players, team_length):
    """_summary_

    Args:
        teams (_type_): _description_

    """
    # creating an empty dictionary to hold balanced  player teams
    # creating an empty dictionary to hold balanced  player teams
    balanced_teams = {}
    # loop through the teams
    for team in teams:
        # making the teams the keys of the dictionary,
        # initializing them with a value of an empty list
        balanced_teams[team] = []

    # starting the index at 0
    player_index = 0
    # looping through the list of players:
    while player_index < len(cleaned_players):
        for team in teams:
            if len(balanced_teams[team]) < team_length:
                # appending the player to the team
                balanced_teams[team].append(cleaned_players[player_index])
                # incrementing the index
                player_index += 1
                if player_index >= len(cleaned_players):
                    break

    print(f"the panthers, roar{balanced_teams['Panthers']}")
    print()
    print()
    print(f" the bandits{balanced_teams['Bandits']}")
    print()
    print()
    print(f" The warriors: {balanced_teams['Warriors']}")

    print(len(balanced_teams['Bandits']))
    print(len(balanced_teams['Warriors']))
    print(len(balanced_teams['Panthers']))
