import json
import os

# Le json do SMART
with open('/opt/gprommonitoracao/monitora_dispositivos/ambientes/renav/configuracao/topologia_rede.json') as arquivo_json_smart:
    topologia_arquivo_smart = json.load(arquivo_json_smart)
    arquivo_json_smart.close()


ambiente = 'RENAV'
teste = ['conexao','interface - estado',
        'interface - pacotes com erro',
        'BGP - estado vizinho',
        'BGP - divulgacao incompleta',
        'BGP - quedas multiplas',
        'BGP - tempo UP',
        'Ping - perda pacotes',
        'Ping - tempo RTT'
        ]
cidade = ''
host = ''
ip_gerenciamento = ''
membro = ''
interface_local = ''
ip_interface = ''
ip_vizinho = ''
circuito = ''
operadora = ''
nas = ''

par = {"membro" : membro, "interface_local" : interface_local, "ip_interface" : ip_interface, "ip_vizinho" : ip_vizinho, "circuito" : circuito, "operadora" : operadora, "as" : nas}
equipamento = {"host" : host, "ip_gerenciamento" : ip_gerenciamento, "par" : par}
localidade = {"cidade" : cidade, "equipamento" : equipamento}
raiz = json.dumps({"ambiente" : ambiente, "teste" : teste, "localidade" : localidade})

raiz = json.loads(raiz)

print('#############################################')
#print(raiz["ambiente"])
print('#############################################')

#print(raiz)

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

        #elif (item02['tipo'] == 'ping'):
        #    print('  TESTE PING')
        #    for item03 in item02['ips_testar'] :
        #        print('    Testar para IP: {0}, que ta na INTERFACE: {1}, com HOST: {2}, atraves do CIRCUITO: {3}, da OPERADORA: {4}'.format( item03.split('|')[0], item03.split('|')[1].split('#')[0], item03.split('|')[1].split('#')[1].split(' - ')[0], item03.split('|')[1].split('#')[1].split(' - ')[1], item03.split('|')[1].split('#')[1].split(' - ')[1].split(' ')[0] ))

    raiz['ambiente'] = 'RENAV'
    raiz['teste'] = teste
    for json02 in raiz['localidade'] :
        print(json02['cidade'])
        print(cidade)
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
                            json04.append()
                else:
                    json03['host'] = host
                    json03[ip_gerenciamento] = ip_gerenciamento
                    json03.append()
                    for json04 in json03['par'] :
                        json04['membro'] = membro
                        json04['interface_local'] = interface_local
                        json04['ip_interface'] = ip_interface
                        json04['ip_vizinho'] = ip_vizinho
                        json04['circuito'] = circuito
                        json04['operadora'] = operadora
                        json04['as'] = nas
                        json04.append()
        else:
            json02['cidade'] = cidade
            json02.append()
            for json03 in json02['equipamento'] :
                json03['host'] = host
                json03[ip_gerenciamento] = ip_gerenciamento
                json03.append()
                for json04 in json03['par'] :
                    json04['membro'] = membro
                    json04['interface_local'] = interface_local
                    json04['ip_interface'] = ip_interface
                    json04['ip_vizinho'] = ip_vizinho
                    json04['circuito'] = circuito
                    json04['operadora'] = operadora
                    json04['as'] = nas
                    json04.append()

raiz = json.dumps(raiz)


print(raiz)
