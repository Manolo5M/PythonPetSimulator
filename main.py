

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

#Program

print(color.BOLD + 'Welcome to the Pet Simulator ' + color.END)

start = input("Type 'Start' to proceed: ")
if start == "Start":
    print(color.UNDERLINE + 'Select Pet. ' + color.END)
    print("Dog")
    print("Katt")
    print("Bird")
    import time
    import random
    num1 = random.randint(1, 20)
    while True:
        choice = input("Enter Pet Type (Dog/Katt/Bird): ")
        if choice in ('Dog', 'Katt', 'Bird'):
            print("Select gender.")
            print("Male")
            print("Female")
            petGender = input("Choose pets gender (Male/Female): ")
            petName = input("Name the pet: ")
            time.sleep(0.4)
            print("Rendering your pet...")
            time.sleep(0.6)
            print(color.UNDERLINE + 'Your pet. ' + color.END)
            time.sleep(0.2)
            print("Name:", petName)
            time.sleep(0.2)
            print("Gender:", petGender)
            time.sleep(0.2)
            print("Age:", num1, "year(s) old")
            time.sleep(0.3)
            if choice == 'Katt':
                print(" /\_/\ ")
                time.sleep(0.3)
                print("( o.o )")
                time.sleep(0.3)
                print(" > ^ < ")
            elif choice == 'Dog':
                print("---------")
                time.sleep(0.3)
                print(",-.___,-.")
                time.sleep(0.3)
                print("\_/_ _\_/")
                time.sleep(0.3)
                print("  )O_O(")
                time.sleep(0.3)
                print(" { (_) }")
                time.sleep(0.3)
                print("  `-^-' ")
            elif choice == 'Bird':
                print("Fågel")
        
        break
    else:
        print("Invalid Input")
else:
    print("Invalid Input")
