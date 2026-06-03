import json
#classe pessoa---------------------------------

class Pessoa:
    def __init__(self, nome, idade, email):

        self.nome = nome
        self.idade = idade
        self.email = email        

#classe aluno----------------------------------

class Alunos(Pessoa):
    def __init__(self, nome, idade, email, nota1, nota2, nota3):
        super().__init__(nome, idade, email)

        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

#metodo calcular media

    def calcular_media(self):

        return (self.nota1 + self.nota2 + self.nota3) / 3
    
#metodo situação

    def situacao_aluno(self):

        media = self.calcular_media()

        if media >= 7:
            return 'Aprovado'
        elif media >= 5:
            return 'Recuperação'
        else:
            return 'Reprovado'
        
#metodo alterar nota

    def alterar_nota(self, n1, n2, n3):

        self.nota1 = n1
        self.nota2 = n2
        self.nota3 = n3
        
#metodo to dict

    def to_dict(self):
        return {

            'nome': self.nome,
            'idade': self.idade,
            'email': self.email,
            'nota1': self.nota1,
            'nota2': self.nota2,
            'nota3': self.nota3

        }

#classe professor-------------------------------

class Professor(Pessoa):
    def __init__(self, nome, idade, email, disciplina, salario):
        super().__init__(nome, idade, email)

        self.disciplina = disciplina
        self.salario = salario

#metodo to dict

    def to_dict(self):
        return {

            'nome': self.nome,
            'idade': self.idade,
            'email': self.email,
            'disciplina': self.disciplina,
            'salario': self.salario

        }

    
#carregar alunos--------------------------------

def carregar_alunos():
    
    try:
        with open("alunos.json", "r") as arquivo:
            dados = json.load(arquivo)
            lista = []
            for item in dados:
                alunos = Alunos(item['nome'], item['idade'], item['email'], item['nota1'], item['nota2'], item['nota3'])
                lista.append(alunos) 
            return lista

    except FileNotFoundError:
        return []       
    
#salvar alunos-----------------------------------

def salvar_alunos(lista_objeto):

    dados = [obj.to_dict() for obj in lista_objeto]
    with open("alunos.json", "w") as arquivo:
        json.dump(dados, arquivo, indent=4)

#carregar professor-------------------------------

def carregar_professor():

    try:
        with open("professor.json", "r") as arquivo:
            dados = json.load(arquivo)
            lista = []
            for item in dados:
                professor = Professor(item['nome'], item['idade'], item['email'], item['disciplina'], item['salario'])
                lista.append(professor)
            return lista
    
    except FileNotFoundError:
        return []

#salvar professor---------------------------------

def salvar_professor(lista_objeto):

    dados = [obj.to_dict() for obj in lista_objeto]
    with open("professor.json", "w") as arquivo:
        json.dump(dados, arquivo, indent=4)

#validar------------------------------------------

def validar_nome(nome):
    #nome
    if not nome.strip():
        return 'Campo nome vazio'
    
    if not nome.replace(" ","").isalpha():
        return 'Apenas letras'
    
    return 'ok'

def validar_email(email):    
    #email
    if "@" not in email or ".com" not in email:
        return 'Email invalido'
    
    return 'ok'
    
def validar_idade(idade):
    #idade
    if not idade.isdigit():
        return 'Apenas numeros'
    
    if len(idade) > 3:
        return 'Idade invalida'    
    
    return 'ok'

def validar_disciplina(disciplina):
    #disciplina
    if not disciplina.strip():
        return 'Campo disciplina vazio'
    
    if not disciplina.replace(" ","").isalpha():
        return 'Apenas letras'
    
    return 'ok'
    
    #validações alteração-------------------------

def validar_novo_nome(novo_nome):
    #novo_nome
    if not novo_nome.strip():
        return 'Campo nome vazio'
    
    if not novo_nome.replace(" ","").isalpha():
        return 'Apenas letras'
    
    return 'ok'
    
def validar_novo_email(novo_email):
    #novo_email
    if "@" not in novo_email or ".com" not in novo_email:
        return 'Email invalido'
    
    return 'ok'

def validar_nova_idade(nova_idade):
    #nova_idade
    if not nova_idade.isdigit():
        return 'Apenas numeros'
    
    if len(nova_idade) > 3:
        return 'Idade invalida'   
    
    return 'ok'

def validar_nova_disciplina(nova_disciplina):    
    #nova_disciplina
    if not nova_disciplina.strip():
        return 'Campo disciplina vazio'
    
    if not nova_disciplina.replace(" ","").isalpha():
        return 'Apenas letras'

    return 'ok'

