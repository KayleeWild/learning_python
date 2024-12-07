#CHOOSE YOUR OWN ADVENTURE PROJECT!!#

from playsound import playsound

print('''\nWARNING: This adventure uses audio clips. Audio will play at the
beginning and the end. You\'ll get a differnt audio depending on which path
you choose. If you would like to use headphones, please put them in now.''')
input('Press the Enter key to continue: ')
playsound('week6/audio/choose_your_fighter.aiff')
print('\nChoose your fighter:')
fighter = input('CAPTAIN JACK SPARROW or SHIA LABEOUF? \n')
#1.0.0
if fighter.lower() == 'captain jack sparrow':
    print('''\nYou have chosen to embark on a voyage as Captain Jack Sparrow. 
You meet Will Turner and break the bad news to him that he is the son
of a pirate. He can either choose to sail under your command, or not.''')
    will = input('''Does he choose to SAIL or NOT? (or do you get CAPTURED
while he\'s deciding?) ''')
    #1.1.0
    if will.lower() == 'sail':
        print('''\nExcellent. You visit Tortuga to raid, pillage, plunder and 
otherwise pilfer your weasely black guts out. You eventually 
encounter the heart of Davy Jones.''')
        heart = input('STAB the heart? or DON\'T STAB the heart? ')
        #1.1.1
        if heart.lower() == 'stab':
            print('''\nCongratulations! You sail the seas for eternity, rum 
is good, and you can make port to get it once every 10 years. Ten 
years is a long time mate. Even longer given the deficit of rum. 
But eternity is longer still. And you'll be spending it not dead.
But Mr. Turner on the other hand? Yeah, he'll be dead. :(''')
            playsound('week6/audio/ten_years.aiff')
        #1.1.2
        elif heart.lower() == 'don\'t stab':
            
            print('''\nYou sacrifice the task of being captian of the Flying 
Dutchman so that Will Turner can stab the heart, free his father,
and see Elizabeth only once every ten years. It may be a steep 
price, but it depends on the one day.''')
            playsound('week6/audio/one_day.aiff')
        else:
            print('\nFor real? That wasn\'t an option. Try again.')
    #1.2.0
    elif will.lower() == 'not':
        print('''\nWell, that\'s very unfortunate for you. You can\'t bring the
ship into Tortuga all by your onesie. You end up getting caught by
Norrington and your sailing days are over... for now.''')
        jail = input('''You can choose to STAY in jail or BREAK OUT with the
dog\'s key. ''')
        #1.2.1
        if jail.lower() == 'stay':
            print('\nWell, you\'re dumb. You will never sail the seas again.')
            playsound('week6/audio/tortuga.aiff')
        #1.2.2
        elif jail.lower() == 'break out':
            print('\nWell, it\'s a pirate\'s life for you... savvy?')
            playsound('week6/audio/savvy.aiff')
        else:
            print('\nFor real? That wasn\'t an option. Try again.')
    #1.3.0
    elif will.lower() == 'captured':
        print('''\nWill\'s been captured sir, everyone\'s been captured! Ah!
you\'ve been captured!! You\'ve been captured by none other than the 
half-dead, pirate captain, Hector Barbossa. To make matters worse, he 
is hungry and doesn\'t have an apple.''')
        apple = input('''Do you get him an APPLE, or LEAVE him with nothing but a 
name on some beach with your word it\'s the one he needs? ''')
        #1.3.1
        if apple.lower() == 'apple':
            print('''\nOh you get him an apple alright... right after an epic battle
in Isle de Muerta where Will end\'s up shooting him and he dies. Barbossa stays
hungry forever.''')
            playsound('week6/audio/barbossa.aiff')
        #1.3.2
        elif apple.lower() == 'leave':
            print('''\nOf the two of you, you are the only one who hasn\'t
committed mutiny, therefore, it\'s your word we\'ll be trusting. Long
story short, the ship is yours! Huzzah! Huzzah!''')
            playsound('week6/audio/huzzah.aiff')
        else:
            print('\nFor real? That wasn\'t an option. Try again.')
    else:
        print('\nFor real? That wasn\'t an option. Try again.')
#2.0.0
elif fighter.lower() == 'shia labeouf':
    print('''\nYou're walking in the woods. There\'s no one around and your 
phone is dead. Out of the corner of your eye you spot him. Shia LaBeouf.''')
    playsound('week6/audio/shia_labeouf.aiff')
    shia = input('Do you RUN or FIGHT? ')
    #2.1.0 
    if shia.lower() == 'run':
        print('''\nRunning for your life from Shia LaBeouf... Now it\'s dark
and you seem to have lost him, but you\'re hopelessly lost yourself.
Now your leg! Ah! It\'s caught in a bear trap!! ''')
        trap = input('Do you GNAW it off, or STAY to probably die? ')
        #2.1.1
        if trap.lower() == 'gnaw':
            print('''\nGnawing off your leg! Quiet, quiet. Limping to the cottage!
Quiet, quiet. Now you\'re on the doorstep, and sitting inside is Shia LaBeouf. You
sneak up behind him and strangle him. You can finally relax. ''')
            playsound('week6/audio/gnawing_off_leg.aiff')
        #2.1.2
        elif trap.lower() == 'stay':
            print('''\nYou realize that this is just all a theatrical performance.
You hear someone clapping from the nearly empty auditorium. He then stands up to 
reveal that he is, in fact, Shia LaBeouf, and he approved of your performance.''')
            playsound('week6/audio/clapping.aiff')
        else:
            print('\nFor real? That wasn\'t an option. Try again.')  
    #2.2.0
    elif shia.lower() == 'fight':
        print('''\nHe's brandishing a knife, it\'s Shia LaBeouf, lurking in 
the shadows. Fighting for your life with Shia LaBeouf, wrestling a knife from Shia
LaBeouf, stab it in his kidney. You're safe at last..... Wait!! He isn\'t dead! Shia
surprise!''')
        playsound('week6/audio/shia_surprise.aiff')
        surprise = input('Do you FIGHT him again or go straight to CHOP off his head? ')
        #2.2.1
        if surprise.lower() == 'fight':
            print('''\nThere\'s a gun to your head, and death in his eyes. But you
can do Jiu Jitsu, so you bodyslam superstar Shia LaBeouf. You are safe at last. For 
real this time.''')
            playsound('week6/audio/bodyslam.aiff')
        #2.2.2
        elif surprise.lower() == 'chop':
            print('''\nLegendary fight with Shia LaBeouf, normal Tuesday night for Shia
LaBeouf. You try to swing an axe, and you have just decapitated Shia LaBeouf. His head
topples to the floor, expressionless. You're finally safe from Shia LaBeouf.''')
            playsound('week6/audio/finally_safe.aiff')
        else:
            print('\nFor real? That wasn\'t an option. Try again.')
    else:
        print('\nFor real? That wasn\'t an option. Try again.')
else:
    print('\nFor real? That wasn\'t an option. Try again.')

# credits #
    #song 'Choose Your Fighter' by Ava Max
    #song 'Shia LaBeouf Live' by Rob Cantor