import random
import time

class Enemy:
    def __init__(self, health: int, name: str, attack: int):
        self.health = health
        self.name = name
        self.attack = attack
        
class Character:
    def __init__(self, health: int, name: str, attack: int, potion: int, dungeon_key: bool, willows_key: bool):
        self.health = health
        self.name = name
        self.attack = attack
        self.potion = potion
        self.dungeon_key = dungeon_key
        self.willows_key = willows_key

class Player(Character):
    def __init__(self, player: Character):
        health = player.health
        name = player.name
        attack = player.attack
        potion = player.potion
        dungeon_key = player.dungeon_key
        willows_key = player.willows_key
        Character.__init__(self, health, name, attack, potion, dungeon_key, willows_key)

    def player_attack(self, other_char):
        self.attack = int(random.randrange(12, 18))
        other_char.health = other_char.health - self.attack
        return other_char.health
    
    def use_potion(self):
        self.potion = self.potion - 1
        self.health = self.health + 10
        return self.health
    
class Troll(Enemy):
    def __init__(self, troll: Enemy):
        health = troll.health
        name = troll.name
        attack = troll.attack
        Enemy.__init__(self, health, name, attack)

    def troll_attack(self, other_char):
        self.attack = 10
        other_char.health = other_char.health - self.attack
        return other_char.health
    
class Ghoul(Enemy):
    def __init__(self, ghoul: Enemy):
        health = ghoul.health
        name = ghoul.name
        attack = ghoul.attack
        Enemy.__init__(self, health, name, attack)

    def ghoul_attack(self, other_char):
        self.attack = int(random.randrange(7, 10))
        other_char.health = other_char.health - self.attack
        return other_char.health
    
class Meijer(Enemy):
    def __init__(self, meijer: Enemy):
        health = meijer.health
        name = meijer.name
        attack = meijer.attack
        Enemy.__init__(self, health, name, attack)

    def meijer_attack(self, other_char):
        self.attack = int(random.randrange(9, 13))
        other_char.health = other_char.health - self.attack
        return other_char.health

def intro():
    intro_choice = True
    # Font from: https://www.asciiart.eu/text-to-ascii-art
    print("""\n╔╦╗╦ ╦╔═╗  ╔═╗ ╦ ╦╔═╗╔═╗╔╦╗  ╔═╗╔═╗╦═╗  ╔╦╗╦ ╦╔═╗  ╔═╗╔╗  ╦╔═╗╔═╗╔╦╗
 ║ ╠═╣║╣   ║═╬╗║ ║║╣ ╚═╗ ║   ╠╣ ║ ║╠╦╝   ║ ╠═╣║╣   ║ ║╠╩╗ ║║╣ ║   ║ 
 ╩ ╩ ╩╚═╝  ╚═╝╚╚═╝╚═╝╚═╝ ╩   ╚  ╚═╝╩╚═   ╩ ╩ ╩╚═╝  ╚═╝╚═╝╚╝╚═╝╚═╝ ╩ 
\n""")
    time.sleep(4)
    print("All is quiet in the land of the Quigley Kingdom and then...\n")
    time.sleep(2) 
    print("THUNDER STRIKES\n") 
    time.sleep(1)
    print("CRASH!!!! Someone broke into the castle...\n")
    while intro_choice:
        intro_decision = input("Do you investigate? (1), or, Do you go back to sleep? (2): ")
        if intro_decision == "1":
            intro_choice = False
            print("\nYou get up out of bed and make your way to the hall...\n")
            time.sleep(4)
            print("You run over to see the king knocked out on the floor...\n")
            time.sleep(4)
            print("In the shadows, a dark hooded figure runs away...\n")
            time.sleep(4)
            print("With a stark and sinister laugh he disappears into the night,\n you look back down to see King John stirring.\n")
            time.sleep(4)
            print("With a weak voice he says, 'Mejier The Mystic has returned...'\n")
            time.sleep(4)
            print("You quickly go to put on your armor but the king tells you to stop\n and wait until morning. You head back to bed.\n")
            time.sleep(4)
            print("Z")
            time.sleep(1)
            print("Z")
            time.sleep(1)
            print("z")
            time.sleep(1)
            quigleyKingdom()

        elif intro_decision == "2":
            intro_choice = False
            print("""\n'Ahhh must've been the wind' you say with a yawn.\n You go back to sleep.\n""")
            time.sleep(3)
            print("Z")
            time.sleep(1)
            print("Z")
            time.sleep(1)
            print("z")
            time.sleep(1)
            quigleyKingdom()        
        else:
            print("Please Enter a vaild input")
    
