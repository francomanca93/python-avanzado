

def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, 'Solo se pueden usar cadenas'
        return string * n
    return repeater

def run():
    repeat_5 = make_repeater_of(5)
    print(repeat_5('hola'))
    repeat_10 = make_repeater_of(10)
    print(repeat_10('Franco'))

# Ejercicio:
def make_division_by(n):
    def division(x):
        assert type(x) == int, 'Solo se pueden usar enteros'
        return int(x / n)
    return division

def run_division():
    division_by_3 = make_division_by(3)
    print(division_by_3(18)) # The expected result is 6
    division_by_5 = make_division_by(5)
    print(division_by_5(100)) # The expected result is 20
    division_by_18 = make_division_by(18)
    print(division_by_18(54)) # The expected result is 3


if __name__ == '__main__':
    run_division()