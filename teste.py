import json
import os

# Le json do SMART
with open('/opt/gprommonitoracao/monitora_dispositivos/ambientes/renav/configuracao/topologia_rede.json') as arquivo_json_smart:
    topologia_arquivo_smart = json.load(arquivo_json_smart)
    arquivo_json_smart.close()

elemento = []

elemento_depois = []

print('====== INICIO DA EXECUCAO ========================================')

for item01 in topologia_arquivo_smart :
    print('=============')
    print('CIDADE:      {0}'.format(item01['grupo']))
    print('HOST:        {0}'.format(item01['nome']))
    print('IP_GERENCIA: {0}'.format(item01['ip_gerencia']))

    for item02 in item01['testes'] :

        if (item02['tipo'] == 'interface'):
            print('==INTERFACES')
            for item03 in item02['nomes_interfaces'] :                
                print('  INTERFACE: {0}'.format(item03.split('#')[0]))
                print('    INTERFACE: {0}, com HOST: {1}, atraves do CIRCUITO: {2}'.format(item03.split('#')[0],item03.split('#')[1].split(' - ')[0],item03.split('#')[1].split(' - ')[1]))

        elif (item02['tipo'] == 'bgp'):
            for item03 in item02['ip_vizinhos'] :
                print(item03)

        elif (item02['tipo'] == 'ping'):
            for item03 in item02['ips_testar'] :
                print(item03)
        

        





            

    elemento_antes = [item01['grupo'], item01['nome'], item01['ip_gerencia']] 

    

    elemento_depois.append(elemento_antes)




data = {}
data['ambiente'] = 'CRBB'
json_data = json.dumps(data)




#print(elemento_depois)