import os

# Configuração do Banco de Dados
SECRET_KEY = 'uma_chave_secreta_qualquer_aqui'


SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = '',
        servidor = 'localhost',
        database = 'playmusica'
    )



UPLOAD_PASTA = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
