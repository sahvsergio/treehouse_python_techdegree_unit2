from constants import TEAMS
import copy



def balance_teams(teams, cleaned_players,team_length):
    """_summary_

    Args:
        teams (_type_): _description_
        
    """
    #creating an empty dictionary to hold balanced  player teams
    balanced_teams={}
    #loop through the teams
    for team in teams:
        # making the teams the keys of the dictionary, 
        # initializing them with a value of an empty list
        balanced_teams[team]=[]
        #looping through the list of players:
        for player in cleaned_players:
            #appending 
            balanced_teams[team].append(player)
            if len(balanced_teams[team])<team_length :
            
                continue
            else:
                break
    print(len(balanced_teams['Panthers']))
    print(len(balanced_teams['Bandits']))
    print(len(balanced_teams['Warriors']))
        