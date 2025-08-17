
# Health Data Pipeline

 1. Overview
This project aims to build a **complete health data pipeline** using Python.  
It covers **data extraction from public APIs**, **processing through Medallion layers (Bronze, Silver, Gold)**, and **visualization with interactive dashboards**.




## Technical Stack

| Component            | Recommended Version | Purpose                  |
|----------------------|---------------------|--------------------------|
| **Python**           | 3.11+               | Main programming language |
| **Apache Airflow**   | 2.9.x               | Workflow orchestration   |
| **DuckDB**           | 1.1+                | Analytical queries over Parquet |
| **Pandas**           | 2.2+                | Data transformations     |
| **PyArrow**          | 16+                 | Parquet interoperability |
| **Pandera**          | 0.20+               | Data validation schemas  |
| **HTTPX/Requests**   | 0.27+ / 2.32+       | API data extraction      |
| **Streamlit**        | 1.36+               | Interactive dashboards   |
| **Plotly**           | 5.22+               | Visualizations           |
| **Docker**           | 26+                 | Containerization         |
| **docker-compose**   | 2.25+               | Service orchestration    |
| **pytest**           | 8+                  | Automated testing        |

## Project Structure

```
health-pipeline/
├─ dags/ # Airflow DAGs
├─ src/
│ ├─ extract/ # API extractors
│ ├─ load/ # Data loading (Parquet, DuckDB)
│ ├─ transform/ # Cleaning and standardization
│ ├─ dq/ # Data quality checks (pandera)
│ └─ utils/ # Logging, retry, configs
├─ data/
│ ├─ bronze/ # Raw data
│ ├─ silver/ # Standardized data
│ └─ gold/ # Analytical datasets
├─ dash/ # Streamlit/Dash app
├─ tests/ # Unit and integration tests
├─ docker-compose.yaml # Example config (see below)
├─ Dockerfile
├─ requirements.txt # Example dependencies (see below)
├─ Makefile
└─ README.md
```
## Prerequisites

Before starting, make sure you have installed:

- [Python 3.11+](https://www.python.org/downloads/)  
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) or [Docker Engine](https://docs.docker.com/engine/install/)
- [docker-compose](https://docs.docker.com/compose/install/)  
- [Git](https://git-scm.com/downloads)
- [VSCode](https://code.visualstudio.com/)
## Environment Setup

### Clone the repository
```bash
git clone https://github.com/your-user/health-pipeline.git
cd health-pipeline
```

### Create a Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate # Linux/Mac
.venv\Scripts\activate # Windows
```

### Install dependencies
```bash
pip Install -r requirements.txt
```

### Run with Docker (Full Environment including Airflow + Streamlit)
```bash
docker compose up --build -d
```