code_employee = [15, 1, 26, 12, 8]
name_employee = ["João da Silva", "Pedro Santos", "Maria Oliveira", "Rita Alcântara", "Ligia Matos"]
cargos = [2500, 1500, 10000, 1200, 800]
code_cargo = [0, 1, 2, 3, 4]

def exibirRelatorio(new_name, new_code_employee):
    code_employee.append(new_code_employee)
    name_employee.append(new_name)
    # code_cargo.append(new_cargo)

    print("----------------------------------------------------")
    print("                   RELATÓRIO                        ")
    print("----------------------------------------------------")
    for i in range(len(code_employee)):
        for j in range(len(name_employee)):
            if(i==j):
                print("Nome:"+ name_employee[j] + ",codigo " + str(code_employee[i]))

#função tem como finalidade mostrar o salário total de todos os funcinários referente ao cargo informado
def exibirSalarioTotal(new_cargo):
    code_cargo.append(new_cargo)
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
        print("Cadastro realizado com sucesso!")
        return salario
    else:
        print("Não foi possível realizar o cadastro, tente novamente!")
        cadastrarCargo()

#função que verifica se o código de funcionário já está sendo usado
def checkExistingCode(new_code_employee, code_employee):
    for i in range(len(code_employee)):
        if new_code_employee == code_employee[i]:
            print("Não foi possível realizar o cadastro, codigo de funcionário já existe!")
            cadastrarFuncionario()
    # print("Usuario cadastrado com sucesso!")

#função que possui como finalidade checar se o cargo já existe na lista de cargos
def checkExistingCodeCargo(new_cargo):
    if new_cargo in code_cargo:
        print("Usuario cadastrado com sucesso!")
    else:
        print("Não foi possível realizar o cadastro!!")
        cadastrarFuncionario()

#função responsável por cadastrar um novo funcionário
def cadastrarFuncionario():
    print("------------------------------------------------------------------------")
    print("                  Cadastro de Funcioonário                              ")
    print("------------------------------------------------------------------------")

    new_name = input("Informe o nome do seu funcinário: ")
    new_code_employee = int(input("Informe o codigo do seu funcionário: "))

    checkExistingCode(new_code_employee, code_employee)

    new_cargo = int(input("Informe o cargo deste funcionário: "))
    checkExistingCodeCargo(new_cargo)

    return new_name, new_code_employee, new_cargo

#menu para selecionar a ação desejada pelo usuário
def menu():
    new_name, new_code_employee, new_cargo = cadastrarFuncionario()
    print("1 - Cadastrar Cargo\n2 - Cadastrar Funcionário\n3 - Exibir Relatório\n4 - Exibir Salário Total")
    opcao = input("Bem vindo, o que deseja fazer?")

    if opcao == "1":
        salario = cadastrarCargo()
    elif opcao == "2":
        cadastrarFuncionario()
    elif opcao == "3":
        exibirRelatorio(new_name, new_code_employee)
    elif opcao == "4":
        exibirSalarioTotal(new_cargo)
    

def main():
    print(cargos)
    while True:  # Loop infinito para manter o menu
        menu()
        continuar = input("Deseja realizar outra ação? (yes/no): ")
        if continuar.lower() == 'no':
            print("Encerrando o programa...")
            break  # Sai do loop e encerra o programa
main()







