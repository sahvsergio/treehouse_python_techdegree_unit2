from constants import TEAMS
import copy
import random



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
            #appending the player to the team
            if len(balanced_teams[team])==0:
                balanced_teams[team].append(player)
                
                
            
            elif len(balanced_teams[team])<team_length :
                status = balanced_teams[team][-1]['Experience']
                if status!=player['Experience']:
                    balanced_teams[team].append(player)
        
                    
                    
               
    
         
                
                
                    
                    
                    
                
                
                    
                
            
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
    
        