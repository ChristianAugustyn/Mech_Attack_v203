#Author's: Austin Witherall, Christian Augustyn
#Date: 5/12/2016
#File Name: mech_attack.py
#Description: This is a turn based game of Mechs battling in a tournament format.
#The goal is to win the entire tournament.

import random

def mainMenu(): #creates a definition for the mainMenu function
    menu = True #creates a boolean for menu
    while menu: #creates a loop when menu is true
        print('        _____                .__         _____   __    __                 __    ') #next 6 lines are welcoming messages for the game
        print('       /     \   ____   ____ |  |__     /  _  \_/  |__/  |______    ____ |  | ___')
        print('      /  \ /  \_/ __ \_/ ___\|  |  \   /  /_\  \   __\   __\__  \ _/ ___\|  |/  /')
        print('     /    Y    \  ___/\  \___|   Y  \ /    |    \  |  |  |  / __ \\  \___|     < ')
        print('     \____|____/\_____>\_____>___|__/ \____|____/__|  |__| (_____/ \______>__|__\ ')
        print('WELCOME TO MECH ATTACK!')
        menu_pick = input('PLEASE TYPE AN OPTION: P = Play Game, H = Rules and Help, Q = Quit Game \n> ') #creates variable menu_pick which is set to an input
        if menu_pick == 'P': #creates an option for if the user types P to play
            scraps_start = 1000 #creates a variable for the players scraps_start
            cur_scraps = 0 #creates a variable for the users current scraps
            scraps = scrapsStorage(cur_scraps, scraps_start) #varaible scraps calls for function scrapsStorage with parameters cur_scraps and scraps_start
            player_mech = chooseStarterMech() #player_mech calls for the function chooseStarterMech with no parameters
            player_w_or_l = playGame(player_mech, scraps) #player_w_or_l calls for playGame with parameters player_mech and scraps
            if player_w_or_l == 'Win': #creates an option for if player_w_or_l is win and displays a win message
                print('CONGRATUALATIONS YOU HAVE WON!')
                menu = True #restarts menu loop
            else: #creates an alternate option and displays you have lost
                print('You Have Lost Play Again if You Dare.')
        elif menu_pick == 'H': #creates an option for if the user type H for menu_pick
            helpMenu() #calls for the function helpMenu with no parameters
            menu = True #sets menu to true
        elif menu_pick == 'Q': #creates an option for if the user type Q for menu_pick
            menu = False #ends the menu loop
        else: #creates an option for if the user does not type a specified value for menu_pick
            print('That is not a valid command.') #tells the user that what they entered is not valid
            menu = True #sets menu to True, returning to the menu loop
        
def helpMenu(): #creates a definition for helpMenu
    print('      \_/      ') #next 9 lines are a welcoming message for the help menu
    print('     (* *)     ')
    print('    __)#(__    ')
    print('   ( )...( )(_)')
    print('   -| |_| ||// ')
    print('>==() | | ()/  ')
    print('    _(___)_    ')
    print('   [-]   [-]   ')
    print("Hello My Name Is H-231. I'm Here To Help You.")
    help_op = True #sets help_op variable to true
    while help_op: #creates a loop when help_op is false
        help_chose = input('Type R For the Rules, Type S For Stat Definitions or Type Q To Return To The Main Menu: \n> ') #creates a variable help_chose with an user input 
        if help_chose == 'R': #creates an option for when the user type R for help_chose
            print(' _____________________________________________________________________________________________') #next 9 lines displays the rules for the program
            print('|                                                                                             |')
            print("|                                    ---How To Play---                                        |")
            print('| 1. Mech Attack is a turn base game where Mechs duke it out until one can no longer fight.   |')
            print('| 2. You will be able to buy items and mech upgrades in the shop using Scraps as the currency.|')
            print('| 3. When in a battle you are able to choose between a basic attack or a special attack.      | \n|    The special attack has a higher chance of doing 1.5x damage but has a lower hit rate.    |')
            print('| 4. When you win a battle you will earn Parts which can be saved or used in the store.       | \n|    You will then move onto the next stage, where opponents become tougher to beat.          |')
            print('|_____________________________________________________________________________________________|') 
            print('')
        elif help_chose == 'S': #creates an option for when the user type S for help_chose
            print(' _______________________________________________________________________________________________') #next 9 lines displays the definitions of each stat in the game
            print('|                                                                                               |')
            print('| Health: Health is the amount of damge your Mech can endure before it dies.                    |')
            print('| Armour: Armour acts as additional health for your bot.                                        |')
            print('| Attack: The attack stats is the amount of base damage that your Mech does for each basic move.|')
            print('| Special Attack: Special attack is the critical hit chance of your special.                    |')
            print('| Speed: The speed stat determines who attacks first in a battle.                               |')
            print('|_______________________________________________________________________________________________|')
            print('')
        elif help_chose == 'Q': #creates an option for when the user type R for help_chose
            help_op = False #sets help_op to false ending the help_op loop
            
def chooseStarterMech(): #defines a function called chooseStarterMech
    negotiate = open("mech_choose.txt")
    print(negotiate.read())
    starter = True #Flag
    while starter: #while the flag is True
        mechChoices = ['Tank', 'Jager', 'Berserker', 'Marauder'] #creates a list of all the mechs
        print('           === MECHS === \n' + str(mechChoices)) #prints a header and the list of mechs
        choice = input("Please Select Your Starter Mech Or \nType stats to See the Stats of Each Mech or quit to Return to the Menu. \n> ") #takes the users input as a string and assigns it to choice    
        check = choice in mechChoices #assigns the return of choice in menuChoices to the variable check            
        if choice == 'stats': #if choice is equal to stats
            # potentially add speed, attack, defence, and special for every starter mech
            print("|-----------------------------------------------------------------------|")
            print("|--- Tank ---| \nTank is a heavily armoured mech designed for front line combat.  \nHealth: 1000 \nArmour: 250 \nAttack: 60 \nSpecial Attack: 60% \nSpeed: 2 ")
            print("|--- Jager ---| \nJager is a standard issue mech with a trick up its sleeve. \nHealth: 700 \nArmour: 100 \nAttack: 66 \nSpecial Attack: 75% \nSpeed: 4 ")
            print("|--- Berserker ---| \nBerserker is an uncontrollable mech that attacks anything in it's path. \nHealth: 700 \nArmour: 100 \nAttack: 85 \nSpecial Attack: 50% \nSpeed: 5 ")
            print('|--- Marauder ---| \nMarauder is a high speed mech, running up to 70km/h. \nHealth: 550 \nArmour: 100 \nAttack: 65 \nSpecial Attack: 60% \nSpeed: 7 ')
            print('|-----------------------------------------------------------------------|')
            starter = True #loop starts again showing the user the mechs
        elif choice == 'quit': #if choice is equal to quit
            starter = False #exits the program                     
        elif check == True: #if check is equal to True
            mech = getMech(choice)
            starter = False #stops the loop
            return mech #returns the mechs choice        
        elif check == False: #if check is False
            print('! That Is Not a Valid Choice, Please Try Again !') #tells the user its not a valid choice
            print() #blank space
            starter = True #returns the user to the begginning of the loop
        else: #if none of the above is True
            print('something is wrong with chooseStarterBot()') #Prints something is wrong with the function

