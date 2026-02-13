# 🚀 Pipeline de Consolidação de Dados do Tesouro Direto  
### Data Engineering • DataOps • Docker • Airflow • PostgreSQL

---

## 📌 Sobre o Projeto

Este projeto implementa um pipeline completo de Engenharia de Dados responsável por consolidar, transformar e estruturar dados públicos do **Tesouro Direto**, automatizando todo o fluxo de ingestão até a carga final em banco relacional.

### A solução simula um cenário real de mercado onde múltiplos arquivos CSV precisam ser:

- Consolidados  
- Padronizados  
- Modelados  
- Automatizados  
- Orquestrados  

Tudo isso em ambiente containerizado e reprodutível.

---

## 🎯 Problema Resolvido

Os dados públicos do Tesouro Direto são disponibilizados em múltiplos arquivos CSV e não estão estruturados para análise direta.

### Este projeto resolve:

✔ Consolidação de múltiplas fontes  
✔ Padronização de datas e valores monetários  
✔ Modelagem relacional  
✔ Automatização do processo  
✔ Reprodutibilidade com Docker  
✔ Orquestração com Apache Airflow  

---

## 🏗 Arquitetura da Solução

- CSV (dados brutos)
- ↓
- Concatenação
- ↓
- Pipeline ETL (Pandas)
- ↓
- PostgreSQL (Banco do Projeto)
- ↓
- Orquestração via Airflow
- ↓
- Ambiente Containerizado


---

## 🛠 Tecnologias Utilizadas

- Python  
- Pandas  
- PostgreSQL  
- Apache Airflow  
- Docker & Docker Compose  
- SQLAlchemy  

---

## 🗄 Estrutura de Bancos

O projeto utiliza:

### 🔹 Banco de Metadados do Airflow

Responsável por armazenar:

- DAGs  
- Logs  
- Histórico de execução  

---

## 🔹 Banco do Projeto

Banco onde o pipeline grava as tabelas tratadas:

- `titulo`  
- `movimentacao`  

### 📌 **Importante:**  
O nome do banco do projeto deve ser definido nas variáveis de ambiente.  
No desenvolvimento deste projeto foi utilizado o banco:

tesouro

Certifique-se de que o banco esteja criado e configurado corretamente no ambiente Docker antes de executar a DAG.

## ⚙️ Como Executar o Projeto

### 1️⃣ Clone o repositório

- git clone https://github.com/JhonDX/fastapi-docker.git
- cd fastapi-docker

### 2️⃣ Configure as variáveis de ambiente
### Defina corretamente:

- Credenciais do banco

- Nome do banco do projeto

- Caminho do dataset

- Configuração do Airflow

### 📌 O banco do projeto deve estar configurado (ex: tesouro).

### 3️⃣ Suba os containers

- docker compose up -d

### 4️⃣ Acesse o Airflow
- http://localhost:8080
- Ative a DAG e execute manualmente para rodar o pipeline.

### 🔄 Fluxo do Pipeline

- Concatenação dos arquivos CSV

- Transformações:

- Conversão de datas

- Conversão de valores monetários

- Normalização de colunas

- Cálculo de validade dos títulos

## Criação das tabelas:

- titulo

- movimentacao

- Carga automatizada no banco do projeto

- Orquestração via Apache Airflow

## 👥 Colaboração
- Projeto desenvolvido em parceria simulando ambiente real de mercado:

### 👨‍💻 Data Engineering
- Desenvolvimento do pipeline ETL

- Modelagem relacional

- Implementação da DAG

### ⚙️ DevOps
- Containerização

- Infraestrutura Docker

- Configuração do Airflow

### 📈 Possíveis Evoluções
- Camada de API para exposição dos dados

- Monitoramento e alertas

- Testes automatizados

- Integração com ferramentas de BI

- Data Quality Checks

### 💡 Principais Aprendizados
- Construção de pipeline end-to-end

- Integração entre Airflow e PostgreSQL

- Separação entre banco de metadados e banco analítico

- Containerização com Docker

- Organização colaborativa em ambiente DataOps