FROM python:3.9.1

RUN pip install pandas sqlalchemy psycopg2 wget pyarrow

WORKDIR /app
COPY get_green_data.py get_green_data.py
COPY get_zones.py get_zones.py

ENTRYPOINT [ "python", "get_green_data.py", "get_zones.py" ]
