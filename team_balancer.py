from constants import TEAMS
import copy
import random


def balance_teams(teams, cleaned_players, team_length):
   
    balanced_teams={}
    for team in teams:
        balanced_teams[team] =[]
        if len(cleaned_players)>0:
            index_player=0
            for player in cleaned_players:
                while len(balanced_teams[team])<team_length:
                    print(len(cleaned_players))
                    if player['First Name'] not in balanced_teams[team]:
                        
                        
                       
                       popped=cleaned_players.pop(0)
                       balanced_teams[team].append(popped)
                       
                       print(popped)
                       print(len(cleaned_players))
                       
                       continue
                else:
                    break
        elif len(cleaned_players)==0:
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
    print(len(balanced_teams['Panthers']))
    print(len(balanced_teams['Bandits']))
    print(len(balanced_teams['Warriors']))

    with open('team_balancer.txt','w') as my_file:
        my_file.write(f"the panthers, roar{balanced_teams['Panthers']}")
        my_file.write(f" the bandits{balanced_teams['Bandits']}")
        my_file.write(f" The warriors: {balanced_teams['Warriors']}")
