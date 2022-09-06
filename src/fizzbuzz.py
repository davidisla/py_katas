class fizzbuzz():

    @classmethod
    def do(cls, value):
        if cls.isMultipleOf(value, 3):
            return "fizz"

        if cls.isMultipleOf(value, 5):
            return "buzz"

        return str(value)

    @classmethod
    def isMultipleOf(cls, value, module):
        if (value % module) == 0:
            return True
