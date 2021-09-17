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

localidade = {
    "cidade" : "",
    "equipamento" : []
        }

equipamento = {
    "host" : "",
    "ip_gerenciamento" : "",
    "par" : [
    ]
}

par = {
    "membro" : "",
    "interface_local" : "",
    "ip_interface" : "",
    "ip_vizinho" : "",
    "circuito" : "",
    "operadora" : "",
    "as" : ""
    }

for item01 in topologia_arquivo_smart:

    cidade = item01['grupo']
    host = item01['nome']
    ip_gerenciamento = item01['ip_gerencia']


    lista_interface = []
    lista_bgp = []
    y2 = []
    z3 = []
        
    for item02 in item01['testes']:
        
        if (item02['tipo'] == 'interface'):
            for item03 in item02['nomes_interfaces']:
                membro = item03.split('#')[1].split(' - ')[0]
                interface_local = item03.split('#')[0]
                circuito = item03.split('#')[1].split(' - ')[1]
                operadora = item03.split('#')[1].split(' - ')[1].split(' ')[0]

                #lista_interface.append(item03)
                par = {'membro' : membro, 'interface_local' : interface_local, 'circuito' : circuito, 'operadora' : operadora}
                lista_interface.append(par)

            #print(lista_interface)

        elif (item02['tipo'] == 'bgp'):
            for item04 in item02['ip_vizinhos']:
                #membro = item04.split('#')[1].split(' - ')[0]
                ip_vizinho = item04.split('#')[0]
                ip_interface = ''
                nas = ''
                
                #par = membro, ip_vizinho, nas
                #lista_bgp.append(par)

            #print(lista_bgp)

    
    equipamento['par'].append(lista_interface)
    equipamento = {'host' : host, 'ip_gerenciamento' : ip_gerenciamento, 'par' : [] }
    
    
    
    y2.append(equipamento)
    localidade = {'cidade' : cidade, 'equipamento' : [] }
    localidade['equipamento'].append(y2)

    z3.append(localidade)
    registro_vazio['localidade'].append(z3)


print(registro_vazio)
    
    

    












        

            

        
        





'''
                lista_interface.append(item03)

            for item03 in item02['bgp']:
                membro = item03.split('#')[1].split(' - ')[0]
                ip_vizinho = item03.split('#')[0]

                lista_bgp.append(item03)
'''

'''
            for item04 in lista_interface:
                #membro_index = item04['membro']
                for item05 in lista_bgp:
                    if item05['membro'] == item04['membro']:
                        ip_interface = ''
                        nas = ''
                        item04['ip_vizinho'] = item05['ip_vizinho']
                    
'''



#print(interfaces)
#print(vizinhos)
#print(testar_ips)


#        if (item02['tipo'] == 'interface'):
#            print(item02['nomes_interfaces'])
#        if (item02['tipo'] == 'bgp'):
#            print(item02['ip_vizinhos'])
#        if (item02['tipo'] == 'ping'):
#            print(item02['ips_testar'])
        

'''
        if (item02['tipo'] == 'interface'):

            for item03 in item02['nomes_interfaces'] :
                membro = item03.split('#')[1].split(' - ')[0]
                interface_local = item03.split('#')[0]
                circuito = item03.split('#')[1].split(' - ')[1]
                operadora = item03.split('#')[1].split(' - ')[1].split(' ')[0]

                par_01 = {
                    "membro" : membro,
                    "interface_local" : interface_local,
                    "circuito" : circuito,
                    "operadora" : operadora,
                }

                x.append(par_01)

            z.append(x)

        elif (item02['tipo'] == 'bgp'):
            
            for item03 in item02['ip_vizinhos'] :
                membro = item03.split('#')[1].split(' - ')[0]
                ip_interface = ""
                ip_vizinho = item03.split('#')[0]
                nas = ""

                par_02 = {
                    "membro" : membro,
                    "ip_interface" : ip_interface,
                    "ip_vizinho" : ip_vizinho,                
                    "as" : nas
                }

                y.append(par_02)

            z.append(y)

    print('=========================================================')
    print(z)
    print('=========================================================')

'''