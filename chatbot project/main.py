from functions import *

# create chatbot 
home_bot = create_bot('Jordan')

# train all data
train_all_data(home_bot)

# check identity
identity = input("State your identity please: ")

# rules for responding to different identities
if identity == "Aafreen":
    print("Welcome, Aafreen. Happy to have you at home.")

elif identity == "Masha":
    print("Aafreen is out right now, but you are welcome to the house Masha.")

elif identity == "Deepa":
    print("Aafreen is out right now, but you are welcome to the house Deepa.")

else:
    print("Your access is denied here.")
    exit()

# custom data
house_owner = [
    "Who is the owner of this house?",
    "Aafreen is the owner of this house."
]
custom_train(home_bot, house_owner)

print("------ Training custom data ------")
# write and train your custom data here IF the identity is Mark
if identity == 'Aafreen':   
    city_born = [
        "Where was I born?",
        "Aafreen, you were born in Andamans."
    ]

    fav_book = [
        "What is my favourite book?",
        "That is easy. Your favourite book is The Hunger Games."
    ]
    fav_movie = [
        "What is my favourite movie?",
        "You have watched Inception more times than I can count."
    ]

    fav_sports = [
        "What is my favourite sport?",
        "You have always loved basketball."
    ]
    # train chatbot with your custom data
    custom_train(home_bot, city_born)
    custom_train(home_bot, fav_book)
    custom_train(home_bot, fav_movie)
    custom_train(home_bot, fav_sports)

# start chatbot
start_chatbot(home_bot)