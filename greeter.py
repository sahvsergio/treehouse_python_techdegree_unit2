import time
import sys

def greet(balanced_teams,teams):
    """
    Create Person
    This path creates a person in the app and save  the information in the database

    Parameters:
    -Requests body Parameter:
        -**person: Person**-> A person model with 1st name, lastname, age, hair color and marital status.

    Returns a person model with 1stname, last lanem, age, hair color and marital status
    """


    
    app_title = 'BASKETBALL TEAM STATS TOOL'
    menu_str='---MENU---'
    instructions = ['Here are your choices', '1) Display Team Stats','2) Quit']
    team_instructions =[' 1) Panthers', '2) Bandits', '3) Warriors']
       

    good_bye='Bye, Thank you for visiting the '
    print(app_title.center(100))
    print(menu_str.center(100))
    
    print()
    print()
    for instruction in instructions:
        print(instruction)
    while True:
        print()
        print()
        selections = input('Enter an option \u25B6'.center(50))
        if selections=='1':    
            for team_instruction in team_instructions:
                print(team_instruction)

            team = input('Enter the team name \u25B6'.center(50))

            if team.title() in teams:
                print(f'Team: {team.title()} stats'.center(127))
                deco='-'*20
                print(deco.center(127))
                print(f'total players:{len(balanced_teams[team.title()])}')
                list_of_heights=[]
                experienced=[]
                inexperienced=[]
                for player in balanced_teams[team.title()]:
                    list_of_heights.append(player['Height'])
                    if player['Experience']==True:
                        experienced.append(player)
                    
                    else:
                        inexperienced.append(player)
                
                print(f'Experienced: {len(experienced)}')
                print(f'Inexperienced: {len(inexperienced)}')
                average_height = (sum(list_of_heights) / len(balanced_teams[team.title()]))
                print(f'Average Height:{average_height:.2f}')
                print()
                print()
                print('players on teams:'.center(127))
                list_of_players=[]
                for player in balanced_teams[team.title()]:
                   list_of_players.append(f'{player['First Name']} {player['Last Name']}')

                player_on_teams=','.join(list_of_players)
                print(player_on_teams)
                
                
            
                
            else:
                print('Please enter a valid option'.center(70))
                
            
        elif selections=='2':
            print()
            print()
            print(f'Thank you for visiting {app_title}.Hope to see you again, soon')
            sys.exit()
        else:
             print('Please enter a valid option'.center(70))