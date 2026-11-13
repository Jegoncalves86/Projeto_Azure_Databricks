from pyspark.sql import SparkSession

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
    camada_tratada = camada.lower()

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
    spark = SparkSession.builder.getOrCreate()
    caminho_bronze = buscar_caminho("bronze")
    
    # Removida a barra extra antes dos nomes, pois caminho_bronze já termina com '/'
    bronze_map = {
        "tmp_bronze_brands":      f"{caminho_bronze}brands",
        "tmp_bronze_categories":  f"{caminho_bronze}categories",
        "tmp_bronze_customers":   f"{caminho_bronze}customers",
        "tmp_bronze_order_items": f"{caminho_bronze}order_items",
        "tmp_bronze_orders":      f"{caminho_bronze}orders",
        "tmp_bronze_products":    f"{caminho_bronze}products",
        "tmp_bronze_staffs":      f"{caminho_bronze}staffs",
        "tmp_bronze_stocks":      f"{caminho_bronze}stocks",
        "tmp_bronze_stores":      f"{caminho_bronze}stores"
    }

    for view_name, path in bronze_map.items():
        (
            spark.read.format("delta")
            .load(path)
            .createOrReplaceTempView(view_name)
        )
        print(f"View '{view_name}' criada com sucesso!")
       
    return bronze_map
