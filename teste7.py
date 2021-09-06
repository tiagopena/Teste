import json
import os

with open('/opt/gprommonitoracao/SMARTLOG/Smartlog_Beta/app_ConsultaLog/static/entradas/renav2.json') as arquivo_json_smartlog:
    topologia_arquivo_smartlog = json.load(arquivo_json_smartlog)
    arquivo_json_smartlog.close()

"""
registro_vazio = {
    "ambiente":"RENAV",
    "teste": [
        "Interface - estado",
        "Interface - pacotes com erro"
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
    ]
}
"""

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
    

registro_vazio['localidade'].append(registro_01)
registro_vazio['localidade'].append(registro_02)

print(registro_vazio)



#with open('/opt/gprommonitoracao/SMARTLOG/Smartlog_Beta/app_ConsultaLog/static/entradas/renav3.json', 'w') as arquivo_json_smartlog:
#    json.dump(topologia_arquivo_smartlog,arquivo_json_smartlog)
#    arquivo_json_smartlog.close()


