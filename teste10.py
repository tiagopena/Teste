import json
import os

with open('/opt/gprommonitoracao/monitora_dispositivos/ambientes/renav/configuracao/topologia_rede.json') as arquivo_json_smart:
    topologia_original_smart = json.load(arquivo_json_smart)
    arquivo_json_smart.close()

# - Recebe a topologia original do SMART e cria
#   uma nova com cada um dos hosts
def cria_topologia_01_do_smartlog (topologia_original_smart):
    lista = {
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

        lista['localidade'].append(localidade)

    x = lista

    return(x)

print(cria_topologia_01_do_smartlog (topologia_original_smart))