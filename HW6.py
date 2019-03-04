class LemonadeStand:

    """
    Represent a dealership that sells cars.
    Argument:
    location (string): location of lemonade stand
    Attributes:
    location (string): location of  lemonade stand
    profit (float): profit made since opening day
    """

    recipe = ['Lemons','Water','Sugar'] # class variable

    def __init__(self,location):
        self.location = location
        self.profit = 0
    def __str__(self):
        return "Lemonade stand at " + self.location + \
               " has made $" + self.profit

    @classmethod
    def add_ingredient(cls,ingredient):
        """
        Adds an ingredient to the list of ingredients.
        :param ingredient: (string) the ingredient to be added to the recipe
        """
        cls.recipe.append(ingredient)

    def makeSale(self):
        """
        Adds $1.50 to the profit to mark a sale
        """
        self.profit += 1.5

    def __le__(self, other):
        return (self.profit <=other.profit)
    def __eq__(self, other):
        return (self.profit == other.profit) and (self.location == other.location)
    def __add__(self, other):
        return self.profit + other.profit
    def __getattribute__(self, item):
        return super().__getattribute__(item)