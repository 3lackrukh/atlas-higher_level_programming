#!/usr/bin/python3
class Dawg:
    def __init__(self, name, race, klass, level):
        self.name = name
        self.race = race
        self.klass = klass
        self.level = level

    def dawg_deets(self):
        return f"| {self.name:<30} | {self.race:<10} | {self.klass:<10} | {self.level:>5} |"
text = "MUH DAWGS"
width = 66
centered_text = text.center(width)
print("+{}+".format("-" * 66))
print(centered_text)
#print("+{}+".format("-" * 66))
#$print("+{}+{}+{}+{}+".format("-" * 32, "-" * 12, "-" * 12, "-" * 7))

Dawgs = [
    Dawg("Drizt", "Drow", "Ranger", 35),
    Dawg("Zephyr", "Djinn", "Sorcerer", 5),
    Dawg("Bane", "DragonBorn", "Paladin", 43),
    Dawg("Varda", "Half-Elf", "Monk", 6),
    Dawg("Snoop", "Human","Bard-G", 52),
    Dawg("Ice-T", "Elemental", "Bard-G", 50)
]

#print(f"| {self.name:<30} | {self.race:<10} | {self.klass:<10} | {self.level:>5} |")
print("+{}+{}+{}+{}+".format("-" * 32, "-" * 12, "-" * 12, "-" * 7))
for dawg in Dawgs:
    print(dawg.dawg_deets())
    print("+{}+{}+{}+{}+".format("-" * 32, "-" * 12, "-" * 12, "-" * 7))
new_text = "EN O MUH DAWGS"
new_centered_text = new_text.center(width)
print(new_centered_text)

