import json
import os

with open('/opt/gprommonitoracao/monitora_dispositivos/ambientes/renav/configuracao/topologia_rede.json') as arquivo_json_smart:
    topologia_original_smart = json.load(arquivo_json_smart)
    arquivo_json_smart.close()

#with open('/opt/gprommonitoracao/SMARTLOG/Smartlog_Beta/app_ConsultaLog/static/entradas/renav4.json') as arquivo_json_smartlog:
#    topologia_modificada_smartlog = json.load(arquivo_json_smartlog)
#    arquivo_json_smartlog.close()

topologia_final_smartlog = {
        'ambiente' : 'RENAV',
        'teste' : [
            "conexao",
            "interface - estado",
            "interface - pacotes com erro",
            "BGP - estado vizinho",
            "BGP - divulgacao incompleta",
            "BGP - quedas multiplas",
            "BGP - tempo UP",
            "Ping - perda pacotes",
            "Ping - tempo RTT"],
        'localidade' : []
        }


for item01 in topologia_original_smart:
    if (item01['grupo'] == 'BSB-CCT-I') or (item01['grupo'] == 'BSB-CCT-II'):
        item01['grupo'] = 'BRASILIA'
    elif (item01['grupo'] == 'SP-VD') or (item01['grupo'] == 'SP-AP'):
        item01['grupo'] = 'SAO PAULO'
    elif (item01['grupo'] == 'RJ-TL') or (item01['grupo'] == 'RJ-SD'):
        item01['grupo'] = 'RIO DE JANEIRO'
    elif (item01['grupo'] == 'SJP'):
        item01['grupo'] = 'SAO JOSE DOS PINHAIS'
    elif (item01['grupo'] == 'SDR'):
        item01['grupo'] = 'SALVADOR'
    elif (item01['grupo'] == 'BHE'):
        item01['grupo'] = 'BELO HORIZONTE'
    else:
        item01['grupo'] = 'nulo'

cidade = []
host = []
membro = []

for item01 in topologia_original_smart:
    if item01['grupo'] not in cidade:
        cidade.append(item01['grupo'])
    if item01['nome'] not in host:
        host.append(item01['nome'])
    for item02 in item01['testes']:
        if item02['tipo'] == 'interface':
            for item03 in item02['nomes_interfaces']:
                membro.append(item03.split('#')[1].split(' - ')[0])

def agrega_cidade (cidade):
    localidade = {
        'cidade' : cidade,
        'equipamento' : []
        }
    for item01 in topologia_original_smart:
        if item01['grupo'] == cidade:
            equipamento = {
                'host' : item01['nome'],
                'ip_gerenciamento' : item01['ip_gerencia'],
                'par' : []
                }
            localidade['equipamento'].append(equipamento)

    topologia_final_smartlog['localidade'].append(localidade)

for item01 in cidade:
    agrega_cidade(item01)


           

print(topologia_final_smartlog)