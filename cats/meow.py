import random
from random import randrange

breedstr = '''Persian
Siamese
Sphinx
Burmese
Tabby
Manx'''

namestr='''Bella
Kitty
Lily
Lilly
Charlie
Lucy
Leo
Milo
Jack
Nala
Sam
Simba
Chloe
Baby
Sadie
Ziggy
Princess
Salem
Sophie
Shadow
Izzy
Cleo
Boots
Loki
Daisy
Cooper
Missy
Oreo
Tiger
Lulu
Tucker
Jasmine
Jackson
Murphy
Pepper
Fiona
Jax
Frank
Romeo
Millie
Abby
Minnie
Olivia
Lola
Athena
Teddy
Ruby
Oscar
Bear
Moose
Pumpkin
Willow
Mittens
Coco
Penny
Sammy
Sammie
Theo
Kali
Bob
Clyde
Tigger
Buddy
Joey
Emma
Ollie
Toby
George
Marley
Bagheera
Belle
Binx
Boo
Ash
Scout
Gizmo
Louie
Ginger
Midnight
Mochi
Blue
Frankie
Rosie
Ella
Calvin
Lucky
Hazel
Thor
Gus
Maggie
Piper
Harley
Rocky
Peanut
Mimi
Kitten
Remy
Remi
Annie
Sunny
Layla
Leila
Riley
Walter
'''

names = namestr.split()
breeds = breedstr.split()

cats = list()
for name in names:
    cat = name+','+random.choice(breeds)+','+str(6.0+randrange(40)/10.0)
    cats.append(cat)

for cat in sorted(cats):
    print(cat)
