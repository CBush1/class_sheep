# lab26.py
import random

'''Game Class'''

class Entity:
    def __init__(self, location_i, location_j, character):
        self.location_i = location_i
        self.location_j = location_j
        self.character = character

class Player(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '☺')

class Zombie(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '⨀')

class Skeleton(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '⨂')

class Matador(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '⨷')

class Lich(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '⨁')

class Bomb(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '⨶')

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def random_location(self):
        return random.randint(0, self.width - 1), random.randint(0, self.height - 1)

    def print(self, entities):
        for i in range(self.height):
            for j in range(self.width):
                for k in range(len(entities)):
                    if entities[k].location_i == i and entities[k].location_j == j:
                        print(entities[k].character, end='')
                        break
                else: # the else executes if the loop does NOT break
                    print(' ', end='') # no entity found, break
            print()
# class Inventory:
#     def __init__(self, items):
#         self.source = source
#         self.items = []
#
#     def get_item(self, mon_type):
#         item_dict = {'zombie': 'useless decoration', 'wilted salad', 'skeleton': 'notched saber', 'sacrificial jizo', 'litch': 'phylactery', 'bony finger', 'matador': 'red capote']
#         lucky_draw = []
#         for item in item_dict[mon_type]:
#             lucky_draw.append(item)
#         add_item = random.choice(lucky_draw)
#         self.items.append(add_item)



'''Flavor Functions'''

def flavor_intro(instring):
    if instring == 'zombie':
        return 'A zombie shambles blindly into you.'
    if instring == 'skeleton':
        return 'A skeleton warrior draws their sword, gnashing their teeth.'
    if instring == 'lich':
        return 'A lich begins weaving their evil magicks.'
    if instring == 'matador':
        return 'A skeleton matador challenges you, swearing they will once again prove victorious.'
    if instring == 'bomb':
        return 'You run into a bomb and explode. Life is unfair. Like this game.'

def flavor_combat(monster, action):
    if monster == 'zombie':
        effective = ['attack', 'magic', 'throw', 'dance']
        if action in effective:
            result = 'win'
            if action == 'attack':
                flavor = 'You easily slay the zombie by removing the head or destroying the brain.'
            if action == 'magic':
                flavor = 'You blow the zombie up. He was just minding his own busines, you know.'
            if action == 'throw':
                flavor = 'You hurl a throwing star coated with oil into the zombie, burning it to ash.'
            if action == 'dance':
                flavor = 'You and the zombie have a dance off. They leave, impressed with your moves.'
        else:
            flavor ='The zombie has no idea what you\'re trying to do and just eats you.'
            result = 'lose'

    if monster == 'skeleton':
        effective = ['attack', 'magic']
        if action in effective:
            result = 'win'
            if action == 'attack':
                flavor = 'You fight the skeleton warrior. Make no bones about it, you win.'
            if action == 'magic':
                flavor = 'Your spells destroy the skeleton warrior, leaving only their chattering skull behind.'
        else:
            result = 'lose'
            if action == 'throw':
                flavor = 'You hurl a throwing star straight through the skeleton\'s ribcage. Good job.'
            if action == 'dance':
                flavor = 'You dance with the skeleton, like something out of a Holbein woodblock printing. Then you remember the title of those printings.'
            else:
                flavor = 'The skeleton warrior has a bone to pick with you.'

    if monster == 'lich':
        effective = ['throw']
        if action in effective:
            result = 'win'
            flavor = 'You shatter a canopic jar at the lich\'s waist with a throwing star. It contained their spirit, and the lich turns to dust.'
        else:
            result = 'lose'
            if action == 'attack':
                flavor = 'You attempt to slice the lich but they turn your sword into a string of beetles.'
            if action == 'magic':
                flavor = 'Trying to beat an undead sorcerer in a magic duel?\n ...lol'
            if action == 'dance':
                flavor = 'The lich is a horrible dancer. Rigor mortis isn\'t fun.\nThey\'re also a horrible loser, as you find out, engulfed in flames.'
            else:
                flavor = 'Is it lich or liche?'
        print('\nYou Died.')

    if monster == 'matador':
        result = 'lose'
        if action == 'attack':
            flavor = 'Your sword hits nothing but his red capote. They skewer you with an obnoxious flourish.'
        if action == 'magic':
            flavor = 'They are too impatient to let you finish casting. You bleed out cursing at how unfair it is.'
        if action == 'throw':
            flavor = 'Your throwing star ruins the red capote, which only makes the matador really, really mad.'
        if action == 'dance':
            flavor = 'The matador dances circles around you, being experienced at pasadoble. You feel so embarrassed you could die. And you do.'
        else:
            flavor ='The matador wasn\'t kidding.'
    return (flavor, result)


