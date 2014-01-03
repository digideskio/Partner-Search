'''
Created on 2014-01-02

@author: Gord
'''

import dancer
import dancerSet

class dancerParser(object):

    def __init__(self, dancersFile):
        self.file = open(dancersFile, 'r')
        
    def parseToDancerSet(self):
        # name|email|lead/follow|code
        set = dancerSet.dancerSet()
        
        for line in self.file:
            arr = line.split("|")
            if (len(arr) != 4):
                print("Error: file contains incorrectly formatted line.")
                print(line)
                return
            else:
                name = arr[0]
                email = arr[1]
                isLead = arr[2].lower() == "lead"
                code = arr[3]
                
                dancer = dancer.dancer(name, email, isLead, code)
                set.addDancer(dancer)
        
        self.file.close()        
        return set
        