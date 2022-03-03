import requests
import json

f1 = open('caminhoes.json',)
caminhoes = json.load(f1)

for caminhao in caminhoes:
    
        page = requests.post('https://veiculos.fipe.org.br/api/veiculos//ConsultarModelos?codigoTipoVeiculo=3&codigoTabelaReferencia=279&codigoMarca='+caminhao['Value'])
        r = page.json()
        r1 = r['Modelos']

        f2 = open('marcas/'+caminhao['Label']+".json", "a")
        f2.write(json.dumps(r1))
        f2.close()

f1.close()




