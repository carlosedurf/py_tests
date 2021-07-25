from calculator import sum


try:
    print(sum('15', 15))
except AssertionError as e:
    print(f'Conta inválida: {e}')
