
operator = input('Podaj jakie działanie chcesz wykonać: ( + , - , * , / ): ')

if operator not in ['+','-','*', '/']:
    print('Wprowadziłeś nieprawidłowy znak')

else:

    num_1 = float(input('Podaj pierwszą liczbę: '))
    num_2 = float(input('Podaj drugą liczbę: '))


    if operator == '+':
        rezultat = num_1 + num_2

    elif operator == '-':
        rezultat = num_1 - num_2

    elif operator == '*':
        rezultat = num_1 * num_2

    elif operator == '/':
        if num_2 == 0:
            print('Nie wolno dzielić przez zero')
            exit()
            
        else:
            rezultat = num_1 / num_2



    if rezultat.is_integer():
        print(f'Wynik twojego dzialania to: {int(rezultat)}')
    else:
        print(f'Wynik twojego dzialania to: {rezultat}')