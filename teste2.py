import json
import os

# Le json do SMART
with open('/opt/gprommonitoracao/monitora_dispositivos/ambientes/renav/configuracao/topologia_rede.json') as arquivo_json_smart:
    topologia_arquivo_smart = json.load(arquivo_json_smart)
    arquivo_json_smart.close()

ambiente = 'RENAV'
teste = ['CONEXAO','BGP','PING']
cidade = 'BRASILIA'
host = 'BACK-01'
ip_gerenciamento = '196.194'
membro = 'SJP'
interface_local = 'Gi4/5'
ip_interface = '42.9'
ip_vizinho = '42.10'
circuito = '85817'
operadora = 'OI'
nas = '65518'

par = {'membro' : membro, 'interface_local' : interface_local, 'ip_interface' : ip_interface, 'ip_vizinho' : ip_vizinho, 'circuito' : circuito, 'operadora' : operadora, 'as' : nas}
equipamento = {'host' : host, 'ip_gerenciamento' : ip_gerenciamento, 'par' : par}
localidade = {'cidade' : cidade, 'equipamento' : equipamento}
raiz = {'ambiente' : ambiente, 'teste' : teste, 'localidade' : localidade}

raiz = json.dumps(raiz)

print(raiz)


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





    for json01 in raiz :
        for json02 in json01['localidade'] :
            if json02['cidade'] == item01['grupo']:
                for json03 in json02['equipamento'] :
                    if json03['host'] == item01['nome'] :
                        # Faltando verificar igualdade de ip de gerencia
                        for json04 in json03['par'] :
                            if json04['membro'] == 'XXX MEMBRO XXX' :
                                print('Este item já existe')
                            else:
                                json04['membro'] = 'XXX XXXXX XXX'
                                json04['interface_local'] = 'XXX XXXXX XXX'
                                json04['ip_interface'] = 'XXX XXXXX XXX'
                                json04['ip_vizinho'] = 'XXX XXXXX XXX'
                                json04['circuito'] = 'XXX XXXXX XXX'
                                json04['operadora'] = 'XXX XXXXX XXX'
                                json04['as'] = 'XXX XXXXX XXX'
                                json04.append()


        
        
        

        





            

        #elemento_antes = [item01['grupo'], item01['nome'], item01['ip_gerencia']] 

    

    #elemento_depois.append(elemento_antes)