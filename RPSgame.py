import random

def get_computer_choice():
    choices  = ['1','2','3']
    computer_move = random.choice(choices)
    return computer_move

def get_user_choice():
    while True:
        user_input = input("Enter your move:\n1. Rock.\n2. Paper.\n3. Scissors.\n4. QUIT.\n").lower()

        if user_input == '4':
            return '4'
        
        valid_choices = ['1','2','3'] 

        if user_input in valid_choices:
            return user_input
        else:
            print ("❌ Invalid choice. Please enter 1, 2, 3, or 4 to quit.")

def determine_winner(user_move, computer_move):
    if user_move == computer_move:
        return "Tie."
    elif (user_move == '1' and computer_move == '3') or \
         (user_move == '2' and computer_move == '1') or \
         (user_move == '3' and computer_move == '2'):
        return "Win."
    else:
        return "Lose."

def move_to_word(move):
    if move == '1':
        return "ROCK"
    elif move == '2':
        return "PAPER"
    elif move == '3':
        return "SCISSORS"
    return "QUIT"

def play_game():
    user_score = 0
    computer_score = 0

    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("WELCOME TO ROCK, PAPER, SCISSORS! (●'◡'●)")
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    while True:
        computer_move = get_computer_choice()
        user_move = get_user_choice()

        if user_move == '4':
            break

        user_text = move_to_word(user_move)
        computer_text = move_to_word(computer_move)
        
        print(f"\n---You chose **{user_text}** vs Computer chose **{computer_text}**---")
        
        result = determine_winner(user_move , computer_move)

        if result == 'Tie.':
            print ("🤝 It's a TIE!!!")
        elif result == 'Win.':
            user_score += 1 
            print ("🎉 You Won this round!")
        else:
            computer_score += 1
            print("😟 You Lost it.")

        print(f"Current Score: You {user_score} | Computer {computer_score}\n")
    
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print (f"FINAL SCORE: You: {user_score} | Computer: {computer_score}")
    print ("THANKS FOR PLAYING!!!😘")
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


if __name__ == "__main__":
    play_game()