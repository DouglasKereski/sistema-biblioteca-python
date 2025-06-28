# 📚 Sistema de Gerenciamento de Biblioteca

Trabalho AS *Lógica de Programação* (ADS)  
Aluno: *Douglas Kereski*  
Professor: *Victor Costa Melo*

---

## 🎯 Objetivo

Desenvolver um sistema de gerenciamento de biblioteca utilizando a linguagem Python, aplicando os conceitos de lógica de programação com foco em:

- Funções
- Estruturas de controle
- Estruturas de dados (dataclass, listas)
- Simulação de tempo sem datetime

---

## ⚙ Funcionalidades

- 📘 Gerenciar livros (cadastro, listagem e busca)
- 👤 Gerenciar usuários (aluno/professor)
- 🔄 Realizar empréstimos com prazos diferentes (7 ou 10 dias)
- 📅 Simular passagem de tempo (dias no sistema)
- 📥 Devolução com cálculo de multa por atraso
- 📊 Relatórios de empréstimos ativos e em atraso

---

## 🧠 Como funciona a simulação de tempo?

O sistema utiliza uma variável chamada dia_atual_sistema, que representa o "dia atual".  
O usuário pode avançar os dias manualmente pelo menu.  
Todos os empréstimos e devoluções utilizam esse valor para calcular prazos e multas.

---

## ▶ Como executar

1. Certifique-se de ter o Python instalado (recomendado Python 3.10+)
2. Baixe o arquivo sistema_biblioteca_douglas_kereski.py
3. Execute no terminal:

```bash
python sistema_biblioteca_douglas_kereski.py
