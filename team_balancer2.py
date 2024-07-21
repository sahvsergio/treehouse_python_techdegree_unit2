import random
import copy



def balance_teams(teams, cleaned_players, team_length):
    """_summary_

    Args:
        teams (_type_): _description_
        
    """
    # creating an empty dictionary to hold balanced  player teams
    balanced_teams = {}
    # loop through the teams
    for team in teams:
        # making the teams the keys of the dictionary,
        # initializing them with a value of an empty list
        balanced_teams[team] = []
        # looping through the list of players:
        while cleaned_players:
            # appending the player to the team
            for player in cleaned_players:
                if len(balanced_teams[team]) == 0:
                    balanced_teams[team].append(player)
                    break
                cleaned_players.pop(0)

                if len(balanced_teams[team]) < team_length:
                    status = balanced_teams[team][-1]['Experience']
                    if status != player['Experience']:
                        continue
                balanced_teams[team].append(player)
                break
        else:
            continue

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