def quigleyKingdom():
    # ASCII Art from: https://www.asciiart.eu/buildings-and-places/castles
    print("""                             -|             |-
         -|                  [-_-_-_-_-_-_-_-]                  |-
         [-_-_-_-_-]          |             |          [-_-_-_-_-]
          | o   o |           [  0   0   0  ]           | o   o |
           |     |    -|       |           |       |-    |     |
           |     |_-___-___-___-|         |-___-___-___-_|     |
           |  o  ]              [    0    ]              [  o  |
           |     ]   o   o   o  [ _______ ]  o   o   o   [     | ----__________
_____----- |     ]              [ ||||||| ]              [     |
           |     ]              [ ||||||| ]              [     |
       _-_-|_____]--------------[_|||||||_]--------------[_____|-_-_
      ( (__________------------_____________-------------_________) )
                            THE QUIGLEY KINGDOM\n""")
    time.sleep(4)

    print("""   TRUMPETS BLAZE\n
          'Last night, King John's Castle was broken into,
          The Object was stolen from his secret room. A dark hooded figure
          was last seen running away. Please tell a guard if you have and information.'
          said the messenger.\n""")
    time.sleep(8)
    print("You walk up to the King sitting on his throne,\n 'My Lord, how may I assist in the search this morning?'\n")
    time.sleep(4)
    user_name = str(input("To which the king replied,\n 'I am sorry remind me of your name dear knight: "))
    player = Player(Character(100, user_name, 12, 3, False, False))
    print(f"\n'Ahh yes, Knight {user_name}, please forgive me my head is spinning from last night.'\n")
    time.sleep(4)
    print("Last night, Meijer The Mysitc, an evil wizard that has tormented the land for years,\n broke into the castle and stole The Object.\n")
    time.sleep(5)
    print("'I am sending you on a journey to search for The Object\n PLEASE find Meijer The Mystic before he uses its power!'\n")
    time.sleep(4)
    print("'In your inventory you'll have 3 health potions and a sword that deals 12-17 damage.\n I am also giving you some special new armor'\n")
    time.sleep(4)
    quigley_choice = True
    while quigley_choice:
        quigley_input = input("'Where would you like to go first?'\n The Dungeon? (1) or, The Whispering Willows? (2): ")
        if quigley_input == "1":
            quigley_choice = False
            Player.dungeon_key = True
            print("\nTo the depths of the dungeon we go\n be mindful of The Ghoul...")
            time.sleep(4)
            theDungeon(player)
        elif quigley_input == "2":
            quigley_choice = False
            Player.willows_key = True
            print("\nAhh The Whispering Willows,\n watch out, the I hear The Troll dwells there...")
            time.sleep(4)
            whisperingWillows(player)
        else:
            print("Please Enter a vaild input")

def theDungeon(player: Player):
    # ASCII Art from: https://www.asciiart.eu/text-to-ascii-art
    print("""\n    ================================
     ||     ||<(.)>||<(.)>||     || 
     ||    _||     ||     ||_    || 
     ||   (__D     ||     C__)   || 
     ||   (__D     ||     C__)   ||
     ||   (__D     ||     C__)   ||
     ||   (__D     ||     C__)   ||
     ||     ||     ||     ||     ||
    ================================
              THE DUNGEON\n""")
    time.sleep(4)

    print("You slowly make your way down the steps of The Dungeon,\n in the distance you hear as though someone was speaking.\n")
    time.sleep(5)
    print("Then silence...\n")
    time.sleep(2)
    print("SCREECH!!! Something scratched your armor!!!\n")
    time.sleep(3)
    print("With little visablitiy you see it is The Ghoul,\n You must attack!\n")
    ghoul = Ghoul(Enemy(85, "The Ghoul", 10))
    while ghoul.health > 0:
        if player.health <= 0:
            lossGame()
            break
        else:
            player_hp = ghoul.ghoul_attack(player)
            print(f"The Ghoul strikes you and your health is now at {player_hp} HP\n")
            time.sleep(3)
            heal_up(player)
            ghoul_hp = player.player_attack(ghoul)
            if ghoul_hp <= 0:
                print("With a swift final blow, you knock down The Ghoul!\n")
                time.sleep(2)
            else:
                print(f"You attack The Ghoul and his health is now at {ghoul_hp}\n")

    if ghoul.health <= 0:
        print("No, please don't kill me!\n My name is Oswin and I am from the Quigley Kindom!\n Meijer used his magic to turn me into this monster.\n")
        time.sleep(6)
        print("""'Meijer?' You exclaim\n 'That's actually who I am looking for. Have you seen him?'\n""")
        time.sleep(4)
        print("""'OH! Don't go looking for him! You will surely die!\n But for your bravery I will award you with three health potions.'\n""")
        player.potion = player.potion + 3
        player.dungeon_key = True
        time.sleep(4)
        if player.willows_key == True:
            print("""'I can smell the leaves of the willow trees on you\n so I know you've already been there and visited The Troll.\n Head to Mount Galdr, it is Meijers home...'\n""")
            time.sleep(7)
            print("To Mount Galdr we go...")
            time.sleep(2)
            mountGaldr(player)
        else:
            print("""'Often Meijer is seen in the Whispering Willows\n Speaking with the spirits there and learning new magic.\n Go there, but be careful of The Troll...'\n""")
            time.sleep(7)
            print("To the Whispering Willows we go...")
            time.sleep(2)
            whisperingWillows(player)

