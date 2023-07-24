# raise Exception('Not supported operation')

def summ(a, b):
    suma = 0
    try:
        assert a == b
        suma = a + b
    except TypeError as e:
        print(e)
    except AssertionError as e:
        print('assertion error')
    else:
        print('else block')
    finally:
        print('final block of code')
    return suma
    print('this is code')


summ(2, 2)
