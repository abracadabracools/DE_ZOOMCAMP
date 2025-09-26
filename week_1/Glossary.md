# 📚 Data Engineering Glossary

| Term | Definition | Why It Matters | Example / Usage | Where It's Used |
|------|------------|------------------|------------------|------------------|
| **Docker** | A tool to package and run applications inside isolated containers. | Ensures the same environment everywhere (local, dev, prod). | `docker run -it postgres:13` | Deploying DBs, services, pipelines |
| **Container** | A lightweight, standalone runtime environment. | Keeps dependencies and environments separate and reproducible. | Postgres container running inside Docker | Every stage of a data pipeline |
| **Volume** | A way to persist data outside the container lifecycle. | Without volumes, DB data is lost when containers stop. | `-v $(pwd)/data:/var/lib/postgresql/data` | Database storage, ETL output |
| **Docker Network** | Virtual network for containers to communicate. | Needed for services like Postgres & pgAdmin to talk. | `docker network create pg-network` | Multi-service pipelines |
| **PostgreSQL** | An open-source relational database system. | Stores structured data for querying and analysis. | `postgres:13` image | Data ingestion, storage, transformation |
| **SQLAlchemy Engine** | A Python object for connecting to databases. | Lets pandas and scripts send SQL commands. | `create_engine("postgresql://root:root@localhost:5432/ny_taxi")` | ETL scripts, ingestion jobs |
| **pgcli** | CLI tool for interacting with Postgres. | Makes testing queries faster during development. | `pgcli -h localhost -p 5432 -u root -d ny_taxi` | Debugging & quick queries |
| **pgAdmin** | Web UI for managing PostgreSQL visually. | Helps you browse tables, run queries, and inspect schemas. | Access via `http://localhost:8080` | Admin tasks, validation |
| **Docker Compose** | Tool to run multi-container apps via a single YAML config. | Starts entire stack (DB, pgAdmin, scripts) at once. | `docker-compose up` | Real-world pipeline deployments |
| **SQL Schema** | The structure of a database table (columns, types). | Defines how data is stored and queried. | `pd.io.sql.get_schema(df, name="table", con=engine)` | Database design, ingestion validation |
