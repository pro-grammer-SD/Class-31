from abc import ABC, abstractmethod

class Coding(ABC):
    """docstring for Coding."""
    def __init__(self):
        super(Coding, self).__init__()
        
        #self.name = __class__.__name__
        
    #def intro(self):
        #return self.name+" is fun!"

    @abstractmethod
    def sus(self):
        pass
        
class Python(Coding):
    """docstring for Python."""
    def __init__(self):
        super(Python, self).__init__()
        
        self.name = __class__.__name__
        
    def intro(self):
        return self.name+" is fun!"
        
    def sus(self):
        return "WEE!"
        
#_1 = Coding()
_1 = print(Python().intro())