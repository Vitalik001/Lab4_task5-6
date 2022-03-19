import game

kozelnytska = game.Street("Kozelnytska")
kozelnytska.set_description("A homeland for UCU students")

stryjska = game.Street("Stryjska")
stryjska.set_description("A large street")

shewchenka= game.Street("Shewczenka")
shewchenka.set_description("A quite tiny street")

franka=game.Street('Franka')
franka.set_description('A very crowded street')

krakiwska=game.Street('Your half way')

kozelnytska.link_room(stryjska, "up")
kozelnytska.link_room(shewchenka, "down")
stryjska.link_room(kozelnytska, "down")
stryjska.link_room(franka, "up")
franka.link_room(stryjska, "down")
franka.link_room(krakiwska, 'up')
krakiwska.link_room(franka, 'down')
krakiwska.limk_room(shewchenka, 'up')
shewchenka.link_room(krakiwska, 'down')
shewchenka.link_room(kozelnytska, 'up')

student=game.Friend('Jake', "an UCU student")
student.set_conversation("I will give my soul for a book")
student.set_weakness('book')
kozelnytska.set_character(student)




lotr = game.Enemy("Dave", "A smelly zombie")
lotr.set_conversation("What's up, dude! I'm hungry.")
lotr.set_weakness("umbrella")
stryjska.set_character(lotr)

batiar = game.Enemy("Tabitha", "An enormous spider with countless eyes and furry legs.")
batiar.set_conversation("Sssss....I'm so bored...")
batiar.set_weakness("cheese")
franka.set_character(batiar)

laidak=game.Enemy('Boss', "I'm afraid of students")
laidak.set_conversation("heloo...")
laidak.set_weakness('student')
krakiwska.set_character(laidak)

kavalier=game.Enemy("Boy", "i love smth sweet")
kavalier.set_conversation("How are u?")
kavalier.set_weakness('chocolate')

stone=game.Support('stone')
stone.set_description("With this stone u can defeat everybody")
franka.set_item(stone)

cheese = game.Support("cheese")
cheese.set_description("A large and smelly block of cheese")
shewchenka.set_item(cheese)

book = game.Support("book")
book.set_description("A really good book entitled 'Knitting for dummies'")
stryjska.set_item(book)

chocolate = game.Support("chocolate")
cheese.set_description("A large and smelly block of chocolate")
franka.set_item(chocolate)

umbrella = game.Weapon("umbrella")
cheese.set_description("The most powerfull weapon")
kozelnytska.set_item(umbrella)

current_street = kozelnytska
backpack = []

dead = False

while dead == False:

    print("\n")
    current_street.get_details()

    inhabitant = current_street.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_room.get_item()
    if item is not None:
        item.describe()

    command = input("> ")

    if command in ["up", "down"]:
        # Move in the given direction
        current_room = current_room.move(command)
    elif command == "talk":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "fight":
        if inhabitant is not None:
            # Fight with the inhabitant, if there is one
            print("What will you fight with?")
            fight_with = input()

            # Do I have this item?
            if fight_with in backpack:

                if inhabitant.fight(fight_with) == True:
                    # What happens if you win?
                    print("Hooray, you won the fight!")
                    current_room.character = None
                    if inhabitant.get_defeated() == 2:
                        print("Congratulations, you have vanquished the enemy horde!")
                        dead = True
                else:
                    # What happens if you lose?
                    print("Oh dear, you lost the fight.")
                    print("That's the end of the game")
                    dead = True
            else:
                print("You don't have a " + fight_with)
        else:
            print("There is no one here to fight with")
    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your backpack")
            backpack.append(item.get_name())
            current_room.set_item(None)
        else:
            print("There's nothing here to take!")
    else:
        print("I don't know how to " + command)