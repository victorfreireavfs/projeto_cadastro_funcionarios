# ---------------------------------------------- 
# SISTEMA DE GERENCIAMENTO DE FUNCIONÁRIOS (Versão Web)
# Adaptado por Antônio Victor Freire
# ---------------------------------------------- 

lista_funcionarios = []
id_global = 5437156

def cadastrar_funcionario(id, nome, setor, salario):
    funcionario = {
        "id": id,
        "nome": nome,
        "setor": setor,
        "salario": salario
    }
    lista_funcionarios.append(funcionario.copy())
    return f"Funcionário {nome} cadastrado com sucesso! ID: {id}\n"

def consultar_funcionarios():
    if not lista_funcionarios:
        return "Nenhum funcionário cadastrado.\n"
    else:
        saida = "\n--- Funcionários cadastrados ---\n"
        for f in lista_funcionarios:
            saida += f"ID: {f['id']} | Nome: {f['nome']} | Setor: {f['setor']} | Salário: R$ {f['salario']:.2f}\n"
        return saida

def remover_funcionario(id_remove):
    for f in lista_funcionarios:
        if f["id"] == id_remove:
            lista_funcionarios.remove(f)
            return f"Funcionário {f['nome']} removido com sucesso!\n"
    return "Funcionário não encontrado.\n"

# -------------------------
# Simulação de execução web
# -------------------------
saida = "Bem-vindo ao Sistema de Gerenciamento de Funcionários!\n"
saida += "Desenvolvido por: Antônio Victor Freire\n\n"

# Cadastro automático de exemplo
saida += cadastrar_funcionario(id_global, "João", "RH", 3500.0)
saida += cadastrar_funcionario(id_global+1, "Maria", "TI", 4500.0)

# Consulta
saida += consultar_funcionarios()

# Remoção
saida += remover_funcionario(5437156)

# Consulta final
saida += consultar_funcionarios()

saida
