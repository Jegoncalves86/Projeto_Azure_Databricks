
-- Schemas e volumes externos
CREATE CATALOG IF NOT EXISTS projetobd;

CREATE SCHEMA IF NOT EXISTS projetobd.azure;

create external volume projetobd.azure.projeto_anac -- volume aparecer no catalog Databricks 
comment 'Volume externo na Azure'
location 'abfss://projetoanac@externalazureanac.dfs.core.windows.net/projeto_anac' -- pasta dentro do Azure  ideal Volume e Catalog e pasta azure ter o mesmo nome