def getMech(name): #defines the function getMech with parameters: name
    #name = ['name', 'health', 'amour', 'attack', 'spattack', 'speed', 'dodge']
    Tank = ['Tank', 1000, 250, 50, 60, 2] #stats for Tank
    Jager = ['Jager', 700, 100, 65, 75, 4] #stats for Jager
    Berserker = ['Beserker', 700, 100, 85, 55, 5] #stats for Beserker
    Marauder = ['Marauder', 600, 100, 75, 60, 7] #stats for Marauder
    if name == 'Tank': #if name = Tank, function returns the list named Tank
        return Tank
    elif name == 'Jager': #if name = Jage, function returns the list named Jager
        return Jager
    elif name == 'Berserker': #if name = Beserker, function returns the list named Beserker
        return Berserker
    elif name == 'Marauder': #if name = Marauder, function returns the list named Marauder
        return Marauder
    else: #if the above is not true then it prints an error message
        print('something wrong with getMech()') 

def playGame(stats, scraps): #defines the function playGame with parameters stats and scraps
    inventory = [] #creates an outside list for inventory
    game = 0 #creates a counter for game which determine the round of the tournament
    enemy0 = ['B-103', 450, 0, 45, 50, 1, 750] #creates stats for enemy0 into a list
    enemy1 = ['B-200', 500, 50, 55, 50, 3, 800] #creates stats for enemy1 into a list
    enemy2 = ['T-150', 700, 100, 40, 50, 1, 900] #creates stats for enemy2 into a list
    enemy3 = ['T-874', 700, 100, 65, 60, 4, 1000] #creates stats for enemy3 into a list
    enemy4 = ['Model-450', 750, 100, 60, 60, 4, 1100]#creates stats for enemy4 into a list
    enemy5 = ['Model-750', 750, 100, 65, 60, 4, 1200] #creates stats for enemy5 into a list
    enemy6 = ['G-540', 800, 100, 70, 60, 4, 1250] #creates stats for enemy6 into a list
    enemy7 = ['G-650', 850, 150, 75, 65, 6, 1300] #creates stats for enemy7 into a list
    enemy8 = ['V-650', 950, 200, 80, 65, 6, 2000] #creates stats for enemy8 into a list
    enemy9 = ['UMech-1400', 1200, 200, 80, 70, 7, 0] #creates stats for enemy9 into a list
    enemies = enemy0 + enemy1 + enemy2 + enemy3 + enemy4 + enemy5 + enemy6 + enemy7 + enemy8 + enemy9 #concatenates all of the enemy stats into a large list
    tournament = True #creates a boolean for tournament
    while tournament: #creates a loop for when tournament is true
        all_information = mechShop(stats, scraps, inventory) #all_information calls for mechShop with the list of stats returned in getMech, the variable scraps and the list inventory
        scraps = all_information.pop(0) #sets scraps to all_information at index 0 and pops it out
        stats = all_information[0:6] #sets stats to all_information at index 0 to 6
        play_stats = stats.copy() #makes a copy of play_stats which can then be changed
        start_enemy_stats = int(game) * 7 #creates a starting variable for chosing the enemy stats in accordance to the round
        end_enemy_stats = int(start_enemy_stats) + 7 #creates an ending variable for end of enemy stats
        cpu_stats = enemies[start_enemy_stats:end_enemy_stats] #sets cpu_stats to the index of enemies start_enemy_stats to end_enemy_stats from the list enemies        
        enemyMechDes(game) #calls for function enemyMechDes with parameter of game
        results_battle = setBattleSequence(play_stats, inventory, cpu_stats) #calls for function setBattleSequence with parameters play_stats, inventory and cpu_stats
        while True: #creates a whiel loop
            try: #creates a try statement
                scraps_won = int(results_battle[0]) #attempts to turn results_battle at index 0 to an int
                scraps = scrapsStorage(scraps, scraps_won) #if successful calls for scrapsStorage with parameters scraps and scraps_won and sets it back into scraps
                inventory = results_battle[1:] #resets inventory to what is returned by setBattleSequence
                tournament = True #sets tournament to true
                game += 1 #adds 1 to game counter
                break #breaks the while loop
            except ValueError: #if unsuccessful and returned ValueError
                print("You Have Been Knocked Out of the Tournament.") #user has lost, gives losing message
                tournament_outcome = 'Lose' #sets tournament_outcome to Lose
                tournament = False #sets tournament variable to False ending tournament loop
                return tournament_outcome #returns tournament outcome
                break #breaks while loop
        if game >= 10: #creates a variable for if game is >10
            tournament_outcome = 'Win' #sets tournament_outcome to True
            tournament = False #ends tournament loop
    return tournament_outcome #returns tournament_outcome
        
        
def mechShop(mech_stats, scraps, inventory): #defines mechShop with parameters mech_stats, scraps and inventory
    shop_owner = open("shop_owner.txt") #opens shop_owner text file and displays it
    print(shop_owner.read())
    shop = True #creates boolean and loop for shop
    while shop:
        print('--- Current Balance: ' + str(scraps) + ' ---') #prints a message and the varaible scraps
        go_to_shop = input('Type B for Battle Items, U for Upgrade and Weapons, or C to continue to the Tournament: \n> ') #creates an input for go_to_shop
        if go_to_shop == 'B': #creates option for if go_to_shop is B
            battle_list = battleItems(scraps) #calls function battleItems with parameter scraps
            scraps = battle_list.pop(0) #sets scraps to battle_list at index 0 and pops it out
            inventory += battle_list #and the remains of battle_list to the inventory list
            print('Inventory: ') #prints message
            print(inventory) #prints the list inventory
            shop = True #resets shop to True
        elif go_to_shop == 'U': #creates option for if go_to_shop is B
            mech_up = upgradeShop(mech_stats, scraps) #calls for function upgradeShop with parameters of mech_stats and scraps
            scraps = mech_up.pop(0) #sets scraps to mech_up at index 0 and pops it out
            mech_stats = mech_up[0:6] #sets mech_stats to the index of 0 to 6 in mech_up
            print(mech_stats) #prints mech_stats
            shop = True #resets shop loop
        elif go_to_shop == 'C': #creates an option for if go_to_shop is C
            mech_stats.insert(0, scraps)#inserts scraps into mech_stats at index 0
            mech = mech_stats + inventory #adds list inventory to the list mech_stats
            shop = False #sets shop to False
            return mech #returns variable mech
        else: #creates an alternate option and states that the command was not valid and resets shop loop
            print('That is not a valid command.')
            shop = True
            