#menu----------------------------------------------

while True:
    print("-------Sistema escolar (herança)------")
    print("1 - Cadastro")
    print("2 - Buscar")    
    print("3 - Remover")
    print("4 - Alterar dados")
    print("5 - Sair")

    opcao = input("Digite sua escolha: ")
    if opcao not in ["1", "2", "3", "4", "5"]:
        print("Digite uma opção valida")
        continue

#cadastro-------------------------------------------

    if opcao == "1":
        print("----Cadastro----\n")

        print("1 - Professor")
        print("2 - Aluno")
        print("3 - Volta")

        opcao = input("Digite sua escolha: ")
        if opcao not in ["1", "2", "3"]:
            print("Digite uma opção valida")
            continue

        #cadastro professor--------------------------------------
        if opcao == "1":
            print("----Cadastro de professor----\n")

            nome = input("Digite seu nome: ").lower()
            #validar nome--------------------------
            validar = validar_nome(nome)
            if validar != "ok":
                print(validar)
                continue

            idade = input("Digite sua idade: ")
            #validar idade------------------------
            validar = validar_idade(idade)
            if validar != "ok":
                print(validar)                
                continue
            idade = int(idade)

            email = input("Digite seu email: ")
            #validar email-------------------------
            validar = validar_email(email)
            if validar != "ok":
                print(validar)
                continue

            disciplina = input("Digite sua diciplina: ").lower()
            #validar disciplina--------------------
            validar = validar_disciplina(disciplina)
            if validar != "ok":
                print(validar)
                continue
            try:
                salario = float(input("Digite seu salario R$: "))
            except ValueError:
                print("Apenas numeros")

            lista = carregar_professor()

            professor = Professor(nome, idade, email, disciplina, salario)

            lista.append(professor)
            salvar_professor(lista)

            print("Professor cadastrado")
        
        #cadastro aluno-------------------------------------------
        elif opcao == "2":
            print("----Cadastro aluno----\n")

            nome = input("Digite seu nome: ").lower()
            #validar nome--------------------------
            validar = validar_nome(nome)
            if validar != "ok":
                print(validar)
                continue

            idade = input("Digite sua idade: ")
            #validar idade------------------------
            validar = validar_idade(idade)
            if validar != "ok":
                print(validar)
                continue
            idade = int(idade)

            email = input("Digite seu email: ")
            #validar email-------------------------
            validar = validar_email(email)
            if validar != "ok":
                print(validar)
                continue

            try:       
                nota1 = float(input("Digite sua primeira nota: "))
                if nota1 < 0 or nota1 > 10:
                    print("Nota invalida")
            except ValueError:
                print("Apenas numeros")

            try:
                nota2 = float(input("Digite sua segunda nota: "))
                if nota2 < 0 or nota2 > 10:
                    print("Nota invalida")
            except ValueError:
                print("Apenas numeros")

            try:
                nota3 = float(input("Digite sua terceira nota: "))
                if nota3 < 0 or nota3 > 10:
                    print("Nota invalida")
            except ValueError:
                print("Apenas numeros")

            lista = carregar_alunos()

            alunos = Alunos(nome, idade, email, nota1, nota2, nota3)

            lista.append(alunos)
            salvar_alunos(lista)

            print("Aluno cadastrado")

        elif opcao == "3":
            continue

