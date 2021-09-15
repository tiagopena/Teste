import json
import os


def retorna_resultado_consulta_topologia (ambiente):
    
    with open('/opt/gprommonitoracao/monitora_dispositivos/ambientes/' + ambiente.lower() + '/configuracao/topologia_rede.json') as arquivo_json_smart:
        topologia_original_smart = json.load(arquivo_json_smart)
        arquivo_json_smart.close()

    try:
        with open('/opt/gprommonitoracao/SMARTLOG/Smartlog_Beta/app_ConsultaLog/static/entradas/' + ambiente.lower() + '10.json', encoding='utf-8') as arquivo_novo_json_smartlog:
            topologia_final_smartlog = json.load(arquivo_novo_json_smartlog)
            arquivo_novo_json_smartlog.close

    except FileNotFoundError as e:
        print('Arquivo nao existe')
        cria_arquivo_tolologia_smartlog(ambiente)









        
        #with open('/opt/gprommonitoracao/SMARTLOG/Smartlog_Beta/app_ConsultaLog/static/entradas/renav10.json', 'w+', encoding='utf-8') as arquivo_novo_json_smartlog:
        #    json.dump(topologia_final_smartlog, arquivo_novo_json_smartlog, ensure_ascii=False, indent=2)
        #    arquivo_novo_json_smartlog.close