def battleItems(scraps): #defines battleItems with parameter scraps
    inventory_actual = [] #creates outisde list of inventory_actual
    print('Shock Charge: Stuns opponent for 2 turns, making them unable to attack (400 Scraps) \nIncendiary: Does 30 damage per turn, lasting for 2-4 turns, meglects armour (450 Scraps).') #next 2 lines are messages for items in shop
    print('Blow Torch: Restores 150 Health Points (400 Scraps) \nRepair Kit: Restores 300 Health Point (700 Scraps).')
    shock = ['Shock Charge: Stuns opponent for 2 turns, making them unable to attack.', 400, 'Scraps'] #next 4 lines are list for each individual item in order Shock Charge
    inc = ['Incendiary: Does 30 damage per turn, lasting for 2-4 turns', 450, 'Scraps'] #Incendiary
    torch = ['Blow Torch: Restores 150 Health Points', 400, 'Scraps'] #Blow Torch
    kit = ['Repair Kit: Restores 300 Health Point', 700, 'Scraps'] #Repair Kit
    battle_shop = True #creates boolean for battle_shop and creates loop
    while battle_shop:
        buy = input('Type the First Letter of What you Want to Buy or Type Q to Return to the Main Shop: \n> ') #user input and set it to variable buy
        if buy == 'Q': #if buy = Q ends sets inventory_buy to None and ends battle_shop loop
            print('')
            inventory_buy = []
            battle_shop = False 
        elif buy == 'S':  #if buy = S 
            add_item = 'Shock Charge' #sets add_item to Shock Charge 
            amount = amountItem() #calls for amountItem function
            sub_scraps = amount * shock[1] #sets sub_scraps to amount multiplieds by index 1 in shock
            if sub_scraps <= scraps: #sets option for if sub_scraps is less than or equal to scraps
                sub_scraps = -int(sub_scraps) #sets sub_scraps to negative
                scraps = scrapsStorage(scraps, sub_scraps) #calls for function scrapsStorage
                inventory_buy = [] #creates list inventory_buy
                for item in range(amount): #creates a loop for range of amount
                    inventory_buy.append(add_item) #appends add_item to inventory_buy
                print('---Current Balance: ' + str(scraps) + '---') #prints users new balance
            else: #creates an option if user cant afford items and prints message, sets invenotry_buy to an empty list
                print("You Can't Afford That")
                inventory_buy = []
                print('---Current Balance: ' + str(scraps) + '---') #prints users new balance
            battle_shop = True #sets battle_shop loop to true and resets it
        elif buy == 'I': #repeats lines 213 to 228 for Incendiary except for
            add_item = 'Incendiary' #sets add_item to Incendiary
            amount = amountItem()
            sub_scraps = amount * inc[1] #sets sub_scraps to amount multiplied by inc at index 1
            if sub_scraps <= scraps:
                sub_scraps = -int(sub_scraps)
                scraps = scrapsStorage(scraps, sub_scraps)
                inventory_buy = []
                for item in range(amount):
                    inventory_buy.append(add_item)
                print('---Current Balance: ' + str(scraps) + '---') #prints users new balance
            else:
                print("You Can't Afford That")
                inventory_buy = []
                print('---Current Balance: ' + str(scraps) + '---') #prints users new balance
            battle_shop = True
        elif buy == 'B': #repeats lines 213 to 228 for Blow Torch except for
            add_item = 'Blow Torch' #sets add_item to Blow Torch
            amount = amountItem()
            sub_scraps = amount * torch[1] #sets sub_scraps to amount multiplied by torch at index 1
            if sub_scraps <= scraps:
                sub_scraps = -int(sub_scraps)
                scraps = scrapsStorage(scraps, sub_scraps)
                inventory_buy = []
                for item in range(amount):
                    inventory_buy.append(add_item)
                print('---Current Balance: ' + str(scraps) + '---') #prints users new balance
            else:
                print("You Can't Afford That")
                inventory_buy = []
                print('---Current Balance: ' + str(scraps) + '---') #prints users new balance
            battle_shop = True
        elif buy == 'R': #repeats lines 213 to 228 for Repair Kit except for
            add_item = 'Repair Kit' #sets add_item to Repair Kit
            amount = amountItem()
            sub_scraps = amount * kit[1] #sets sub_scraps to amount multiplied by kit at index 1
            if sub_scraps <= scraps:
                sub_scraps = -int(sub_scraps)
                scraps = scrapsStorage(scraps, sub_scraps)
                inventory_buy = []
                for item in range(amount):
                    inventory_buy.append(add_item)
                print('---Current Balance: ' + str(scraps) + '---') #prints users new balance
            else:
                print("You Can't Afford That")
                inventory_buy = []
                print('---Current Balance: ' + str(scraps) + '---') #prints users new balance
            battle_shop = True
        else:
            print('That is Not a Valid Item.')
            inventory_buy = []
            battle_shop = True
        inventory_actual += inventory_buy #add list of inventory_buy to inventory_actual
        inventory_buy.clear() #clears list inventory_buy
    inventory = inventoryManage(inventory_actual, scraps) #calls function inventorManage with parameters inventory_actual and scraps
    return inventory #returns varaible inventory

def amountItem(): #defines amountItem with no paramters
    while True: #create loop
        try: #tries the following
            num_amount = int(input("How Many Would you Like to Buy: ")) #sets input and checks if input is an int
            break #breaks loop
        except ValueError: #if fail as ValueError, prints message
            print("Oops! That was not a valid number.  Try again...")
    return num_amount #returns num_amount
    
def scrapsStorage(cur_scraps, addscraps): #defines scrapsStorage with parameters cur_scraps and addscraps
    cur_scraps += addscraps #adds cur_scraps and addscraps
    return cur_scraps #returns new value for cur_scraps

def inventoryManage(inv, scraps): #defines inventoryManage with parameters inv and scraps
    inventory_man = [] #sets empty list for inventory_man
    inventory_man += inv #adds list of inv to inventory_man
    inventory_man.insert(0, scraps) #inserts scraps at index 0 in inventory_man
    return inventory_man #returns inventory_man

