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

    auth = OAuth1(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    #introductory texts are written
    introduction()

    #set up both elon_tweets and kanye_tweets arrays
    setup_tweets(elon_tweets, kanye_tweets, auth)
 
    #main game playing method
    num_guess, num_success = play_game(elon_tweets, kanye_tweets, num_guess, num_success)

    #stats for the user
    game_result(num_guess, num_success)

def introduction():
    print("Welcome to the game \"Guess Whose tweet this is? Technology giant Elon Musk? OR Music giant Kanye West?")
    print("You will be prompted with randomly selected tweet from either of the persons and you are to guess which one wrote that tweet!")
    print("__________________________\n")

def setup_tweets(elon_tweets, kanye_tweets, auth):
    counter = 0
    index = 0

    #MAKE SURE TO CHANGE THE COUNT TO 3200!!!!!!!!!!!
    kanye_data = requests.get('https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=kanyewest&count=200', auth=auth).json()
    elon_data = requests.get('https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=elonmusk&count=200', auth=auth).json()

    #putting the tweets into the list in that does not have a tag or link
    while counter < MAX_TWEET:
        if index < len(elon_data):
            elon_tweet = elon_data[index]["text"]
            if elon_tweet.find("http") == -1 and elon_tweet.find("@") == -1:
                elon_tweets.append(elon_tweet)

        if index < len(kanye_data):
            kanye_tweet = kanye_data[index]["text"]
            if kanye_tweet.find("http") == -1 and elon_tweet.find("@") == -1:
                kanye_tweets.append(kanye_tweet)
        
        counter += 1
        index += 1

def play_game(elon_tweets, kanye_tweets, num_guess, num_success):
    gameStatus = 'A'

    while(gameStatus != 'N'):
        # 0 = elon and 1 = kanye
        elonOrKanye = random.randint(0, 1)
        
        if(elonOrKanye == 0):
            user_guessed(elon_tweets, elonOrKanye, num_guess, num_success)

        elif(elonOrKanye == 1):
            user_guessed(kanye_tweets, elonOrKanye, num_guess, num_success)
            
        #ask for continuing the game
        print("__________________________\n")
        playAgain = input("Would you like to play again? (Y/N) ")
        
        while((len(playAgain) != 1) and (playAgain.lower() != 'y' or playAgain.lower() != 'n')):
            playAgain = input("Please input alphabet 'y' or 'n' to continue or not! ")
        if(playAgain.upper() == "N"):
            gameStatus = 'N'
    

    return num_guess, num_success;

def user_guessed(array_of_tweets, which_persons_tweet, num_guess, num_success):
    randomElement = random.randint(0, len(array_of_tweets) - 1)
    guess = input("Whose tweet is this? (Press 'e' for Elon and 'k' for Kanye): " + "\"" + array_of_tweets[randomElement] + "\" ")
    if(which_persons_tweet == 0):
        while((len(guess) != 1) and (guess.lower() != 'e' or guess.lower() != 'k')):
            guess = input("Please input alphabet 'e' or 'k' for the answer! ")
            
        if(guess.lower() == 'e'):
            num_guess += 1
            num_success += 1
            print("Great job! You got it right!")

        elif(guess.lower() == 'k'):
            num_guess += 1
            print("It was actually Elon's tweet! :(")
    elif(which_persons_tweet == 1):
        while((len(guess) != 1) and (guess.lower() != 'e' or guess.lower() != 'k')):
            guess = input("Please input alphabet 'e' or 'k' for the answer! ")
                          
        if(guess.lower() == 'k'):
            num_guess += 1
            num_success += 1
            print("Great job! You got it right!")

        elif(guess.lower() == 'e'):
            num_guess += 1
            print("It was actually Kanye's tweet! :(")
    

def game_result(num_guess, num_success):
    percentage = round((num_success/num_guess * 100), 2)
    print("____________________")
    print("RESULT::")
    print("I hope you enjoyed playing the game!" + " You got " + str(num_success) + " question right out of " + str(num_guess) + " (" + str(percentage) + "%) questions!")


#start the program
if __name__ == "__main__":
    main()
 








