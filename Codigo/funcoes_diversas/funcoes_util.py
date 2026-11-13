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

def gerar_tabela_temporaria(tabelas: list, camada: str = "bronze"):
    """
    Recebe uma lista com os nomes das tabelas e a camada,
    monta o dicionário automaticamente e cria as views temporárias.
    """
    spark = SparkSession.builder.getOrCreate()
    caminho_base = buscar_caminho(camada)  # Reutiliza sua função buscar_caminho!

    # Monta o dicionário automaticamente a partir da lista de nomes
    mapa_tabelas = {
        f"tmp_{camada}_{tabela}": f"{caminho_base}{tabela}"
        for tabela in tabelas
    }

    # Cria as views normalmente
    for view_name, path in mapa_tabelas.items():
        (
            spark.read.format("delta")
            .load(path)
            .createOrReplaceTempView(view_name)
        )
        print(f"View '{view_name}' criada com sucesso!")

    return mapa_tabelas
