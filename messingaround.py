from ast import If
from ntpath import join
import sys

name= input("Hello there, what is your name: ") 
print("Ah, hi", name, "you look fabulous today!!!")
age = int(input("How old are you?: "))
print("So that means you were born in", 2026-age)
if age>16: 
    print("DAMN You are old")
if age==16:
    print("hello there fellow kid")
if age<16:
    print("Awww does the baby need changing?")  


print ("now that I know a bit about you, lets try something.")
levels = int(input("How many levels do you want?: "))
for i in range(1, levels +1):
  spaces = " " * (levels - i)
  stars = "*" * (2 * i - 1)
  print(spaces + stars)

print("lets try something else now, shall we?")
morse = input("Type something and I will translate it to morse code: ")
 
MORSECODE_DICT = {'A': '.-',   'B': '-...', 'C': '-.-.', 'D': '-..',  'E': '.',
    'F': '..-.', 'G': '--.',  'H': '....', 'I': '..',   'J': '.---',
    'K': '-.-',  'L': '.-..', 'M': '--',   'N': '-.',   'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',  'S': '...',  'T': '-',
    'U': '..-',  'V': '...-', 'W': '.--',  'X': '-..-', 'Y': '-.--',
    'Z': '--..', ' ': '/'}
def morse_translation(text):
    morselist = []
    for char in text.upper():
        if char in MORSECODE_DICT:
            morselist.append(MORSECODE_DICT[char])
    return ' '.join(morselist)

result = morse_translation(morse)
print(result)
print ("pretty cool huh?")

try:
    print ("would you like to try something else?")
    if input("yes or no: ").lower() == "yes":
        print("ok, lets do it")
    elif input("yes or no: ").lower() == "no":
        sys.exit("Fine, Be like that then, not that i wanted you to play anyway...")
except: 
    print("only use yes or no, you are not very smart are you?")
    sys.exit 

print("ok, now we are going to play a trivia game")
print("every right answer will add a point to your score BUT you will not get to see it till they are all done, capiche?")
score = 0 
Q1=input ("""What is the meaning of life, the universe, and everything?
          A 42
          B To be happy 
          C 383
          D to be kind to one another""")
if Q1.lower() == "a":
    score += 1 
Q2=input ("""What city is the azerbaijani grand prix held in?
          A Tajikistan
          B Addis Ababa
          C Baku
          D Nurburgring""")
if Q2.lower() == "c":
    score += 1
Q3=input ("""how many UN recognised countries are there?
          A 200
          B 195
          C 193
          D 199""")
if Q3.lower() == "c":
    score += 1


if score == 3:
    print("You got all of them right, you are not stupid")
if score == 2:
    print("You got 2 out of 3 right, Hm, I'll pay it")
if score == 1:
    print("You got 1 out of 3 right, you suck at this dont you...")
if score == 0:
    print("You got 0 out of 3 right, you are a failure")
print ("Thank you for trying this program I made, some parts may suck but this is my attempt to learn the basics of python, so I hope you found it satisfactory. And in case I don't see you, good afternoon, good evening, and good night.")
End = input("Press enter to exit the program") 
if End == "":
    sys.exit("Goodbye")
