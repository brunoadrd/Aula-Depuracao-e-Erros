x = [1, 2, 3]
y = 1

try:
    x + y
except Exception as e:
    print("Erro: {}.".format(e))
finally:
    print("Sempre executar.")