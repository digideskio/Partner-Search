'''
Created on 2013-01-08

@author: Gord
'''

import emailer
import random

class dancerSet(object):
    '''
    A set of dancers, split into partners and leads
    For use in a partner search
    '''
   
    def __init__(self):
        self.leads = list()
        self.follows = list()
        self.matchesMade = 0
        self.iterationCursor = 0
        
    
    
    def addDancer(self, dancer):
        ## Adds a dancer to the appropriate list
        if(dancer.isLead):
            self.leads.append(dancer)
        else:
            self.follows.append(dancer)
            
    def removeDancer(self, code):
        for i in range(len(self.leads)):
            if self.leads[i].code == code:
                self.leads.pop(i)
                break
        
        for j in range(len(self.follows)):
            if self.follows[j].code == code:
                self.follows.pop(j)
                break
                
    def setChoicesByCode(self, code, choices):
        for lead in leads:
            if (code == lead.code):
                lead.setChoices(choices)
                return
        
        for follow in follows:
            if (code == follow.code):
                follow.setChoices(choices)
                return
    
    
    def sendEmails(self, mailer):
        ## Sends match emails to everyone in the set
        if(self.matchesMade == 1):
            for i in range(len(self.leads)):
                mailer.sendEmail(self.leads[i])
            for j in range(len(self.leads)):
                mailer.sendEmail(self.follows[j])
            
    
    def makeMatches(self):
        ## Generates matches for everyone in the set
        for i in range(len(self.leads)):
            for j in range(len(self.follows)):
                self.leads[i].match(self.follows[j])
                self.follows[j].match(self.leads[i])
        self.matchesMade = 1
    
    
    def printMatches(self):
        ## Prints everyone's matches out in the console
        if self.matchesMade == 1:
            for i in range(len(self.leads)):
                output = self.leads[i].toString()
                output += ": "
                output += "\n"
                output += self.leads[i].getMatchesString()
                print(output)
            
            print() ## newline
            
            for j in range(len(self.follows)):
                output = self.follows[j].toString()
                output += ": "
                output += self.follows[j].getMatchesString()
                print(output)
        else:
            print("Matches not made\n")
    
    def printLeads(self):
        for i in range(len(self.leads)):
            print(self.leads[i].toString())
            
    def printFollows(self):
        for i in range(len(self.follows)):
            print(self.follows[i].toString())
    
    def resetBusy(self):
        for i in range(len(self.leads)):
            self.leads[i].busy = 0
        for j in range(len(self.follows)):
            self.follows[j].busy = 0
            
    def makeDancePairings(self):
        ## Not tested
        random.shuffle(self.leads)
        random.shuffle(self.follows)
        
        ## alg idea. Create all matchings first with progressive offset
        ## then shuffle the order
        
        bigGroup = len(self.leads) > len(self.follows) ? self.leads : self.follows
        smallGroup = bigGroup == self.leads ? self.follows : self.leads 
        allPairings = list()
        
        for offset in range(max(len(self.leads), len(self.follows)):      
            pairing = list()
            
            for i in range(len(smallGroup)):
                i = (i + offset) % len(smallGroup)
                
                for j in range(len(bigGroup)):
                    if smallGroup[i].hasDancedWith(bigGroup[j]):
                        match = smallGroup[i].toStringNumName() + " and " + bigGroup[j].toStringNumName()
                        pairing.append(match)
                        smallGroup[i].danceWith(bigGroup[j])
                        bigGroup[j].danceWith(smallGroup[i])
                        break        
                        
            allPairings.append(pairings)
            
        return random.shuffle(allPairings)
        
    def undoLastDanceMatches(self):
        for i in range(len(self.leads)):
            if len(self.leads[i].dancedWith) != 0:
                self.leads[i].dancedWith.pop()
        
        for j in range(len(self.follows)):
            if len(self.follows[j].dancedWith) != 0:
                self.follows[j].dancedWith.pop()
            
    def setup(self):
        ## previously added dancers here
        print("Did nothing.")