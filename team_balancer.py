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
        player_index=0
        while player_index<len(cleaned_players):
            #looping through the list of players:
            for team in teams: 
                #appending the player to the team if 
                if len(balanced_teams[team])<team_length:
                    balanced_teams[team].append(cleaned_players[player_index])
                    player_index=+1
                    if player_index>=len(cleaned_players):
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
    
        