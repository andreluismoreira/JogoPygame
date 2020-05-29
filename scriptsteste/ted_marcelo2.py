nome = str(input("Digite seu nome completo: ")).title().strip()
sepnome = nome.split()
print("O seu primeiro nome é {}".format(sepnome[0]))
print("O seu ultimo nome é {}.".format(sepnome[len(sepnome)-1]))