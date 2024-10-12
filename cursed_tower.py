# L'Évasion de la Tour Maudite 
# 
# Contexte : 
# 
# Tu es un aventurier emprisonné dans une tour maudite, où des énigmes et des pièges complexes t'attendent à chaque étage. Ton objectif est de t'échapper de la tour en atteignant son sommet. Pour cela, tu devras résoudre des énigmes et prendre des décisions stratégiques. Tes choix seront déterminants pour ta survie et ta libération. 
# Tu dois écrire un programme qui simule cette aventure, en utilisant des conditions plus complexes, comme des comparaisons multiples ( and , or ) et des conditions imbriquées. 
# 
# Scénario détaillé : 
# 
# //1. Début de l'aventure – Le choix de l'arme : 
# //  
# //  Dès le début de ton aventure, tu trouves trois armes différentes dans ta cellule : 
# //  
# //      Une épée rouillée. 
# //      Une baguette magique abîmée. 
# //      Un bouclier en bois. 
# //  
# //  Le programme doit demander à l'utilisateur de choisir une arme parmi ces trois objets : 
# //      - Si l'utilisateur choisit l'épée, il aura une attaque puissante mais peu de défense. 
# //      - Si l'utilisateur choisit la baguette, il pourra utiliser des sorts mais ils sont imprévisibles. 
# //      - Si l'utilisateur choisit le bouclier, il aura une grande défense mais peu de capacité d'attaque. 
# //  
# //  Les statistiques de départ sont les suivantes : 
# //      Épée : attaque = 10, défense = 2 
# //      Baguette : attaque = 6, défense = 5 
# //      Bouclier : attaque = 3, défense = 8 
# //  
# //  Ces valeurs détermineront les résultats des combats à venir. 
#//
#// 2. Premier étage – La porte verrouillée : 
#//   
#//   Après avoir pris ton arme, tu montes au premier étage et trouves une porte fermée. Trois mécanismes sont disponibles pour l'ouvrir : 
#//       Mécanisme 1 : Résoudre une énigme mathématique (si la réponse est correcte, la porte s'ouvre).
#//       Mécanisme 2 : Forcer la porte avec ton arme (la réussite dépend de ton arme). 
#//       Mécanisme 3 : Tenter de trouver une clé cachée dans la pièce (la clé est cachée, il faut de la chance pour la trouver). 
#//   
#//   Le programme doit demander à l'utilisateur de choisir l'un des trois mécanismes, avec des conditions pour chaque option : 
#//       - Si l'utilisateur choisit de résoudre l'énigme (Mécanisme 1) : 
#//           Il doit résoudre une équation simple du type : "Combien font 8 + 3 * 2 ?". 
#//               - Si la réponse est correcte, la porte s'ouvre. 
#//               - Sinon, le piège s'active, et l'aventure se termine. 
#//   
#//       - Si l'utilisateur choisit de forcer la porte (Mécanisme 2) : 
#//           La réussite dépend de son arme : 
#//               - Si l'utilisateur a l'épée, il a 50 % de chances d'ouvrir la porte. 
#//               - Si l'utilisateur a le bouclier, il échoue automatiquement (car le bouclier n'est pas une arme offensive). 
#//               - Si l'utilisateur a la baguette, il a 30 % de chances de réussir (parce que la magie est instable). 
#//   
#//       - Si l'utilisateur choisit de chercher la clé (Mécanisme 3) : 
#//           Il a 40 % de chances de la trouver. 
#//               - Si l'utilisateur ne la trouve pas, un piège s'active. 
#// 
# 3. Deuxième étage – Combat contre un garde spectral : 
#   
#   Tu arrives au deuxième étage et fais face à un garde spectral. Le programme doit comparer tes statistiques d'attaque et de défense à celles du garde pour déterminer l'issue du combat : 
#       Le garde spectral a une attaque de 8 et une défense de 6. 
#       Les règles du combat sont les suivantes : 
#           - Si ton attaque est supérieure à la défense du garde, tu le blesses et tu passes au prochain étage. 
#           - Si ta défense est supérieure à l'attaque du garde, il ne peut pas te blesser, mais tu dois trouver une autre solution pour t'en sortir (comme fuir). 
#           - Si ni ton attaque ni ta défense ne sont supérieures, tu perds le combat et l'aventure se termine. 
#           
#           Conditions complexes : 
#               - Si tu as l'épée, ta grande attaque te permet de blesser le garde immédiatement. 
#               - Si tu as le bouclier, ta grande défense te permet de résister, mais tu ne pourras pas vaincre le garde sans trouver une autre stratégie. 
#               - Si tu as la baguette, tu dois lancer un sort magique aléatoire : il peut soit doubler ton attaque pour ce combat, soit échouer.
# 
# 4. Troisième étage – La salle du miroir magique : 
#   
#   Au troisième étage, tu rencontres un miroir magique qui te pose une énigme et t'offre trois choix en fonction de ta réponse. L'énigme est la suivante : 
#       "Je suis toujours devant toi, mais tu ne peux jamais me dépasser. Qui suis-je ?" Trois réponses sont proposées : 
#           Réponse 1 : "Le futur". 
#           Réponse 2 : "Le chemin". 
#           Réponse 3 : "Ton ombre". 
#   
#   Le programme doit utiliser des conditions imbriquées pour gérer les conséquences : 
#       - Si l'utilisateur choisit "Le futur" (Réponse 1) : 
#           Le miroir lui montre un futur dangereux, et il doit faire demi-tour. Fin de l'aventure. 
#       - Si l'utilisateur choisit "Le chemin" (Réponse 2) : 
#           Le miroir l'ouvre et il continue son aventure. 
#       - Si l'utilisateur choisit "Ton ombre" (Réponse 3) : 
#           Le miroir l'emprisonne dans une boucle temporelle, et l'aventure échoue. 
#  
#  5. Dernier étage – Le gardien du sommet : 
#   Au sommet de la tour, tu fais face au Gardien du Sommet, un puissant sorcier qui te lance un défi. 
#   Il te demande de choisir une porte parmi trois : 
#       Porte 1 : Une porte enflammée. 
#       Porte 2 : Une porte gelée. 
#       Porte 3 : Une porte d'ombre. 
#   Selon l'arme que tu as choisie au début, les résultats varient : 
#       - Si tu as l'épée : Tu peux traverser la porte enflammée sans te blesser. 
#       - Si tu as le bouclier : Tu peux te protéger du froid et traverser la porte gelée. 
#       - Si tu as la baguette : Tu peux dissiper l'ombre et traverser la porte d'ombre. 
#   - Si tu choisis la bonne porte en fonction de ton arme, tu t'échappes de la tour et tu gagnes. 
#   - Si tu fais le mauvais choix, tu es emprisonné pour toujours dans la tour. 

