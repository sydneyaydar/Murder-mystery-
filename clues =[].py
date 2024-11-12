import random
t=random.randint(1,3)

def bathroom_scene():
    bathroom = input("You go inside the bathroom. Where do you look first (A) The bathtub (B) Under the sink (C) In the toilet ").upper()
    if bathroom == "A":
        tub_scene()
    elif bathroom == "B":
        sink_scene()

    return bathroom

def nightvision():
    print("You look at the wall and see writeing that says go to the bedroom and look under the bed and eat") 

def tub_scene():
    tub = input("You look in the bathtub and you see a dead body! What do you do (A)Take pictures (B) Explore more of the house").upper()
    if tub == "A":
        print("You start to take photos then a ring catches your eye, you pick it up and see that it looks just like the ring your boss had on earlier.")
        ring = True
    elif tub == "B":
        explore_more()

def sink_scene():
    sink = input("Under the sink you find a strand of dark black hair. What do you do next (A) Put it in a ziplock bag or (B) keep exploring").upper()

def explore_more():
    place = input("You decide to go to another room, where do you go (A) The bedroom (B) The kitchen").upper()
    if place == "A":
        bedroom_scene()
    elif place == "B":
        kitchen_scene()
        
def toilet_scene():
    toilet = input("In the tolilet you see nothing where do you look next(A)Sink (B) Bathtub").upper
    if toilet== "A":
        sink_scene()
    elif toilet == "B":
        tub_scene()
    
def bedroom_scene():
    bed = input("You walk to the bedroom and find a bed. Where do you look first (A) Under the Bed (B) In the Closet? ").upper()
    if bed == "B":
        duck_scene()
    elif bed == "A":
        turnip()
def turnip():
    turnip = input("Under the bed you find a moldy turnip. Do you (A)Eat it (B) Throw it away")
    if turnip == "A":
        MW= ("You start to pick up the turnip when you notice writing on it, and it looks just like the chief of polices.what do you do (A) go back to the station and confront her alone (B) go with backup")
        if MW== "A":
            office_scene2()
def kitchen_scene():
    greensause= input("You walk into the kitchen and see a bunch of cabentents. You open them and see a mistirous green sause. what do you do ? (A) try a little on a spoon (B) put it back (C) look somewhere else")

def duck_scene():
    input("Inside the closet you find a room with a bunch of rubber duckies, you dig through the ducks and find another dead body. What do you do (A) call your boss (B) take photos? ")

def office_scene():
    print("You run back to your boss's office and ask her for the suspects. She hands you a file.")
    file = input("Suspect 1\nName: Amy Terious\nAge: 20\nProfession: Dentist\nMarried Widow\nBirthday: Jan 28th\nHair color: dirty blond\nSkin Color: Blue\nEye Color: Green\nPress B for back").upper()
    if file == "B":
        input("You decide to interview the first suspect, what do you ask? (A) Are you the murderer? (B) What were you doing at the time of the murder")


def office_scene2():
    print("You run to the station and confront your boss and tell her what you found.")
    print("She starts to look worried the more you tell her.")
    if t == 1:
        print("\'Well\' she says.\'Now that you know my secret you will have to join me!\'")
        evil_scene()
    elif t== 2:
        print("\'Please help me! I don't have enough money to support me and my frog Andrew, because Andew the frog only eats 24 carrot gold.\'") 
        print ("You decide to create a tiktok acount for your fundraier FEED ANDREW DA FROG.")
        print("Your videos get billions of views and you become famous fast.")
        print("Now Andrew the frog has plenty of gold to eat!")
        print("YOU WON THE GAME!!!!!!")
    
def evil_scene():
    print("oh no you think you knew you should have brought backup!!")
    print("Now you have to join her evil scheme")
    print("'What did you even do to kill this many people?'")
    print("\'Well jonny knew I was commiting tax avation, but I could not support me and my frog Andrew because he only eats 24 carrot gold, so I killed him.\'")
    escape= input("She keeps on talking but you think you could make a run for it. (A) Run (B) Stay")
    if escape== "A":
        print("'Hey, where do you think your going?'")
        print("She blocks your path to the door. and everything turns black")
        print("YOU FAILED. TRY AGAIN NEXT TIME.")

    elif escape =="B":
        print("It is five years later, you are rich, and known as the most evil villan in the world.")
        print("You think back to the years when you were poor and had a small police job.You are glad you changed.")
        print("GOOD JOB YOU WON THE GAME!")




while True:
    
    print("You are a cop, you just got to work when you got a call from your boss that says to go to her office ASAP.You run up to her office and knock on her door.\'come in\' she says.\'You have been selected to solve a murder mystery\' your boss says her dark black hair almost as shiny as her wedding ring")
    the_call=input("You decide to get started right away. Where do you go? (A) To the victims house (B) Interview suspects ").upper()

    if the_call == "A":
        house = input("You get to the house and start looking around. What room do you go to first? (A) The bathroom (B) The bedroom (C) The kitchen").upper()
        if house == "A":
            bathroom = bathroom_scene()
            if bathroom == "A":
                tub_scene()
            elif bathroom == "B":
                sink_scene()
        elif house == "B":
            bedroom_scene()
            if bedroom_scene =="A":
                turnip()
            elif bedroom_scene == "B":
                bed()
        elif house =="C":
           kitchen_scene()
           if kitchen_scene == "A":
            nightvision()
    elif the_call == "B":
        office_scene()



