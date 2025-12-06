# --------------------------------------------------------------
# IN THE NAME OF ALLAH, THE MOST BENEFICENT, THE MOST MERCIFUL
# --------------------------------------------------------------
#                          student.py
# --------------------------------------------------------------

class Student:

    _Count = 0
    
    def __init__(self, name = 'Ali', id = 0, section = 'A'):
        self.name   =   name
        self.id     =   id
        self.section=   section
        
        Student._Count += 1
