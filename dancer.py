'''
Created on 2013-01-08

@author: Gord
'''

class dancer(object):
    '''
    A class for dancers, to be used in a partner search
    '''


    def __init__(self, name, email, isLead, code):
        self.name = str(name)
        self.email = str(email)
        self.isLead = bool(isLead)
        self.choices = list()
        self.code = code
        self.matches = list()
        self.choices = list()
        self.dancedWith = list()
        self.busy = 0
        
    def setChoices(self, choices):
        self.choices = choices;
    
    ## Adds PARAM to SELFs matches if PARAM is a match
    def match(self, partner):
        ## Adds partner to SELFs matches if there is a match
        if(partner.isLead != self.isLead):
            if(partner.code in self.choices and self.code in partner.choices):
                self.matches.append(partner)
    
    def getFirstName(self):
        names = self.name.split(" ")
        return names[0]
    
    
    def getMatchesString(self):
        ## Returns a dancer's matches with their emails, one match/email per line
        output = str()
        if len(self.matches) == 0:
            return "no matches\n\r"
        else:
            output += "\n\r"
            for i in range(len(self.matches)):
                output += "#" + str(self.matches[i].code) + " "
                output += self.matches[i].toString()
                output += "\n\r"
            return output
    
    
    def getMatchEmails(self):
        ## Returns a list of matches' emails
        output = list()
        for i in range(len(self.matches)):
            output.append(self.matches[i].email)
        return output
    
    def getLeadFollow(self):
        return self.isLead
        
    def toString(self):
        return self.name + " - " + self.email
    
    def toStringNumName(self):
        splitName = self.name.split()
        return str(self.code) + " - " + splitName[0]
    
    def danceWith(self,otherDancer):
        self.dancedWith.append(otherDancer.code)
        
    def hasDancedWith(self, otherDancer):
        ## Returns 1 if they have danced, 0 otherwise
        if otherDancer.code in self.dancedWith:
            return 1;
        else:
            return 0;
        
        