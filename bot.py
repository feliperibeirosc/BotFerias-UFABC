import tweepy
import datetime
import os
from dotenv import load_dotenv
load_dotenv() # Carrega os valores do arquivo .env

# 1. Atribuição dos valores para cada variável
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

# 2. Autenticação
client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)

# 3. Calculo dos dias restantes
ferias = datetime.date(2023, 8, 24) # Coloque aqui a data do início das férias no modelo (ANO,MES,DIA)
agora = datetime.date.today() # Computa o dia de hoje
fdias = (ferias - agora).days

# 4. Texto do tweet
if fdias !=1:
    if fdias % 10 != 0: # Testando para ver se o dia é um multiplo de 10
      texto = "Faltam " + str(fdias) + " dias para as férias da UFABC"
    else:
      texto = "Faltam " + str(fdias) + " dias para as férias da UFABC!"
elif fdias == 1:
    texto = "🚨URGENTE! Falta 1 (um) dia para as férias da UFABC!!!"
else:
    texto = "Começaram as férias da UFABC!!! 🥳🎉"

# 5. Tweet
response = client.create_tweet(text = texto)
print(f"https://twitter.com/user/status/{response.data['id']}")