print('Choose your fighter:')
fighter = input('CAPTAIN JACK SPARROW or SHIA LABEOUF? \n')
if fighter.lower() == 'captain jack sparrow':
    print('''\nYou have chosen to embark on a voyage as Captain Jack Sparrow. 
    You meet Will Turner and break the bad news to him that he is the son
    of a pirate. He can either choose to sail under your command, or not.''')
    will = input('Does he choose to SAIL or NOT? ')
    if will.lower() == 'sail':
        print('''\nExcellent. You visit Tortuga to raid, pillage, plunder and 
        otherwise pilfer your weasely black guts out. You eventually 
        encounter the heart of Davy Jones.''')
        heart = input('STAB the heart? or DON\'T STAB the heart? ')
        if heart.lower() == 'stab':
            print('''\nCongratulations! You sail the seas for eternity, rum 
            is good, and you can make port to get it once every 10 years. Ten 
            years is a long time mate. Even longer given the deficit of rum. 
            But eternity is longer still. And you'll be spending it not dead.
            But Mr. Turner on the other hand? Yeah, he'll be dead. :(''')
        elif heart.lower() == 'don\'t stab':
            print('''\nYou sacrifice the task of being captian of the Flying 
            Dutchman so that Will Turner can stab the heart, free his father,
            and see Elizabeth only once every ten years. It may be a steep 
            price, but it depends on the one day.''')
        else:
            print('\nFor real? That wasn\'t an option. Try again.')
    elif will.lower() == 'not':
        print('''\nWell, that\'s very unfortunate for you. You can\'t bring the
        ship into Tortuga all by your onesie. You end up getting caught by
        Norrington and your sailing days are over... for now.''')
        jail = input('''You can choose to STAY in jail or BREAK OUT with the
        dog\'s key. ''')
        if jail.lower() == 'stay':
            print('\nWell, you\'re dumb. You will never sail the seas again.')
        elif jail.lower() == 'break out':
            print('\nYou continue your life as a pirate doing pirate things.')
        else:
            print('\nFor real? That wasn\'t an option. Try again.')
    else:
        print('\nFor real? That wasn\'t an option. Try again.')
elif fighter.lower() == 'shia labeouf':
    print('''\nYou're walking in the woods. There\'s no one around and your 
    phone is dead. Out of the corner of your eye you spot him. Shia LaBeouf.''')
    shia = input('Do you RUN or FIGHT? ')
    if shia.lower() == 'run':
        print('''\nRunning for your life from Shia LaBeouf... Now it\'s dark
        and you seem to have lost him, but you\'re hopelessly lost yourself.
        Now your leg! Ah! It\'s caught in a bear trap!! ''')
        trap = input('Do you GNAW it off, or STAY to probably die? ')
        if trap.lower() == 'gnaw':
            print('''\n''')
        elif trap.lower() == 'stay':
            print('''\n''')
        else:
            print('\nFor real? That wasn\'t an option. Try again.')  
    elif shia.lower() == 'fight':
        print('''\nHe's brandishing a knife, it\'s Shia LaBeouf, lurking in 
        the shadows.''')
    else:
        print('\nFor real? That wasn\'t an option. Try again.')
else:
    print('\nFor real? That wasn\'t an option. Try again.')