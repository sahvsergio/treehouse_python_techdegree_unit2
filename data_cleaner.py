import logging
import pdb
import os


logging.basicConfig(filename='data_cleaner.log', level=logging.DEBUG)


def clean_data(players):
    """
    Create Person
    This path creates a person in the app  and save  \
    the information in the database
    Parameters:
    -Requests body Parameter:
        -**person:Person**-> A person model with 1st name,\
        lastname, age, hair color and \
        marital status.

    Returns a person model with 1stname, \
        last lanem , age, hair color and marital status
    """
    # creating  the empty new collection
    cleaned_players = []
    try:
        # loop thorugh players
        for player in players:
            # creating a new dictionary
            fixed = {}
            #creating the key,value pairs for the fixed dictionary
            logging.info('')
            fixed['First Name'] = player['name'].split(' ')[0]
            fixed['Last Name'] = player['name'].split(' ')[1]
            fixed['Guardians'] = player['guardians'].split('and')
            #print(f'this is the guardian list{fixed['Guardians']}')

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

        #returning the list
        return cleaned_players
        #handling the exception of the constant file not being present
    except FileNotFoundError:
        print('There is no constant files')


if __name__ == '__main__':

    print(clean_data.__doc__)