def whisperingWillows(player: Player):
    # ASCII Art from: https://www.asciiart.eu/text-to-ascii-art
    print("""\n                             ..---.......                                    
                            .-...........-.                                  
                         .-.-.. .....-.....-.                                
                       .......-.-.....  .. .--.--..                          
                     ..-...-..-...-.... .....  .. .-..                       
                    ...-......-....-.......-.... ....-.                      
                 ......-....-.... .+.  ....-..  ..-..-.                      
                ...... .....-.....-+-.....-.--. .-...-..                     
                .-.... .-. .-- .-.-+...-....-.. .-. ....                     
                .-......+-.... .++-++-.-.---.... ...-..-.                    
                .......-.-.-.-.--+-.--.-...-....  .-.....                    
                .......-...--.--++.....-....-..........-.                    
                .-... ....-.+-..+--.-....-...-.---.-..-.                     
                 ... .-...-...-++----....--..-...--..-.                      
                  .-.-.-...-..-..+..-.-...-.....  ....                       
                   .-.....-....-..-..-.-. .--.    .-..                       
                       ..-..-...-..--..+.  ...    ....                       
                       .-.  .--.    ....+..                                  
                             ...    ..-..--.                                 
                                      --..-+.                                
                                      .-..--.                                
                                       .-..-+..                              
                                        -...-+.                              
                                     ...-....-+.......                       
                                  ..--..--...-..--.--..                      
                                           ....-....                         
                                                .. 
                                THE WHISPERING WILLOWS\n""" )
    time.sleep(4)
    print("As you walk into The Whispering Willows,\n you hear strange things and then quite. \n Almost a bit too quiet...")
    time.sleep(4)
    print("\nUP FROM THE RIVER THE TROLL APPEARS, and he is singing a song\n")
    troll = Troll(Enemy(100, "The Troll", 10))
    time.sleep(3)
    print("""           As the cool fog rolls,
          
          A traveler comes marching,

            Is he scared of trolls,
          
          Or will he come charging,

            Oh, Do not hurt thee!
          
            I only want to play a game,
          
          Answer these riddles three,

          And I will send you on your way!\n""")
    time.sleep(10)
    print("You draw back, and accept The Troll's game.\n")
    time.sleep(3)

    while player.health > 0:
        print("""The first riddle,\n
                I have roots that nobody sees,
                I am taller than the trees,
                        Up, Up I go,
                    But I never grow.
                        What am I?\n""")
        mountain_input = input("A Giant (1), A Mountain (2), A Dragon (3), A Beanstalk (4): ")
        if mountain_input == "2":
            print("\n'So you got past the first one,\n this next one won't be as easy.'\n")
            time.sleep(3)
            break
        else:
            player_hp = troll.troll_attack(player)
            if player_hp <= 0:
                lossGame()
            else:
                print(f"WRONG! The Whispering Winds attack you,\n your health is now at {player_hp} HP")
                time.sleep(2)
                heal_up(player)
                time.sleep(1)
                print("You must try again!\n")
                time.sleep(1)


    while player.health > 0:
        print("""       The more you take, the more you leave behind.
                        What am I?\n""")
        footsteps_input = input("A Shadow (1), A Coin (2), Time (3), Footsteps (4): ")
        if footsteps_input == "4":
            print("\n'BLAST, two down,\n this last one is my favorite.'\n")
            time.sleep(3)
            break
        else:
            player_hp = troll.troll_attack(player)
            if player_hp <= 0:
                lossGame()
            else:
                print(f"WRONG! The Whispering Winds attack you,\n your health is now at {player_hp} HP")
                time.sleep(2)
                heal_up(player)
                time.sleep(1)
                print("You must try again!")
                time.sleep(1)

    while player.health > 0:
        print("""       I speak with a mouth and hear without ears.
            I have no body but come alive with wind.
                        What am I?\n""")
        echo_input = input("An Echo (1), A Bird (2), A Ghost (3), A Flute (4): ")
        if echo_input == "1":
            print("\n'A clever one you are! For your bravery I will give you 3 health potions! \n Now what are you looking for?\n Why are you in my woods?'\n")
            player.potion = player.potion + 3
            player.willows_key = True
            time.sleep(5)
            print("'I am looking for Meijer The Mystic, have you seen him?' you exclaim.\n")
            time.sleep(3)
            if player.dungeon_key == True:
                print("""
OH NO NOT HIM, HE IS THE ONE WHO TURNED ME INTO THIS GREEN MONSTER!
My name was Richard and I used to be a normal fellow who ran The Tavern in Quigley Kingdom
I see by the claw marks on your armor that means you've paid a visit to The Ghoul...
Go to Mount Galdr, you will find Meijer there...\n""")
                time.sleep(9)
                print("To Mount Galdr we go...")
                time.sleep(3)
                mountGaldr(player)
                break
            else:
                print("""
OH NO NOT HIM, HE IS THE ONE WHO TURNED ME INTO THIS GREEN MONSTER!
My name was Richard and I used to be a normal fellow who ran The Tavern in Quigley Kingdom
If it might help, he is often seen in The Dungeon but be careful!
The Ghoul resides there in the darkness...\n""")
                time.sleep(9)
                print("To The Dungeon we go...")
                time.sleep(3)
                theDungeon(player)
                break
        else:
            player_hp = troll.troll_attack(player)
            if player_hp <= 0:
                lossGame()
            else:
                print(f"WRONG! The Whispering Winds attack you,\n your health is now at {player_hp} HP\n")
                time.sleep(2)
                heal_up(player)
                time.sleep(1)
                print("You must try again!\n")
                time.sleep(1)

