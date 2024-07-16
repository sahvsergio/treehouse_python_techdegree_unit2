
from constants import PLAYERS
from constants import TEAMS
from data_cleaner import clean_data
from team_balancer import balance_teams
from greeter import greet
import copy


def main():

     #read data for both teams and players
     player_list = copy.deepcopy(PLAYERS)
     teams=copy.deepcopy(TEAMS)
     #
     cleaned_players= clean_data(player_list)
     print(cleaned_players)
     
     #team_length=len(cleaned_players)//len(teams)
     #balanced_teams=balance_teams(cleaned_players, teams, team_length)
    
    
   

if __name__=='__main__':
    main()
   







       

   
 

   