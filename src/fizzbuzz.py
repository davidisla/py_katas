class fizzbuzz():

    def do(value):
        if (value % 3) == 0:
            return "fizz"

        if (value % 5) == 0:
            return "buzz"

        return str(value)
