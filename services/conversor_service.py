from .taxa_cambio_service import obter_taxas_cambio

def converter_moeda(valor, moeda_origem, moeda_destino):
    taxas = obter_taxas_cambio()
    
    if moeda_origem not in taxas or moeda_destino not in taxas:
        raise ValueError("Moeda não suportada")
    
    valor_usd = valor / taxas[moeda_origem]
    
    valor_convertido = valor_usd * taxas[moeda_destino]
    
    return round(valor_convertido, 2)