def mountGaldr(player: Player):
    # ASCII Art from: https://www.asciiart.eu/text-to-ascii-art
    print("""                               .++.                              
                            ..-..+#-.                            
                     ...  ..+.. ..+##-.                          
                    .--#+--. ....+.##+-.. .-#.                   
                  .+..-#+...+-#+....####++.-##+.                 
                .+..+#+..-+.....++..+##+--...-###-               
             .-...++.-.++. .-...+##+.++..+-##+-.-##-..           
           .-. .--...--.+...  ....##-.-+.-..##+-+--##+.          
         ...  .... ... ..     .. -........  ..-+-....--.  
                            MOUNT GALDR""")
    time.sleep(4)

    print("You slowly make your way up the trail of Mount Galdr\n in the distance you see a light, then...\n")
    time.sleep(5)
    print("""In front of you Meijer appears saying,
    'Greetings adventurer! I hope youve enjoyed the 
    thrills, chills, and spills of this climb but now you will meet your doom...'\n""")
    time.sleep(6)
    print("With the wave of his staff he cast a magic spell,\n the orb flew and hits you right in the chest\n 'Take that HAHA!'\n")
    time.sleep(5)
    print("You stand unphased, the armor the King gave was resistant to magic attacks!\n")
    time.sleep(5)
    print("'WHAT!? It cant be! Fine, I will attack you with my staff!'\n Then disappearing and reappearing he begins his attacks!\n You must defend yourself!\n")
    time.sleep(5)
    meijer = Meijer(Enemy(100, "Meijer The Mystic", 10))
    while meijer.health > 0:
        if player.health <= 0:
            lossGame()
            break
        else:
            player_hp = meijer.meijer_attack(player)
            print(f"Meijer The Mystic strikes you and your health is now at {player_hp} HP\n")
            time.sleep(3)
            heal_up(player)
            meijer_hp = player.player_attack(meijer)
            if meijer_hp <= 0:
                print("With a swift final blow, you knock down Meijer The Mystic!\n")
                time.sleep(2)
            else:
                print(f"You attack Meijer The Mystic and his health is now at {meijer_hp}\n")

    if meijer.health <= 0:
        print("As Meijer falls towards the ground, The Object falls out of his pocket.\n IT'S HEADING TOWARDS THE LAVA PIT!!\n What do you do?\n")
        time.sleep(4)
        end_choice = True
        while end_choice:
            end_input = input("Do you go after The Object? (1) Or do you bind Meijer? (2): ")
            if end_input == "1":
                end_choice = False
                end_Game_One()
            elif end_input == "2":
                end_choice = False
                end_Game_Two()
            else:
                print("Please enter a vaild input.")

