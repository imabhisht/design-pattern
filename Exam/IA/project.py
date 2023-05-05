from cheif import Chief

#Implementations of Factory - 1
class Italian(Chief):
    #onverrideFunction
    def cook(self, dishName):
        print("[Food Factory]: (Italian Cooking) " + dishName)
        pass


class American(Chief):
    #onverrideFunction
    def cook(self, dishName):
        print("[Food Factory]: (American Cooking) " + dishName)
        pass


class European(Chief):
    #onverrideFunction
    def cook(self, dishName):
        print("[Food Factory]: (European Cooking) " + dishName)
        pass


class WesternFoodFactory:
    # dishes = [{
    #         "name": "Italian",
    #         "fun": Italian()
    #     },{
    #         "name": "American",
    #         "fun": American()
    #     },{
    #         "name": "European",
    #         "fun": European()
    #     }]
    def __init__(self):
        self.dishes = [{
            "name": "Italian",
            "fun": Italian()
        },{
            "name": "American",
            "fun": American()
        },{
            "name": "European",
            "fun": European()
        }]

    @staticmethod
    def get_food_factory(type, dishes):
        for dish in dishes:
            if dish["name"] == type:
                return dish['fun']



#Implementations of Factory - 2

class SouthIndian(Chief):
    #onverrideFunction
    def cook(self, dishName):
        print("[Food Factory]: (South Indian Cooking) " + dishName)
        pass

class NorthIndian(Chief):
    #onverrideFunction
    def cook(self, dishName):
        print("[Food Factory]: (North Indian Cooking) " + dishName)
        pass


class Gujarati(Chief):
    #onverrideFunction
    def cook(self, dishName):
        print("[Food Factory]: (Gujarati Cooking) " + dishName)
        pass

class IndianFoodFactory:

    def __init__(self):
        self.dishes = [{
            "name": "South Indian",
            "fun": SouthIndian()
        },{
            "name": "North Indian",
            "fun": NorthIndian()
        },{
            "name": "Gujarati",
            "fun": Gujarati()
        }]

    @staticmethod
    def get_food_factory(type, dishes):
        for dish in dishes:
            if dish["name"] == type:
                return dish['fun']
        raise Exception("Invalid Food Factory Type")


#Implementations of Factory - 3

class Chinese(Chief):
    #onverrideFunction
    def cook(self, dishName):
        print("[Food Factory]: (Chinese Cooking) " + dishName)
        pass

class Japanese(Chief):
    #onverrideFunction
    def cook(self, dishName):
        print("[Food Factory]: (Japanese Cooking) " + dishName)
        pass

class Korean(Chief):
    #onverrideFunction
    def cook(self, dishName):
        print("[Food Factory]: (Korean Cooking) " + dishName)
        pass

class AsianFoodFactory:
    def __init__(self):
        self.dishes = [{
            "name": "Chinese",
            "fun": Chinese()
        },{
            "name": "Japanese",
            "fun": Japanese()
        },{
            "name": "Korean",
            "fun": Korean()
        }]

    @staticmethod
    def get_food_factory(type, dishes):
        for dish in dishes:
            if dish.name == type:
                return dish['fun']

        raise Exception("Invalid Food Factory Type")

        