board = Board(25, 25)

pi, pj = board.random_location()
player = Player(pi, pj)

entities = [player]
enemies = []
enemy_types = []

for i in range(6):
    ei, ej = board.random_location()
    enemy = Zombie(ei, ej)
    entities.append(enemy)
    enemies.append(enemy)
    enemy_types.append('zombie')

for i in range(4):
    ei, ej = board.random_location()
    enemy = Skeleton(ei, ej)
    entities.append(enemy)
    enemies.append(enemy)
    enemy_types.append('skeleton')

for i in range(3):
    ei, ej = board.random_location()
    enemy = Lich(ei, ej)
    entities.append(enemy)
    enemies.append(enemy)
    enemy_types.append('lich')

for i in range(4):
    ei, ej = board.random_location()
    enemy = Bomb(ei, ej)
    entities.append(enemy)
    enemies.append(enemy)
    enemy_types.append('bomb')

for i in range(1):
    ei, ej = board.random_location()
    enemy = Matador(ei, ej)
    entities.append(enemy)
    enemies.append(enemy)
    enemy_types.append('matador')

while True:

    board.print(entities)

    command = input('what is your command? ').lower()  # get the command from the user

    if command == 'done':
        break  # exit the game
    elif command in ['l', 'left', 'w', 'west']:
        player.location_j -= 1  # move left
        if player.location_j < 0:
            player.location_j += 1
            print('You can\'t go that way.')
    elif command in ['r', 'right', 'e', 'east']:
        player.location_j += 1  # move right
        if player.location_j > 25:
            player.location_j -= 1
            print('You can\'t go that way.')
    elif command in ['u', 'up', 'n', 'north']:
        player.location_i -= 1  # move up
        if player.location_i < 0:
            player.location_i += 1
            print('You can\'t go that way.')
    elif command in ['d', 'down', 's', 'south']:
        player.location_i += 1  # move down
        if player.location_i > 24:
            player.location_i -= 1
            print('You can\'t go that way.')

    for enemy in enemies:
        if enemy.location_i == player.location_i and enemy.location_j == player.location_j:
            for index in range(len(enemies)):
                if enemies[index] == enemy:
                    for i in range(len(enemy_types)):
                        if i == index:
                            encounter_type = enemy_types[index]
            print(flavor_intro(encounter_type))
            if encounter_type == 'bomb':
                print('\nYou Died.')
                exit()
            action = input('what will you do? ').lower()
            result = flavor_combat(encounter_type, action)
            print(result[0])
            if result[1] == 'win':
                entities.remove(enemy)
                enemies.remove(enemy)
                break
            else:
                print('\nYou Died.')
                exit()

# width = 25  # the width of the board
# height = 25  # the height of the board
#
# # create a board with the given width and height
# # we'll use a list of list to represent the board
# board = []  # start with an empty list
# for i in range(height):  # loop over the rows
#     board.append([])  # append an empty row
#     for j in range(width):  # loop over the columns
#         board[i].append(' ')  # append an empty space to the board
#
# # define the player position

    # def movement_system(self, command):
    #     if command == 'done':
    #         return 'break'  # exit the game
    #     elif command == 'left':
    #         player_j -= 1  # move left
    #     elif command == 'right':
    #         player_j += 1  # move right
    #     elif command == 'up':
    #         player_i -= 1  # move up
    #     elif command == 'down':
    #         player_i += 1  # move down
    #     elif command == 'magic':
    #         aim = input('In which direction? ')
    #         if aim == 'right':
    #             return 'break'
    #         if aim == 'left':
    #             return 'break'
    #         if aim == 'up':
    #             return 'break'
    #         if aim == 'down':
    #             return 'break'
    #     elif command == 'throw':
    #         aim = input('In which direction? ')
    #         if aim == 'right':
    #             return 'break'
    #         if aim == 'left':
    #             return 'break'
    #         if aim == 'up':
    #             return 'break'
    #         if aim == 'down':
    #             return 'break'
    #
    # def setup(): # add random number of enemies in random locations
    #     for zombie in range(0, 5):
    #         enemy_i = random.randint(0, height - 1)
    #         enemy_j = random.randint(0, width - 1)
    #         board[enemy_i][enemy_j] = '⨀'
    #     for skeleton in range(0, 3):
    #         enemy_i = random.randint(0, height - 1)
    #         enemy_j = random.randint(0, width - 1)
    #         board[enemy_i][enemy_j] = '⨂'
    #     for skeleton_knight in range(1):
    #         enemy_i = random.randint(0, height - 1)
    #         enemy_j = random.randint(0, width - 1)
    #         board[enemy_i][enemy_j] = '⨷'
    #     for lich in range(0,2):
    #         enemy_i = random.randint(0, height - 1)
    #         enemy_j = random.randint(0, width - 1)
    #         board[enemy_i][enemy_j] = '⨁'
    #     for bomb in range(0,4):
    #         enemy_i = random.randint(0, height - 1)
    #         enemy_j = random.randint(0, width - 1)
    #         board[enemy_i][enemy_j] = '⨶'
