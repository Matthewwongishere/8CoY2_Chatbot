#Adventure Game

#LOCATIONS / MESSAGES
mountains = "you are in a snowy mountain, you see a cave"
plains = "you find yourself in a grassy plain, there's a tree nearby"
forest = "you find yourself in a deep dark forest"
welcome = "Welcome adventurer!"
cave = "you enter a pitch black cave, you can't see anything"
torchcave = "you use the flashlight and see there's a D3AD BODY! in the centre of the cave."
inventory = []

#LOGIC
print(welcome)
print(forest)
move = input("which direction do you want to go?")
if move == "north":
    print(mountains)
    goCave = input("Would you like to enter the cave?")
    if goCave == "yes":
                    if "torch" in inventory:
                            print(torchcave)
                    print(cave)
elif move == "east":
    print(plains)
    if not "torch" in inventory:
            print("there's a torch on the floor")
            pickup = input("do you want to pick up the torch? ")
            if pickup == "yes":
                    inventory.append("torch")
lookin = input("Do you want to look at your inventory?")
if lookin == "yes":
        print(inventory)

