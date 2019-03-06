class LemonadeStand(object):
    """
    Represent a lemonade stand that sells lemonade.
    Argument:
    location (string): location of lemonade stand
    Attributes:
    location (string): location of lemonade stand
    profit (float): profit made since opening day
    """

    branch = 0 # total number of lemonade stands

    def __init__(self,location):
        self.location = location
        self.profit = 0
        self.recipe = ['Lemons', 'Water', 'Sugar']
        self.add_branch()

    def __str__(self):
        return f'Lemonade stand at {self.location} ' \
               f'has made ${self.profit:.2f}'

    @classmethod
    def add_branch(cls):
        """
        Update the number of branches.
        """
        cls.branch += 1

    def add_ingredient(self, ingredient):
        """
        Adds an ingredient to the list of ingredients.
        :param ingredient: (string) the ingredient to be added to the recipe
        """
        super().__getattribute__('recipe').append(ingredient)

    def makeSale(self, n = 1):
        """
        Add $2.50 x number of lemonade sold to the profit.
        :param n: number of lemonade sold
        :return:
        """
        self.profit += n * 2.5

    def __le__(self, other):
        return (self.profit <= other.profit)

    def __eq__(self, other):
        return (self.profit == other.profit) and \
               (self.location == other.location)

    def __add__(self, other):
        new_branch = LemonadeStand(self.location + '/' + other.location)
        new_branch.profit = self.profit + other.profit
        return new_branch

    def __getattribute__(self, attr_name):
        value = super().__getattribute__(attr_name)
        if attr_name == 'recipe':
            return 'Secret'
        else:
            return value
