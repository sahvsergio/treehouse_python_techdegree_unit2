import logging
import pdb
import os


logging.basicConfig(filename='data_cleaner.log', level=logging.DEBUG)


def clean_data(players):
    """
    Clean Data

    Args:
        players (List): _description_

    Returns:
        List: _description_
    """
    # creating  the empty new collection
    cleaned_players = []
    try:
        # loop thorugh
        for player in players:
            # creating a new dictionary
            fixed = {}
            #creating the key,value pairs for the fixed dictionary
            logging.info('')
            fixed['Fist Name'] = player['name'].split(' ')[0]
            fixed['Last Name'] = player['name'].split(' ')[1]
            fixed['Guardians'] = player['guardians'].split('and')
            print(f'this is the guardian list{fixed['Guardians']}')
            
            split_height = player['height'].split(' ')
            fixed['Height'] = int(split_height[0])
            #turning the experience into a boolean 
            # by check what the string says
            if player['experience'] == 'YES':
                fixed['Experience'] = True
            else:
                fixed['Experience'] = False
            #appending the resulting dictionary to the initial list
            
            cleaned_players.append(fixed)
        print(cleaned_players)
        #returning the list
        return cleaned_players
    #handling the exception of the constant file not being present
    except FileNotFoundError:
        print('There is no constant files')

def show_stats(team):
    """
    Total players: 6
    Total experienced: 3
    Total inexperienced: 3
    Average height: 42.5
    """
    #total_players=len(teams)
    pass
    

if __name__=='__main__':
  
    print(clean_data.__doc__)
    

