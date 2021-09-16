import json
import os
import hashlib
import sys


def retorna_resultado_consulta_topologia (ambiente):
    
    with open('/opt/gprommonitoracao/monitora_dispositivos/ambientes/' + ambiente.lower() + '/configuracao/topologia_rede.json', 'rb') as arquivo_json_smart:
        #topologia_original_smart = json.load(arquivo_json_smart)      

        # BUF_SIZE is totally arbitrary, change for your app!
        BUF_SIZE = 65536  # lets read stuff in 64kb chunks!

        md5 = hashlib.md5()

        while True:
            data = arquivo_json_smart.read(BUF_SIZE)
            if not data:
                break
            md5.update(data)
    
        arquivo_json_smart.close()

    

    resultado_hash = format(md5.hexdigest())
    
    try:
        with open('/opt/gprommonitoracao/SMARTLOG/Smartlog_Beta/app_ConsultaLog/static/entradas/' + ambiente.lower() + '10.json', encoding='utf-8') as arquivo_novo_json_smartlog:
            topologia_final_smartlog = json.load(arquivo_novo_json_smartlog)
            arquivo_novo_json_smartlog.close
            resultado = 'Arquivo existe'

    except FileNotFoundError as e:
        resultado = 'Arquivo inexistente'

    return(resultado_hash, resultado)



print(retorna_resultado_consulta_topologia('RENAV'))
print(retorna_resultado_consulta_topologia('EXTRANET'))