import time
import os

rows = 22
columns = 22
ball = "b"
xcor = 10
ycor = 10
up = False
left = False
down = False
right = False


def printField():
    global xcor
    global ycor
    global up
    global left
    global down
    global right

    if xcor == rows - 2:
        up = False
        left = True
        down = False
        right = False

    elif xcor == 1:
        up = False
        left = False 
        down = False 
        right = True

    elif ycor == columns - 2:
        up = True 
        left = False 
        down = False 
        right = False

    elif ycor == 1:
        up = False 
        left = False 
        down = True 
        right = False

    if up:
        ycor -=1
    elif left:
        xcor -=1
    elif down:
        ycor +=1
    elif right:
        xcor +=1
    else:
        xcor +=1

    for i in range(rows):
        for j in range(columns):
            if i == ycor and j == xcor:
                print(ball, end= ' ')
            elif i == 0 or i == rows -1 or j == 0 or j == columns - 1:
                print("*", end= ' ')
            else:
                print(" ", end= ' ')
        print("")

def wipe():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')

while(True):
    time.sleep(1)
    wipe()
    printField()    



def replacetest():
    text = "aaabbbcccdddeee"
    print(text.replace("a", "z", 2))

# replacetest()
def test():
    string = "#          #"
    position = 6
    new_character = 'b'
    string = string[:position] + new_character + string[position+1:]
    print(string)
#test()
