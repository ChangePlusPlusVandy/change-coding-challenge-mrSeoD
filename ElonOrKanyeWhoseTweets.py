import random
import requests
from requests_oauthlib import OAuth1

API_KEY = 'FeqiiXVXRr7Mgx0JTr3DxSzs6'
API_SECRET = '87lh17cNUL6pdxO5ZGLrX161orE7lNYCdkY53I3skJtTKqfVYN'
ACCESS_TOKEN = '1306076500848861184-p7MpRN5Ouyj5fOissjyN6yMbKp56yf'
ACCESS_TOKEN_SECRET = 'V4SBHnwUgicZazja9D42I9ErFFQ91ANp0Pn1SGboJLKpP'

MAX_TWEET = 3200

# number of guesses and successes of the user to provide stats in the end of the game
num_guess = 0
num_success = 0

# arrays of elon and kanye tweets that are filtered out from tags and url links
elon_tweets = []
kanye_tweets = []

auth = OAuth1(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


############# setting up the arrays
counter = 0
index = 0

kanye_data = requests.get('https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=kanyewest&count=200', auth=auth).json()
elon_data = requests.get('https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=elonmusk&count=200&include_rts=false', auth = auth).json()

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

#DEBUGGGGG
print(len(elon_tweets))
print(len(kanye_tweets))

############# game playing itself
gameStatus = 'a'

while(gameStatus != 'N'):
    # 0 = elon and 1 = kanye
    elonOrKanye = random.randint(0, 1)
    
    if(elonOrKanye == 0):
        randomElement = random.randint(0, len(elon_tweets) - 1)
        guess = input("Whose tweet is this? (Press 'e' for elon and 'k' for kanye): " + "\"" + elon_tweets[randomElement] + "\"")
        if(guess.lower() == 'e'):
            num_guess += 1
            num_success += 1
            print("Great job! You got it right!")

        elif(guess.lower() == 'k'):
            num_guess += 1
            print("It was actually Elon's tweet! :(")
            
        #if neither e or k is input
        #else:
            #just move on or go back..?
        

    elif(elonOrKanye == 1):
        randomElement = random.randint(0, len(kanye_tweets) - 1)
        guess = input("Whose tweet is this? (Press 'e' for elon and 'k' for kanye): " + "\"" + kanye_tweets[randomElement] + "\"")
        
        if(guess.lower() == 'k'):
            num_guess += 1
            num_success += 1
            print("Great job! You got it right!")

        elif(guess.lower() == 'e'):
            num_guess += 1
            print("It was actually Kanye's tweet! :(")
        

    #ask for continuing the game
    playAgain = input("Would you like to play again? (Y/N)")
    if(playAgain.upper() == "N"):
        gameStatus = 'N'
    #what is random is input?
    #else:
        #nothing as of now

####### end page
percentage = round((num_success/num_guess * 100), 2)
print("____________________")
print("RESULT::")
print("I hope you enjoyed playing the game!" + " You got " + str(num_success) + " question right out of " + str(num_guess) + " (" + str(percentage) + "%) questions!")

#print(elon_tweets[0])
#print(kanye_tweets[0])
#print(elon_data[0]["text"])
#print(elon_data[0]["entities"]["hashtags"] == [])
 








