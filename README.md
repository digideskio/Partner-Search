Partner-Search
==============
A set of scripts for use in a partner search. Created for use by UBC Dance Club.

Use
==============
NOTE: Angle brackets (<>) indicate somewhere a value should go, you don't want them in the end command. Quotation marks MUST stay.
NOTE: everything is case sensitive.

To add a dancer:
<firstname> = root.dancer.dancer("<full name>", "<email>", <1 for a lead, 0 for a follow>, <number>, [])
danceClub.addDancer(<firstname>)

ex.
jordan = root.dancer.dancer("Jordan Mahar", "maharjordan@gmail.com", 1, 21, [])
danceClub.addDancer(jordan)


To remove a dancer:
danceClub.removeDancer(<code of dancer to remove>)

To make dance matches:
danceClub.makeDanceMatches()

To undo the last set of dance matches you made:
danceClub.undoLastDanceMatches()


To start things up JUST IN CASE
if it isn't opened, open git bash or command prompt in C:\Users\Gord\PartnerSearch
in git bash, enter the following command:
python
then enter the followin commands:
import root
danceClub = root.dancerSet.dancerSet()
danceClub.setup()