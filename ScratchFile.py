import subprocess

def say(text):
    subprocess.call(['say', text])

say("Hello Elsa")

#catname = input("What is the name of your cat?\n")
#print(f'Your cat is called {catname}')

#say("Once upon a time there was a cat named "+catname)

print("Cat {} is on duty.".format(4))