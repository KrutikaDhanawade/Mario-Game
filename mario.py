#  Mario Game

class character():
    def __init__(self,name):
        self.name = name
        self.__life = 3
        self.__score = 0

    def kick(self):
        self.__score+=10

    def punch(self):
        self.__score+=5

    def stab(self):
        self.__life -= 1

    def dislife(self):
        return self.__life

    def disScore(self):
        return self.__score

    def intro(self):
        print(f"Name : {self.name.title()}")
        print(f"Score : {self.__score}")
        print(f"Life : {self.__life}")


def playmario():
    name = input("Enter Your Name : ")

    mario = character(name)



    while True:
        print("\nEnter 1 for Kick")
        print("Enter 2 for Punch")
        print("Enter 3 for Stab")
        print("Enter 4 to Display Life & Score")
        print("Enter 5 for Exit\n")

        choice = int(input("Enter Your Choice : "))

        if choice == 1:
            mario.kick()
            
        elif choice == 2:
            mario.punch()

        elif choice == 3:
            stbval = mario.dislife()
            #print(stbval)
            mario.stab()
            if stbval > 1:
                continue
            else:
                print("Game Over")
                print("Score is : ",mario.disScore(),"\n")
                playmario()
                break
                

        elif choice == 4:
            print("\n")
            mario.intro()

        elif choice == 5:
            sur = input("Are You Sure (Y/N)")
            sur = sur.lower()

            if sur == "n":
                continue
            elif sur == "y":
                break
            else:
                print("Invalid Input")
                continue

    
playmario()   


