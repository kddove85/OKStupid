'''
@author: Greg Saxton
@author: Kyle Dove

Purpose: Log in to OKCupid account and cycle through questions.

Modification History:

DATE           Author               Description   
===========    ===============      =============
Aug 10 2014    Kyle Dove            Created
'''

class Question:

    def __init__(self, qtext):
        self.qtext = qtext
        self.answers = []
        
    def addAnswer (self, answer):
        self.answers.append(answer)
        
    def toString(self):
        print(self.qtext)
        print ', '.join(self.answers)