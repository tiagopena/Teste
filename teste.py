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
    print('=============================================================')
    print('CIDADE:      {0}'.format(item01['grupo']))
    print('HOST:        {0}'.format(item01['nome']))
    print('IP_GERENCIA: {0}'.format(item01['ip_gerencia']))

    for item02 in item01['testes'] :

        if (item02['tipo'] == 'interface'):
            print('  TESTAR INTERFACES')
            for item03 in item02['nomes_interfaces'] :                
                print('    INTERFACE: {0}, com HOST: {1}, atraves do CIRCUITO: {2}'.format(item03.split('#')[0],item03.split('#')[1].split(' - ')[0],item03.split('#')[1].split(' - ')[1]))

        elif (item02['tipo'] == 'bgp'):
            print('  TESTAR BGP')
            for item03 in item02['ip_vizinhos'] :
                print('    IP VIZINHO: {0}, da INTERFACE: {1}, no CIRCUITO: {2}'.format(item03.split('#')[0],item03.split('#')[1].split(' - ')[0],item03.split('#')[1].split(' - ')[1]))

        elif (item02['tipo'] == 'ping'):
            print('  TESTE PING')
            for item03 in item02['ips_testar'] :
                print('    Testar para IP: {0}, que ta na INTERFACE: {1}, com HOST: {2}, atraves do CIRCUITO: {3}, da OPERADORA: {4}'.format( item03.split('|')[0], item03.split('|')[1].split('#')[0], item03.split('|')[1].split('#')[1].split(' - ')[0], item03.split('|')[1].split('#')[1].split(' - ')[1], item03.split('|')[1].split('#')[1].split(' - ')[1].split(' ')[0] ))
        

        





            

        #elemento_antes = [item01['grupo'], item01['nome'], item01['ip_gerencia']] 

    

    #elemento_depois.append(elemento_antes)




#data = {}
#data['ambiente'] = 'CRBB'
#json_data = json.dumps(data)




#print(elemento_depois)