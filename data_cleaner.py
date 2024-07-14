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
    # loop thorugh
    for player in players:
        #
        # creating a new dictionary
       fixed = {}
       # creating the key,value pairs for the fixed dictionary
       fixed['Fist Name'] = player['name'].split(' ')[0]
       fixed['Last Name'] = player['name'].split(' ')[1]
       fixed['Guardians'] = player['guardians']
       split_height = player['height'].split(' ')
       fixed['Height'] = int(split_height[0])

       if player['experience'] == 'YES':
           fixed['Experience'] = True
       else:
           fixed['Experience'] = False
       cleaned_players.append(fixed)

    return cleaned_players

if __name__=='__main__':
  
    print(clean_data.__doc__)

