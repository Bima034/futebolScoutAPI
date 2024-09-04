# Instalação do FutebolScout

Este documento guiará você na instalação e configuração do FutebolScout.

## Pré-requisitos
- **Python 3.10**: A aplicação requer a instalação do Python.
- **Git**: Para clonar o repositório da aplicação.
- **pip**: O gerenciador de pacotes para Python.

## Passo 1: Clonando o Repositório

Primeiramente, clone o repositório da aplicação para o seu ambiente local:

```
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

## Passo 2: Criando e Ativando o Ambiente Virtual
É recomendado o uso de um ambiente virtual para isolar as dependências da aplicação. Siga os passos abaixo para criar e ativar o ambiente virtual:

```
python -m venv venv
```
Ativando o Ambiente Virtual
- Windows:
```
venv\Scripts\activate
```
- macOS e Linux:
```
source venv/bin/activate
```
Após a ativação, o terminal indicará que você está dentro do ambiente virtual.

## Passo 3: Instalando as Dependências
Com o ambiente virtual ativo, instale as dependências necessárias para a aplicação. Estas estão listadas no arquivo requirements.txt.

```
pip install -r requirements.txt
```

## Passo 4: Configurando a Aplicação
### Execute as migrações do banco de dados
```
python manage.py migrate
```

## Passo 5: Executando o Servidor de Desenvolvimento
Para iniciar o servidor de desenvolvimento e verificar se a instalação foi bem-sucedida, utilize o seguinte comando:

```
python manage.py runserver
```

