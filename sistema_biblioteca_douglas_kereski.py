#========================
# TRABALHO AS 
# SISTEMAS DE GERENCIAMENTO 
# DE BIBLIOTECA
#========================
# ALUNO: DOUGLAS KERESKI
# PROF: VICTOR COSTA MELO
#========================
# OBJETIVO DO TRABALHO
# DESENVOLVER UM SISTEMA DE BIBLIOTECA EM PYTHON,
# APLICANDO OS CONCEITOS DE LÓGICA DE PROGRAMAÇÃO,
# COM FUNÇÕES, ESTRUTURAS DE DADOS E SIMULAÇÃO DE TEMPO.
#=========================

from dataclasses import dataclass

# ========================
# CONFIGURAÇÕES INICIAIS
# ========================
dia_atual_sistema = 1
VALOR_MULTA_POR_DIA = 1.00

# ========================
# ESTRUTURAS DE DADOS
# ========================
@dataclass
class Livro:
    codigo: str
    titulo: str
    autor: str
    ano: int
    genero: str
    quantidade_total: int
    quantidade_disponivel: int

@dataclass
class Usuario:
    id: str
    nome: str
    tipo: str  # aluno ou professor

@dataclass
class Emprestimo:
    id_usuario: str
    codigo_livro: str
    dia_emprestimo: int
    dia_devolucao_prevista: int
    dia_devolucao_efetiva: int = None
    status: str = "ativo"  # ativo ou devolvido

# ========================
# LISTAS GLOBAIS
# ========================
livros = []
usuarios = []
emprestimos = []

