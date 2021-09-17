import json
import os

def cria_arquivo_topologia_smart(ambiente):

    with open('/opt/gprommonitoracao/monitora_dispositivos/ambientes/' + ambiente.lower() + '/configuracao/topologia_rede.json') as arquivo_json_smart:
        topologia_original_smart = json.load(arquivo_json_smart)
        arquivo_json_smart.close()

    if ambiente == 'acesso-internet':
        topologia_final_smartlog = {
            'hash': '',
            'ambiente' : 'ACESSO-INTERNET',
            'teste' : [],
            'localidade' : []
            }
    elif ambiente == 'bovespa':
        topologia_final_smartlog = {
            'hash': '',
            'ambiente' : 'BOVESPA',
            'teste' : [],
            'localidade' : []
            }
    elif ambiente == 'crbb':
        topologia_final_smartlog = {
            'hash': '',
            'ambiente' : 'CRBB',
            'teste' : [],
            'localidade' : []
            }
    elif ambiente == 'extranet':
        topologia_final_smartlog = {
            'hash': '',
            'ambiente' : 'EXTRANET',
            'teste' : [],
            'localidade' : []
            }
    elif ambiente == 'man-df':
        topologia_final_smartlog = {
            'hash': '',
            'ambiente' : 'MAN-DF',
            'teste' : [],
            'localidade' : []
            }
    elif ambiente == 'renav':

        topologia_final_smartlog = {
            'hash': '',
            'ambiente' : 'RENAV',
            'teste' : [
                "conexao",
                "interface - estado",
                "interface - pacotes com erro",
                "BGP - estado vizinho",
                "BGP - divulgacao incompleta",
                "BGP - quedas multiplas",
                "BGP - tempo UP",
                "Ping - perda pacotes",
                "Ping - tempo RTT"],
            'localidade' : []
            }

        # - Altera o conteudo do GRUPO para CIDADE
        for item01 in topologia_original_smart:
            if (item01['grupo'] == 'BSB-CCT-I') or (item01['grupo'] == 'BSB-CCT-II'):
                item01['grupo'] = 'BRASILIA'
            elif (item01['grupo'] == 'SP-VD') or (item01['grupo'] == 'SP-AP'):
                item01['grupo'] = 'SAO PAULO'
            elif (item01['grupo'] == 'RJ-TL') or (item01['grupo'] == 'RJ-SD'):
                item01['grupo'] = 'RIO DE JANEIRO'
            elif (item01['grupo'] == 'SJP'):
                item01['grupo'] = 'SAO JOSE DOS PINHAIS'
            elif (item01['grupo'] == 'SDR'):
                item01['grupo'] = 'SALVADOR'
            elif (item01['grupo'] == 'BHE'):
                item01['grupo'] = 'BELO HORIZONTE'
            else:
                item01['grupo'] = 'nulo'

        # - Cria uma lista com cidades para indexar
        #   a nova topologia
        cidades = []
        for item01 in topologia_original_smart:
            if item01['grupo'] not in cidades:
                cidades.append(item01['grupo'])        

        # - Funcao que recebe a cidade da LISTA CIDADES,
        #   indexa a nova topologia, e preenche os itens
        #   da mesma.
        def agrega_cidade (cidade):
            localidade = {
                'cidade' : cidade,
                'equipamento' : []
                }
            for item01 in topologia_original_smart:
                if item01['grupo'] == cidade:
                    equipamento = {
                        'host' : item01['nome'],
                        'ip_gerenciamento' : item01['ip_gerencia'],
                        'par' : []
                        }
                    for item02 in item01['testes']:
                        if item02['tipo'] == 'interface':
                            for item03 in item02['nomes_interfaces']:
                                par = {
                                    'membro' : item03.split('#')[1].split(' - ')[0],
                                    'interface_local' : item03.split('#')[0],
                                    'ip_interface' : item03.split(';;')[1].split('--')[0],
                                    'ip_vizinho' : item03.split('--')[1],
                                    'circuito' : item03.split(' - ')[1].split(';;')[0].split(' ')[1],
                                    'operadora' : item03.split('#')[1].split(' - ')[1].split(' ')[0],
                                    'as' : 'AS'
                                    }

                                equipamento['par'].append(par)

                    localidade['equipamento'].append(equipamento)

            topologia_final_smartlog['localidade'].append(localidade)

        # - Chama a funcao e cria a nova topologia
        for item01 in cidades:
            agrega_cidade(item01)



        with open('/opt/gprommonitoracao/SMARTLOG/Smartlog_Beta/app_ConsultaLog/static/entradas/renav.json', 'w', encoding='utf-8') as arquivo_novo_json_smartlog:
            json.dump(topologia_final_smartlog, arquivo_novo_json_smartlog, ensure_ascii=False, indent=2)
            arquivo_novo_json_smartlog.close()








    elif ambiente == 'worldnet':
        topologia_final_smartlog = {
            'hash': '',
            'ambiente' : 'WORLDNET',
            'teste' : [],
            'localidade' : []
            }


    

    

    

    


cria_arquivo_topologia_smart('renav')