'''
Created on 2013-01-08

@author: Gord
'''

import root.emailer
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
            
    def makeDanceMatches(self):
        ## Not tested
        self.resetBusy()
        random.shuffle(self.leads)
        random.shuffle(self.follows)
        
        ## Crappy O(n^2) algorithm
        for i in range(len(self.leads)):
            for j in range(len(self.follows)):
                if self.leads[i].hasDancedWith(self.follows[j]) == 0 and self.leads[i].busy == 0 and self.follows[j].busy == 0:
                    print(self.leads[i].toStringNumName() + " and " + self.follows[j].toStringNumName())
                    self.leads[i].danceWith(self.follows[j])
                    self.follows[j].danceWith(self.leads[i])
                    self.leads[i].busy = 1
                    self.follows[j].busy = 1
                    break
        ## something to see if you've exhaused your possibilities 
    
    def undoLastDanceMatches(self):
        for i in range(len(self.leads)):
            if len(self.leads[i].dancedWith) != 0:
                self.leads[i].dancedWith.pop()
        
        for j in range(len(self.follows)):
            if len(self.follows[j].dancedWith) != 0:
                self.follows[j].dancedWith.pop()
            
    def setup(self):
        corneliu = root.dancer.dancer("Corneliu ", "cbolbocean@gmail.com", 1, 21, [44,48,34,26,36,30])
        self.addDancer(corneliu)
        micah = root.dancer.dancer("Micah Sienna", "micah.sienna@gmail.com", 1, 23, [])
        self.addDancer(micah)
        wen = root.dancer.dancer("Wen Cheang", "cheangwen@hotmail.com", 1, 25, [20,26,32,36,28,22,34,30,40])
        self.addDancer(wen)
        connor = root.dancer.dancer("Connor Omand", "comand92@hotmail.com", 1, 27, [20,40,44,28,36,22,24])
        self.addDancer(connor)
        kirk = root.dancer.dancer("Kirk Lee", "kirklee@hotmail.com", 1, 29, [])
        self.addDancer(kirk)
        calvin = root.dancer.dancer("Calvin Pin", "calvman_778@hotmail.com", 1, 33, [20,24,48])
        self.addDancer(calvin)
        joseph = root.dancer.dancer("Joseph", "josephparedes1@gmail.com", 1, 35, [28,36,20])
        self.addDancer(joseph)
        jian = root.dancer.dancer("Jian ", "jian_ji1@hotmail.com", 1, 39, [28,34,44,24,40,48])
        self.addDancer(jian)
        albert = root.dancer.dancer("Albert Saravi", "atasaravi@hotmail.com", 1, 41, [34,30,48,22,36,40,28,20,44,26,32])
        self.addDancer(albert)
        
        alex = root.dancer.dancer("Alex Franco", "3afranco@gmail.com", 0, 20, [33])
        self.addDancer(alex)
        isabella = root.dancer.dancer("Isabella Laird", "izzylaird@yahoo.ca", 0, 22, [33,23])
        self.addDancer(isabella)
        jessica = root.dancer.dancer("Jessica Yeung", "jessicaylyeung@gmail.com", 0, 24, [33])
        self.addDancer(jessica)
        jessie = root.dancer.dancer("Jessie Chung", "jessie.cl.chung@gmail.com", 0, 26, [])
        self.addDancer(jessie)
        kristina = root.dancer.dancer("Kristina Richmond", "k+richmond21@hotmail.com", 0, 28, [])
        self.addDancer(kristina)
        gloria = root.dancer.dancer("Gloria ", "gloria_cyb@yahoo.ca", 0, 30, [41,21,39,33])
        self.addDancer(gloria)
        ruth = root.dancer.dancer("Ruth Gu", "542184491@qq.com", 0, 32, [])
        self.addDancer(ruth)
        katherine = root.dancer.dancer("Katherine Crawford", "kathacrawford@gmail.com", 0, 34, [])
        self.addDancer(katherine)
        theresa = root.dancer.dancer("Theresa Mammarella", "mammarellatheresa8@gmail.com", 0, 36, [])
        self.addDancer(theresa)
        angela = root.dancer.dancer("Angela Wang", "angela9wang@gmail.com", 0, 38, [])
        self.addDancer(angela)
        natchar = root.dancer.dancer("Natchar Ratanasirigulchai", "n.ratanasirigulchai@yahoo.com", 0, 40, [])
        self.addDancer(natchar)
        angela2 = root.dancer.dancer("Angela Hu", "angelahu@live.ca", 0, 42, [])
        self.addDancer(angela2)
        judy = root.dancer.dancer("Judy Zhu", "judytvxqyz@gmail.com", 0, 44, [21,39])
        self.addDancer(judy)
        julia = root.dancer.dancer("Julia Wei", "juliawei2009@gmail.com", 0, 48, [])
        self.addDancer(julia)
            