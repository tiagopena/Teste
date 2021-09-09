import json
import os

with open('/opt/gprommonitoracao/monitora_dispositivos/ambientes/renav/configuracao/topologia_rede.json') as arquivo_json_smart:
    topologia_original_smart = json.load(arquivo_json_smart)
    arquivo_json_smart.close()

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

def cria_topologia_01_do_smartlog (topologia_original_smart):
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
        host = item01['nome']
        ip_gerenciamento = item01['ip_gerencia']
        cidade = item01['grupo']
        localidade = {
            'cidade' : cidade,
            'equipamento' : []
        }
        for item02 in item01['testes']:
            equipamento = {
                'host' : host,
                'ip_gerenciamento' : ip_gerenciamento,
                'par' : []
                }
            if item02['tipo'] == 'interface':
                for item03 in item02['nomes_interfaces']:
                    membro = item03.split('#')[1].split(' - ')[0]
                    interface_local = item03.split('#')[0]
                    ip_interface = ''
                    ip_vizinho = '' #Vai precisar de mais um FOR
                    circuito = item03.split('#')[1].split(' - ')[1]
                    operadora = item03.split('#')[1].split(' - ')[1].split(' ')[0]
                    nas = ''

                    par = {
                        'membro' : membro,
                        'interface_local' : interface_local,
                        'ip_interface' : ip_interface,
                        'ip_vizinho' : ip_vizinho,
                        'circuito' : circuito,
                        'operadora' : operadora,
                        'as' : nas
                    }

                    equipamento['par'].append(par)

                localidade['equipamento'].append(equipamento)

        topologia_final_smartlog['localidade'].append(localidade)

    # - Finaliza a topologia em sua ultima versao
    for item01 in topologia_final_smartlog:
        cidades = []
        for item02 in item01['localidade']:
            if item02['cidade'] not in cidades:
                cidades.append(item02['cidade'])
                novo_equipamento = item02['equipamento']


    return(topologia_final_smartlog)



print(cria_topologia_01_do_smartlog (topologia_original_smart))
