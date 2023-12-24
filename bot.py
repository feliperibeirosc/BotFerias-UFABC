import tweepy
import datetime
import os
from dotenv import load_dotenv

load_dotenv()  # Carrega os valores do arquivo .env

# Atribuição dos valores para cada variável
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

# Autenticação
client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)

# Função do Tweet
def create_tweet(fdias):
    if fdias > 1:
        texto = f"Faltam {fdias} dias para as férias da UFABC"
    elif fdias == 0:
        texto = "Começaram as férias da UFABC!!! 🥳🎉"
    else:
        texto = "🚨URGENTE! Falta 1 (um) dia para as férias da UFABC!!!"

    return texto

# Calculo dos dias restantes
ferias = datetime.date(2024, 5, 7)  # Coloque aqui a data do início das férias no modelo (ANO,MES,DIA)
agora = datetime.date.today()  # Computa o dia de hoje
fdias = (ferias - agora).days

# Tweet
if fdias >= 0:
    texto = create_tweet(fdias)
    response = client.create_tweet(text=texto)
    print(f"https://twitter.com/user/status/{response.data['id']}")
