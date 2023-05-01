#Test python env
def print_hello():
    animals = ['dog','cat','hamster', 'tiger'] # in one line
    foods = [
            'ramen',
            'pizza',
            'gimbap'
    ] # w/o trailing comma
    names = [
        'john',
        'jane',
        'gil-dong',
        'Dong-eun',
    ] #/ trailing comma
    for f_name in names:
        print(f'hello,  {f_name}')
if __name__ == '__main__':
    print_hello()

