De notebooks soltos para Engenharia de Dados como Código (IaC) com Azure Databricks e Asset Bundles!
Acabo de concluir e versionar no GitHub um projeto completo de pipeline ETL (Bikestore) utilizando Azure Databricks, Azure Data Lake Storage (ADLS) e PySpark, estruturado na Arquitetura Medalhão (Bronze, Silver e Gold).
O grande diferencial desta entrega foi ir além do desenvolvimento na interface gráfica e implementar Databricks Asset Bundles (databricks.yml):
✅ Todo o Workflow (14 tasks orquestradas entre ingestão, tratamento e regras de negócio) definido como código em YAML;
✅ Modularização de funções utilitárias em Python;
✅ Versionamento completo e controle de ambientes (dev / prod) via Databricks CLI e Git.
<img width="1916" height="1017" alt="execucao_job_bikestore" src="https://github.com/user-attachments/assets/70f4465b-518f-44ab-8404-1259331eee2b" />



