import json
import os

with open('/opt/gprommonitoracao/monitora_dispositivos/ambientes/renav/configuracao/topologia_rede.json') as arquivo_json_smart:
    topologia_original_smart = json.load(arquivo_json_smart)
    arquivo_json_smart.close()

#with open('/opt/gprommonitoracao/SMARTLOG/Smartlog_Beta/app_ConsultaLog/static/entradas/renav4.json') as arquivo_json_smartlog:
#    topologia_modificada_smartlog = json.load(arquivo_json_smartlog)
#    arquivo_json_smartlog.close()

topologia_modificada_smartlog_xxxx = {	
    "ambiente":"RENAV",
    "teste": [
        "conexao",
        "interface - estado",
        "interface - pacotes com erro",
        "BGP - estado vizinho",
        "BGP - divulgacao incompleta",
        "BGP - quedas multiplas",
        "BGP - tempo UP",
        "Ping - perda pacotes",
        "Ping - tempo RTT"
    ],
    "localidade" : [
        {
            "cidade": "",
            "equipamento": [
                {
                    "host":"",
                    "ip_gerenciamento":"",
                    "par": [
                        {
                            "membro":"SAO JOSE DOS PINHAIS",
                            "interface_local":"TenGigabitEthernet4/5",
                            "ip_interface":"192.168.42.9",
                            "ip_vizinho" :"192.168.42.10",
                            "circuito":"SJPBSADI7185817",
                            "operadora":"OI",
                            "as":"65518"
                        }
                    ]
                }
            ]
        }
    ]
}



def constroi_topologia_smartlog (cidade, host, ip_gerenciamento, membro, interface_local, ip_interface, ip_vizinho, circuito, operadora, nas):
    localidade = []
    for item01 in topologia_modificada_smartlog_xxxx['localidade']:
        if item01['cidade'] != cidade:
            localidade = {
                'cidade' : cidade,
                'equipamento' : []
                }
        else:
            print('Cidade nao encontrada')

    

    ####topologia_modificada_smartlog_xxxx['localidade'].append(localidade)

constroi_topologia_smartlog ('cidade', 'host', 'ip_gerenciamento', 'membro', 'interface_local', 'ip_interface', 'ip_vizinho', 'circuito', 'operadora', 'nas')
constroi_topologia_smartlog ('cidade1', 'host1', 'ip_gerenciamento1', 'membro1', 'interface_local1', 'ip_interface1', 'ip_vizinho1', 'circuito1', 'operadora1', 'nas1')
constroi_topologia_smartlog ('cidade2', 'host2', 'ip_gerenciamento2', 'membro2', 'interface_local2', 'ip_interface2', 'ip_vizinho2', 'circuito2', 'operadora2', 'nas2')

#print(topologia_modificada_smartlog_xxxx)

