import random

# Storing random data into lists to crate story
#
when = ['A long time ago', 'Yesterday', 'Before you were born', 'Before Thanos arrived']
who = ['Shazam', 'Iron Man', 'Batman', 'Superman', 'Captain America']
went = ['Arkham Asylum', 'Gotham City', 'Stark Tower', 'Bat Cave', 'Avenger HQ']
what = ['to eat a lot of cakes', 'to fight for justice', 'to steal ice cream', 'to dance']

# Using string concatenition & randome.choice() to print a random element from all the lists
print(random.choice(when), + ', ' + random.choice(who) + ' went to ' + random.choice(went) + ' ') #+ random.choice(what) + '.')
