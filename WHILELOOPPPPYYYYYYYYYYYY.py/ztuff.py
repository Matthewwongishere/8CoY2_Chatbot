#Adventure Game
#LOCATIONS / MESSAGES

mountains = "you are in a snowy mountain, you see a cave"
plains = "you find yourself in a grassy plain, there's a tree nearby"
forest = "you find yourself in a deep dark forest"
welcome = "Welcome adventurer!"
cave = "you enter a pitch black cave, you can't see anything"
torchcave = "you use the flashlight and see there's a D3AD BODY! in the centre of the cave."
inventory = []
punch = ("you have performed a punch, HAI-YAA!")
fist = ("just a thingy")
songy = ("Look at the stars Look how they shine for you And everything you do Yeah, they were all yellow I came along I wrote a song for you And all the things you do And it was called Yellow So then I took my turn Oh, what a thing to have done And it was all yellow Your skin, oh yeah, your skin and bones Turn into something beautiful And you know, you know I love you so You know I love you so I swam across I jumped across for you Oh, what a thing to do 'Cause you were all yellow I drew a line I drew a line for you Oh, what a thing to do And it was all yellow And your skin, oh yeah, your skin and bones Turn into something beautiful And you know, for you, I'd bleed myself dry For you, I'd bleed myself dry It's true Look how they shine for you Look how they shine for you Look how they shine for Look how they shine for you Look how they shine for you Look how they shine Look at the stars Look how they shine for youAnd all the things that you do")

#LOGIC
inventory.append(fist)
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
punchy = input("Do you want to punch air?")
if punchy == "yes":
        print(punch)
song = input("Do you want the lyrics to Coldplay (it was ALLL YELLOOOWWW)")
if song == "yes" or song == "YES":
        print(songy)
if song == "no" or song == "NO":
        print("I am going to give it to you anyways!")
        print(songy)
else:
        print("I am going to give it to you anyways!")
        print(songy)


