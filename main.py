def read_list():
    lst = []
    n = int(input("Introduceti numarul de elemente din lista"))
    for i in range(n):
        x = int(input("a[{}]=". format(i+1)))
        lst.append(x)
    return lst


def numere_negative(lst):
    '''
    Programul afiseaza numerele negative nenule din lista
    :param lst: lista de numere intregi
    :return: rez ce reprezinta numerele negative nenule din lista
    '''

    rez = []
    for x in lst:
        if x < 0:
            rez.append(x)
    return rez


def test_numere_negative():
    assert numere_negative([7, -16, -13, 9]) == [-16, -13]
    assert numere_negative([17, -1, 3, -9]) == [-1, -9]

test_numere_negative()

def show_menu():
    '''
    Print menu
    :return:
    '''
    print('''
    1. Citirea unei liste de numere întregi.
    2. Afișarea tuturor numerelor negative nenule din listă.
    3. Afișarea celui mai mic număr care are ultima cifră egală cu o cifră citită de la tastatură.
    4. Afișarea tuturor numerelor din listă care sunt superprime.
    5. Afișarea listei obținute din lista inițială în care numerele pozitive și nenule au fost înlocuite cu
       CMMDC-ul lor și numerele negative au cifrele în ordine inversă.
    6. Ieșire.
    ''')


    def main():
        lst = []
        while True:
            show_menu()
            cmd = input("Command: ")
            if cmd == '1':
                lst = read_list()
            elif cmd == '2':
                rez = numere_negative(lst)
                print(rez)
            elif cmd == '3':
                pass
            elif cmd == '4':
                pass
            elif cmd == '5':
                pass
            elif cmd == '6':
                break
            else:
                print("Invalid command")

    main()