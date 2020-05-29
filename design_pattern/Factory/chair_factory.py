from abc import ABCMeta, abstractstaticmethod

class IChair(metaclass=ABCMeta):

    @abstractstaticmethod
    def get_dimesions():
        """Chair Interface"""


class bigChair(IChair):
    def __init__(self):
        self.height = 80
        self.width = 80
        self.depth = 80

    def get_dimesions(self):
        return {"height": self.height, "width": self.width, "depth": self.width}

class MediumChair(IChair):
    def __init__(self):
        self.height = 70
        self.width = 70
        self.depth = 70

    def get_dimesions(self):
        return {"height": self.height, "width": self.width, "depth": self.width}

class SmallChair(IChair):
    def __init__(self):
        self.height = 60
        self.width = 60
        self.depth = 60

    def get_dimesions(self):
        return {"height": self.height, "width": self.width, "depth": self.width}



class ChairFactory():
    
    @staticmethod
    def get_chair(chairtype):
        try:
            if chairtype == "BigChair":
                return bigChair()
            if chairtype == "MediumChair":
                return MediumChair()
            if chairtype == "SmallChair":
                return SmallChair()
            raise AssertionError("Chair not found")
        except AssertionError as _e:
            print(_e)


if __name__=="__main__":
    CHAIR = ChairFactory.get_chair("BigChair")
    print(CHAIR.get_dimesions())
    CHAIR = ChairFactory.get_chair("MediumChair")
    print(CHAIR.get_dimesions())
    CHAIR = ChairFactory.get_chair("SmallChair")
    print(CHAIR.get_dimesions())