import random
import time

print("**************************************")
print("***                                ***")
print("*** Bienvenue dans la tour Maudite ***")
print("***                                ***")
print("**************************************")

###############################
#                             #
#  1st floor: Inside the jail #
#                             #
###############################

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

# Start of the game loop
while not end_of_game:

    # while not choice_made:
    #     try:
    #         weapon_choice = int(input("Avant de sortir de la cellule, quelle arme choisissez-vous? : "))

    #         if weapon_choice <= 0 or weapon_choice > 3:
    #             print("La tour est dangereuse, ne sortez pas sans l'une des trois armes. Tapez 1, 2 ou 3, sinon la mort vous attend!")
    #         else: 
    #             choice_made = True
    #     except ValueError:
    #         print("La tour est dangereuse, ne sortez pas sans l'une des trois armes. Tapez 1, 2 ou 3, sinon la mort vous attend!")

    # time.sleep(0.5)

    # player_stat = {
    #     "weapon" : "",
    #     "attack" : 0,
    #     "defense" : 0 
    # }

    # if weapon_choice == 1:
    #     print()
    #     print("Vous avez fait le choix de la puissance. Au fond de vous, vous savez que c'est le bon choix.")
        
    #     player_stat["weapon"] = "épée"
    #     player_stat["attack"] = 10
    #     player_stat["defense"] = 2
    # elif weapon_choice == 2:
    #     print()
    #     print("Vous avez fait le choix de la magie. Au fond de vous, vous savez que c'est le bon choix.")
        
    #     player_stat["weapon"] = "baguette"
    #     player_stat["attack"] = 6
    #     player_stat["defense"] = 5
    #     player_stat["spells"] = {
    #         "boule de feu": 1,
    #         "defense": 2,
    #         "puissance": 2
    #     }
    # elif weapon_choice == 3:
    #     print()
    #     print("Vous avez fait le choix de la défense. Au fond de vous, vous savez que c'est le bon choix.")
        
    #     player_stat["weapon"] = "bouclier"
    #     player_stat["attack"] = 3
    #     player_stat["defense"] = 8

    # time.sleep(0.5)

    # print("Vous sortez de la cellule et montez au premier étage.")
    # print()

    # time.sleep(0.5)
    ###########################
    #                         #
    #  2nd floor: closed door #
    #                         #
    ###########################

    # print("Vous arrivez devant une porte fermée.")
    # time.sleep(0.5)
    # print("Vous l'observez bien: voyez à droite un mécanisme avec un livre et un crayon.")
    # time.sleep(0.5)
    # print("     1. à droite se trouve un mécanisme avec un livre et un crayon. Rha une énigme, serez-vous assez intelligent pour la résoudre?")
    # time.sleep(0.5)
    # print("     2. Et si vous utilisiez votre arme pour enfoncer cette maudite porte?")
    # time.sleep(0.5)
    # print("     3. Pendant votre temps de réflexion vous voyez une serrure, la clé se trouve peut être quelque part!")
    # print()

    # choice_made = False

    # # The player make the choice between the options
    # while not choice_made:
        
    #     try:
    #         player_choice = int(input("Quelle solution choisissez-vous? "))

    #         if player_choice <= 0 or player_choice > 3:
    #             print("Vous trouvez un petit cailloux par terre et le lancez contre la porte. Les dieux se moquent de vous. Choisissez entre 1, 2 ou 3")
    #         else:
    #             choice_made = True
    #     except ValueError:
    #         print("Vous tournez en rond cherchant une solution, alors qu'il suffit de choisir entre 1, 2, ou 3")

    # # The player chooses the riddle
    # if player_choice == 1:
    #     print("Vous vous approchez du livre et l'ouvrez.")
    #     print("Une page blanche.")
    #     print("Vous prenez la torche accrochez à côté de la porte et survolez le livre.")
    #     print("La chaleur de la flamme fait apparaître un texte!!!")
    #     print("Voici l'énigme:")

    #     riddle_answer = 8 + 3 * 2

    #     user_answer = int(input("     Combien font 8 + 3 x 2? "))
        
    #     if user_answer == riddle_answer:
    #         print("Vous entendez la porte se dévérouiller. Vous vous félicitez.")
    #     else: 
    #         print("Vous entendez un bruit sous vos pieds. Le sol se dérobe, vous tombez dans une fosse à serpent.")
    #         print("Des milliers de serpents vous attaquent. Vous mourez empoisonné.")
    #         end_of_game = True  

    # # The player chooses the fight
    # elif player_choice == 2:
        
    #     # The player has sword
    #     if player_stat["weapon"] == "épée":
    #         weapon_damage = random.randint(1,2)

    #         if weapon_damage == 1:
    #             print("Vous assenez un énorme coup sur la porte. Vous n'en faites que des brindilles. QUEL PUISSANCE!")
    #         elif weapon_damage == 2:
    #             print("Vous assenez un énorme coup sur la porte. Malheureusement elle est trop robuste.")
    #             print("L'épée vous revient dessus et vous frappe violament. Vous êtes mort!")
    #             end_of_game = True

    #     # The player has wand
    #     elif player_stat["weapon"] == "baguette":
    #         weapon_damage = random.randint(1, 10)

    #         if weapon_damage == 1 or weapon_damage == 2 or weapon_damage == 3:
    #             print("Vous vous concentrez. Une boule de feu sort de la baguette et pulvérise la porte. QUEL PUISSANCE!")
    #         elif weapon_damage == 2:
    #             print("Vous vous concentrez. La baguette chauffe terriblement et explose dans votre main.")
    #             print("VOUS N'AVEZ PLUS DE MAINS!")
    #             print("Le sang gicle partout, vous vous effondrez et mourez!")
    #             end_of_game = True

    #     # The player has shield
    #     elif player_stat["weapon"] == "bouclier":
    #         print("Vous frappez la porte avec votre bouclier!")
    #         time.sleep(0.5)
    #         print("Vous frappez la porte avec votre bouclier!")
    #         time.sleep(1)
    #         print("Vous frappez la porte avec votre bouclier!")
    #         time.sleep(1.5)
    #         print("Vous frap... Vous vous effondrez de fatigue et de faim. Vous êtes mort!")
    #         end_of_game = True

    # # The player chooses to find the key
    # elif player_choice == 3:

    #     odds_find_key = random.randint(0,5)
    #     if odds_find_key == 1 or odds_find_key == 2:
    #         print("Un petit tapis de paille se trouve sur le pas de la porte. Vous le soulevez et trouvez la clé. Quel idiot met sa clé sous le tapis.")
    #         print("Vous insérez la clé dans la serrure et ouvrez la porte")
    #     else:
    #         print("Vous soulevez un pot de fer. ** CLIC **. Le plafond s'effondre sur vous. Vous êtes mort!")
    #         end_of_game = True

    # print()
    # print("Vous sortez et montez à l'étage supérieur")
    # time.sleep(0.5)

    ###########################
    #                         #
    #  3rd floor: ghost fight #
    #                         #
    ###########################

    ghost_stat = {
        "attack": 8,
        "defense": 6
    }

    player_stat = {
        "weapon" : "baguette",
        "attack" : 6,
        "defense" : 5,
        "spells": {
            "Boule de feu": 1,
            "defense": 2,
            "puissance": 2
        } 
    }

    print("Vous arrivez dans une grande pièce. Des torches sont accrochées au mur.")
    print("En face de vous se trouve la porte entrouverte.")
    print(f"Vous avancez prudemment votre {player_stat['weapon']} tendu devant vous.")
    print("Un spectre surgit de nulle part et se tient entre vous et la porte.")

    end_of_fight = False
    win = False

    # TODO: retravailler le combat
    while not end_of_fight:
    
        if player_stat["weapon"] == "épée":
            
            print("Dans un réflexe héroïque, vous attaquez le spectre.")
            print(f"Votre {player_stat['weapon']} transperce l'ectoplasme et tue le revenant.")
            print("Vous courez vers la porte")
            end_of_fight = True

        elif player_stat["weapon"] == "baguette":
            
            print("Vous vous concentrez.")
            random_spell = random.randint(1, 4)

            if random_spell == 1:
                print(f"Une {player_stat['spells']['Boule de feu']} sort de la baguette.")
                print("Elle traverse le spectre.")
                print("Surpris, vous ne voyez pas arriver l'attaque du spectre.")
                print(f"Il vous inflige {ghost_stat['attack']} points de dégât.")
                print("Vous tombez au combat. Vous êtes mort.")
                end_of_fight = True

            elif random_spell == 2:
                print("Vous sentez la puissance de la baguette s'activer.")
                print("Une aura de lumière vous entoure.")
                print("Le spectre se lance et vous attaque.")
                print("Votre bouclier de lumière vous as protégé.")
            elif random_spell == 3:
                print("Vous sentez la puissance de la baguette s'activer.")
                print("Votre main s'entour d'une aura rouge")
                print(f"Vous lancez une {player_stat['spells']['Boule de feu']}.")
                print("Elle atteint votre ennemie qui disparaît dans les ténèbres.")
                win = True
                end_of_fight = True                
            elif random_spell == 4:
                print("Face à la vision de cette horreur, vous perdez la raison.")
                print("Le spectre vous attaque!!!")
                print(f"Il vous inflige {ghost_stat['attack']} points de dégât.")
                end_of_fight = True

        elif player_stat["weapon"] == "bouclier":

            # TODO: faire le choix de la stratégie
            print("Le spectre vous attaque!!!")
            print("En voyant de spectre vous avez le réflexe de lever votre bouclier pour vous protéger!")
            print("vous choisissez de courir vers la porte en traversant le spectre")
            end_of_fight = True

    if not win:
        end_of_game = True


            
