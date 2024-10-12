# L'Évasion de la Tour Maudite 
# 
# Contexte : 
# 
# Tu es un aventurier emprisonné dans une tour maudite, où des énigmes et des pièges complexes t'attendent à chaque étage. Ton objectif est de t'échapper de la tour en atteignant son sommet. Pour cela, tu devras résoudre des énigmes et prendre des décisions stratégiques. Tes choix seront déterminants pour ta survie et ta libération. 
# Tu dois écrire un programme qui simule cette aventure, en utilisant des conditions plus complexes, comme des comparaisons multiples ( and , or ) et des conditions imbriquées. 

import random
import time

print("**************************************")
print("***                                ***")
print("*** Bienvenue dans la tour Maudite ***")
print("***                                ***")
print("**************************************")

################################
#                              #
#  1st floor: Inside the jail  #
#                              #
################################

print("Vous vous réveillez dans une cellule. Votre tête vous fait encore mal.")
time.sleep(0.5)
print("En observant la pièce vous voyez la porte ouverte et à sa droite trois objets:")
time.sleep(0.5)
print("     1. Une épée robuste. De la force pure.")
time.sleep(0.5)
print("     2. Une baguette. Vous sentez un puissance magique s'en dégager.")
time.sleep(0.5)
print("     3. Un bouclier. Difficile d'attaquer, mais vous vous sentirez en sécurité.")
print()
time.sleep(0.5)

choice_made = False
end_of_game = False
success = False
player_stat = {
    "weapon" : "",
    "attack" : 0,
    "defense" : 0 
}

