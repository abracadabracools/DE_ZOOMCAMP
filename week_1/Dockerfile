FROM python:3.9.1

# Install required Python packages
RUN pip install pandas sqlalchemy psycopg2-binary requests

# Set the working directory inside the container
WORKDIR /app

# Copy your ingestion script into the container
COPY ingest_data.py ingest_data.py 

# Run the ingestion script by default
ENTRYPOINT ["python", "ingest_data.py"]
