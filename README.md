# 🎵 MusifyDB — Aplicação web para cadastro e gerenciamento de músicas

MusifyDB é uma aplicação web desenvolvida com Python e Flask, que permite cadastrar, editar e excluir músicas com informações completas, incluindo imagem da capa do álbum. Possui também autenticação de usuários, tornando o gerenciamento personalizado e seguro.

---

## 📌 Visão Geral

O MusifyDB é ideal para quem deseja organizar sua coleção musical de forma simples, prática e acessível via navegador. Além do cadastro de músicas, o sistema permite fazer login, registrar novos usuários e associar cada música a uma imagem representativa do álbum.

---

## 🔍 Funcionalidades

✅ Cadastro de músicas com título, artista, álbum, gênero, imagem e outros dados

✅ Listagem de todas as músicas cadastradas

✅ Edição e exclusão de músicas

✅ Upload de imagem para representar a música/álbum

✅ Cadastro e login de usuários com autenticação

✅ Interface responsiva com Bootstrap

✅ Templates dinâmicos com Jinja2

---

## 🧱 Tecnologias Utilizadas

### 🖥️ Backend

- Python
- Flask (framework web)
- MySQL (banco de dados relacional)

### 💻 Frontend

- HTML
- CSS
- Bootstrap (estilização responsiva)
- Jinja2 (motor de templates)
  
---

## 🧠 Arquitetura do Projeto

```
musifydb/
│
├── __pycache__/                    # Cache do Python
│
├── static/                         # Arquivos estáticos (CSS)
│   └── bootstrap.css
│
├── templates/                      # Templates HTML com Jinja2
│   ├── cadastra_musica.html
│   ├── cadastra_usuario.html
│   ├── editar_musica.html
│   ├── lista_musicas.html
│   ├── login.html
│   └── padrao.html
│
├── uploads/                        # Imagens dos álbuns/músicas
│
├── comandos_banco.sql             # Script SQL para criação do banco de dados
├── config.py                      # Configurações gerais da aplicação
├── definicoes.py                  # Constantes e definições globais
├── models.py                      # Interação com o banco de dados
├── musica.py                      # Arquivo principal para iniciar o app
├── requirements.txt               # Dependências do projeto
├── views_musica.py                # Rotas relacionadas às músicas
└── views_usuario.py
```

---

## 🚀 Como Rodar o Projeto

1. Clone o repositório:

```bash
git clone https://github.com/Aleckenzo/musifydb.git
cd musifydb
```

2. Crie e ative um ambiente virtual:

- No Linux/Mac:

```bash
python3 -m venv venv
source venv/bin/activate
```

- No Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Configure seu banco de dados MySQL:

- Crie o banco de dados com o script comandos_banco.sql

- Atualize as configurações de acesso no config.py se necessário

5. Execute a aplicação:

```bash
python musica.py
```

6. Acesse no navegador:

[http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## ⚙️ Funcionamento Geral

- O usuário se cadastra e faz login para acessar o sistema.

- Pode cadastrar músicas com informações completas e uma imagem de capa.

- As músicas podem ser listadas, editadas ou excluídas.

- O layout usa Bootstrap para responsividade e os dados são renderizados dinamicamente via Jinja2.

- Toda a lógica backend é feita com Flask e os dados são persistidos no MySQL.

---

Feito com 🎶 e 💻 para facilitar a organização da sua coleção musical!


