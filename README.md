# trabalho_password

## PYTHON ----- VERSAO 3.10.7
git clone https://github.com/EricSacardo/trabalho_password.git

## iniciar e habiitar o servidor para instalar as dependencias na pasta do projeto 
cd trabalho_password 
python -m venv venv 

## ativar o ambiente virtual
venv\Scripts\activate

## upgrade do instalador das dep. 
python -m pip install --upgrade pip

## instalar dep. 
pip install -r requirements.txt

## iniciar migrations
python manage.py makemigrations

## iniciar H2 (django rode)
python manage.py migrate

## iniciar server (django rode)
python manage.py runserver

## rodando no localhost:8000 

---------------------------------------------------------------------------------------------

## SOBRE O TRABALHO:

Trabalho - Gerenciador de Senhas WEB

Esse sistema, apenas um usuário vai gerenciar as senhas.

Ao acessar o sistema, o usuário vai precisar fazer a autenticação e na sequencia ser redirecionado para a tela de lista das senhas cadastradas; Spring Security;

Na tela de lista de senhas cadastradas o usuário pode realizar as seguintes operações. Criar, Visualizar, Alterar, Consultar pela descrição e Excluir as senhas. JPA

Os dados serão cadastrados em uma tabela no banco de dados.

Tabela Exemplo Password
id, descrição, url, senha;

OBS: A senha precisa ser salva no banco de dados de forma embaralhada e desembaralhar na tela de detalhe do usuário;

Back-end e front-end;

Data de entregue dia 12/10/2022 individual;
Prova 13/10/2022