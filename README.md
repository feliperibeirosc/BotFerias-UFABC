# Bot Férias UFABC

Este projeto é um bot do Twitter que publica diariamente quantos dias faltam para as férias da Universidade Federal do ABC (UFABC). O bot utiliza a biblioteca Tweepy para se autenticar no Twitter e fazer as postagens e está hospedado no [Python Anywhere](www.pythonanywhere.com).

## Pré-requisitos

Antes de utilizar o bot, você precisará ter os seguintes itens instalados/configurados:

1. Conta no Twitter: Crie uma conta no Twitter, caso ainda não tenha uma.

2. Chaves de API do Twitter: Acesse https://developer.twitter.com/ e crie um projeto para obter as chaves de API (consumer_key, consumer_secret, access_token e access_token_secret).

3. Python: Certifique-se de ter o Python instalado em seu sistema. Você pode baixar a versão mais recente do Python em https://www.python.org/downloads/.

4. Bibliotecas Python: Instale as bibliotecas necessárias executando o seguinte comando em seu terminal/prompt de comando:

```bash
pip install tweepy python-dotenv
```

## Configuração

1. Clone o repositório: Faça um clone deste repositório para obter o código do bot.

```bash
git clone https://github.com/feliperibeirosc/BotFerias-UFABC.git
cd BotFerias-UFABC
```

2. Crie o arquivo .env: No diretório raiz do projeto, crie um arquivo chamado `.env` e preencha as chaves de API do Twitter conforme abaixo:

```env
CONSUMER_KEY= SuaConsumerKeyAqui (API Key)
CONSUMER_SECRET= SuaConsumerSecretAqui (API Secret)
ACCESS_TOKEN= SeuAccessTokenAqui (Client ID)
ACCESS_TOKEN_SECRET= SeuAccessTokenSecretAqui (Client Secret)
```

## Personalização

Antes de executar o bot, você pode personalizar as seguintes informações:

1. Data das férias: No arquivo `bot.py`, localize a linha onde a variável `ferias` é definida e atualize a data de início das férias da UFABC.

```python
ferias = datetime.date(2023, 8, 24) # Coloque aqui a data do início das férias no modelo (ANO, MES, DIA)
```

2. Texto do tweet: No mesmo arquivo `bot.py`, você pode alterar o texto do tweet que será postado. Os tweets são gerados automaticamente com base no cálculo dos dias restantes, você pode customizá-los como desejar.

```python
if fdias != 1:
    if fdias % 10 != 0:
        texto = "Faltam " + str(fdias) + " dias para as férias da UFABC"
    else:
        texto = "Faltam " + str(fdias) + " dias para as férias da UFABC!"
elif fdias == 1:
    texto = "🚨URGENTE! Falta 1 (um) dia para as férias da UFABC!!!"
else:
    texto = "Começaram as férias da UFABC!!! 🥳🎉"
```

## Execução

Com as chaves de API configuradas e as personalizações feitas, agora você pode executar o bot. No terminal/prompt de comando, navegue até o diretório raiz do projeto e execute o seguinte comando:

```bash
python bot.py
```

O bot irá calcular automaticamente a quantidade de dias restantes para as férias da UFABC e publicará a postagem na sua conta do Twitter.

## Agendamento

Para que o bot publique automaticamente todos os dias, você pode configurar o agendamento usando o Python Anywhere ou outra ferramenta de agendamento de tarefas. No Python Anywhere, você pode criar uma tarefa agendada para executar o arquivo `bot.py` diariamente. 
