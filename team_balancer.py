from constants import TEAMS
import copy



def balance_teams(teams, cleaned_players,team_length):
    """_summary_

    Args:
        teams (_type_): _description_
        
    """
    balanced_teams={}
    for team in teams:
      balanced_teams[team]=' '
    #print(balanced_teams)
    for player in cleaned_players:
        balanced_teams[team]=player
    print(balanced_teams)

    
        
        
        
        
        
   
    
 
            
    
            
        