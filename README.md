
# Health Data Pipeline

 1. Overview
This project aims to build a **complete health data pipeline** using Python.  
It covers **data extraction from public APIs**, **processing through Medallion layers (Bronze, Silver, Gold)**, and **visualization with interactive dashboards**.




## Technical Stack

| Component            | Recommended Version | Purpose                  |
|----------------------|---------------------|--------------------------|
| **Python**           | 3.11+               | Main programming language |
| **Apache Airflow**   | 2.11x               | Workflow orchestration   |
| **DuckDB**           | 1.1+                | Analytical queries over Parquet |
| **Pandas**           | 2.2+                | Data transformations     |
| **PyArrow**          | 16+                 | Parquet interoperability |
| **Pandera**          | 0.20+               | Data validation schemas  |
| **HTTPX/Requests**   | 0.27+ / 2.32+       | API data extraction      |
| **Streamlit**        | 1.36+               | Interactive dashboards   |
| **Plotly**           | 5.22+               | Visualizations           |
| **Docker**           | 26+                 | Containerization         |
| **docker-compose**   | 3+                  | Service orchestration    |
| **pytest**           | 8+                  | Automated testing        |
| **jupyter/pyspark-notebook**          | Latest                  | Testing, exploring data|

## Project Structure

```
health_data_pipeline/
├─ app/ # Streamlit/Dash app
├─ dags/ # Airflow DAGs
├─ Data/
│ ├─ bronze/ # Raw data
│ ├─ silver/ # Standardized data
│ └─ gold/ # Analytical datasets
├─ logs/ # Airflow Logs
├─ notebooks/ # Jupyter notebooks
├─ postgres-init/ # Postgres init persistence
├─ requirements/ # Requirements folder
├─ docker-compose.yaml 
├─ Dockerfile.airflow
├─ Dockerfile.jupyter
├─ Dockerfile.streamlit
└─ README.md
```
## Prerequisites

Before starting, make sure you have installed:

- [Python 3.11+](https://www.python.org/downloads/)  
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) or [Docker Engine](https://docs.docker.com/engine/install/)
- [docker-compose](https://docs.docker.com/compose/install/)  
- [Git](https://git-scm.com/downloads)
- [VSCode](https://code.visualstudio.com/)

And guarantee these ports are open in your firewall:
- 8080
- 5433
- 5432
- 8501
- 8888

## Environment Setup

### Clone the repository
```bash
git clone https://github.com/Paul0Junior/health_data_pipeline.git
cd health_data_pipeline
```

### Build up containers with Docker
```bash
docker compose build --no-cache
```
### Run containers
```bash
docker compose up # If you want to debug the first execution, just in case....
docker compose up -d # If you are more confident :D
```

### Acessing the apps:

After running the guide above, you should be able to access all Apps.
If you are running on your local machine, these are the links you wanna access:

- [Airfow](http://localhost:8080/)
- [Jupyter Notebook](http://localhost:8888/lab)
- [Streamlit App](http://localhost:8501/)


