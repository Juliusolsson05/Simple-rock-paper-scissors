import random
import time

# ASCII art numbers for countdown
ascii_numbers = {
    '5': """
  #####
 #     
 #     
  #####
      #
 #    #
  #### 
""",
    '4': """
   #  #
  #   #
 #    #
#######
     #
     #
""",
    '3': """
 ######
#     #
      #
 ######
      #
#     #
 ######
""",
    '2': """
 ######
#     #
      #
 #####
#     
#     
#######
""",
    '1': """
   ##
  # #
    #
    #
    #
    #
   ###
"""
}

def countdown():
    for number in ['5', '4', '3', '2', '1']:
        print(ascii_numbers[number])
        time.sleep(1)  # Wait for one second

def rock_paper_scissors():
    # Ordbok för att lagra de möjliga valen
    choices = {1: 'Sten', 2: 'Sax', 3: 'Påse'}

    user_choice = int(input("Gör ett val (1 för Sten, 2 för Sax, 3 för Påse): "))
    if user_choice in choices:
        print(f"Användarens val är: {choices[user_choice]}")

        print("Datorn gör sitt val...")
        countdown()  # Start the countdown

        computer_choice = random.randint(1, 3)
        print(f"Datorns val är: {choices[computer_choice]}")

        # Bestäm vinnaren
        if user_choice == computer_choice:
            print("Det är lika!")
        elif (user_choice == 1 and computer_choice == 2) or \
             (user_choice == 2 and computer_choice == 3) or \
             (user_choice == 3 and computer_choice == 1):
            print("Du vinner!")
        else:
            print("Du förlorar!")
    else:
        print("Ogiltigt val. Vänligen ange 1, 2, eller 3.")

# Kör spelet
if __name__ == "__main__":
    while True:
        rock_paper_scissors()
        # Fråga användaren om hen vill spela igen
        play_again = input("Spela igen? (ja/nej): ")
        if play_again.lower() != 'ja':
            break

