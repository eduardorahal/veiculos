import requests
import json

f1 = open('caminhoes.json',)
marcas = json.load(f1)
for marca in marcas:
    valormarca = marca['Value']
    f2 = open('marcas/'+marca['Label']+'.json')
    modelos = json.load(f2)
    final = []
    for modelo in modelos:
        valormodelo = modelo['Value']
        page = requests.post('https://veiculos.fipe.org.br/api/veiculos//ConsultarAnoModelo?codigoTipoVeiculo=3&codigoTabelaReferencia=279&codigoModelo='+str(valormodelo)+'&codigoMarca='+str(valormarca))
        response = page.json()
        anos = []
        for ano in response:
            anos.append(ano['Label'])
        f3 = open('caminhoes/'+marca['Label']+'.json', "a")
        carro = {'Modelo': modelo['Label'], 'Anos': (anos)}
        final.append(carro)
    f3.write(json.dumps(final))
    f3.close
    f2.close()

f1.close()



