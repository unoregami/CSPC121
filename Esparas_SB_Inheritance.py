import random


class Humanoid:
    height = 0  # 3-7ft
    weight = 0  # 60-300lbs
    hcolor = "" # white, silver, gray, black, brown, green, blue, yellow, pink, red, blonde
    ecolor = "" # white, black, red, brown, green, blue, purple, amber
    stre = 0
    dex = 0
    cons = 0
    inte = 0
    wis = 0
    char = 0


class Humans(Humanoid):  # +2 attribute
    def __init__(self, a, b, c, d, e, f, g, h, i, j):
        self.height = a
        self.weight = b
        self.hcolor = c
        self.ecolor = d
        self.stre = e
        self.dex = f
        self.cons = g
        self.inte = h
        self.wis = i
        self.char = j
        self.passive = ""

        x = input(
            "As a Human Class, you gain +2 points in ATTRIBUTES!\nChoose an attribute you want to add your points "
            "(Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma): ").lower()
        while x != "strength" and x != "dexterity" and x != "constitution" and x != "intelligence" and x != "wisdom" and x != "charisma":
            x = input("The input is not an option: ").lower()
        if x == "strength":
            self.stre += 2
        elif x == "dexterity":
            self.dex += 2
        elif x == "constitution":
            self.cons += 2
        elif x == "intelligence":
            self.inte += 2
        elif x == "wisdom":
            self.wis += 2
        elif x == "charisma":
            self.char += 2


class Elves(Humanoid):  # 100% res to sleep | +2 dex and char
    def __init__(self, a, b, c, d, e, f, g, h, i, j):
        self.height = a
        self.weight = b
        self.hcolor = c
        self.ecolor = d
        self.stre = e
        self.dex = f + 2
        self.cons = g
        self.inte = h
        self.wis = i
        self.char = j + 2
        self.passive = "100% Resistance to Sleep (Cannot be put to sleep)"


class Dwarves(Humanoid):    # 20% res to magic | +2 str and cons | -2 char
    def __init__(self, a, b, c, d, e, f, g, h, i, j):
        self.height = a
        self.weight = b
        self.hcolor = c
        self.ecolor = d
        self.stre = e + 2
        self.dex = f
        self.cons = g + 2
        self.inte = h
        self.wis = i
        self.char = j - 2
        self.passive = "20% Resistance to Magic"


def characterCreation():
    x = input("Pick a Class\n\tHumans — Gain +2 additional points to add of your chosen ATTRIBUTE\n\tElves — "
              "100% Resistance to Sleep | +2 Dexterity | +2 Charisma\n\tDwarves — 20% Resistance to Magic | +2 Strength | +2 Constitution\nInput: ").lower()
    while x != "humans" and x != "elves" and x != "dwarves":
        x = input("Please choose from the given classes: Humans | Elves | Dwarves\n").lower()
    return x


print("==========\tWelcome to RPG Inheritance!\t==========\n")

userclass = characterCreation()

height = int(input("Input Height (3ft - 7ft): "))
while height < 3 or height > 7:
    height = int(input("Please input between 3ft - 7ft: "))

weight = int(input("Input Weight (60lbs - 300lbs): "))
while weight < 60 or height > 300:
    weight = int(input("Please input between 60lbs - 300lbs: "))

hcolor = input(
    "Input Hair Color (white, silver, gray, black, brown, green, blue, yellow, pink, red, blonde): ").lower()
while hcolor != "white" and hcolor != "silver" and hcolor != "gray" and hcolor != "black" \
        and hcolor != "brown" and hcolor != "green" and hcolor != "blue" and hcolor != "yellow" \
        and hcolor != "pink" and hcolor != "red" and hcolor != "blonde":
    hcolor = input("The input is not an option: ").lower()

ecolor = input("Input Eye Color (white, black, red, brown, green, blue, purple, amber): ").lower()
while ecolor != "white" and ecolor != "black" and ecolor != "red" and ecolor != "brown" \
        and ecolor != "green" and ecolor != "blue" and ecolor != "purple" and ecolor != "amber":
    ecolor = input("The input is not an option: ").lower()

stre = random.randint(1, 18)
dex = random.randint(1, 18)
cons = random.randint(1, 18)
inte = random.randint(1, 18)
wis = random.randint(1, 18)
char = random.randint(1, 18)
print(f"\nThese are your random attributes\nStrength: {stre}\nDexterity: {dex}\nConstitution: {cons}\nIntelligence: {inte}\nWisdom: {wis}\nCharisma: {char}")

print()
if userclass == "humans":
    obj = Humans(height, weight, hcolor, ecolor, stre, dex, cons, inte, wis, char)
elif userclass == "elves":
    obj = Elves(height, weight, hcolor, ecolor, stre, dex, cons, inte, wis, char)
else:
    obj = Dwarves(height, weight, hcolor, ecolor, stre, dex, cons, inte, wis, char)
print()

print(f"=====================================================================\nCHARACTER\nClass: {userclass.capitalize()}\
\nHeight: {obj.height}\nWeight: {obj.weight}\nHair Color: {obj.hcolor.capitalize()}\nEye Color: {obj.ecolor.capitalize()}\n\nATTRIBUTES \
\nStrength: {obj.stre}\nDexterity: {obj.dex}\nConstitution: {obj.cons}\nIntelligence: {obj.inte}\nWisdom: {obj.wis}\nCharisma: {obj.char}\n{obj.passive}")