# ========================
# FUNÇÕES: MENU PRINCIPAL
# ========================
def menu_principal():
    global dia_atual_sistema
    while True:
        print("\n===== SISTEMA DE BIBLIOTECA =====")
        print(f"Dia atual do sistema: {dia_atual_sistema}")
        print("1. Gerenciar Livros")
        print("2. Gerenciar Usuários")
        print("3. Realizar Empréstimo")
        print("4. Realizar Devolução")
        print("5. Relatórios")
        print("6. Gerenciar Tempo")
        print("7. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_livros()
        elif opcao == "2":
            menu_usuarios()
        elif opcao == "3":
            realizar_emprestimo()
        elif opcao == "4":
            realizar_devolucao()
        elif opcao == "5":
            menu_relatorios()
        elif opcao == "6":
            dia_atual_sistema = menu_gerenciar_tempo(dia_atual_sistema)
        elif opcao == "7":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida.")

# ========================
# FUNÇÕES: LIVROS
# ========================
def menu_livros():
    while True:
        print("\n--- GERENCIAR LIVROS ---")
        print("1. Cadastrar novo livro")
        print("2. Listar todos os livros")
        print("3. Buscar livro")
        print("4. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_livro()
        elif opcao == "2":
            listar_livros()
        elif opcao == "3":
            buscar_livro()
        elif opcao == "4":
            break
        else:
            print("Opção inválida.")

def cadastrar_livro():
    print("\n--- Cadastro de Livro ---")
    codigo = input("Código do livro: ")

    for livro in livros:
        if livro.codigo == codigo:
            print("Código já existe.")
            return

    titulo = input("Título: ")
    autor = input("Autor: ")
    try:
        ano = int(input("Ano de publicação: "))
    except:
        print("Ano inválido.")
        return
    genero = input("Gênero: ")
    try:
        quantidade_total = int(input("Quantidade total: "))
        if quantidade_total <= 0:
            print("Quantidade deve ser positiva.")
            return
    except:
        print("Quantidade inválida.")
        return

    novo = Livro(codigo, titulo, autor, ano, genero, quantidade_total, quantidade_total)
    livros.append(novo)
    print("Livro cadastrado com sucesso!")

def listar_livros():
    print("\n--- Lista de Livros ---")
    if not livros:
        print("Nenhum livro cadastrado.")
        return
    for l in livros:
        print(f"\nCódigo: {l.codigo}")
        print(f"Título: {l.titulo}")
        print(f"Autor: {l.autor}")
        print(f"Ano: {l.ano}")
        print(f"Gênero: {l.genero}")
        print(f"Total: {l.quantidade_total} | Disponível: {l.quantidade_disponivel}")

def buscar_livro():
    termo = input("Buscar por código, título ou autor: ").lower()
    encontrados = [l for l in livros if termo in l.codigo.lower() or termo in l.titulo.lower() or termo in l.autor.lower()]
    if not encontrados:
        print("Nenhum livro encontrado.")
        return
    for l in encontrados:
        print(f"\nCódigo: {l.codigo}")
        print(f"Título: {l.titulo}")
        print(f"Autor: {l.autor}")
        print(f"Ano: {l.ano}")
        print(f"Gênero: {l.genero}")
        print(f"Total: {l.quantidade_total} | Disponível: {l.quantidade_disponivel}")

# ========================
# FUNÇÕES: USUÁRIOS
# ========================
def menu_usuarios():
    while True:
        print("\n--- GERENCIAR USUÁRIOS ---")
        print("1. Cadastrar novo usuário")
        print("2. Listar todos os usuários")
        print("3. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "3":
            break
        else:
            print("Opção inválida.")

def cadastrar_usuario():
    id_usuario = input("ID do usuário: ")
    for u in usuarios:
        if u.id == id_usuario:
            print("ID já cadastrado.")
            return
    nome = input("Nome: ")
    tipo = input("Tipo (aluno/professor): ").lower()
    if tipo not in ["aluno", "professor"]:
        print("Tipo inválido.")
        return
    usuarios.append(Usuario(id_usuario, nome, tipo))
    print("Usuário cadastrado com sucesso!")

def listar_usuarios():
    print("\n--- Lista de Usuários ---")
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return
    for u in usuarios:
        print(f"\nID: {u.id}")
        print(f"Nome: {u.nome}")
        print(f"Tipo: {u.tipo}")

# ========================
# FUNÇÕES: EMPRÉSTIMO
# ========================
def realizar_emprestimo():
    global dia_atual_sistema
    print("\n--- Realizar Empréstimo ---")
    id_usuario = input("ID do usuário: ")
    codigo_livro = input("Código do livro: ")

    usuario = next((u for u in usuarios if u.id == id_usuario), None)
    livro = next((l for l in livros if l.codigo == codigo_livro), None)

    if not usuario:
        print("Usuário não encontrado.")
        return
    if not livro:
        print("Livro não encontrado.")
        return
    if livro.quantidade_disponivel <= 0:
        print("Livro indisponível.")
        return

    prazo = 7 if usuario.tipo == "aluno" else 10
    emprestimo = Emprestimo(id_usuario, codigo_livro, dia_atual_sistema, dia_atual_sistema + prazo)
    emprestimos.append(emprestimo)
    livro.quantidade_disponivel -= 1
    print("Empréstimo realizado.")
    print(f"Devolução prevista: Dia {emprestimo.dia_devolucao_prevista}")

def realizar_devolucao():
    global dia_atual_sistema
    print("\n--- Realizar Devolução ---")
    id_usuario = input("ID do usuário: ")
    codigo_livro = input("Código do livro: ")

    emprestimo = next((e for e in emprestimos if e.id_usuario == id_usuario and e.codigo_livro == codigo_livro and e.status == "ativo"), None)
    if not emprestimo:
        print("Nenhum empréstimo ativo encontrado.")
        return

    emprestimo.dia_devolucao_efetiva = dia_atual_sistema
    emprestimo.status = "devolvido"
    livro = next((l for l in livros if l.codigo == codigo_livro), None)
    if livro:
        livro.quantidade_disponivel += 1

    atraso = dia_atual_sistema - emprestimo.dia_devolucao_prevista
    if atraso > 0:
        multa = atraso * VALOR_MULTA_POR_DIA
        print(f"Devolução em atraso ({atraso} dia[s]). Multa: R${multa:.2f}")
    else:
        print("Devolução no prazo.")
    print("Livro devolvido com sucesso.")

# ========================
# FUNÇÕES: RELATÓRIOS
# ========================
def menu_relatorios():
    while True:
        print("\n--- RELATÓRIOS ---")
        print("1. Livros emprestados atualmente")
        print("2. Livros com devolução em atraso")
        print("3. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            relatorio_emprestimos_ativos()
        elif opcao == "2":
            relatorio_atrasos()
        elif opcao == "3":
            break
        else:
            print("Opção inválida.")

def relatorio_emprestimos_ativos():
    print("\n--- Empréstimos Ativos ---")
    ativos = [e for e in emprestimos if e.status == "ativo"]
    if not ativos:
        print("Nenhum empréstimo ativo.")
        return
    for e in ativos:
        u = next((u for u in usuarios if u.id == e.id_usuario), None)
        l = next((l for l in livros if l.codigo == e.codigo_livro), None)
        print(f"\nLivro: {l.titulo if l else 'Desconhecido'}")
        print(f"Usuário: {u.nome if u else 'Desconhecido'}")
        print(f"Devolução prevista: Dia {e.dia_devolucao_prevista}")

def relatorio_atrasos():
    global dia_atual_sistema
    print("\n--- Empréstimos em Atraso ---")
    atrasados = [e for e in emprestimos if e.status == "ativo" and e.dia_devolucao_prevista < dia_atual_sistema]
    if not atrasados:
        print("Nenhum empréstimo em atraso.")
        return
    for e in atrasados:
        u = next((u for u in usuarios if u.id == e.id_usuario), None)
        l = next((l for l in livros if l.codigo == e.codigo_livro), None)
        atraso = dia_atual_sistema - e.dia_devolucao_prevista
        print(f"\nLivro: {l.titulo if l else 'Desconhecido'}")
        print(f"Usuário: {u.nome if u else 'Desconhecido'}")
        print(f"Dias de atraso: {atraso}")

# ========================
# FUNÇÃO: GERENCIAR TEMPO
# ========================
def menu_gerenciar_tempo(dia):
    while True:
        print("\n--- GERENCIAR TEMPO ---")
        print(f"Dia atual: {dia}")
        print("1. Avançar 1 dia")
        print("2. Avançar 7 dias")
        print("3. Avançar N dias")
        print("4. Consultar dia atual")
        print("5. Voltar")
        op = input("Escolha uma opção: ")

        if op == "1":
            dia += 1
        elif op == "2":
            dia += 7
        elif op == "3":
            try:
                n = int(input("Quantos dias avançar? "))
                if n > 0:
                    dia += n
                else:
                    print("Número deve ser positivo.")
            except:
                print("Entrada inválida.")
        elif op == "4":
            print(f"Dia atual: {dia}")
        elif op == "5":
            break
        else:
            print("Opção inválida.")
    return dia

# ========================
# INICIAR PROGRAMA
# ========================
menu_principal()
