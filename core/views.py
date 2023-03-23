import requests
import os
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Summoner
from .serializers import SummonerSerializer
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())


@api_view(['GET'])
def summoner_view(request, summoner_name=None):
    if request.method == 'GET':
        # Verifica se o Summoner já existe no banco de dados
        summoner = Summoner.objects.filter(name=summoner_name).first()
        if summoner is not None:
            # Retorna os dados do Summoner do banco de dados
            serializer = SummonerSerializer(summoner)
            return Response(serializer.data)
        else:
            # Chamada à API da Riot Games para buscar o Summoner
            headers = {
                'X-Riot-Token': os.environ['RIOT_KEY']
            }
            response = requests.get(
                f'https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}', headers=headers)
            if response.status_code == 200:
                summoner_data = response.json()
                # Cria ou atualiza o objeto Summoner no banco de dados com os dados da API
                summoner, created = Summoner.objects.update_or_create(
                    name=summoner_data['name'],
                    defaults={
                        'summonerLevel': summoner_data['summonerLevel'],
                        'accountId': summoner_data['accountId']
                    }
                )
                serializer = SummonerSerializer(summoner)
                return Response(serializer.data, status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def summoner_list(request):
    summoners = Summoner.objects.all()
    serializer = SummonerSerializer(summoners, many=True)
    return Response(serializer.data)
