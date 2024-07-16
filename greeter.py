import time
import sys

def greet(teams):
    """ creates an inital_menu"""

    
    app_title = 'BASKETBALL TEAM STATS TOOL'
    instructions = ['Here are your choices', '1. Display Team Stats','2. Quit']
    good_bye='Bye, Thank you for visiting the '
        
    
    print(155*' ', 30*'*')
    #creating the lower part of the box by multiplying a string
    # printing the highscore at the top
    print(f'{app_title}'.center(127))
    time.sleep(3)
    for instruction in instructions:
        if instruction=='2. Quit':
            print(f'{instruction}'.center(113))
            
        else:
            print(f'{instruction}'.center(127))    
        time.sleep(3)
    
    

    
    print(155*' ', 30*'*')
    print()
    print()
    while True:
        selections = input('Enter an option \u25B6'.center(70))
        if selections=='1':
             team = input('Please enter a team \u25B6'.center(70))
             if team.title() in teams:
                 return team.title()
                 continue
                 
                 
             else:
                 print('Please enter a valid option'.center(70))
                
            
        elif selections=='2':
            print()
            print()
            print(f'Thank you for visiting {app_title}.Hope to see you again, soon')
            sys.exit()
        else:
             print('Please enter a valid option'.center(70))