def upgradeShop(stats, scraps): #defines upgradeShop with parameters stats and scraps
    print('Welcome to the Upgrade Shop! Each Module or Weapons Costs 1000 Scraps.') #next 6 lines prints out messages for each item
    print("Health Module: Adds 100 Stat Points to Your Mech's Health.")
    print('Armour: Adds 100 Amour Points.')
    print('Crit Module: Adds 15 Points to Your Special Attack Stat.')
    print("Speed Moudule: Adds 1 Point to Your Mech's Speed Stat.")
    print("Upgraded Weapon: Increases Attack Stat by 10.")
    type_mech = stats[0] #creates variavle tpye_mech as the index of 0 in stats
    if type_mech == 'Tank': #creates option for if type_mech is Tank, prints message
        print("Brutal Battle Axe: Increases Attack by 15 and Health Stat by 75. (2000 Scraps)")
    elif type_mech == 'Jager': #creates option for if type_mech is Jager, prints message
        print('Merciless Rifle: Increases Attack by 15 and Special Attack by 10. (2000 Scraps)')
    elif type_mech == 'Berserker': #creates option for if type_mech is Berserker, prints message
        print('Barbaric Longsword: Increases Attack by 25. (2000 Scraps)')
    else: #creates option for if type_mech is Marauder, prints message
        print('Ferocious Kitana: Increases Attack by 15 and Speed by 1. (2000 Scraps)')
    upgrade_shop = True #creates loop and boolean for upgrade_shop
    while upgrade_shop:
        player_choice = input('Type the First Letter of the Upgrade you Would Like to Choose, W for the Special Weapon, V to View Mech Stats or Q to Return to the Main Shop. \n>') #users input for player_choice
        if player_choice == 'Q': #creates option for if player_choice is Q
            stats.insert(0, scraps) #inserts scraps at index 0 in stats
            return stats #returns list of stats
            upgrade_shop = False #sets upgrade_shop to False
        elif player_choice == 'V': #creates option for if player_choice is V and prints message and the list stats
                print('Order of Stats: Mech Type, Health, Armour, Attack, Special Attack, Speed')
                print(stats)
        else: #from lines 332 to 397, checks for each item in the shop and changes the scraps value and stats acccordinglly
            if scraps >= 1000:
                if player_choice == 'H':
                    health = stats.pop(1)
                    health += 100
                    stats.insert(1, health)
                    scraps += -1000
                elif player_choice == 'A':
                    armour = stats.pop(2)
                    armour += 100
                    stats.insert(2, armour)
                    scraps += -1000
                elif player_choice == 'C':
                    crit = stats.pop(4)
                    crit += 15
                    stats.insert(4, crit)
                    scraps += -1000
                elif player_choice == 'S':
                    speed = stats.pop(5)
                    speed += 1
                    stats.insert(5, speed)
                    scraps += -1000
                elif player_choice == 'U':
                    attack = stats.pop(3)
                    attack += 10
                    stats.insert(3, attack)
                    scraps += -1000
                elif player_choice == 'W':
                    if scraps >= 2000:
                        attack = stats.pop(3)
                        attack += 15
                        stats.insert(3, attack)
                        if type_mech == 'Tank':
                            health = stats.pop(1)
                            health += 75
                            stats.insert(1, health)
                        elif type_mech == 'Jager':
                            crit = stats.pop(4)
                            crit += 10
                            stats.insert(4, crit)
                        elif type_mech == 'Berserker':
                            attack = stats.pop(3)
                            attack += 10
                            stats.insert(3, attack)
                        else:
                            speed = stats.pop(5)
                            speed += 1
                            stats.insert(5, speed)
                        scraps += -2000
                    else: #creates an option for if the user cannot afford to buy the upgrade
                        scraps = scraps #sets scraps to scraps, prints message and returns user to the upgrade_shop loop
                        print('You Cannot Afford This Upgrade.') 
                        upgrade_shop = True
                else: #creates option for if the user didnt input a valid option, prints message and returns to the upgrade_shop loop
                    print("That is Not a Valid Option (Tip: Use Capital Letters and it's Only the First Letter)")
                    upgrade_shop = True
            else: #creates an option for if the user cannot afford to buy the upgrade, prints message and returns user to upgrade_shop loop
                print('You Cannot Afford This Upgrade.')
                upgrade_shop = True
        print('---Current Balance: ' + str(scraps) + '---') #prints message and the value of scraps

def enemyMechDes(mech_num):#defines enemyMechDes with parameter mech_num
    if mech_num == 0:#for each mech_num value from 0 to 9 the program reads the files accordingly
        r1 = open('round1.txt')
        print(r1.read())
        mech = open("mech_zero.txt")
        print(mech.read())
    elif mech_num == 1:
        r2 = open('round2.txt')
        print(r2.read())
        mech = open("mech_one.txt")
        print(mech.read())
    elif mech_num == 2:
        r3 = open('round3.txt')
        print(r3.read())
        mech = open("mech_two.txt")
        print(mech.read())
    elif mech_num == 3:
        r4 = open('round4.txt')
        print(r4.read())
        mech = open("mech_three.txt")
        print(mech.read())
    elif mech_num == 4:
        r5 = open('round5.txt')
        print(r5.read())
        mech = open("mech_four.txt")
        print(mech.read())
    elif mech_num == 5:
        r6 = open('round6.txt')
        print(r6.read())
        mech = open("mech_five.txt")
        print(mech.read())
    elif mech_num == 6:
        r7 = open('round7.txt')
        print(r7.read())
        mech = open("mech_six.txt")
        print(mech.read())
    elif mech_num == 7:
        r8 = open('round8.txt')
        print(r8.read())
        mech = open("mech_seven.txt")
        print(mech.read())
    elif mech_num == 8:
        r9 = open('round9.txt')
        print(r9.read())
        mech = open("mech_eight.txt")
        print(mech.read())
    elif mech_num == 9:
        r10 = open('round10.txt')
        print(r10.read())
        mech = open("mech_nine.txt")
        print(mech.read())

