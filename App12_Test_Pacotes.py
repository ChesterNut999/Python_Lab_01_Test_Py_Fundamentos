from datetime import datetime
import requests

def retornaDadosCep(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    if response.status_code == 200:
        print('STATUS CODE HTTPS:',response.status_code,'| ACESSO OK!')
    else:
        print('Status Code HTTPS:',response.status_code,'| FALHA DE ACESSO!')

    dados_cep = response.json()
    print('CEP: ',dados_cep['cep'])
    print('LOGRADOURO: ', dados_cep['logradouro'],)

    return dados_cep

def retornaDadosPokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon.lower()))
    dados_pokemon = response.json()
    print(dados_pokemon['sprites']['front_shiny'])

    return dados_pokemon

def retornaRespose(url):
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    print('# ------------------------ CASO 1 - JSON CEP API')
    retornaDadosCep(input('Digite o cep para consulta: '))
    print('')

    print('# ------------------------ CASO 2 - JSON POKEMON API')
    retornaDadosPokemon(input('Digite o nome do pokemon: '))
    print('')

    print('# ------------------------ CASO 3 - OBTER CÓDIGO HTML/CSS PADRÃO SITE')
    print('Abrindo arquivo...')
    dir_arq = open('/home/Maurilio/PycharmProjects/Python_Lab_01_Test/resources/files/get_url.txt', 'w')

    print('Escrevendo no arquivo... Consulte o arquivo gerado.')
    dir_arq.write(retornaRespose('https://digitalinnovation.one/'))

    print('Fechando arquivo...')
    dir_arq.close()