# Start of the game loop
while not end_of_game:

    # The player will choose his weapon:
    # 1. sword
    # 2. Wand
    # 3. Shield
    while not choice_made:
        try:
            weapon_choice = int(input("Avant de sortir de la cellule, quelle arme choisissez-vous? : "))

            if weapon_choice <= 0 or weapon_choice > 3:
                print("La tour est dangereuse, ne sortez pas sans l'une des trois armes. Tapez 1, 2 ou 3, sinon la mort vous attend!")
            else: 
                choice_made = True
        except ValueError:
            print("La tour est dangereuse, ne sortez pas sans l'une des trois armes. Tapez 1, 2 ou 3, sinon la mort vous attend!")

    time.sleep(0.5)

    # We define player stat depending of the weapon choice
    if weapon_choice == 1:
        print()
        print("Vous avez fait le choix de la puissance. Au fond de vous, vous savez que c'est le bon choix.")
        
        player_stat["weapon"] = "épée"
        player_stat["attack"] = 10
        player_stat["defense"] = 2
    elif weapon_choice == 2:
        print()
        print("Vous avez fait le choix de la magie. Au fond de vous, vous savez que c'est le bon choix.")
        
        player_stat["weapon"] = "baguette"
        player_stat["attack"] = 6
        player_stat["defense"] = 5
        player_stat["spells"] = {
            "boule de feu": 1,
            "defense": 2,
            "puissance": 2
        }
    elif weapon_choice == 3:
        print()
        print("Vous avez fait le choix de la défense. Au fond de vous, vous savez que c'est le bon choix.")
        
        player_stat["weapon"] = "bouclier"
        player_stat["attack"] = 3
        player_stat["defense"] = 8

    time.sleep(0.5)

    print("Vous sortez de la cellule et montez au premier étage.")
    print()

    time.sleep(0.5)

    ############################
    #                          #
    #  2nd floor: closed door  #
    #                          #
    ############################

    print("Vous arrivez devant une porte fermée.")
    time.sleep(0.5)
    print("Vous l'observez bien: voyez à droite un mécanisme avec un livre et un crayon.")
    time.sleep(0.5)
    print("     1. à droite se trouve un mécanisme avec un livre et un crayon. Rha une énigme, serez-vous assez intelligent pour la résoudre?")
    time.sleep(0.5)
    print("     2. Et si vous utilisiez votre arme pour enfoncer cette maudite porte?")
    time.sleep(0.5)
    print("     3. Pendant votre temps de réflexion vous voyez une serrure, la clé se trouve peut être quelque part!")
    print()

    choice_made = False

    # The player make the choice between the options
    while not choice_made:
        
        try:
            player_choice = int(input("Quelle solution choisissez-vous? "))

            if player_choice <= 0 or player_choice > 3:
                print("Vous trouvez un petit cailloux par terre et le lancez contre la porte. Les dieux se moquent de vous. Choisissez entre 1, 2 ou 3")
            else:
                choice_made = True
        except ValueError:
            print("Vous tournez en rond cherchant une solution, alors qu'il suffit de choisir entre 1, 2, ou 3")

    # The player chooses the riddle
    if player_choice == 1:
        print("Vous vous approchez du livre et l'ouvrez.")
        print("Une page blanche.")
        print("Vous prenez la torche accrochez à côté de la porte et survolez le livre.")
        print("La chaleur de la flamme fait apparaître un texte!!!")
        print("Voici l'énigme:")

        riddle_answer = 8 + 3 * 2

        user_answer = int(input("     Combien font 8 + 3 x 2? "))
        
        if user_answer == riddle_answer:
            print("Vous entendez la porte se dévérouiller. Vous vous félicitez.")
        else: 
            print("Vous entendez un bruit sous vos pieds. Le sol se dérobe, vous tombez dans une fosse à serpent.")
            print("Des milliers de serpents vous attaquent. Vous mourez empoisonné.")
            end_of_game = True  

    # The player chooses the fight
    elif player_choice == 2:
        
        # The player has sword
        if player_stat["weapon"] == "épée":
            weapon_damage = random.randint(1,2)

            if weapon_damage == 1:
                print("Vous assenez un énorme coup sur la porte. Vous n'en faites que des brindilles. QUEL PUISSANCE!")
            elif weapon_damage == 2:
                print("Vous assenez un énorme coup sur la porte. Malheureusement elle est trop robuste.")
                print("L'épée vous revient dessus et vous frappe violament. Vous êtes mort!")
                end_of_game = True

        # The player has wand
        elif player_stat["weapon"] == "baguette":
            weapon_damage = random.randint(1, 10)

            if weapon_damage == 1 or weapon_damage == 2 or weapon_damage == 3:
                print("Vous vous concentrez. Une boule de feu sort de la baguette et pulvérise la porte. QUEL PUISSANCE!")
            elif weapon_damage == 2:
                print("Vous vous concentrez. La baguette chauffe terriblement et explose dans votre main.")
                print("VOUS N'AVEZ PLUS DE MAINS!")
                print("Le sang gicle partout, vous vous effondrez et mourez!")
                end_of_game = True

        # The player has shield
        elif player_stat["weapon"] == "bouclier":
            print("Vous frappez la porte avec votre bouclier!")
            time.sleep(0.5)
            print("Vous frappez la porte avec votre bouclier!")
            time.sleep(1)
            print("Vous frappez la porte avec votre bouclier!")
            time.sleep(1.5)
            print("Vous frap... Vous vous effondrez de fatigue et de faim. Vous êtes mort!")
            end_of_game = True

    # The player chooses to find the key
    elif player_choice == 3:

        odds_find_key = random.randint(0,5)
        if odds_find_key == 1 or odds_find_key == 2:
            print("Un petit tapis de paille se trouve sur le pas de la porte. Vous le soulevez et trouvez la clé. Quel idiot met sa clé sous le tapis.")
            print("Vous insérez la clé dans la serrure et ouvrez la porte")
        else:
            print("Vous soulevez un pot de fer. ** CLIC **. Le plafond s'effondre sur vous. Vous êtes mort!")
            end_of_game = True

    print()
    print("Vous sortez et montez à l'étage supérieur")
    time.sleep(0.5)

    ############################
    #                          #
    #  3rd floor: ghost fight  #
    #                          #
    ############################

    ghost_stat = {
        "attack": 8,
        "defense": 6
    }

    print("Vous arrivez dans une grande pièce. Des torches sont accrochées au mur.")
    time.sleep(0.5)
    print("En face de vous se trouve la porte entrouverte.")
    time.sleep(0.5)
    print(f"Vous avancez prudemment votre {player_stat['weapon']} tendu devant vous.")
    time.sleep(0.5)
    print("Un spectre surgit de nulle part et se tient entre vous et la porte.")
    time.sleep(0.5)
    print()

    end_of_fight = False
    win = False

    def fight(player_stat, ghost_stat):

        result = player_stat - ghost_stat

        if result > 0:
            return True
        else:
            return False

    # Fight loop against the ghost
    while not end_of_fight:
        
        # Fight with the sword
        if player_stat["weapon"] == "épée":
            
            print("Dans un réflexe héroïque, vous attaquez le spectre.")
            time.sleep(0.5)
            fight_result = fight(player_stat["attack"], ghost_stat["defense"])

            if fight_result:
                print(f"Votre {player_stat['weapon']} transperce l'ectoplasme et tue le revenant.")
                time.sleep(0.5)
                print("Vous courez vers la porte")
                time.sleep(0.5)
                print()
                win = True
                end_of_fight = True

        # Fight wiht the wand
        elif player_stat["weapon"] == "baguette":
            
            print("Vous vous concentrez.")
            time.sleep(0.5)
            random_spell = random.randint(1, 4)

            # Use the first spell: Fire Ball
            if random_spell == 1:
                
                fight_result = fight(player_stat["attack"], ghost_stat["defense"])

                if fight_result:
                    print(f"Vous lancez une {list(player_stat['spells'].keys())[0]}.")
                    time.sleep(0.5)
                    print("Elle atteint votre ennemie qui disparaît dans les ténèbres.")
                    time.sleep(0.5)
                    print()
                    win = True
                    end_of_fight = True 

                else:
                    print(f"Une {list(player_stat['spells'].keys())[0]} sort de la baguette.")
                    time.sleep(0.5)
                    print("Elle traverse le spectre.")
                    time.sleep(0.5)
                    print("Surpris, vous ne voyez pas arriver l'attaque du spectre.")
                    time.sleep(0.5)
                    print(f"Il vous inflige {ghost_stat['attack']} points de dégât.")
                    time.sleep(0.5)
                    print("Vous tombez au combat. Vous êtes mort.")
                    time.sleep(0.5)
                    print()
                    end_of_fight = True

            # Use the second spell: Defense boost
            elif random_spell == 2:
                print("Vous sentez la puissance de la baguette s'activer.")
                time.sleep(0.5)
                print("Une aura de lumière vous entoure.")
                time.sleep(0.5)

                fight_result = fight(player_stat["defense"] * 2, ghost_stat["attack"])

                if fight_result:
                    print("Le spectre se lance et vous attaque.")
                    time.sleep(0.5)
                    print("Votre bouclier de lumière vous as protégé.")
                    time.sleep(0.5)
                    print()

            # Use the third spell: Attack Boost
            elif random_spell == 3:
                print("Vous sentez la puissance de la baguette s'activer.")
                time.sleep(0.5)
                print("Votre main s'entour d'une aura rouge")
                time.sleep(0.5)

                player_stat["attack"] *= 2

            # The spell doesn't work
            elif random_spell == 4:
                print("Face à la vision de cette horreur, vous perdez la raison.")
                time.sleep(0.5)
                print("Le spectre vous attaque!!!")
                time.sleep(0.5)

                fight_result = fight(player_stat["defense"] * 2, ghost_stat["attack"])
                
                if not fight_result:
                    print(f"Il vous inflige {ghost_stat['attack']} points de dégât.")
                    time.sleep(0.5)
                    print("Vous tombez au combat. Vous êtes mort.")
                    time.sleep(0.5)
                    print()
                    end_of_fight = True

        # Fight with the shield
        elif player_stat["weapon"] == "bouclier":

            print("Le spectre vous attaque!!!")
            time.sleep(0.5)
            
            fight_result = fight(player_stat["defense"], ghost_stat["attack"])
            
            if fight_result:
                print("En voyant de spectre vous avez le réflexe de lever votre bouclier pour vous protéger!")
                time.sleep(0.5)

            print("Vous observez la salle et voyez deux solutions:")
            print("     1. Prendre une torche et la lancer sur le spectre")
            print("     2. Courir droit sur la porte")

            choice_made = False

            # The player make the choice between the options
            while not choice_made:
                
                try:
                    player_choice = int(input("Quelle solution choisissez-vous? "))

                    if player_choice <= 0 or player_choice > 2:
                        print("Vous trouvez un petit cailloux par terre et le lancez contre la porte. Les dieux se moquent de vous. Choisissez entre 1, 2")
                    else:
                        choice_made = True
                except ValueError:
                    print("Vous tournez en rond cherchant une solution, alors qu'il suffit de choisir entre 1, 2")

            # Throw the torch choice
            if player_choice == 1:
                print("vous saisissez la torche et la lancé sur le spectre")
                time.sleep(0.5)
                odds_to_win = random.randint(1,10)
                
                # Throw succeed
                if odds_to_win == 1 or odds_to_win == 2 or odds_to_win == 3:
                    print("Votre dextérité vous a réussi, le spectre prend feu.")
                    win = True
                    end_of_fight = True

                # Throw failed
                else:
                    print("Au moment de saisir la torche le spectre vous attaque")

                    fight_result = fight(player_stat["defense"] - 5, ghost_stat["attack"])

                    if not fight_result:
                        print(f"Il vous inflige {ghost_stat['attack']} points de dégât.")
                        time.sleep(0.5)
                        print("Vous tombez au combat. Vous êtes mort.")
                        time.sleep(0.5)
                        print()
                        end_of_fight = True

            # Run choice
            elif player_choice == 2:
                print("vous choisissez de courir vers la porte en traversant le spectre")
                time.sleep(0.5)
                odds_to_win = random.randint(1,2)

                # Run succeed
                if odds_to_win == 1:
                    print("Vous êtes assez vif et rapide pour atteindre la porte sans problème.")
                    win = True
                    end_of_fight = True

                # Run failed
                elif odds_to_win == 2:
                    print("Au moment de traverser le spectre vous suffoquez et vous noyez dans l'ectoplasme. Vous êtes mort!")
                    end_of_fight = True
                

    # End of game if player doesn't win
    if not win:
        end_of_game = True

    print("Une fois la porte atteinte vous l'ouvrez et montez à l'étage!")
    print()

    ############################
    #                          #
    #  4th floor: mirror room  #
    #                          #
    ############################
            
    print("Vous arrivez dans une pièce orné d'ambre.")
    time.sleep(0.5)
    print("En face de vous se trouve une porte avec un mirroir.")
    time.sleep(0.5)
    print("En vous apporchant une voix se fait entendre.")
    time.sleep(0.5)
    print("Si ton destin est de passer cette porte alors tu répondras correctement à cette énigme.")
    time.sleep(0.5)
    print("Je suis toujours devant toi, mais tu ne peux jamais me dépasser. Qui suis-je?")
    time.sleep(0.5)
    print("     1. Le futur")
    print("     2. Le chemin")
    print("     3. Ton ombre")

    choice_made = False

    # Player have to choose between options
    while not choice_made:

        try:
            user_choice = int(input("Quelle est ta réponse? "))

            if user_choice <= 0 or user_choice > 3:
                print("Je perds patience. Choisis 1, 2 ou 3")
            else:
                choice_made = True

        except ValueError:
            print("Je perds patience. Choisis 1, 2 ou 3")

    # Futur choice: End of game
    if user_choice == 1:
        time.sleep(0.5)
        print("Tel est ton choix.")
        time.sleep(0.5)
        print("Voici ton avenir")
        time.sleep(0.5)
        print("Vous voyez dans le miroir une ombre apparaître. C'est vous")
        time.sleep(0.5)
        print("Vous montez les marches et un énorme rocher dévale les escaliers et vous écrase.")
        time.sleep(0.5)
        print("Vous prenez peur et faites demi-tour.")
        time.sleep(0.5)
        print("Malheureusement ne trouvant pas d'autres issues, vous mourez de faim!")
        time.sleep(0.5)
        end_of_game = True

    # Path choice: good choice
    elif user_choice == 2:
        time.sleep(0.5)
        print("Bravo, ton destin est d'atteindre le prochain étage")
        time.sleep(0.5)
        print("Vous entendez un mécanisme s'enclencher.")
        time.sleep(0.5)
        print("La porte d'ouvre!")
        time.sleep(0.5)

    # Shadow choice: loop choice, end of game
    elif user_choice == 3:

        end_countdown = 4

        while end_countdown != 0:

            print("Je suis toujours devant toi, mais tu ne peux jamais me dépasser. Qui suis-je?")
            time.sleep(0.5)
            print("     1. Le futur")
            print("     2. Le chemin")
            print("     3. Ton ombre")

            end_countdown -= 1
        
        time.sleep(0.5)
        print("Tu deviens fou et meurt")
        end_of_game = True

    print("Vous traversez la porte et montez à l'étage suivant")
    print()
    time.sleep(0.5)

    ##############################
    #                            #
    #  5th floor: roof guardian  #
    #                            #
    ##############################

    print("Vous arrivez dans une très grande salle")
    time.sleep(0.5)
    print("Au centre se trouve un trône sur lequel est assis une étrange créature.")
    time.sleep(0.5)
    print("Sur sa droite vous voyez 3 portes portes.")
    time.sleep(0.5)
    print("Vous vous approchez. Non sans crainte.")
    time.sleep(0.5)

    print("La créature se lève et s'adresse à vous:")
    time.sleep(0.5)

    print("Bravo d'être arrivé jusqu'ici. Tu as déjoué tous mes pièges")
    time.sleep(0.5)
    print("Je t'offre un dernier choix.")
    time.sleep(0.5)
    print("Vous remarquez que les portes ont changé")
    time.sleep(0.5)

    print("Tu as le choix entre:")
    print("     1. La porte enflammée")
    print("     2. La porte glacée")
    print("     3. La porte d'ombre")

    choice_made = False
    fifth_floor = True

    # Player have to choose between 3 doors
    while not choice_made:

        try:
            user_choice = int(input("Quel est ton choix? "))
            print()
            time.sleep(0.5)

            if user_choice <= 0 or user_choice > 3:
                print("Il n'y a pas de porte caché. Si tu veux sortir c'est une des 3 portes.")
            else:
                choice_made = True
        except ValueError:
            print("N'abuse pas de ma patience. Tu choisis la porte 1, 2 ou 3")

    # Flamed door
    if user_choice == 1:
        
        # Player has sword
        if player_stat["weapon"] == "épée":
            
            print("Vous avancez vers la porte enflammée.")
            time.sleep(0.5)
            print("Vous prenez une grande inspiration, levez votre arme et assenez un coup puissant")
            time.sleep(0.5)
            print("Les flammes se dissipe un court instant")
            time.sleep(0.5)
            print("Vous profitez de cette opportunité pour passer la porte et sortir.")
            time.sleep(0.5)
            print()
            success = True
            end_of_game = True

        # Player has wand
        elif player_stat["weapon"] == "baguette":
            
            print("Vous avancez vers la porte enflammée.")
            time.sleep(0.5)
            print("Vous essayez de lancer un sort. Malgré tous vos efforts, rien ne bouge!")
            time.sleep(0.5)
            print()
            end_of_game = True

        # Player has shield
        elif player_stat["weapon"] == "bouclier":
            
            print("Vous avancez vers la porte enflammée.")
            time.sleep(0.5)
            print(f"Vous placez votre {player_stat['weapon']} devant vous et avancez.")
            time.sleep(0.5)
            print("Malheureusement il est fait de bois et prend feu!")
            time.sleep(0.5)
            print()
            end_of_game = True

    # Iced door
    elif user_choice == 2:

        # Player has sword
        if player_stat["weapon"] == "épée":
            
            print("Vous avancez vers la porte glacée.")
            time.sleep(0.5)
            print("Vous prenez une grande inspiration, levez votre arme et assenez un coup puissant")
            time.sleep(0.5)
            print("Votre épée se brise en mille morceaux")
            time.sleep(0.5)
            print()
            end_of_game = True

        # Player has wand
        elif player_stat["weapon"] == "baguette":
            
            print("Vous avancez vers la porte glacée.")
            time.sleep(0.5)
            print("Vous essayez de lancer un sort. Malgré tous vos efforts, rien ne bouge!")
            time.sleep(0.5)
            print()
            end_of_game = True

        # Player has shield
        elif player_stat["weapon"] == "bouclier":
            
            print("Vous avancez vers la porte glacée.")
            time.sleep(0.5)
            print(f"Vous placez votre {player_stat['weapon']} devant vous et avancez.")
            time.sleep(0.5)
            print("Quelle magie. Votre bouclier vous offre une petite faille et vous traversez la porte pour sortir.")
            time.sleep(0.5)
            print()
            success = True
            end_of_game = True

    # Shadowed door
    elif user_choice == 3:

        # Player has sword
        if player_stat["weapon"] == "épée":
            
            print("Vous avancez vers la porte d'ombre.")
            time.sleep(0.5)
            print("Vous prenez une grande inspiration, levez votre arme et assenez un coup puissant")
            time.sleep(0.5)
            print("Votre épée se fait aspirer dans vide sidérale")
            time.sleep(0.5)
            print()
            end_of_game = True

        # Player has wand
        elif player_stat["weapon"] == "baguette":
            
            print("Vous avancez vers la porte d'ombre.")
            time.sleep(0.5)
            print("Vous essayez de lancer un sort. Les ombres se dissipent et vous voyez la sortie.")
            time.sleep(0.5)
            print("Vous traversez la porte et sortez.")
            time.sleep(0.5)
            print()
            success = True
            end_of_game = True

        # Player has shield
        elif player_stat["weapon"] == "bouclier":
            
            print("Vous avancez vers la porte d'ombre.")
            time.sleep(0.5)
            print(f"Vous placez votre {player_stat['weapon']} devant vous et avancez.")
            time.sleep(0.5)
            print("Malheureusement vous vous faites aspirez dans le vide et réapparaissez devant le gardien.")
            time.sleep(0.5)
            print()
            end_of_game = True

#################
#               #
#  End of game  #
#               #
#################

# Player succeed
if success :
    print("Bravo vous vous êtes échapé de la Tour Maudite.")
    time.sleep(0.5)
    print()

# Player reach last floor but doesn't succeed
elif fifth_floor:
    print("Vous avez échoué, le Gardien de la tour vous emprisonne.")
    time.sleep(0.5)
    print()
    print("Game Over")

#player loose before last floor
else:
    print("Vous avez échoué")
    time.sleep(0.5)
    print()
    print("Game Over")