#listar------------------------------------------------------------

    elif opcao == "2":
        print("----Busca---\n")

        print("1 - Alunos")
        print("2 - Professores")
        print("3 - Todos")
        print("4 - Voltar")

        opcao = input("Digite sua escolha: ")
        if opcao not in ["1", "2", "3", "4"]:
            print("Digite uma opção valida")
            continue

        #buscar alunos-----------------------------
        if opcao == "1":
            print("----Busca alunos---\n")

            print("1 - Todos os alunos")
            print("2 - Buscar por aluno")
            print("3 - Voltar")

            opcao = input("Digite sua escolha: ")
            if opcao not in ["1", "2", "3"]:
                print("Digite uma opção valida")
                continue

            #buscar todos alunos-------------------
            if opcao == "1":

                lista = carregar_alunos()

                if not lista:
                    print("Lista de alunos vazia")
                else:
                    for aluno in lista:
                        print(f"Nome: {aluno.nome} - Idade: {aluno.idade} - Email: {aluno.email} - Nota: {aluno.nota1} - Nota: {aluno.nota2} - Nota: {aluno.nota3} - Media: {aluno.calcular_media()} - Situação: {aluno.situacao_aluno()}")

            #buscar por nome------------------------
            elif opcao == "2":

                lista = carregar_alunos()
                encontrou = False

                nome = input("Digite o nome do aluno: ").lower()
                #validar nome--------------------------
                validar = validar_nome(nome)
                if validar != "ok":
                    print(validar)
                    continue

                for aluno in lista:
                    if aluno.nome == nome:
                        encontrou = True
                        print(f"Nome: {aluno.nome} - Idade: {aluno.idade} - Email: {aluno.email} - Nota: {aluno.nota1} - Nota: {aluno.nota2} - Nota: {aluno.nota3} - Media: {aluno.calcular_media()} - Situação: {aluno.situacao_aluno()}")
             
                if not encontrou:
                    print("Aluno não cadastrado")

            #voltar----------------------------------
            elif opcao == "3":
                continue

        #buscar professor-----------------------------------------
        elif opcao == "2":
            print("----Busca professores---\n")

            print("1 - Todos os Professores")
            print("2 - Buscar por Professor")
            print("3 - Voltar")

            opcao = input("Digite sua escolha: ")
            if opcao not in ["1", "2", "3"]:
                print("Digite uma opção valida")
                continue

            #buscar todos Professor-------------------
            if opcao == "1":

                lista = carregar_professor()

                if not lista:
                    print("Lista de professores vazia")
                else:
                    for professor in lista:
                        print(f"Nome: {professor.nome} - Idade: {professor.idade} - Email: {professor.email} - Didsciplina: {professor.disciplina} - Salario: {professor.salario}")

            #buscar por nome------------------------
            elif opcao == "2":

                lista = carregar_professor()
                encontrou = False

                nome = input("Digite o nome do professor: ").lower()
                #validar nome--------------------------
                validar = validar_nome(nome)
                if validar != "ok":
                    print(validar)
                    continue

                for professor in lista:
                    if professor.nome == nome:
                        encontrou = True
                        print(f"Nome: {professor.nome} - Idade: {professor.idade} - Email: {professor.email} - Didsciplina: {professor.disciplina} - Salario: {professor.salario}")
             
                if not encontrou:
                    print("Professor não cadastrado")

            #voltar----------------------------------
            elif opcao == "3":
                continue

        #buscar todos--------------------------------
        elif opcao == "3":

            lista_professor = carregar_professor()
            lista_aluno = carregar_alunos()

            if not lista_professor and not lista_aluno:
                print("Lista vazia")
            else:
                for professor in lista_professor:
                    print("\nProfessores----------")
                    print(f"Professor: {professor.nome} - Idade: {professor.idade} - Email: {professor.email}")
                
                for aluno in lista_aluno:
                    print("\nAlunos----------------")
                    print(f"Aluno: {aluno.nome} - Idade: {aluno.idade} - Email: {aluno.email}")

        #voltar----------------------------------------
        elif opcao == "4":
            continue

#remover----------------------------------------------------------
        
    elif opcao =="3":
        print("\n----Remover----")

        print("1 - Remover professor")
        print("2 - Remover aluno")
        print("3 - Voltar")

        opcao = input("Digite sua escolha: ")
        if opcao not in ["1", "2", "3"]:
            print("Digite uma opção valida")
            continue

        #remover professor----------------------
        if opcao == "1":

            lista = carregar_professor()
            encontrou = False

            nome = input("Digite o nome do professor: ").lower()
            #validar nome--------------------------
            validar = validar_nome(nome)
            if validar != "ok":
                print(validar)
                continue

            for professor in lista:
                if professor.nome == nome:
                    encontrou = True
                    print(f"Professor: {professor.nome} - Idade: {professor.idade} - Email: {professor.email}")

                    confirmar = input("Realmente deseja remover este professor? (s/n): ").lower()

                    if confirmar == "s":
                        lista.remove(professor)
                        salvar_professor(lista)

                        print("Professor removido")
                        break
                    else:
                        print("Remover professor cancelado")

            if not encontrou:
                print("Professor não cadastrado")
        
        #remover aluno----------------------------
        elif opcao == "2":

            lista = carregar_alunos()
            encontrou = False
            nome = input("Digite o nome do aluno: ").lower()
            #validar nome--------------------------
            validar = validar_nome(nome)
            if validar != "ok":
                print(validar)
                continue

            for aluno in lista:
                if aluno.nome == nome:
                    encontrou = True                    
                    print(f"Aluno: {aluno.nome} - Idade: {aluno.idade} - Email: {aluno.email}")

                    confirmar = input("Realmente deseja remover este aluno? (s/n): ").lower()

                    if confirmar == "s":
                        lista.remove(aluno)
                        salvar_alunos(lista)

                        print("Aluno removido")
                        break
                    else:
                        print("Remover aluno cancelado")

            if not encontrou:
                print("Aluno não cadastrado")

