create database playMusica;

-- seleciona banco playmusica
use playmusica;

-- cria tabela música
create table musica(
	id_musica int primary key auto_increment not null,
    nome_musica varchar(50) not null,
    cantor_banda varchar (50) not null,
    genero_musica varchar(20) not null);
    
-- SELECT música
SELECT * FROM musica;

-- cria tabela usuário
create table usuario(
	id_usuario int primary key auto_increment not null,
    nome_usuario varchar(50) not null,
    login_usuario varchar(20) not null,
    senha_usuario varchar(15) not null);

-- SELECT usuário
select * from usuario;

-- Limpa tabela usuário
truncate table usuario;


