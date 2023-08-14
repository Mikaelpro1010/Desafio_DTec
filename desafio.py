#vetores onde estão armazenados os valores já existentes e também onde será adicionados os novos dados
code_employee = [15, 1, 26, 12, 8]
name_employee = ["João da Silva", "Pedro Santos", "Maria Oliveira", "Rita Alcântara", "Ligia Matos"]
cargos = [2500, 1500, 10000, 1200, 800]
code_cargo = [1, 2, 3, 5, 2]

#função responsável por mostrar ao usário mostrando um relatório de informações dos usuários
def exibirRelatorio():
    print("----------------------------------------------------")
    print("                   RELATÓRIO                        ")
    print("----------------------------------------------------")
    for i in range(len(code_employee)):
        for j in range(len(name_employee)):
            if(i==j):
                print("Nome:"+ name_employee[j] + ",codigo " + str(code_employee[i]))

#função tem como finalidade mostrar o salário total de todos os funcinários referente ao cargo informado
def exibirSalarioTotal():
    total = 0
    cargo = int(input("Informe o cargo que você deseja saber o valor total: "))

    for i in range(len(code_cargo)):
        for j in range(len(cargos)):
            if cargo == code_cargo[i] and cargo == j:
                total += cargos[j] 
    print("Os funcionários pertencentes ao cargo " + str(cargo) + " recebem um total de $" + str(total))


#função que tem como objetivo cadastrar um novo tipo de cargo
def cadastrarCargo():
    print("------------------------------------------------------------------------")
    print("                   Cadastro de novo cargo                               ")
    print("------------------------------------------------------------------------")
    salario = int(input("Informe o salário desejado para o novo cargo: "))
    if(salario > 0):
        novo_codigo = max(code_cargo) + 1 if code_cargo else 0  # Incrementar 1 ao último código existente
        code_cargo.append(novo_codigo)  # Adicionar o novo código à lista
        cargos.append(salario)  # Adicionar o novo salário à lista de cargos
        print("Cadastro realizado com sucesso!")
    else:
        print("Não foi possível realizar o cadastro, redirecionando você ao menu!")

#função que verifica se o código de funcionário já está sendo usado
def checkExistingCode(new_code_employee, code_employee):
    for i in range(len(code_employee)):
        if new_code_employee == code_employee[i]:
            print("Não foi possível realizar o cadastro, codigo de funcionário já existe!")
            cadastrarFuncionario()

#função que possui como finalidade checar se o cargo já existe na lista de cargos
def checkExistingCodeCargo(new_cargo):
    if new_cargo in code_cargo:
        print("Usuario cadastrado com sucesso!")
    else:
        print("Não foi possível realizar o cadastro, o codigo do cargo informado não existe!")
        cadastrarFuncionario()

def exibirCodigosCargos():
    print("                    Cargos Disponíveis                                  ")
    for i in range(len(cargos)):
        print(str(i) + "-" + str(cargos[i]))

#função responsável por cadastrar um novo funcionário
def cadastrarFuncionario():
    print("------------------------------------------------------------------------")
    print("                  Cadastro de Funcioonário                              ")
    print("------------------------------------------------------------------------")

    new_name = input("Informe o nome do seu funcinário: ")

    new_code_employee = int(input("Informe o codigo deste funcionário: "))

    checkExistingCode(new_code_employee, code_employee)

    exibirCodigosCargos()

    new_cargo = int(input("Informe o codigo do cargo deste funcionário: "))
    checkExistingCodeCargo(new_cargo)

    #usando a função append para adicionar os dados do novo funcionário em seus respectivos vetores
    code_employee.append(new_code_employee)
    name_employee.append(new_name)
    code_cargo.append(new_cargo)

    return new_name, new_code_employee, new_cargo

#menu para selecionar a ação desejada pelo usuário
def menu():
    print("1 - Cadastrar Cargo\n2 - Cadastrar Funcionário\n3 - Exibir Relatório\n4 - Exibir Salário Total")
    opcao = input("Bem vindo, o que deseja fazer?")

    #dependendo do numero escolhido pelo usuário, o mesmo será direcionado a função atrelada a este número
    if opcao == "1":
        cadastrarCargo()
    elif opcao == "2":
        cadastrarFuncionario()
    elif opcao == "3":
        exibirRelatorio()
    elif opcao == "4":
        exibirSalarioTotal()

#função principal do código, onde todas as funções serão chamadas aqui através da função menu
def main():
    continuar = True

    while continuar:  # Loop infinito para manter o menu
        menu()
        resposta = input("Deseja realizar outra ação? (yes/no): ")
        if resposta.lower() != 'yes':
            continuar = False
            print("Encerrando o programa...")
main()