# this function determines if the player wins or loses based upon their upgrades and all the stats from their mech as well as the cpu mech
def setBattleSequence(ori_mech, inventory, ori_cpu):
    winnings = ori_cpu.pop(6) #pops out the money that the player wins at the end of the round and assigns it to winnings
    first_attack = setWhoGoesFirst(ori_mech, ori_cpu) #calls on setWhoGoesFirst assigns it to the variable first_attack
    cpu_inventory = ['Shock Charge', 'Repair Kit', 'Blow Torch'] #list of the items in the cpus inventory
    player_mech = ori_mech.copy() #creates a copy of the original player mech, assigns it to player_mech
    cpu_mech = ori_cpu.copy() #creates a cop of the original cpu mech and assigns it to cpu_mech
    p_shock = False #asigns False tp p_shock
    p_burn = 0  #assigns 0 to p_burn
    c_shock = False #assigns False to c_shock
    
    battle = True #assigns True to battle
    while battle: #creates a loop while battle is True
    
        if first_attack == True: #if first_attack is equal to True it is the players turn
            showPlayerGauge(player_mech) #calls on the showPlayer function
            showCpuGauge(cpu_mech) #calls on the showCpu function
            player_turn = input("--- " + player_mech[0] + "'s ---" "turn \n What would you like to do? \nA = Attack \nSP = Special Attack \nI = Inventory \nQ = Quit \n> ") #calls fo user input and assigns it to player_turn

            #if the player chooses attack
            if player_turn == 'A':
                player_attack = player_mech[3] # slice the players attack damage and assigns it to player_attack
                cpu_armour = cpu_mech[2] #slices the cpu's armour and assigns it to cpu_armour
                cpu_health = cpu_mech[1] #slices cpu's health and assigns it to cpu_health

                # if the cpu armour is greater than player attack subtracts player attack from cpu armour and returns it back into the players stats
                if cpu_armour > player_attack:
                    dmg_armour = cpu_armour - player_attack
                    cpu_mech.pop(2)
                    cpu_mech.insert(2, dmg_armour)
                    print('---------------------\nYou attacked Cpu, ' + str(player_attack) + ' Damage was done to their Armour\n---------------------') #prints the damage done
                    # checks for inventory use by player and cpu and applies it if the instance is true other wise attack_first is equal to false 
                    if p_shock == True:
                        first_attack = True
                        p_shock = False
                    
                    elif p_burn > 0:
                        cpu_health = cpu_mech[1]
                        cpu_burn = cpu_health - 30
                        cpu_mech.pop(1)
                        cpu_mech.insert(1, cpu_burn)
                        p_burn -= 1
                        print('**********\n' + cpu_mech[0] + ' was burned for 30 damage\n**********')
                        first_attack = False
                    
                    else:
                        first_attack = False
                # if the cpu's armour is less than or equal to player attack and the cpu armour is greater than or equal to 0
                #subtracts the player attack from the armour and the remainder of that is added to health, health is than inserted back into player stats
                elif (cpu_armour <= player_attack) and (cpu_armour > 0):
                    dmg_armour = cpu_armour - player_attack
                    dmg_health = cpu_health + dmg_armour
                    cpu_mech.pop(2)
                    cpu_mech.insert(2, 0)
                    cpu_mech.pop(1)
                    cpu_mech.insert(1, dmg_health)
                    print('---------------------\nyou attacked Cpu, ' + str(player_attack) + ' damage was done to their armour \nyou broke their armour!\n---------------------')#prints the damage donme by the player
                    # checks for inventory use by player and cpu and applies it if the instance is true other wise attack_first is equal to false 
                    if p_shock == True:
                        first_attack = True
                        p_shock = False
                    
                    elif p_burn > 0:
                        cpu_health = cpu_mech[1]
                        cpu_burn = cpu_health - 30
                        cpu_mech.pop(1)
                        cpu_mech.insert(1, cpu_burn)
                        p_burn -= 1
                        print('**********\n' + cpu_mech[0] + ' was burned for 30 damage\n**********')
                        first_attack = False
                    
                    else:
                        first_attack = False
                    
                elif cpu_armour == 0: #if the cpu's armour is equal to 0

                    #if the cpu's health is greater than the players attack
                    #subtracts player attack from the cpu health anf inserts it into the cpu stats
                    if cpu_health > player_attack:
                        dmg_health = cpu_health - player_attack
                        cpu_mech.pop(1)
                        cpu_mech.insert(1, dmg_health)
                        print('---------------------\nyou attacked Cpu, ' + str(player_attack) + ' damage was done\n---------------------') #prints the damage done
                        # checks for inventory use by player and cpu and applies it if the instance is true other wise attack_first is equal to false 
                        if p_shock == True:
                            first_attack = True
                            p_shock = False
                        
                        elif p_burn > 0:
                            cpu_health = cpu_mech[1]
                            cpu_burn = cpu_health - 30
                            cpu_mech.pop(1)
                            cpu_mech.insert(1, cpu_burn)
                            p_burn -= 1
                            print('**********\n' + cpu_mech[0] + ' was burned for 30 damage\n**********')
                            first_attack = False
                       
                        else:
                            first_attack = False
                    #if the cpu's health is less then or equal to 0 or cpu health is less then or equal to player attack
                    #sets the health to zero and declares the player as the winner
                    elif (cpu_health <= 0) or (cpu_health <= player_attack):
                        cpu_mech.pop(1)
                        cpu_mech.insert(1, 0)
                        print(player_mech[0] + ' has defeated The enemy Bot!!!!!')
                        battle = False
                        inventory.insert(0, winnings)
                        return inventory
                            
                    else:#incase of error
                        print('error, battleSequence(), cpu health damage')
                                     
                else:#incase of error
                    print(' error, battleSequence(), cpu armour damage')
                            
            #if the player chooses special attack      
            elif player_turn == 'SP':
                player_special = 1.5 * (player_mech[3]) #gets the players attack and multiplies 1.5, assigns it to player_special
                special_chance = player_mech[4] #slices the chance that the player will hit with special attack, assigns it to special_chance
                random_num = random.randint(1, 100) #generates a random number between 1 and 100, assigns it tp random_num

                #if the random number is between 1 and the special chance the special attack is a hit
                if (random_num >= 1) and (random_num <= special_chance):
                    cpu_armour = cpu_mech[2]#slices cpu armour, assigns it to cpu_armour
                    cpu_health = cpu_mech[1] #slices health, assigns it to cpu_health

                    # if the cpu armour is greater than player attack subtracts player attack from cpu armour and returns it back into the players stats
                    if cpu_armour > player_special:
                        dmg_armour = cpu_armour - player_special
                        cpu_mech.pop(2)
                        cpu_mech.insert(2, dmg_armour)
                        print('---------------------\nyou attacked Cpu, ' + str(player_special) + ' damage was done to their armour\n---------------------')#prints the special attack damage done to the cpu
                        # checks for inventory use by player and cpu and applies it if the instance is true other wise attack_first is equal to false 
                        if p_shock == True:
                            first_attack = True
                            p_shock = False
                        
                        elif p_burn > 0:
                            cpu_health = cpu_mech[1]
                            cpu_burn = cpu_health - 30
                            cpu_mech.pop(1)
                            cpu_mech.insert(1, cpu_burn)
                            p_burn -= 1
                            print('**********\n' + cpu_mech[0] + ' was burned for 30 damage\n**********')
                            first_attack = False
                        
                        else:
                            first_attack = False

                    # if the cpu's armour is less than or equal to player attack and the cpu armour is greater than or equal to 0
                    #subtracts the player attack from the armour and the remainder of that is added to health, health is than inserted back into player stats
                    elif (cpu_armour <= player_special) and (cpu_armour > 0):
                        dmg_armour = cpu_armour - player_special
                        dmg_health = cpu_health + dmg_armour
                        cpu_mech.pop(2)
                        cpu_mech.insert(2, 0)
                        cpu_mech.pop(1)
                        cpu_mech.insert(1, dmg_health)
                        print('---------------------\nyou attacked Cpu, ' + str(player_special) + ' damage was done to their armour \nyou broke their armour!\n---------------------')#prints the special attack damage done to the cpu
                        # checks for inventory use by player and cpu and applies it if the instance is true other wise attack_first is equal to false 
                        if p_shock == True:
                            first_attack = True
                            p_shock = False
                        
                        elif p_burn > 0:
                            cpu_health = cpu_mech[1]
                            cpu_burn = cpu_health - 30
                            cpu_mech.pop(1)
                            cpu_mech.insert(1, cpu_burn)
                            p_burn -= 1
                            print('**********\n' + cpu_mech[0] + ' was burned for 30 damage\n**********')
                            first_attack = False
                        
                        else:
                            first_attack = False
                    #if cpu armour is equal to 0
                    elif cpu_armour == 0:

                        #if the cpu's health is greater than the players attack
                        #subtracts player attack from the cpu health anf inserts it into the cpu stats
                        if cpu_health > player_special:
                            dmg_health = cpu_health - player_special
                            cpu_mech.pop(1)
                            cpu_mech.insert(1, dmg_health)
                            print('---------------------\nyou attacked Cpu, ' + str(player_special) + ' damage was done\n---------------------')#prints the special attack damage done to the cpu
                            # checks for inventory use by player and cpu and applies it if the instance is true other wise attack_first is equal to false 
                            if p_shock == True:
                                first_attack = True
                                p_shock = False
                            
                            elif p_burn > 0:
                                cpu_health = cpu_mech[1]
                                cpu_burn = cpu_health - 30
                                cpu_mech.pop(1)
                                cpu_mech.insert(1, cpu_burn)
                                p_burn -= 1
                                print('**********\n' + cpu_mech[0] + ' was burned for 30 damage\n**********')
                                battle = False
                            
                            else:
                                first_attack = False

                        #if the cpu's health is less then or equal to 0 or cpu health is less then or equal to player attack
                        #sets the health to zero and declares the player as the winner
                        elif (cpu_health <= 0) or (cpu_health <= player_special):
                            cpu_mech.pop(1)
                            cpu_mech.insert(1, 0)
                            print(player_mech[0] + ' has defeated The enemy Bot!!!!!')#declares that the player has defeated the bot
                            battle = False
                            inventory.insert(0, winnings)
                            return inventory
                        else:#error prompt
                            print('Special atk, cpu health error')
                        
                    else:#error prompt
                        print('Special atk, cpu armour error')
                        
                else:#if the random number is not in that range between one and special chance
                    print('You missed!')#tells the player they missed
                    # checks for inventory use by player and cpu and applies it if the instance is true other wise attack_first is equal to false 
                    if p_shock == True:
                        first_attack = True
                        p_shock = False
                    
                    elif p_burn > 0:
                        cpu_health = cpu_mech[1]
                        cpu_burn = cpu_health - 30
                        cpu_mech.pop(1)
                        cpu_mech.insert(1, cpu_burn)
                        p_burn -= 1
                        print('**********\n' + cpu_mech[0] + ' was burned for 30 damage\n**********')
                        first_attack = False
                    
                    else:
                        first_attack = False
                    
            #if player chooses inventory
            elif player_turn == 'I':
                bag = True #assigns True to bag
                while bag: #creates a loop as long as bag is True
                    print('    === Inventory ===') #Prints header
                    print(inventory) #prints items in players inventory
                    get_item = input('Please select an item from your inventory or type back for other options\n> ')#asks for the user to input an item they want to use or go back
                    check = get_item in inventory #checks to see if item is in inventory

                    #if check returns True
                    if check == True:
                        inventory.pop(inventory.index(get_item))# pops the item out of the inventory so it cant be used again

                        #if get item is equal to Shock Charge
                        #prints a statement letting the user know that the cpu is paralyzed, assigns True p_shock end the loop for the inventory and sets First attack to True
                        if get_item == 'Shock Charge':
                            print('**********\nCpu: ' + cpu_mech[0] + ' is paralyzed for 2 turns\n**********')
                            p_shock = True
                            bag = False
                            first_attack = True

                        #if get_item is equal to Incendiary
                        #generates a random between 2-4 which is the amount turns the player is burned for, subtracts 30 for the enemies health, subtracts 1 from the counter
                        #ens the inventory loop and assigns False to first_attack
                        elif get_item == 'Incendiary':
                            cpu_health = cpu_mech[1]
                            p_burn = random.randint(2, 4)
                            cpu_burn = cpu_health - 30
                            cpu_mech.pop(1)
                            cpu_mech.insert(1, cpu_burn)
                            p_burn -= 1
                            print('**********\n' + cpu_mech[0] + ' was burned for 30 damage\n**********')
                            bag = False
                            first_attack = False
                        
                        #if get_item is equal to Repair Kit
                        #regens the players health + 300 but not above their original health
                        elif get_item == 'Repair Kit':
                            rk = 300
                            player_health = player_mech[1]

                            if (rk + player_health) > ori_mech[1]:
                                player_mech.pop(1)
                                player_mech.insert(1, ori_mech[1])
                                print('**********\nyou used Repair Kit, regen + 300 health\n**********')
                                bag = False
                                battle = True
                                first_attack = False

                            elif (rk + player_health) < ori_mech[1]:
                                regen = rk + player_health
                                player_mech.pop(1)
                                player_mech.insert(1, regen)
                                print('**********\nyou used Repair Kit, regen + 300 health\n**********')
                                bag = False
                                battle = True
                                first_attack = False
                                
                            else: #else regen is not possible
                                print('regen is not possible')
                        
                        #if get_item is equal to Blow Torch
                        #regens the players health + 150 but not above their original health
                        elif get_item == 'Blow Torch':
                            bt = 150
                            player_health = player_mech[1]

                            if (bt + player_health) > ori_mech[1]:
                                player_mech.pop(1)
                                player_mech.insert(1, ori_mech[1])
                                print('**********\nyou used Blow Torch, regen + 150 health\n**********')
                                bag = False
                                battle = True
                                first_attack = False
                                
                            elif (bt + player_health) < ori_mech[1]:
                                regen = bt + player_health
                                player_mech.pop(1)
                                player_mech.insert(1, regen)
                                print('**********\nyou used Blow Torch, regen + 150 health\n**********')
                                bag = False
                                battle = True
                                first_attack = False
                                
                            else:#else regen is not possible
                                print('regen is not possible')
                        else:#else error with the inventory
                            print('! error with inventory in battleSequence() !')
                    
                    #if get_item is equal to back
                    #sets the inventory loop to false and returns player back to the attack screen
                    elif get_item == 'back':
                        bag = False
                        battle = True
                            
                    else:#if item isnt in the users inventory
                        print('! That item is not in your inventory, please try again !')
            #if player_turn is equal to Q
            #ends the game  
            elif player_turn == 'Q':
                print('Have  great day!')
                battle = False
                exit()

            else:#if player_turn is not a valid option, prints a warning message, and asks the user again
                print('! That is not a valid choice, please try again !')
                battle = True
        # this is the cpu's turn-------------------------------------------------------------------------------------------------------------------------------------------------------------     
        else: #if first_attack = False
            
            option = random.randint(1, 10) #generates a random number for choosing between attack, special attack, and inventory

            #if option is between 1 and 7
            if (option >= 1) and (option <= 7):
                cpu_attack = cpu_mech[3] #slices cpu's attack, assigns it to cpu_attack
                player_armour = player_mech[2] #slices player armour, assigns it to player_armour
                player_health = player_mech[1] #slices player health, assigns it to player_health

                #if player armour is greater then cpu attack
                #subtracts the cpu attack from player armour and inserts it into the player stats
                if player_armour > cpu_attack:
                    dmg_armour = player_armour - cpu_attack
                    player_mech.pop(2)
                    player_mech.insert(2, dmg_armour)
                    print('---------------------\nCpu: ' + cpu_mech[0] + ' attacked you, ' + str(cpu_attack) + ' damage was done to your armour\n---------------------') # prints damage done
                    # checks for inventory use by player and cpu and applies it if the instance is true other wise attack_first is equal to True
                    if c_shock == True:
                        first_attack = False
                        c_shock = False
                    
                    elif p_burn > 0:
                        cpu_health = cpu_mech[1]
                        cpu_burn = cpu_health - 30
                        cpu_mech.pop(1)
                        cpu_mech.insert(1, cpu_burn)
                        p_burn -= 1
                        print('**********\n' + cpu_mech[0] + ' was burned for 30 damage\n**********')
                        first_attack = True
                    
                    else:
                        first_attack = True

                #if player armour is less then or equal to cpu attack and player armour is greater than 0
                #subtracts the cpu attack from the player armour and adds the total to player health, then inserts the new health to player stats 
                elif (player_armour <= cpu_attack) and (player_armour > 0):
                    dmg_armour = player_armour - cpu_attack
                    dmg_health = player_health + dmg_armour
                    player_mech.pop(2)
                    player_mech.insert(2, 0)
                    player_mech.pop(1)
                    player_mech.insert(1, dmg_health)
                    print('---------------------\nCpu: ' + cpu_mech[0] + ' attacked you, ' + str(cpu_attack) + ' damage was done to your armour \nyou broke their armour!\n---------------------')# prints damage done
                    # checks for inventory use by player and cpu and applies it if the instance is true other wise attack_first is equal to True
                    if c_shock == True:
                        first_attack = False
                        c_shock = False
                    
                    elif p_burn > 0:
                        cpu_health = cpu_mech[1]
                        cpu_burn = cpu_health - 30
                        cpu_mech.pop(1)
                        cpu_mech.insert(1, cpu_burn)
                        p_burn -= 1
                        print('**********\n' + cpu_mech[0] + ' was burned for 30 damage\n**********')
                        first_attack = True
                    
                    else:
                        first_attack = True
                    
                #if player armour is equal to 0
                elif player_armour == 0:

                    #if player health is greater then cpu attack
                    #subtract cpu attack form player health and inserts it back into the player stats
                    if player_health > cpu_attack:
                        dmg_health = player_health - cpu_attack
                        player_mech.pop(1)
                        player_mech.insert(1, dmg_health)
                        print('---------------------\nCpu: ' + cpu_mech[0] + ' attacked you, ' + str(cpu_attack) + ' damage was done\n---------------------') #prints damage done
                       # checks for inventory use by player and cpu and applies it if the instance is true other wise attack_first is equal to True
                        if c_shock == True:
                            first_attack = False
                            c_shock = False
                        
                        elif p_burn > 0:
                            cpu_health = cpu_mech[1]
                            cpu_burn = cpu_health - 30
                            cpu_mech.pop(1)
                            cpu_mech.insert(1, cpu_burn)
                            p_burn -= 1
                            print('**********\n' + cpu_mech[0] + ' was burned for 30 damage\n**********')
                            first_attack = True
                        
                        else:
                            first_attack = True

                    # if player health is less then or equal to 0 or player health is less then or equal to cpu attack
                    #sets player health to 0
                    #returns player as a loser
                    elif (player_health <= 0) or (player_health <= cpu_attack):
                        player_mech.pop(1)
                        player_mech.insert(1, 0)
                        print('Cpu: ' + cpu_mech[0] + ' has defeated you!!!!!')
                        battle = False
                        inventory.insert(0, 'L')
                        return inventory
                            
                    else:#prints an error
                        print('error, battleSequence(), player health damage')
                                     
                else:# prints an error
                    print(' error, battleSequence(), player armour damage')
                    
            elif (option >= 8) and (option <= 9): #if the cpu chooses special attack
                cpu_special = 1.5 * (cpu_mech[3]) #slices the attack from cpu and muliplies it by 1.5, then assigns it to cpu_special
                special_chance = cpu_mech[4] #assigns the cpu_mech at the index of 4 to special chance
                random_num = random.randint(1, 100) #generates a random number between  1 and 100

                #if random_num is between 1 and special chance slices and assigns player armour and player health
                if (random_num >= 1) and (random_num <= special_chance):
                    player_armour = player_mech[2]
                    player_health = player_mech[1]

                    #if player armour is greater then cpu attack
                    #subtracts the cpu attack from player armour and inserts it into the player stats
                    if player_armour > cpu_special:
                        dmg_armour = player_armour - cpu_special
                        player_mech.pop(2)
                        player_mech.insert(2, dmg_armour)
                        print('---------------------\nCpu you attacked you, ' + str(cpu_special) + ' damage was done to your armour\n---------------------') #prints damage done
                        # checks for inventory use by player and cpu and applies it if the instance is true other wise attack_first is equal to True
                        if c_shock == True:
                            first_attack = False
                            c_shock = False
                        
                        elif p_burn > 0:
                            cpu_health = cpu_mech[1]
                            cpu_burn = cpu_health - 30
                            cpu_mech.pop(1)
                            cpu_mech.insert(1, cpu_burn)
                            p_burn -= 1
                            print('**********\n' + cpu_mech[0] + ' was burned for 30 damage\n**********')
                            first_attack = True
                        
                        else:
                            first_attack = True

                    #if player armour is less then or equal to cpu attack and player armour is greater than 0
                    #subtracts the cpu attack from the player armour and adds the total to player health, then inserts the new health to player stats 
                    elif (player_armour <= cpu_special) and (player_armour > 0):
                        dmg_armour = player_armour - cpu_special
                        dmg_health = player_health + dmg_armour
                        player_mech.pop(2)
                        player_mech.insert(2, 0)
                        player_mech.pop(1)
                        player_mech.insert(1, dmg_health)
                        print('---------------------\nCpu attacked you, ' + str(cpu_special) + ' damage was done to your armour \nthey broke their armour!\n---------------------')#prints damage done
                        # checks for inventory use by player and cpu and applies it if the instance is true other wise attack_first is equal to True
                        if c_shock == True:
                            first_attack = False
                            c_shock = False
                        
                        elif p_burn > 0:
                            cpu_health = cpu_mech[1]
                            cpu_burn = cpu_health - 30
                            cpu_mech.pop(1)
                            cpu_mech.insert(1, cpu_burn)
                            p_burn -= 1
                            print('**********\n' + cpu_mech[0] + ' was burned for 30 damage\n**********')
                            first_attack = True
                        
                        else:
                            first_attack = True
                    
                    #if player armour is equal to 0
                    elif player_armour == 0:

                        #if player health is greater then cpu attack
                        #subtract cpu attack form player health and inserts it back into the player stats
                        if player_health > cpu_special:
                            dmg_health = player_health - cpu_special
                            player_mech.pop(1)
                            player_mech.insert(1, dmg_health)
                            print('---------------------\nCpu attacked you, ' + str(cpu_special) + ' damage was done\n---------------------')#prints damage done
                            # checks for inventory use by player and cpu and applies it if the instance is true other wise attack_first is equal to True
                            if c_shock == True:
                                first_attack = False
                                c_shock = False
                            
                            elif p_burn > 0:
                                cpu_health = cpu_mech[1]
                                cpu_burn = cpu_health - 30
                                cpu_mech.pop(1)
                                cpu_mech.insert(1, cpu_burn)
                                p_burn -= 1
                                print('**********\n' + cpu_mech[0] + ' was burned for 30 damage\n**********')
                                first_attack = True
                            
                            else:
                                first_attack = True

                        # if player health is less then or equal to 0 or player health is less then or equal to cpu attack
                        #sets player health to 0
                        #returns player as a loser
                        elif (player_health <= 0) or (player_health <= cpu_special):
                            player_mech.pop(1)
                            player_mech.insert(1, 0)
                            print(cpu_mech[0] + ' has defeated You!!!!!')
                            battle = False
                            inventory.insert(0, 'L')
                            return inventory
                        
                        else:
                            print('Special atk, cpu health error')
                        
                    else:
                        print('Special atk, cpu armour error')
                        
                else:#else cpu has missed
                    print(cpu_mech[0] + ' missed!')
                    # checks for inventory use by player and cpu and applies it if the instance is true other wise attack_first is equal to True
                    if c_shock == True:
                        first_attack = False
                        c_shock = False
            
                    elif p_burn > 0:
                        cpu_health = cpu_mech[1]
                        cpu_burn = cpu_health - 30
                        cpu_mech.pop(1)
                        cpu_mech.insert(1, cpu_burn)
                        p_burn -= 1
                        print('**********\n' + cpu_mech[0] + ' was burned for 30 damage\n**********')
                        first_attack = True
                    else:
                        first_attack = True
                
            else:
                bag = True #assigns True to bag
                while bag: #while bag is True
                    get_item = random.choice(cpu_inventory)# randomly selects an item from inventoru
                    if get_item == 'Shock Charge': #if the item is Shoch Charge
                        print('**********\n' + cpu_mech[0] + ' used shock charge, you are paralyzed for 2 turns\n**********') #prints the player has missed 2 turns
                        c_shock = True #assigns True to c_shock
                        bag = False #assigns False to bag
                        first_attack = False #assigns False yto first attack

                    # if item is equal to repair kit
                    elif get_item == 'Repair Kit':
                        rk = 300 #assigns 300 to rk
                        cpu_health = cpu_mech[1] #slices health from cpu and assigns it tp cpu_health

                        #adds rk to player health but makes sure it doesnt go over the original health
                        if (rk + cpu_health) > ori_cpu[1]:
                            cpu_mech.pop(1)
                            cpu_mech.insert(1, ori_cpu[1])
                            print('**********\n' + cpu_mech[0] + ' has used Repair Kit, regen + 300 health\n**********')
                            bag = False
                            battle = True
                            first_attack = True

                        elif (rk + cpu_health) < ori_cpu[1]:
                            regen = rk + cpu_health
                            cpu_mech.pop(1)
                            cpu_mech.insert(1, regen)
                            print('**********\n' + cpu_mech[0] + ' has used Repair Kit, regen + 300 health\n**********')
                            bag = False
                            battle = True
                            first_attack = True
                            
                        else:#else regen is not possible
                            print('regen is not possible')

                    #if get_item is equal to blow torch
                    elif get_item == 'Blow Torch':
                        bt = 150#assigns 150 to bt
                        cpu_health = cpu_mech[1] #assigns the slice of cpu_mech at the index 1 to cpu_health

                        #adds bt to player health but makes sure it doesnt go over the original health
                        if (bt + cpu_health) > ori_cpu[1]:
                            cpu_mech.pop(1)
                            cpu_mech.insert(1, ori_cpu[1])
                            print('**********\n' + cpu_mech[0] + ' has used Blow Torch, regen + 150 health\n**********')
                            bag = False
                            battle = True
                            first_attack = True

                        elif (bt + cpu_health) < ori_cpu[1]:
                            regen = bt + cpu_health
                            cpu_mech.pop(1)
                            cpu_mech.insert(1, regen)
                            print('**********\n' + cpu_mech[0] + ' has used Blow Torch, regen + 150 health\n**********')
                            bag = False
                            battle = True
                            first_attack = True
                            
                        else:
                            print('regen is not possible')

                    else:
                        print('error setBattaleSequence() cpu inventory')
 
#showPlayerGauge displays the players health and armour                      
def showPlayerGauge(pMech):
    print()
    name = pMech[0]
    health = str(pMech[1])
    armour = str(pMech [2])
    print('\n---' + name + '---')
    print('Health: ' + health)
    print('Armour: ' + armour)
    
#showCpuGauge displays the players health and armour
def showCpuGauge(cMech):
    name = cMech[0]
    health = str(cMech[1])
    armour = str(cMech [2])
    print('---Cpu: ' + name + '---')
    print('Health: ' + health)
    print('Armour: ' + armour)
    print()
    

#defines setWhoGoesFirst() taking the player mech and the cpuMech, compares the speed from each mech to determine who attacks first
def setWhoGoesFirst(playerMech, cpuMech):
    #name = ['name', 'health', 'armour', 'attack', 'spattack', 'speed', 'dodge']
    player_speed = playerMech[5]
    cpu_speed = cpuMech[5]

    flag = True
    while flag:
        if player_speed > cpu_speed:
            flag = False
            player_first = True

        elif player_speed < cpu_speed:
            flag = False
            player_first = False
            
        else:
            player_speed = random.randint(1, 10)
            cpu_speed = random.randint(1, 10)
            flag = True
            
    return player_first
        
mainMenu()
