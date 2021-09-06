import json
import os

#with open('/opt/gprommonitoracao/SMARTLOG/Smartlog_Beta/app_ConsultaLog/static/entradas/renav2.json') as arquivo_json_smartlog:
#    topologia_arquivo_smartlog = json.load(arquivo_json_smartlog)
#    arquivo_json_smartlog.close()

with open('/opt/gprommonitoracao/monitora_dispositivos/ambientes/renav/configuracao/topologia_rede.json') as arquivo_json_smart:
    topologia_arquivo_smart = json.load(arquivo_json_smart)
    arquivo_json_smart.close()

registro_vazio = {
    "ambiente":"RENAV",
    "teste": [
        "Interface - estado",
        "Interface - pacotes com erro"
    ],
    "localidade" : [
        
    ]
} 

registro_01 = {
            "cidade": "Salvador",
            "equipamento": [
                {
                    "host":"",
                    "ip_gerenciamento":"",
                    "par": [
                        {
                            "membro":"",
                            "interface_local":"",
                            "ip_interface":"",
                            "circuito":"",
                            "operadora":"",
                            "as":""
                        }
                    ]
                }
            ]
        }

registro_02 = {
            "cidade": "Brasilia",
            "equipamento": [
                {
                    "host":"",
                    "ip_gerenciamento":"",
                    "par": [
                        {
                            "membro":"",
                            "interface_local":"",
                            "ip_interface":"",
                            "circuito":"",
                            "operadora":"",
                            "as":""
                        }
                    ]
                }
            ]
        }

for item01 in topologia_arquivo_smart:
    cidade = item01['grupo']
    host = item01['nome']
    ip_gerenciamento = item01['ip_gerencia']

    registro = {
            "cidade": cidade,
            "equipamento": [
                {
                    "host": host,
                    "ip_gerenciamento": ip_gerenciamento,
                    "par": [
                        {
                            "membro":"",
                            "interface_local":"",
                            "ip_interface":"",
                            "circuito":"",
                            "operadora":"",
                            "as":""
                        }
                    ]
                }
            ]
        }

    registro_vazio['localidade'].append(registro)
 


#registro_vazio['localidade'].append(registro_01)
registro_vazio['localidade'].append(registro_02)

print(registro_vazio)



#with open('/opt/gprommonitoracao/SMARTLOG/Smartlog_Beta/app_ConsultaLog/static/entradas/renav3.json', 'w') as arquivo_json_smartlog:
#    json.dump(topologia_arquivo_smartlog,arquivo_json_smartlog)
#    arquivo_json_smartlog.close()


