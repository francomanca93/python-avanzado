import time

def fibo_gen(max=None):
    n1 = 0
    n2 = 1
    counter = 0
    is_infinite = False
    if max == None or max == '':
        is_infinite = True
        print('Infinite loop')
    else:
        max = int(max)
        print(f'{max} iterations')

    while is_infinite or counter < max:
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else:
            aux = n1 + n2
            n1, n2 = n2, aux
            counter += 1
            yield aux


if __name__ == '__main__':
    max = input('Ingrese el numero de elementos a mostrar: ')
    fibonacci = fibo_gen(max)
    for element in fibonacci:
        print(element)
        time.sleep(1)