def end_Game_One():
    print("""\n And as you dove down to towards the lava pit
        you were able to catch The Object in the knick of time.
        You look back and Meijer The Mystic had vanished.
        You headed back down the mountain and presented The Object to King John.
        While you were on adventures, he found a mage that could use The Object
        to reverse Meijers magic. Using The Scroll of Snotor, the mage was able
        to undo the magic. Oswin (The Ghoul) and Richard (The Troll) were finally able to
        return to their homes.
        
        But out there in the darkness, with a sinister laugh echoing through the valley
          Meijer still resided and King John and his knights were ready for when he would return...\n""")
    time.sleep(20)
    print("""╔╦╗╦ ╦╔═╗  ╔═╗╔╗╔╔╦╗
 ║ ╠═╣║╣   ║╣ ║║║ ║║
 ╩ ╩ ╩╚═╝  ╚═╝╝╚╝═╩╝""")

def end_Game_Two():
    print("""\n And as you ran toward Meijer to bind him, you looked back to see
        The Object fall into the lava pit. Returning to the kingdom, King John placed
        Meijer into a special chamber that was able to prevent him from using his magic.
        Sadly, due to The Object being lost, Meijers magic could not be reversed and
        Oswin (The Ghoul) and Richard (The Troll) were stuck in their monstrous states forever.\n""")
    time.sleep(10)
    print("""╔╦╗╦ ╦╔═╗  ╔═╗╔╗╔╔╦╗
 ║ ╠═╣║╣   ║╣ ║║║ ║║
 ╩ ╩ ╩╚═╝  ╚═╝╝╚╝═╩╝""")

def heal_up(player: Player):
    print(f"You have {player.potion} potion(s) in your inventory.")
    if player.potion == 0:
        print("You are out of potions! Looks like you must survive!")
        time.sleep(2)
    else:
        heal_choice = True
        while heal_choice:
            heal_input = input("Do you want to use a health potion? (Y, N): ")
            if heal_input == "Y":
                heal_choice = False
                if player.potion > 0:
                    player_hp = player.use_potion()
                    print(f"\nYou healed up for 10 HP, you are now at {player_hp} HP.\n")
                    time.sleep(2)
            elif heal_input == "y":
                heal_choice = False
                if player.potion > 0:
                    player_hp = player.use_potion()
                    print(f"\nYou healed up for 10 HP, you are now at {player_hp} HP.\n")
                    time.sleep(2)
            else:
                heal_choice = False
                print("\nNo potions were used\n")
                time.sleep(2)

def lossGame():
    print("\nOh no you died!\n Please go on this journey again to find out what happens at the end!\n")

def main():
    main_menu = True
    # Font from: https://www.asciiart.eu/text-to-ascii-art
    print("""\n╔╦╗╔═╗╦╔╗╔  ╔╦╗╔═╗╔╗╔╦ ╦
║║║╠═╣║║║║  ║║║║╣ ║║║║ ║
╩ ╩╩ ╩╩╝╚╝  ╩ ╩╚═╝╝╚╝╚═╝\n""")
    
    while main_menu:
        main_decision = input("Start Game (1), or, Quit (2): ")
        if main_decision == "1":
            main_menu = False
            print("\nTo adventures we go...")
            time.sleep(1)
            intro()
        elif main_decision == "2":
            main_menu = False
            print("\nQuitting game now...")
        else:
            print("Please Enter a valid input")

main()