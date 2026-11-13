# Seus caminhos originais
bronze_path = "abfss://projetoanac@externalazureanac.dfs.core.windows.net/bikestore/bronze/"
silver_path = "abfss://projetoanac@externalazureanac.dfs.core.windows.net/bikestore/silver/"
gold_path = "abfss://projetoanac@externalazureanac.dfs.core.windows.net/bikestore/gold/"
resource_path = "abfss://projetoanac@externalazureanac.dfs.core.windows.net/bikestore/resource/origem"
resource_path_volume = (
    "/Volumes/bikestore/logistics/bikestore_resource/origem/"
)

def buscar_caminho(camada: str) -> str:
    """Retorna o caminho em formato string baseado na camada informada."""
    # Tratando o parâmetro para minúsculas para evitar erros de digitação (ex: 'Bronze' virar 'bronze')
    camada_tratada = camada.lower()

    # Correção da Sintaxe: Atribuição correta dentro de cada bloco condicional
    if camada_tratada == "bronze":
        caminho = bronze_path
    elif camada_tratada == "silver":
        caminho = silver_path
    elif camada_tratada == "gold":
        caminho = gold_path
    elif camada_tratada == "resource":
        caminho = resource_path
    elif camada_tratada == "resource_volume":
        caminho = resource_path_volume
    else:
        raise ValueError(
            f"Camada '{camada}' não encontrada no mapeamento de caminhos."
        )

    return caminho

def gerar_tabela_temporaria():
    bronze_path = buscar_caminho("bronze")
    
    bronze_map = {
        "tmp_bronze_brands":     f"{bronze_path}/brands",
        "tmp_bronze_categories": f"{bronze_path}/categories",
        "tmp_bronze_customers":  f"{bronze_path}/customers",
        "tmp_bronze_order_items":f"{bronze_path}/order_items",
        "tmp_bronze_orders":     f"{bronze_path}/orders",
        "tmp_bronze_products":   f"{bronze_path}/products",
        "tmp_bronze_staffs":     f"{bronze_path}/staffs",
        "tmp_bronze_stocks":     f"{bronze_path}/stocks",
        "tmp_bronze_stores":     f"{bronze_path}/stores"}

    for view_name, path in bronze_map.items():
       (spark.read.format('delta')
         .load(path)
         .createOrReplaceTempView(view_name))
       
    return bronze_map

  



    