'''
Created on 2014-01-02

@author: Gord
'''

import dancer
import dancerSet

class matchParser(object):

    def __init__(self, choicesFile):
        try: 
            self.file = open(choicesFile, 'r')
        except:
            print('Error opening ' + chociesFile)
        
    def parseChoicesToSet(self, set):
        for line in self.file:
            arr = line.split('|')
            if (len(arr) != 2):
                print("Error: file contains incorrectly formatted line.")
                print(line)
                return
            else:
                code = arr[0]
                choices = list(arr[1])
                set.setChoicesByCode(code, choices)
                print(code + str(choices))
        
        self.file.close()