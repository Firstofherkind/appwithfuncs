# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 09:05:52 2021

@author: JENI
"""
from datetime import datetime
import random


database = {
    
    2345678910:['Chidera', 'Attueyi', 'chi', 'kendy@yahoo..com', 100]
    
    }

def init():
    print('************WELCOME TO FIRSTOFHERKIND BANK**********')
    
    timeAndDate()
    
    accountCreated = int(input('Do you have an account with us already? If yes, enter 1 to login, enter 2 to register! \n'))
    if accountCreated == 1:
        login()
    elif accountCreated == 2:
        print(register())
    else:
        print('Enter your preferred option from 1 - 2!')
        init()
        
        
        
        
        
def login():
    
    timeAndDate()
    
    print("Welcome!! Please enter your details: ")
    accountFromUser = int(input('Please enter your account number: \n'))
    passwordFromUser = input('Please enter your password: \n')
    
    for accountNumber, userDetails in database.items():
        if accountNumber == accountFromUser:               
            if userDetails[2] == passwordFromUser:
                print('Login is successful')
                bankOperations(userDetails)
                
            else:
                print('Enter a valid account number and try again!')
                login()
        else:
            print('Enter your correct account no and try again!')
            login()
            
            
            
def register():
    
    timeAndDate()
    
    print('Please input Data for registration.')
    email = input('Please enter your valid email. \n')
    firstName = input('Please enter your first name. \n')
    lastName = input('Please enter your last name. \n')
    password = input('Please create a new password. \n')
    accountNumber = generateAccountNo()
    print("This is your account no:",  accountNumber)
    
    database[accountNumber] = [firstName, lastName, password, email, 100]
    
    yesToLogin =int(input('Your account has been created, would you like to login? If yes, enter 1 or to logout enter 2. \n'))
    if yesToLogin == 1:
        login()
    else:
        logout()
    
def bankOperations(user):
    print(f'Welcome {user[0]} {user[1]}!!')
    operationsOption = int(input('For withdrawal press 1, For Deposit, press 2, For complaint, press 3, For Feedback press 3. \n'))
    if operationsOption == 1:
        withdrawal(user)
    elif  operationsOption == 2:
        Deposit(user)
    elif operationsOption == 3:
        complaint(user)
    elif operationsOption == 4:
        feedback(user)
    else:
        print('Please enter your preferred option from 1-4')
        bankOperations(user)
        
        
def withdrawal(user):
    amountToWithdraw = int(input('How much would you like to withdraw: \n'))
    for accountNumber, userDetails in database.items():
        amountAvailable = userDetails[4]
        #print(amountAvailable)
    
    if amountToWithdraw > amountAvailable:
        print("Insufficient balance! Please enter amount less than or equal to", amountAvailable)
        anotherTransaction(user)
    
        
    elif amountToWithdraw < amountAvailable:
        print('Please take your cash')
        anotherTransaction(user)

def Deposit(user):
    amountToDeposit = int(input('How much would you like to deposit? : \n'))
    for accountNumber, userDetails in database.items():
        availableBal = userDetails[4]
    
    print("You have successfully deposited the sum of", amountToDeposit, 'NGN. Your Balance is :', amountToDeposit + availableBal)
    anotherTransaction(user)

    
def complaint(user):
    complaint = input('Please enter your complaint: \n')
    print('Thank you! Your complaint would be addressed duly!')
    anotherTransaction(user)




def feedback(user):
    feedback = input('Please enter your feedback:\n')
    print('Your response has been recorded! Thank you!')
    anotherTransaction(user)
    
    
        
def logout():
    print('Thank you for banking with us!')
    exit()
    
    

def timeAndDate():
    now = datetime.now()
    dateAndTime = now.strftime('%d/%m/%Y, %H:%M:%S')
    print(dateAndTime)
    
    
    
def anotherTransaction(user):
    anotherTransactionOption = int(input('To perform another transaction? If yes, enter 1, else, press 2 to logout \n'))
    if anotherTransactionOption  == 1:
        bankOperations(user)
    elif anotherTransactionOption == 2:
        logout()
    else:
        print('please enter a valid option 1 - 2!')
        anotherTransaction(user)
    
        
    
def generateAccountNo():
    return random.randint(1111111111, 9999999999)
        
    
init()