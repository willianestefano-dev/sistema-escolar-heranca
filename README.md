# 🎓 Sistema Escolar com Herança

Sistema completo de gerenciamento escolar desenvolvido em Python, utilizando **Programação Orientada a Objetos** com **herança**, **JSON** para persistência de dados e **validações** robustas.

---

## 📚 Sobre o Projeto

Este sistema permite o cadastro, busca, remoção e alteração de **Alunos** e **Professores**, demonstrando o uso de herança onde ambos herdam da classe `Pessoa`.

## 🧱 Estrutura de Classes

Pessoa (classe mãe)
├── nome
├── idade
└── email

Aluno (herda de Pessoa)
├── nota1, nota2, nota3
├── calcular_media()
├── situacao_aluno()
└── alterar_nota()

Professor (herda de Pessoa)
├── disciplina
└── salario

### 📋 Menu Principal

1 - Cadastro
2 - Buscar
3 - Remover
4 - Alterar dados
5 - Sair

### 👨‍🎓 Alunos

- Cadastro (nome, idade, email, 3 notas)
- Listar todos os alunos (com média e situação)
- Buscar aluno por nome
- Remover aluno
- Alterar dados (nome, idade, email, notas)

### 👨‍🏫 Professores

- Cadastro (nome, idade, email, disciplina, salário)
- Listar todos os professores
- Buscar professor por nome
- Remover professor
- Alterar dados (nome, idade, email, disciplina, salário)

### 📊 Funcionalidades Extras

- Exibição de média e situação do aluno (Aprovado/Recuperação/Reprovado)
- Listagem de todos (alunos e professores juntos)

---

## ✅ Validações Implementadas

| Campo | Validações |
| :--- | :--- |
| Nome | Não vazio, apenas letras |
| Idade | Apenas números, máximo 3 dígitos |
| Email | Deve conter "@" e ".com" |
| Disciplina | Não vazio, apenas letras |
| Notas | Entre 0 e 10 |
| Salário | Tratamento de erro para valores não numéricos |

---

## 💾 Persistência

Os dados são salvos em arquivos **JSON**:

- `alunos.json`
- `professores.json`

---

## 🚀 Como Executar

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/sistema-escolar-heranca.git
