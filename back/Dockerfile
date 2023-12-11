# Specify the base image:
FROM python:3.10-slim-bullseye

# Install the pip requirements:
RUN pip install --upgrade pip
ADD /requirements.txt /
RUN pip install -r /requirements.txt

# Add the application code:
COPY . .

# Environment variables:
#ENV PG_HOST=localhost
#ENV PG_PORT=5432
#ENV PG_USER=my_database_user
#ENV PG_PASSWORD=""
#ENV PG_DATABASE=my_database

CMD ["python3","-m", "main"]