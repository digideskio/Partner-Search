'''
Created on 2013-01-08

@author: Gord
'''

import dancer
import dancerSet
import emailer
import partnerSearchManager

if __name__ == '__main__':
    
    danceClub = dancerSet.dancerSet()
    
    ## A list of dancers and their choices
    ## and add them to the club
#    jordan = root.dancer.dancer("Jordan Mahar", "maharjordan@gmail.com", 1, 21, [52, 26, 28, 22])
#    danceClub.addDancer(jordan)
#    geoff = root.dancer.dancer("Geoffrey Lau", "caklexcakle_dot_the-grim@hotmail.com", 1, 23, [58,22,36,32,52])
#    danceClub.addDancer(geoff)
#    ryan = root.dancer.dancer("Ryan S", "stratysphere16@gmail.com", 1, 25, [40,38,32,30])
#    danceClub.addDancer(ryan)
#    derek = root.dancer.dancer("Derek Beeket", "darklightshadow@hotmail.com", 1, 110, [])
#    danceClub.addDancer(derek)
#    jake = root.dancer.dancer("Jake Larson", "xfrogmanx@hotmail.com", 1, 29, [36, 32])
#    danceClub.addDancer(jake)
#    joshua = root.dancer.dancer("Joshua Cheng", "jcheng94@interchange.ubc.ca", 1, 35, [])
#    danceClub.addDancer(joshua)
#    wen = root.dancer.dancer("Wen Cheang", "cheangwen@hotmail.com", 1, 41, [22,24,26,30,52,50,58,34])
#    danceClub.addDancer(wen)
#    mehrdad = root.dancer.dancer("Mehrdad Chapariha", "mehrdad@nobeno.com", 1, 39, [20,24,54,58])
#    danceClub.addDancer(mehrdad)
#    anthony = root.dancer.dancer("Anthony Tam", "anthonytam@shaw.ca", 1, 53, [34,64,48,40,32])
#    danceClub.addDancer(anthony)
#    robert = root.dancer.dancer("Robert Oleksiew", "robert_oleksiew@gmail.com", 1, 107, []) ## no info
#    danceClub.addDancer(robert)
#    benj = root.dancer.dancer("Benj Israel", "benj@alumni.ubc.ca", 1, 57, [26,32,40,48,36,22,30,64,58,50,28])
#    danceClub.addDancer(benj)
#    lawrence = root.dancer.dancer("Lawrence Tse", "lt@alumni.sfu.ca", 1, 106, [])
#    danceClub.addDancer(lawrence)
#    charles = root.dancer.dancer("Charles To", "charlesfto@gmail.com", 1, 27, [50,34,22,52])
#    danceClub.addDancer(charles)
#    cheklon = root.dancer.dancer("Cheklon Liu", "cheklon@gmail.com", 1, 75, [34,24])
#    danceClub.addDancer(cheklon)
#    jullen = root.dancer.dancer("Jullen Fung", "fonglong@gmail.com", 1, 104, []) ## no info
#    danceClub.addDancer(jullen)
#    foster = root.dancer.dancer("Foster Tom", "foster-tom@hotmail.com", 1, 42, [32,50,64,52]) 
#    danceClub.addDancer(foster)
#    
#    tania = root.dancer.dancer("Tania", "kortd1203@learning.fraseric.ca", 0, 20, [35,23,37,77]) 
#    danceClub.addDancer(tania)
#    jessie = root.dancer.dancer("Jessie Chung", "jessie.cl.chung@gmail.com", 0, 22, [37,35,33,57,27])
#    danceClub.addDancer(jessie)
#    kristina = root.dancer.dancer("Kristina Richmond", "k_richmond21@hotmail.com", 0, 24, [55, 75, 25, 77])
#    danceClub.addDancer(kristina)
#    fangwen = root.dancer.dancer("Fangewen Zhao", "fangwen92@yahoo.com", 0, 28, [29,33,57])
#    danceClub.addDancer(fangwen)
#    kai = root.dancer.dancer("Kai Di Chen", "kdchen115@gmail.com", 0, 26, [53,47,29,75,89,77])
#    danceClub.addDancer(kai)
#    shoshana = root.dancer.dancer("Shoshana Hereld", "sj.roses@gmail.com", 0, 30, [55, 37, 77, 57, 25])
#    danceClub.addDancer(shoshana)
#    melody = root.dancer.dancer("Melody Yu", "mussamelon@gmail.com", 0, 32, [29, 23, 47])
#    danceClub.addDancer(melody)
#    melinda = root.dancer.dancer("Melinda Yu", "mel.inda017@gmail.com", 0, 34, [75,29])
#    danceClub.addDancer(melinda)
#    elizabeth = root.dancer.dancer("Elizabeth Sun", "onefiftythree@gmail.com", 0, 36, [55,37,53])
#    danceClub.addDancer(elizabeth)
#    amy = root.dancer.dancer("Amy Yang", "amyyxyang@hotmail.com", 0, 40, [57,75,37,25,55])
#    danceClub.addDancer(amy)
#    angel = root.dancer.dancer("Angel Yang", "star_gazerglory@hotmail.com", 0, 48, [89, 39, 57, 53])
#    danceClub.addDancer(angel)
#    amber = root.dancer.dancer("Amber Rae", "ambee4@hotmail.com", 0, 52, [27,29,77,37,23,39])
#    danceClub.addDancer(amber)
#    cindy = root.dancer.dancer("Cindy Ngan", "cindy.ngan@alumni.ubc.ca", 0, 101, []) ## no info
#    danceClub.addDancer(cindy)
#    sun = root.dancer.dancer("Sun Nee Tan", "tansunnee@gmail.com", 0, 58, [23,29,89,39,57]) 
#    danceClub.addDancer(sun)
#    sicen = root.dancer.dancer("Sicen Lu", "lusicen@hotmail.com", 0, 64, [53])
#    danceClub.addDancer(sicen)
    
    danceClub.setup()
    ## Make the matches and print them in the console
    danceClub.makeMatches()
    danceClub.printMatches()

    
        
    # Setup the emailer and send out the emails
    mailer = emailer.emailer()
    danceClub.sendEmails(mailer)
    mailer.quitEmail()
    print("Done!")
    