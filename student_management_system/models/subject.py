# --------------------------------------------------------------
# IN THE NAME OF ALLAH, THE MOST BENEFICENT, THE MOST MERCIFUL
# --------------------------------------------------------------
#                          subject.py
# --------------------------------------------------------------

class Subject:

    _Count = 0

    def __init__(self, name, code, credits):
        self.name   =   name
        self.code   =   code
        self.credits=   credits
        
        Subject._Count += 1
