#!/usr/bin/env python
# coding: utf-8

# In[ ]:


i=0
user_1 = input('Please enter your name: ')
user_2 = input('Please enter your name: ')
user_1_score = 0
user_2_score = 0
while i<10:
    user_1_choice = input("Enter your choice {} rock, paper or scissors: ".format(user_1))
    user_2_choice = input("Enter your choice {} rock, paper or scissors: ".format(user_2))
    i+=1
    print ('This is game',i) 
    print(" choice of {} is {} and choice of {} is {}".format(user_1,user_1_choice,user_2, user_2_choice))
    if user_1_choice==user_2_choice:
        print("Both players selected {}. It's a tie!".format(user_2_choice))
    elif user_1_choice == "rock":
        if user_2_choice == "scissors":
            print("Rock smashes scissors!{} win!".format(user_1))
            user_1_score+=1
        else:
            print("Paper covers rock!{} win".format(user_2))
            user_2_score+=1
    elif user_1_choice == "paper":
        if user_2_choice == "rock":
            print("Paper covers rock! {} win!".format(user_1))
            user_1_score+=1
        else:
            print("Scissors cuts paper! {} win".format(user_2))
            user_2_score+=1
    elif user_1_choice == "scissors":
        if user_2_choice == "paper":
            print("Scissors cuts paper! {} win!".format(user_1))
            user_1_score+=1
        else:
            print("Rock smashes scissors! win".format(user_2))
            user_2_score+=1
if user_1_score> user_2_score:
    print('Congratulations, {} win, the score is {} and {}'.format(user_1,user_1_score,user_2_score))
elif user_2_score>user_1_score:
    print('Congratulations, {} win,the score is {} and {}'.format(user_2,user_2_score,user_1_score))
else:
    print('It is a tie!')
    print(user_1_score,user_2_score, sep="-")
        

