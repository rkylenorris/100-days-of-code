def calculate(n, **kwargs):
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")  # use .get to avoid an error if that argument was not used, it will return none
        # instead of producing an error
        self.model = kw.get("model")


my_car = Car(make="Toyota")

print(my_car.model)
print(my_car.make)