#alterar dados---------------------------------------

    elif opcao == "4":

        print("\n-----Alterar dados-----")
        print("1 - Alterar dados professor")
        print("2 - Alterar dados aluno")
        print("3 - Voltar")

        opcao = input("Digite sua escolha: ")
        if opcao not in ["1", "2", "3"]:
            print("Digite uma opção valida")
            continue

        #alterar professor------------------------
        if opcao == "1":
            encontrou = False
            lista = carregar_professor()

            nome = input("Digite o nome do professor: ").lower()
            #validar nome--------------------------
            validar = validar_nome(nome)
            if validar != "ok":
                print(validar)
                continue

            for professor in lista:
                if professor.nome == nome:
                    encontrou = True
                    print(f"Nome: {professor.nome} - Idade: {professor.idade} - Email: {professor.email} - Didsciplina: {professor.disciplina} - Salario: {professor.salario}")
                    confirmar = input("Realmente deseja alterar informações do professor? (s/n): ").lower()

                    if confirmar == "s":
                        while True:
                            print("1 - Nome")
                            print("2 - Idade")
                            print("3 - Email")
                            print("4 - Disciplina")
                            print("5 - Salario")
                            print("6 - Voltar")

                            opcao = input("O que gostaria de alterar: ")
                            if opcao not in ["1", "2", "3", "4", "5", "6"]:
                                print("Digite uma opção valida")
                                continue
                            #alterar nome 
                            if opcao == "1":
                                alterar = input("Realmente gostaria de alterar o nome? (s/n): ").lower()

                                if alterar == "s":
                                    novo_nome = input("Digite o novo nome: ").lower()
                                    #validar nome----------------------------
                                    validar = validar_novo_nome(novo_nome)
                                    if validar != "ok":
                                        print(validar)
                                        continue

                                    professor.nome = novo_nome
                                    salvar_professor(lista)
                                    print("Nome alterado")
                                    break
                                else:
                                    print("Alterar nome cancelado")
                                    break
                            
                            #alterar idade
                            elif opcao == "2":
                                alterar = input("Realmente gostaria de alterar sua idade? (s/n): ").lower()

                                if alterar == "s":
                                    nova_idade = input("Digite sua nova idade: ")
                                    #validar idade------------------------
                                    validar = validar_nova_idade(nova_idade)
                                    if validar != "ok":
                                        print(validar)
                                        continue
                                    nova_idade = int(nova_idade)

                                    professor.idade = nova_idade
                                    salvar_professor(lista)
                                    print("Idade alterada")
                                    break
                                else:
                                    print("Alterar idade cancelada")
                                    break

                            #alterar email 
                            elif opcao == "3":
                                alterar = input("Realmente gostaria de alterar seu email? (s/n): ").lower()

                                if alterar == "s":
                                    novo_email = input("Digite seu novo email: ")
                                    #validar email-------------------------
                                    validar = validar_novo_email(novo_email)
                                    if validar != "ok":
                                        print(validar)
                                        continue

                                    professor.email = novo_email
                                    salvar_professor(lista)
                                    print("Email alterado")
                                    break
                                else:
                                    print("Alterar email cancelado")
                                    break

                            #alterar disciplina
                            elif opcao == "4":
                                alterar = input("Realmente gostaria de alterar sua disciplina? (s/n): ").lower()

                                if alterar == "s":
                                    nova_disciplina = input("Digite sua nova disciplina: ").lower()
                                    #validar disciplina--------------------
                                    validar = validar_nova_disciplina(nova_disciplina)
                                    if validar != "ok":
                                        print(validar)
                                        continue

                                    professor.disciplina = nova_disciplina
                                    salvar_professor(lista)
                                    print("Disciplina alterado")
                                    break
                                else:
                                    print("Alterar disciplina cancelado")
                                    break

                            #alterar salario
                            elif opcao == "5":
                                alterar = input("Realmente gostaria de alterar seu salario? (s/n): ").lower()

                                if alterar == "s":
                                    try:
                                        novo_salario = float(input("Digite seu novo salario R$: "))
                                    except ValueError:
                                        print("Apenas numeros")

                                    professor.salario = novo_salario
                                    salvar_professor(lista)
                                    print("Salario alterado")
                                    break
                                else:
                                    print("Alterar salario cancelado")
                                    break
                            
                            #voltar
                            elif opcao == "6":
                                continue
                
                if not encontrou:
                    print("Professor não cadastrado")

        #alterar aluno----------------------------------------------------------------

        elif opcao == "2":

            lista = carregar_alunos()

            nome = input("Digite o nome do aluno: ").lower()            
            #validar nome--------------------------
            validar = validar_nome(nome)
            if validar != "ok":
                print(validar)
                continue

            for aluno in lista:
                if aluno.nome == nome:
                    print(f"Nome: {aluno.nome} - Idade: {aluno.idade} - Email: {aluno.email} - Nota: {aluno.nota1} - Nota: {aluno.nota2} - Nota: {aluno.nota3} - Media: {aluno.calcular_media()} - Situação: {aluno.situacao_aluno()}")
                    confirmar = input("Realmente deseja alterar informações do aluno? (s/n): ").lower()

                    if confirmar == "s":
                        while True:
                            print("1 - Nome")
                            print("2 - Idade")
                            print("3 - Email")
                            print("4 - Notas")     
                            print("5 - Voltar")                      

                            opcao = input("O que gostaria de alterar: ")
                            if opcao not in ["1", "2", "3", "4", "5"]:
                                print("Digite uma opção valida")
                                continue
                            #alterar nome 
                            if opcao == "1":
                                alterar = input("Realmente gostaria de alterar o nome? (s/n): ").lower()

                                if alterar == "s":
                                    novo_nome = input("Digite o novo nome: ").lower()
                                    #validar nome---------------------------
                                    validar = validar_novo_nome(novo_nome)
                                    if validar != "ok":
                                        print(validar)
                                        continue

                                    aluno.nome = novo_nome
                                    salvar_alunos(lista)
                                    print("Nome alterado")
                                    break
                                else:
                                    print("Alterar nome cancelado")
                                    break

                            #alterar idade
                            elif opcao == "2":
                                alterar = input("Realmente gostaria de alterar a idade? (s/n): ").lower()

                                if alterar == "s":
                                    nova_idade = input("Digite sua nova idade: ")
                                    #validar idade------------------------
                                    validar = validar_nova_idade(nova_idade)
                                    if validar != "ok":
                                        print(validar)
                                        continue
                                    nova_idade = int(nova_idade)

                                    aluno.idade = nova_idade
                                    salvar_alunos(lista)
                                    print("Idade alterado")
                                    break
                                else:
                                    print("Alterar idade cancelado")
                                    break

                            #alterar email
                            elif opcao == "3":
                                alterar = input("Realmente gostaria de alterar seu email? (s/n): ").lower()

                                if alterar == "s":
                                    novo_email = input("Digite seu novo email: ")
                                    #validar email-------------------------
                                    validar = validar_novo_email(novo_email)
                                    if validar != "ok":
                                        print(validar)
                                        continue

                                    aluno.email = novo_email
                                    salvar_alunos(lista)
                                    print("email alterado")
                                    break
                                else:
                                    print("Alterar email cancelado")
                                    break

                            #alterar notas
                            elif opcao == "4":
                                alterar = input("Realmente gostaria de alterar as notas? (s/n): ").lower()

                                if alterar == "s":
                                    try:
                                        n1 = float(input("Digite a primeira nota: "))
                                        if n1 < 0 or n1 > 10:
                                            print("Nota invalida")
                                    except ValueError:
                                        print("Apenas numeros")

                                    try:
                                        n2 = float(input("Digite a segunda nota: "))
                                        if n2 < 0 or n2 > 10:
                                            print("Nota invalida")
                                    except ValueError:
                                        print("Apenas numeros")

                                    try:
                                        n3 = float(input("Digite a terceira nota: "))
                                        if n3 < 0 or n3 > 10:
                                            print("Nota invalida")
                                    except ValueError:
                                        print("Apenas numeros")

                                    aluno.alterar_nota(n1, n2, n3)
                                    salvar_alunos(lista)
                                    print("Notas alteradas")
                                    break
                                else:
                                    print("Alterar notas cancelado")
                                    break

                            #voltar
                            elif opcao == "5":
                                continue
    
#sair----------------------------------------------------------------------------------

    elif opcao == "5":
        print("Sair do sistema.......")
        break
                            
                                    


                                    



                        





                








                




            

            








    


