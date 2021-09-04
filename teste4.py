import json
import os

# Le json do SMART
with open('/opt/gprommonitoracao/monitora_dispositivos/ambientes/renav/configuracao/topologia_rede.json') as arquivo_json_smart:
    topologia_arquivo_smart = json.load(arquivo_json_smart)
    arquivo_json_smart.close()

with open('/opt/gprommonitoracao/SMARTLOG/Smartlog_Beta/app_ConsultaLog/static/entradas/renav2.json') as arquivo_json_smartlog:
    topologia_arquivo_smartlog = json.load(arquivo_json_smartlog)
    arquivo_json_smartlog.close()  


print('==============================================')
print(topologia_arquivo_smart)
print('==============================================')
print(topologia_arquivo_smartlog)
print('==============================================')

def inclui_registro (cidade, host, ip_gerenciamento, membro, interface_local, circuito, operadora, ip_interface, ip_vizinho, nas):
    for json02 in topologia_arquivo_smartlog['localidade'] :
        if json02['cidade'] == cidade:
            for json03 in json02['equipamento'] :
                if json03['host'] == host :
                    # Faltando verificar igualdade de ip de gerencia
                    for json04 in json03['par'] :
                        if json04['membro'] == membro :
                            print('Este item já existe')
                        else:
                            json04['membro'] = membro
                            json04['interface_local'] = interface_local
                            json04['ip_interface'] = ip_interface
                            json04['ip_vizinho'] = ip_vizinho
                            json04['circuito'] = circuito
                            json04['operadora'] = operadora
                            json04['as'] = nas
                            #json04.append()
                else:
                    json03['host'] = host
                    json03[ip_gerenciamento] = ip_gerenciamento
                    #json03.append()
                    for json04 in json03['par'] :
                        json04['membro'] = membro
                        json04['interface_local'] = interface_local
                        json04['ip_interface'] = ip_interface
                        json04['ip_vizinho'] = ip_vizinho
                        json04['circuito'] = circuito
                        json04['operadora'] = operadora
                        json04['as'] = nas
                        #json04.append()
        else:
            json02['cidade'] = cidade
            #json02.append()
            for json03 in json02['equipamento'] :
                json03['host'] = host
                json03[ip_gerenciamento] = ip_gerenciamento
                #json03.append()
                for json04 in json03['par'] :
                    json04['membro'] = membro
                    json04['interface_local'] = interface_local
                    json04['ip_interface'] = ip_interface
                    json04['ip_vizinho'] = ip_vizinho
                    json04['circuito'] = circuito
                    json04['operadora'] = operadora
                    json04['as'] = nas
                    #json04.append()


for item01 in topologia_arquivo_smart :    

    cidade = item01['grupo']
    host = item01['nome']
    ip_gerenciamento = item01['ip_gerencia']

    for item02 in item01['testes'] :

        if (item02['tipo'] == 'interface'):
            for item03 in item02['nomes_interfaces'] :
                membro = item03.split('#')[1].split(' - ')[0]
                interface_local = item03.split('#')[0]
                circuito = item03.split('#')[1].split(' - ')[1]
                operadora = item03.split('#')[1].split(' - ')[1].split(' ')[0]

        elif (item02['tipo'] == 'bgp'):
            for item03 in item02['ip_vizinhos'] :
                ip_interface = ''
                ip_vizinho = item03.split('#')[0]
                nas = ''





                for json02 in topologia_arquivo_smartlog['localidade'] :
                    if json02['cidade'] == cidade:
                        for json03 in json02['equipamento'] :
                            if json03['host'] == host :
                                # Faltando verificar igualdade de ip de gerencia
                                for json04 in json03['par'] :
                                    if json04['membro'] == membro :
                                        print('Este item já existe')
                                    else:
                                        json04['membro'] = membro
                                        json04['interface_local'] = interface_local
                                        json04['ip_interface'] = ip_interface
                                        json04['ip_vizinho'] = ip_vizinho
                                        json04['circuito'] = circuito
                                        json04['operadora'] = operadora
                                        json04['as'] = nas
                                        #json04.append()
                            else:
                                json03['host'] = host
                                json03[ip_gerenciamento] = ip_gerenciamento
                                #json03.append()
                                for json04 in json03['par'] :
                                    json04['membro'] = membro
                                    json04['interface_local'] = interface_local
                                    json04['ip_interface'] = ip_interface
                                    json04['ip_vizinho'] = ip_vizinho
                                    json04['circuito'] = circuito
                                    json04['operadora'] = operadora
                                    json04['as'] = nas
                                    #json04.append()
                    else:
                        json02['cidade'] = cidade
                        #json02.append()
                        for json03 in json02['equipamento'] :
                            json03['host'] = host
                            json03[ip_gerenciamento] = ip_gerenciamento
                            #json03.append()
                            for json04 in json03['par'] :
                                json04['membro'] = membro
                                json04['interface_local'] = interface_local
                                json04['ip_interface'] = ip_interface
                                json04['ip_vizinho'] = ip_vizinho
                                json04['circuito'] = circuito
                                json04['operadora'] = operadora
                                json04['as'] = nas
                                #json04.append()


print('==============================================')
print('=============================')
print(topologia_arquivo_smartlog)
print('=============================')
print('==============================================')