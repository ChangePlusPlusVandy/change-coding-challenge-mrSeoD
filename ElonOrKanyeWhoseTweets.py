import random
import requests
from requests_oauthlib import OAuth1

API_KEY = 'FeqiiXVXRr7Mgx0JTr3DxSzs6'
API_SECRET = '87lh17cNUL6pdxO5ZGLrX161orE7lNYCdkY53I3skJtTKqfVYN'
ACCESS_TOKEN = '1306076500848861184-p7MpRN5Ouyj5fOissjyN6yMbKp56yf'
ACCESS_TOKEN_SECRET = 'V4SBHnwUgicZazja9D42I9ErFFQ91ANp0Pn1SGboJLKpP'

MAX_TWEET = 3200

def main():
    # number of guesses and successes of the user to provide stats in the end of the game
    num_guess = 0
    num_success = 0

    # arrays of elon and kanye tweets that are filtered out from tags and url links
    elon_tweets = []
    kanye_tweets = []

    # authentication keys and secrets
    auth = OAuth1(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # introductory texts are written for the game to begin
    introduction()

    # set up both elon_tweets and kanye_tweets arrays
    setup_tweets(elon_tweets, kanye_tweets, auth)
 
    # main game playing method
    num_guess, num_success = play_game(elon_tweets, kanye_tweets, num_guess, num_success)

    # stats for the user
    game_result(num_guess, num_success)

# introduction() method gives information and instructions for the game
def introduction():
    print("Welcome to the game \"Guess Whose tweet this is? Technology giant Elon Musk? OR Music giant Kanye West?")
    print("You will be prompted with randomly selected tweet from either of the persons and you are to guess which one wrote that tweet!")
    print("__________________________\n")

# setup_tweets() method sets up the tweet of each Elon's and Kanye's tweets that don't contain URL or tag
def setup_tweets(elon_tweets, kanye_tweets, auth):
    index = 0

    kanye_data = requests.get('https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=kanyewest&count=3200', auth=auth).json()
    elon_data = requests.get('https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=elonmusk&count=3200', auth=auth).json()

    # putting the tweets into the list in that does not have a tag or link
    while (index < MAX_TWEET):
        if (index < len(elon_data)):
            # get the text part of the tweet in .json file
            elon_tweet = elon_data[index]["text"]
            # check if there is any URL or tag in the text
            if (elon_tweet.find("http") == -1 and elon_tweet.find("@") == -1):
                elon_tweets.append(elon_tweet)

        if (index < len(kanye_data)):
            kanye_tweet = kanye_data[index]["text"]
            if (kanye_tweet.find("http") == -1 and elon_tweet.find("@") == -1):
                kanye_tweets.append(kanye_tweet)
        
        index += 1

# play_game() method controls the game by getting user's input and replaying until the user wants to quit
def play_game(elon_tweets, kanye_tweets, num_guess, num_success):
    # dumby character assigned to start the game in the beginning
    gameStatus = 'A'

    while(gameStatus != 'N'):
        # getting random number between 0 or 1 --> Elon == 0 // Kanye == 1
        elonOrKanye = random.randint(0, 1)
        
        if(elonOrKanye == 0):
            num_guess, num_success = user_guessed(elon_tweets, elonOrKanye, num_guess, num_success)

        elif(elonOrKanye == 1):
            num_guess, num_success = user_guessed(kanye_tweets, elonOrKanye, num_guess, num_success)
            
        # ask for continuing the game
        print("__________________________\n")
        play_again = input("Would you like to play again? (Y/N) ")
        
        while((len(play_again) != 1) or (play_again.lower() != 'y' and play_again.lower() != 'n')):
            play_again = input("Please input alphabet 'Y' or 'N' to continue or not! ")
        if(play_again.upper() == "N"):
            gameStatus = 'N'
    
    return num_guess, num_success;

# user_guessed() method manages the user's input to tell if the user got right or not
def user_guessed(array_of_tweets, which_persons_tweet, num_guess, num_success):
    randomElement = random.randint(0, len(array_of_tweets) - 1)
    guess = input("Whose tweet is this? (Press 'E' for Elon and 'K' for Kanye): \n" + "\"" + array_of_tweets[randomElement] + "\" Your Answer: ")
    if(which_persons_tweet == 0):
        while((len(guess) != 1) or (guess.upper() != 'E' and guess.upper() != 'K')):
            guess = input("Please input alphabet 'E' or 'K' for the answer! ")

        if(guess.upper() == 'E'):
            num_guess += 1
            num_success += 1
            print("Great job! You got it right!")

        elif(guess.upper() == 'K'):
            num_guess += 1
            print("It was actually Elon's tweet! :(")
            
    elif(which_persons_tweet == 1):
        while((len(guess) != 1) and (guess.upper() != 'E' and guess.upper() != 'K')):
            guess = input("Please input alphabet 'E' or 'K' for the answer! ")
                          
        if(guess.upper() == 'K'):
            num_guess += 1
            num_success += 1
            print("Great job! You got it right!")

        elif(guess.upper() == 'E'):
            num_guess += 1
            print("It was actually Kanye's tweet! :(")
            
    return num_guess, num_success

# game_result() method returns the stats of the game with success rate
def game_result(num_guess, num_success):
    percentage = round((num_success/num_guess * 100), 2)
    print("____________________")
    print("RESULT::")
    print("I hope you enjoyed playing the game!" + " You got " + str(num_success) + " question right out of " + str(num_guess) + " (" + str(percentage) + "%) questions!")


#start the program
if __name__ == "__main__":
    main()
 








