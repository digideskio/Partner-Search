'''
Created on 2013-01-08

@author: Gord
'''

import datetime
import sys

import dancer
import dancerSet
import emailer
import partnerSearchManager
from dancerParser import dancerParser
from matchParser import matchParser


def printMainOptions():
    print("""What would you like to do?
    
    0: Set the dancers participating
    1: Set the choices of dancers
    2: Create pairings for each round of dancing 
    3: Perform the matching
    """)
    
def setupDancers():
    file = raw_input("Enter the name of the file contianing the dancer info: ")
    parser = dancerParser(file)
    theSet = parser.parseToDancerSet()
    numDancers = len(theSet.leads) + len(theSet.follows)
    print("Setup " + str(numDancers) + " dancers.")
    return theSet

def setupChoices(danceClub):
    userInput = raw_input("Enter the name of the file containing the dancer's choices: ")
    parser = matchParser(userInput)
    parser.parseChoicesToSet(danceClub)

def doPairings(danceClub):
    allPairings = danceClub.makeDancePairings()
    timeStamp = str(datetime.datetime.now())
    fileName = "pairings-" + timeStamp + ".txt"
    file = open(fileName, 'w')
    count = 0;
    print("Made " + str(len(allPairings)) + " pairings")
    
    for pairing in allPairings:
        count += 1
        file.write("Matching " + str(count) + " of " + str(len(allPairings)) + "\n")
        for match in pairing:
            line = match.replace('\n', '').replace('\r', '')
            file.write(line + '\n')
            
    file.close()

def doMatching(danceClub):
    ## Make the matches and print them in the console
    danceClub.makeMatches()
    danceClub.printMatches()   
    
    userInput = input("Would you like to send emails at this time? (yes/no): ")
    if userInput.lower() == "yes":
        userInput = input("Are you sure? (yeah, nope): ")
        
        if userInput.lower() == "yeah":
            # Setup the emailer and send out the emails
            mailer = emailer.emailer()
            danceClub.sendEmails(mailer)
            mailer.quitEmail()
            print("Done!")

def main():
    print("""Welcome to Partner Search
    
    This program allows you to run a ballroom dance partner search (or speed-dating, as they are the same thing)
    """)
    
    danceClub = dancerSet.dancerSet()
    
    while True:
        while True:
            try:
                printMainOptions()
                userInput = int(input("Select function (0,1,2,3): "))
                validOptions = [0,1,2,3]
                
                if userInput in validOptions:
                    print("")
                    break
                else:
                    print("Error: invalid function selection.")
        
            except ValueError:
                print("Error: you must enter a valid integer.")
            
        if userInput == 0:
            danceClub = setupDancers()
        elif userInput == 1:
            setupChoices(danceClub)
        elif userInput == 2:
            doPairings(danceClub)
        elif userInput == 3:
            doMatching(danceClub)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit("\nUser keyboard interrupt")
    