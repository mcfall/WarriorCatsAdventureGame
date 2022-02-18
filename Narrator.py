import subprocess
import random

def say(text):
    subprocess.call(['say', text])

def print_and_say(text):
    print(text)
    say(text)

valid_catname_prefixes = {"cricket","holly","fern","mouse","fire","dawn","lion","leaf","rain","cloud","feather"}
valid_catname_suffixes = {"watcher","shade","brain","claw","frost","flight","pool","heart","tail","storm"}

def is_valid_catname(name :str):
    is_valid_prefix = False
    for prefix in valid_catname_prefixes:
        if name.startswith(prefix):
            is_valid_prefix = True
            break

    if not is_valid_prefix:
        print("Name does not start with a valid prefix. Allowed prefixes are: ", valid_catname_prefixes)

    is_valid_suffix = False
    for suffix in valid_catname_suffixes:
        if name.endswith(suffix):
            is_valid_suffix = True
            break

    if not is_valid_suffix:
        print("Name does not end with a valid suffix. Allowed suffixes are: ", valid_catname_suffixes)

    return is_valid_prefix & is_valid_suffix

def is_allowed_catname(name: str, existing_catnames):
    # This function first checks that the name has not been used already. If it has, it returns false. If not, it then
    # checks if it is valid
    if catname in existing_catnames:
        print_and_say("Sorry, that cat name is already taken.")
        return False

    return is_valid_catname(name)

def choose_random_catname(existing_catnames):
    random_catname = random.choice(list(valid_catname_prefixes))+random.choice(list(valid_catname_suffixes))
    print("Allow me to make up a cat name for you:", random_catname)
    if random_catname in existing_catnames:
        print("Oops, that already exists, let me try again")
        random_catname = choose_random_catname(existing_catnames)

    return random_catname

print_and_say("Welcome to Elsa's Warrior Cats Adventure!")
print_and_say("Allow me to introduce myself, I'm Conrad, your narrator.")
print_and_say("Let's get the game started. First, please answer a few questions")

num_cats = 0
valid_number_of_cats_entered = False

while not valid_number_of_cats_entered:
    num_cats_input = input("How many cats are there (1-9)?\n")
    while not num_cats_input.isdigit() :
        print(num_cats_input,"is not a number from 1-9. Please try again")
        num_cats_input = input("How many cats are there (1-9)?\n")

    num_cats = int(num_cats_input)
    if num_cats < 1 or num_cats > 9:
        print("Can't you count? I said pick a number between 1 and 9")
    else:
        valid_number_of_cats_entered = True

catnames = []

for i in range(num_cats):
    catname = input("What is cat number {} called? (Or just press return and I'll help you find a good name)\n".format(i+1)).strip()

    if catname == '':
        catname = choose_random_catname(catnames)

    while not is_allowed_catname(catname, catnames):
        catname = input("Please try again\n")

    catnames.append(catname)


print("The cats are called ",catnames)




