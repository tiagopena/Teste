import json
import os

#with open('/opt/gprommonitoracao/SMARTLOG/Smartlog_Beta/app_ConsultaLog/static/entradas/renav2.json') as arquivo_json_smartlog:
#    topologia_arquivo_smartlog = json.load(arquivo_json_smartlog)
#    arquivo_json_smartlog.close()

with open('/opt/gprommonitoracao/monitora_dispositivos/ambientes/renav/configuracao/topologia_rede.json') as arquivo_json_smart:
    topologia_arquivo_smart = json.load(arquivo_json_smart)
    arquivo_json_smart.close()

grupo = {'BSB-CCT-I', 'BSB-CCT-II', 'SP-VD', 'SP-AP', 'RJ-TL', 'RJ-SD', 'SJP', 'SDR', 'BHE' }


topologia_renav = {
    "ambiente":"RENAV",
    "teste": [
        "Interface - estado",
        "Interface - pacotes com erro"],
    "localidade" : []
}

localidade = []
localidade_equipamento_desagregado = []

localidade_desagregada = []
#localidade_agregada = []
equipamento = []
cidades = ['BRASILIA', 'SAO PAULO', 'RIO DE JANEIRO', 'SAO JOSE DOS PINHAIS', 'SALVADOR', 'BELO HORIZONTE']

def insere_host (host, ip_gerenciamento, grupo, membro, interface_local, circuito, operadora):

    item = {
        'cidade' : grupo,
        'equipamento' : {
            'host' : host,
            'ip_gerenciamento' : ip_gerenciamento,
            'par' : {
                'membro' : membro,
                'interface_local' : interface_local,
                'circuito' : circuito,
                'operadora' : operadora
            }
        }
    }

    localidade_desagregada.append(item)

    return (localidade_desagregada)

def agrega_localidade (cidade):
    localidade_agregada = {
        'cidade' : cidade,
        'equipamento' : []
        }

    for item01 in localidade_desagregada :
        if item01['cidade'] == cidade:
            equipamento = item01['equipamento']
            localidade_agregada['equipamento'].append(equipamento)

    return(localidade_agregada)

def agrega_equipamento(host):
    x = {
        'host' : host,
        'ip_gerenciamento' : ip_gerenciamento,
        'par' : []
        }

    for item01 in localidade_equipamento_desagregado:
        for item02 in item01['equipamento']:
            if item02['host'] == host:
                par = item02['par']
                x['par'].append(par)

    return(x)

###############################################################
# - Recebe a topologia inicial do SMART e transforma em itens
#   do para o SMARTLOG apenas separados por cidade
def retorna_itens_por_cidade_desagregado (topologia_arquivo_smart):
    for item01 in topologia_arquivo_smart :
        host = item01['nome']
        ip_gerenciamento = item01['ip_gerencia']

        if (item01['grupo'] == 'BSB-CCT-I') or (item01['grupo'] == 'BSB-CCT-II'):
            cidade = 'BRASILIA'
        elif (item01['grupo'] == 'SP-VD') or (item01['grupo'] == 'SP-AP'):
            cidade = 'SAO PAULO'
        elif (item01['grupo'] == 'RJ-TL') or (item01['grupo'] == 'RJ-SD'):
            cidade = 'RIO DE JANEIRO'
        elif (item01['grupo'] == 'SJP'):
            cidade = 'SAO JOSE DOS PINHAIS'
        elif (item01['grupo'] == 'SDR'):
            cidade = 'SALVADOR'
        elif (item01['grupo'] == 'BHE'):
            cidade = 'BELO HORIZONTE'
        else:
            cidade = 'nulo'

        for item02 in item01['testes']:
            if item02['tipo'] == 'interface':
                for item03 in item02['nomes_interfaces']:
                    membro = item03.split('#')[1].split(' - ')[0]
                    interface_local = item03.split('#')[0]
                    circuito = item03.split('#')[1].split(' - ')[1]
                    operadora = item03.split('#')[1].split(' - ')[1].split(' ')[0]

                    lista_itens_por_cidade_desagregado = insere_host (host, ip_gerenciamento, cidade, membro, interface_local, circuito, operadora)

    return(lista_itens_por_cidade_desagregado)

def retorna_itens_por_cidade_agregado (retorna_itens_por_cidade_desagregado):
    cidade = []
    retorna_equipamentos = []
    for item01 in retorna_itens_por_cidade_desagregado:
        if item01['cidade'] not in cidade:
            cidade.append(item01['cidade'])

    for item02 in cidade:
        retorna_equipamentos.append(agrega_localidade(item02))

    return(retorna_equipamentos)






itens_por_cidades_desagregado = retorna_itens_por_cidade_desagregado(topologia_arquivo_smart)
itens_por_cidades_agregado = retorna_itens_por_cidade_agregado(itens_por_cidades_desagregado)
print(itens_por_cidades_agregado)


#print(retorna_itens_por_cidade(topologia_arquivo_smart))


#print(localidade_equipamento_desagregado)


#print(localidade_desagregada)
#print(localidade_agregada)
#agrega_localidade('SALVADOR')
#print(agrega_localidade('SALVADOR'))

#print(agrega_equipamento("SWBSA01-BACK-01"))