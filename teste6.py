import json
import os

# Le json do SMART
with open('/opt/gprommonitoracao/monitora_dispositivos/ambientes/renav/configuracao/topologia_rede.json') as arquivo_json_smart:
    topologia_arquivo_smart = json.load(arquivo_json_smart)
    arquivo_json_smart.close()

with open('/opt/gprommonitoracao/SMARTLOG/Smartlog_Beta/app_ConsultaLog/static/entradas/renav2.json') as arquivo_json_smartlog:
    topologia_arquivo_smartlog = json.load(arquivo_json_smartlog)
    arquivo_json_smartlog.close()  


def inclui_registro (cidade, host, ip_gerenciamento, membro, interface_local, circuito, operadora, ip_interface, ip_vizinho, nas):
    for json02 in topologia_arquivo_smartlog['localidade'] :
        print('Entrou no primeiro FOR')
        if json02['cidade'] != cidade:
            print('Entrou no primeiro IF')
            json02['cidade'] = cidade

            #topologia_arquivo_smartlog['localidade'].append(json02)

            #print(topologia_arquivo_smartlog)

    print(topologia_arquivo_smartlog)

    with open('/opt/gprommonitoracao/SMARTLOG/Smartlog_Beta/app_ConsultaLog/static/entradas/renav3.json') as arquivo_json_smartlog:
        json.dump(topologia_arquivo_smartlog, arquivo_json_smartlog)        
        arquivo_json_smartlog.close()



inclui_registro (
    'brasilia1',
    'host1',
    'ip_gerenciamento1',
    'membro1',
    'interface_local1',
    'circuito1',
    'operadora1',
    'ip_interface1',
    'ip_vizinho1',
    'nas1'
    )

inclui_registro (
    'Salvador2',
    'host2',
    'ip_gerenciamento2',
    'membro2',
    'interface_local2',
    'circuito2',
    'operadora2',
    'ip_interface2',
    'ip_vizinho2',
    'nas2'
    )

#print(topologia_arquivo_smartlog)