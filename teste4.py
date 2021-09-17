import json
import os

# Le json do SMART
with open('/opt/gprommonitoracao/monitora_dispositivos/ambientes/renav/configuracao/topologia_rede.json') as arquivo_json_smart:
    topologia_arquivo_smart = json.load(arquivo_json_smart)
    arquivo_json_smart.close()

with open('/opt/gprommonitoracao/SMARTLOG/Smartlog_Beta/app_ConsultaLog/static/entradas/renav2.json') as arquivo_json_smartlog:
    topologia_arquivo_smartlog = json.load(arquivo_json_smartlog)
    arquivo_json_smartlog.close()  


#print('==============================================')
#print(topologia_arquivo_smart)
print('= ORIGINAL ========================================================')
print(topologia_arquivo_smartlog)
print('===================================================================')

def inclui_registro (cidade, host, ip_gerenciamento, membro, interface_local, circuito, operadora, ip_interface, ip_vizinho, nas):
    for json02 in topologia_arquivo_smartlog['localidade'] :
        if json02['cidade'] == cidade:
            print('Entrou em Localidade IGUAL')
            for json03 in json02['equipamento'] :
                if json03['host'] == host :
                    print('Entrou em Equipamento IGUAL')
                    # Faltando verificar igualdade de ip de gerencia
                    for json04 in json03['par'] :
                        if json04['membro'] == membro :
                            print('Entrou em Par IGUAL')
                            print('Este item já existe')
                        else:
                            json04['membro'] = membro
                            json04['interface_local'] = interface_local
                            json04['ip_interface'] = ip_interface
                            json04['ip_vizinho'] = ip_vizinho
                            json04['circuito'] = circuito
                            json04['operadora'] = operadora
                            json04['as'] = nas

                            #json03['par'].append(json04)

                            print('PREENCHIDO ==============================================')
                            print(topologia_arquivo_smartlog)
                            print('*========================================================')

        else:
            json02['cidade'] = cidade
            for json03 in json02['equipamento'] :
                json03['host'] = host
                json03['ip_gerenciamento'] = ip_gerenciamento
                # Faltando verificar igualdade de ip de gerencia
                for json04 in json03['par'] :
                    json04['membro'] = membro
                    json04['interface_local'] = interface_local
                    json04['ip_interface'] = ip_interface
                    json04['ip_vizinho'] = ip_vizinho
                    json04['circuito'] = circuito
                    json04['operadora'] = operadora
                    json04['as'] = nas
                    
                    #json03['par'].append(json04)

        topologia_arquivo_smartlog['localidade'].append(json02)


            #print('PREENCHIDO ==============================================')
            #print(topologia_arquivo_smartlog)
            #print('*========================================================')

    print('FINAL ==================================================')
    print(topologia_arquivo_smartlog)
    print('*========================================================')

inclui_registro (
    'Brasilia1',
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