# while True:
#     command = input('What is your command? ') # user input
#     m_action = movement_system(command) # runs movement system at the start of each turn
#     if m_action == 'break':
#         break
#
#     if board[player_i][player_j] == '⨀':
#         print('A zombie shambles blindly into you.')
#         action = input('What will you do? ')
#         if action == 'attack':
#             print('You easily slay the zombie by removing the head or destroying the brain.')
#             board[player_i][player_j] = ' '
#         if action == 'magic':
#             print('You blow the zombie up. He was just minding his own busines, you know.')
#             board[player_i][player_j] = ' '
#         if action == 'throw':
#             print('You hurl a throwing star coated with oil into the zombie, burning it to ash.')
#             board[player_i][player_j] = ' '
#         if action == 'dance':
#             print('You and the zombie have a dance off. They leave, impressed with your moves.')
#             board[player_i][player_j] = ' '
#         else:
#             print('The zombie has no idea what you\'re trying to do and just eats you.')
#             print('\nYou Died.')
#             break
#
#     if board[player_i][player_j] == '⨂':
#         print('A skeleton warrior draws his sword, gnashing his teeth.')
#         action = input('What will you do? ')
#         if action == 'attack':
#             print('You fight the skeleton warrior. Make no bones about it, you win.')
#             board[player_i][player_j] = ' '
#         if action == 'magic':
#             print('Your spells destroy the skeleton warrior, leaving only their chattering skull behind.')
#             board[player_i][player_j] = ' '
#         if action == 'throw':
#             print('You hurl a throwing star straight through the skeleton\'s ribcage. Good job.')
#             print('\nYou Died.')
#             break
#         if action == 'dance':
#             print('You dance with the skeleton, like something out of a Holbein woodblock printing.')
#             print('Then you remembered the title of those printings.')
#             print('\nYou Died.')
#             break
#         else:
#             print('The skeleton warrior has a bone to pick with you.')
#             print('\nYou Died.')
#             break
#
#     if board[player_i][player_j] == '⨁':
#         print('A lich emerges from the darkness, preparing their hideous spells.')
#         action = input('What will you do? ')
#         if action == 'attack':
#             print('You attempt to slice the lich but they turn your sword into a string of beetles.')
#             print('\nYou Died.')
#             break
#         if action == 'magic':
#             print('Trying to defeat a lich in a magic duel?')
#             print()
#             print('lol')
#             print()
#             print('\nYou Died.')
#             break
#         if action == 'throw':
#             print('You shatter a canopic jar at the lich\'s waist with a throwing star. It contained their spirit.')
#             board[player_i][player_j] = ' '
#         if action == 'dance':
#             print('The lich is a horrible dancer. Rigor mortis isn\'t fun.')
#             print('They\'re also a horrible loser, as you find out, engulfed in flames.')
#             print('\nYou Died.')
#             break
#         else:
#             print('Is it lich or liche?')
#             print('\nYou Died.')
#             break
#
#     if board[player_i][player_j] == '⨷':
#         print('A skeleton matador challenges you, swearing they will once again prove victorious.')
#         action = input('What will you do? ')
#         if action == 'attack':
#             print('Your sword hits nothing but his red capote. They skewer you with an obnoxious flourish.')
#             print('\nYou Died.')
#             break
#         if action == 'magic':
#             print('They are too impatient to let you finish casting. You bleed out cursing at how unfair it is.')
#             print('\nYou Died.')
#             break
#         if action == 'throw':
#             print('Your throwing star ruins the red capote, which only makes the matador wroth.')
#             print('\nYou Died.')
#             break
#         if action == 'dance':
#             print('You attempt to dance with the matador, but they do pasadoble with you as the "capote."')
#             print('They cap off their performance by stabbing you.')
#             print('\nYou Died.')
#             break
#         else:
#             print('The matador wasn\'t kidding.')
#             print('\nYou Died.')
#             break
#
#     if board[player_i][player_j] == '⨶':
#         print('You run into a bomb and explode. Life is unfair. Like this game.')
#         print('\nYou Died.')
#         break
#
#             # print out the board
#     for i in range(height):
#         for j in range(width):
#             # if we're at the player location, print the player icon
#             if i == player_i and j == player_j:
#                 print('☺', end=' ')
#             else:
#                 print(board[i][j], end=' ')  # otherwise print the board square
#         print()
