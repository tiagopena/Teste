import json
import os

with open('/opt/gprommonitoracao/monitora_dispositivos/ambientes/renav/configuracao/topologia_rede.json') as arquivo_json_smart:
    topologia_original_smart = json.load(arquivo_json_smart)
    arquivo_json_smart.close()

with open('/opt/gprommonitoracao/SMARTLOG/Smartlog_Beta/app_ConsultaLog/static/entradas/renav4.json') as arquivo_json_smartlog:
    topologia_arquivo_smartlog = json.load(arquivo_json_smartlog)
    arquivo_json_smartlog.close()

def incluir_item_topologia_smartlog (cidade, host, ip_gerenciamento, membro, interface_local, ip_interface, ip_vizinho, circuito, operadora, nas):
    for item01 in topologia_arquivo_smartlog['ambiente']:
        if item01['cidade'] == cidade:
            print('Cidade encontrada')
        else:
            localidade = {
                'cidade' : cidade,
                'equipamento' : []
            }

    return(localidade)

# - Troca o conteudo do item GRUPO

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


for item01 in topologia_original_smart:
    host = item01['nome']
    ip_gerenciamento = item01['ip_gerencia']
    cidade = item01['grupo']
    for item02 in item01['testes']:
        if item02['tipo'] == 'interface':
            for item03 in item02['nomes_interfaces']:
                membro = item03.split('#')[1].split(' - ')[0]
                interface_local = item03.split('#')[0]
                ip_interface = ''
                ip_vizinho = '' #Vai precisar de mais um FOR
                circuito = item03.split('#')[1].split(' - ')[1]
                operadora = item03.split('#')[1].split(' - ')[1].split(' ')[0]
                nas = ''

                localidade = incluir_item_topologia_smartlog (cidade, host, ip_gerenciamento, membro, interface_local, ip_interface, ip_vizinho, circuito, operadora, nas)


    topologia_arquivo_smartlog['localidade'].append(localidade)

print(topologia_arquivo_smartlog)