email = input('Podaj swój email: ')

index = email.index('@')

user = email[:index]
domena = email[index + 1:]

print(f'Twoja nazwa konta to : {user}, a domena to: {domena}')