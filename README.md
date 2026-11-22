# 🚴‍♂️ Pipeline ETL Bikestore — Azure Databricks & Asset Bundles

![Azure Databricks](https://shields.io)
![PySpark](https://shields.io)
![Python](https://shields.io)
![YAML](https://shields.io)

## 📋 Sobre o Projeto

Este projeto implementa um pipeline de Engenharia de Dados *end-to-end* utilizando o conjunto de dados **Bikestore**, processado no **Azure Databricks** com **PySpark** e armazenado no **Azure Data Lake Storage (ADLS)** seguindo a **Arquitetura Medalhão** (*Bronze, Silver e Gold*).
<img width="1567" height="375" alt="arquitetura_armazenamento_bikestore" src="https://github.com/user-attachments/assets/2d467da2-1b39-4df7-b80f-0fa9f2ce1aa5" />
<img width="1576" height="461" alt="arquitetura_armazenamento_diretorios" src="https://github.com/user-attachments/assets/f284af7f-928b-4bfa-8e96-6590af1f75da" />
<img width="1540" height="692" alt="arquitetura_armazenamento_origem" src="https://github.com/user-attachments/assets/29ef64c0-0042-4ffb-ad33-27488652be72" />

<img width="1561" height="706" alt="arquitetura_armazenamento_camada_bronze" src="https://github.com/user-attachments/assets/59fcb80d-39b1-4f75-a328-36ac7dddc159" />
<img width="1572" height="442" alt="arquitetura_armazenamento_camada_silver" src="https://github.com/user-attachments/assets/121fc966-735c-4e7d-b854-ef2af5da9b95" />
<img width="1547" height="422" alt="arquitetura_armazenamento_camada_gold" src="https://github.com/user-attachments/assets/4c6207fd-cf01-4237-b8d3-53a1ab7ef203" />

O grande diferencial desta entrega é ir além da criação manual de notebooks na interface gráfica, aplicando práticas de **Engenharia de Dados como Código (IaC)** através do **Databricks Asset Bundles (`databricks.yml`)**:

* ✅ **Workflow como Código:** Orquestração de **14 tasks** (ingestão, limpeza e regras de negócio) declaradas em arquivos YAML.
* ✅ **Modularização:** Funções utilitárias isoladas e reutilizáveis em Python para padronizar transformações.
* ✅ **Controle de Ambientes:** Versionamento completo com Git e deploy padronizado entre ambientes (`dev` e `prod`) via Databricks CLI.

---

## 🏗️ Arquitetura de Dados (Medalhão)

1. **🥉 Camada Bronze (Raw):** Ingestão dos dados brutos da base Bikestore no ADLS mantendo a fidelidade da origem.
2. **🥈 Camada Silver (Trusted):** Limpeza, tratamento de nulos, tipagem de dados, deduplicação e padronização utilizando funções modulares em PySpark.
3. **🥇 Camada Gold (Refined):** Aplicação de regras de negócio, cruzamentos e agregações prontas para consumo analítico e BI.

---

## ⚙️ Orquestração do Workflow (14 Tasks)

Abaixo está a execução completa do pipeline orquestrado via Databricks Workflows e definido via Asset Bundles:

<img width="1916" height="1017" alt="execucao_job_bikestore" src="https://github.com/user-attachments/assets/1a1e48d4-678b-4eb0-8bdf-50350ab3d697" />


*(Caso a imagem acima não carregue, substitua o link pelo link original da imagem que você já colou no seu README).*

---

## 📂 Estrutura do Repositório

```text
Projeto_Azure_Databricks/
├── Codigo/                 # Scripts e notebooks de desenvolvimento
├── funcoes_diversas/       # Módulos Python com funções utilitárias reutilizáveis
├── resources/              # Definições YAML dos Jobs e recursos do Databricks
├── src/                    # Códigos-fonte principais do pipeline (Bronze, Silver, Gold)
├── databricks.yml          # Arquivo principal de configuração do Databricks Asset Bundle
└── README.md               # Documentação do projeto
```

---

## 🚀 Como Executar o Projeto (Databricks CLI)

Para validar e implantar este bundle em um workspace Azure Databricks:

1. **Clone o repositório:**
   ```bash
   git clone https://github.com
   cd Projeto_Azure_Databricks
   ```

2. **Valide a configuração do bundle:**
   ```bash
   databricks bundle validate
   ```

3. **Faça o deploy no ambiente de desenvolvimento (`dev`):**
   ```bash
   databricks bundle deploy -t dev
   ```

4. **Execute o workflow:**
   ```bash
   databricks bundle run bikestore -t dev
   ```

---

## 👨‍💻 Autor

Desenvolvido por **Jefferson Gonçalves** — [GitHub]([https://github.com/Jegoncalves86/Projeto_Azure_Databricks/))


