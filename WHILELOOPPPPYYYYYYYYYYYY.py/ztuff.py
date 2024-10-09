#Adventure Game

#LOCATIONS / MESSAGES
mountains = "you are in a snowy mountain, you see a cave"
plains = "you find yourself in a grassy plain, there's a tree nearby"
forest = "you find yourself in a deep dark forest"
welcome = "Welcome adventurer!"
cave = "you enter a pitch black cave, you can't see anything"
torchcave = "you use the flashlight and see there's a golden statue in the centre of the cave."

#LOGIC
print(welcome)
print(forest)
move = input("which direction do you want to go?")
if move == "north":
    print(mountains)
    goCave = input("Would you like to enter the cave?")
    if goCave == "yes":
                   if hasTorch:
                           print(torchcave)
                   print(cave)
elif move == "east":
    print(plains)
