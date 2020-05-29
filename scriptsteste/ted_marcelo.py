#andre luis moreira da silva santos


#ex1: nao carrega dois arquivos independentes
nome = str(input("Digite seu nome completo: ")).title().strip()
print("Seu nome tem Silva?", "Silva" in nome)



#ex2: nao carrega dois arquivos independentes
nome = str(input("Digite seu nome completo: ")).title().strip()
sepnome = nome.split()
print("O seu primeiro nome é {}".format(sepnome[0]))
print("O seu ultimo nome é {}.".format(sepnome[len(sepnome)-1]))