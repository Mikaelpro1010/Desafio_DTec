#base de dados onde serão armazenados os dados de funcionário e cargos
employee_data = [
    {"code": 15, "name": "João da Silva", "cargo": 1},
    {"code": 1, "name": "Pedro Santos", "cargo": 2},
    {"code": 26, "name": "Maria Oliveira", "cargo": 3},
    {"code": 12, "name": "Rita Alcântara", "cargo": 2},
    {"code": 8, "name": "Ligia Matos", "cargo": 2}
]

cargos = [
    {"codigo": 0, "salario": 2500},
    {"codigo": 1, "salario": 1500},
    {"codigo": 2, "salario": 10000},
    {"codigo": 3, "salario": 1200},
    {"codigo": 4, "salario": 800}
]

#função responsável por exibir o nome, codigo de funcionario e salario de cada funcionário
def exibirRelatorio():

    print("----------------------------------------------------")
    print("                   RELATÓRIO                        ")
    print("----------------------------------------------------")

    #buscar na base de dados os dados de cada funcionário
    for employee in employee_data:
        for cargo in cargos:
            if employee["cargo"] == cargo["codigo"]:
                print(f"Nome: {employee['name']}, Código: {employee['code']}, Salário: ${cargo['salario']}")

#função tem como finalidade mostrar o salário total de todos os funcinários referente ao cargo informado
def exibirSalarioTotal():
    total = 0
    valor = int(input("Informe o cargo que você deseja saber o valor total: "))

    #busca na base de dados os valores de salário referente ao cargo informado pelo usuário
    for employee in employee_data:
        for cargo in cargos:
            if valor == employee["cargo"] and valor == cargo["codigo"]:
                total+=cargo["salario"]
    
    print("Os funcionários pertencentes ao cargo " + str(valor) + " recebem um total de $" + str(total))


#função que tem como objetivo cadastrar um novo tipo de cargo
def cadastrarCargo():
    print("------------------------------------------------------------------------")
    print("                   Cadastro de novo cargo                               ")
    print("------------------------------------------------------------------------")
    salary = int(input("Informe o salário desejado para o novo cargo: "))
    if(salary > 0):
        #iterando pela lista "cargos" para encontrar o código máximo e, em seguida, incrementando-o em 1.
        new_code_cargo = max(cargo["codigo"] for cargo in cargos) + 1

        #armazenando os dados do novo cargo na base de dados
        cargos.append({"codigo": new_code_cargo, "salario": salary })
        
        print("Cadastro realizado com sucesso!")
    else:
        print("Não foi possível realizar o cadastro, tente novamente!")
        cadastrarCargo()

#função que verifica se o código de funcionário já está sendo usado
def checkExistingCode(new_code_employee):
    for employee in employee_data:
        if new_code_employee == employee["code"]:
            print("Não foi possível realizar o cadastro, codigo de funcionário já existe!")
            cadastrarFuncionario()

#função que possui como finalidade checar se o cargo já existe na lista de cargos
def checkExistingCodeCargo(new_cargo):
        # verifica se pelo menos um item na lista de cargos tem o código de cargo correspondente ao valor de new_cargo
        if any(new_cargo == cargo["codigo"] for cargo in cargos):
            print("Usuário cadastrado com sucesso!")
        else:
            print("Não foi possível realizar o cadastro, cargo informado não existe!")
            cadastrarFuncionario()

#função que como objetivo mostrar ao usuário as opções de cargos existentes para cadastro         
def exibirCodigoCargo():
    print("                    Cargos Disponíveis                                  ")
    for cargo in cargos:
        print(str(cargo["codigo"]) + "- $" + str(cargo["salario"]))

#função responsável por cadastrar um novo funcionário
def cadastrarFuncionario():
    print("------------------------------------------------------------------------")
    print("                  Cadastro de Funcionário                              ")
    print("------------------------------------------------------------------------")

    new_name = input("Informe o nome do seu funcinário: ")
    new_code_employee = int(input("Informe o codigo do seu funcionário: "))

    checkExistingCode(new_code_employee)

    exibirCodigoCargo()

    new_cargo = int(input("Informe o cargo deste funcionário: "))
    checkExistingCodeCargo(new_cargo)

    #armazenando os novos dados do funcionário na base de dados
    employee_data.append({"code": new_code_employee, "name": new_name, "cargo": new_cargo})

    return new_name, new_code_employee, new_cargo

#menu para selecionar a ação desejada pelo usuário
def menu():
    print("1 - Cadastrar Cargo\n2 - Cadastrar Funcionário\n3 - Exibir Relatório\n4 - Exibir Salário Total")
    option = input("Bem vindo, o que deseja fazer?")

    #condicionais de acesso a funcionalidades do sistema de acordo com a opcao desejada pelo usuário
    if option == "1":
        cadastrarCargo()
    elif option == "2":
        cadastrarFuncionario()
    elif option == "3":
        exibirRelatorio()
    elif option == "4":
        exibirSalarioTotal()

#função principal do código, sendo a mesma responsável por dar o start inicial do sistema
def main():
    continuar = True

    while continuar:  # Loop infinito para manter o menu
        menu()
        resposta = input("Deseja realizar outra ação? (yes/no): ")
        if resposta.lower() != 'yes':
            continuar = False
            print("Encerrando o programa...")

#chamando a função main para dar inicio a execução do sistema
main()