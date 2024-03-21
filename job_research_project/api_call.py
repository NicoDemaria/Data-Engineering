import requests
import os
import pandas as pd
import psycopg2
import time
import json

url = "https://jsearch.p.rapidapi.com/search"
pd.set_option("display.max_columns", None)
default_query = os.environ.get("JOB_TITLE", "Data engineer")

query = default_query

querystring = {"query": query, "page": "1", "num_pages": "20"}

headers = {
    "X-RapidAPI-Key": "removed for security reasons, please use your own key in the following link: https://rapidapi.com/letscrape-6bRBa3QguO5/api/jsearch/",
    "X-RapidAPI-Host": "jsearch.p.rapidapi.com",
}
time.sleep(10)

response = requests.get(url, headers=headers, params=querystring)

df = pd.DataFrame(response.json()["data"])

for i in range(2, 20):
    querystring["page"] = str(i)
    response = requests.get(url, headers=headers, params=querystring)

    page_data = pd.DataFrame(response.json()["data"])
    df = pd.concat([df, page_data], ignore_index=True)

    print(f"Obteniendo datos de la página {i}...")


try:
    with psycopg2.connect(
        user="admin",
        password="admin",
        host="db",
        port=5432,
        database="job_research_project_DB",
    ) as connection:
        with connection.cursor() as cursor:
            # Eliminar la tabla existente (puedes comentar esto si no es necesario)
            cursor.execute("DROP  TABLE IF EXISTS jobs CASCADE")

            # Crear la tabla
            cursor.execute(
                """CREATE TABLE jobs (
                id serial PRIMARY KEY,
                employer_name VARCHAR(255),
                employer_logo VARCHAR(255),
                employer_website VARCHAR(255),
                job_title VARCHAR(255),
                job_description TEXT,
                job_apply_link VARCHAR(255),
                employer_company_type VARCHAR(255),
                job_publisher VARCHAR(255),
                job_id VARCHAR(255),
                job_employment_type VARCHAR(255),
                job_apply_is_direct BOOLEAN,
                job_apply_quality_score FLOAT,
                job_is_remote BOOLEAN,
                job_posted_at_timestamp VARCHAR(255),
                job_posted_at_datetime_utc timestamp,
                job_city VARCHAR(255),
                job_state VARCHAR(255),
                job_country VARCHAR(255),
                job_latitude FLOAT,
                job_longitude FLOAT,
                job_benefits TEXT,
                job_google_link VARCHAR(255),
                job_offer_expiration_datetime_utc timestamp,
                job_offer_expiration_timestamp VARCHAR ,
                job_required_skills TEXT,
                job_experience_in_place_of_education BOOLEAN,
                job_min_salary FLOAT,
                job_max_salary FLOAT,
                job_salary_currency VARCHAR(255),
                job_salary_period VARCHAR(255),
                job_job_title VARCHAR(255),
                job_posting_language VARCHAR(255),
                job_onet_soc VARCHAR(255),
                job_onet_job_zone INT,
                job_naics_code VARCHAR(255),
                job_naics_name VARCHAR(255),
                apply_options TEXT,
                job_required_education TEXT,
                job_highlights TEXT,
                job_occupational_categories TEXT,
                job_required_experience TEXT
                

            )"""
            )

            # Iterar sobre las filas y realizar inserciones solo con algunos campos
            for index, row in df.iterrows():
                # Extraer valores del diccionario
                employer_name = row["employer_name"]
                employer_logo = row["employer_logo"]
                employer_website = row["employer_website"]
                job_title = row["job_title"]
                job_description = row["job_description"]
                job_apply_link = row["job_apply_link"]
                employer_company_type = row["employer_company_type"]
                job_publisher = row["job_publisher"]
                job_id = row["job_id"]
                job_employment_type = row["job_employment_type"]
                job_apply_is_direct = row["job_apply_is_direct"]
                job_apply_quality_score = row["job_apply_quality_score"]
                job_is_remote = row["job_is_remote"]
                job_posted_at_timestamp = row["job_posted_at_timestamp"]
                job_posted_at_datetime_utc = row["job_posted_at_datetime_utc"]
                job_city = row["job_city"]
                job_state = row["job_state"]
                job_country = row["job_country"]
                job_latitude = row["job_latitude"]
                job_longitude = row["job_longitude"]
                job_benefits = row["job_benefits"]
                job_google_link = row["job_google_link"]
                job_offer_expiration_datetime_utc = row[
                    "job_offer_expiration_datetime_utc"
                ]
                job_offer_expiration_timestamp = row["job_offer_expiration_timestamp"]
                job_required_skills = row["job_required_skills"]
                job_experience_in_place_of_education = row[
                    "job_experience_in_place_of_education"
                ]
                job_min_salary = row["job_min_salary"]
                job_max_salary = row["job_max_salary"]
                job_salary_currency = row["job_salary_currency"]
                job_salary_period = row["job_salary_period"]
                job_job_title = row["job_job_title"]
                job_posting_language = row["job_posting_language"]
                job_onet_soc = row["job_onet_soc"]
                job_onet_job_zone = row["job_onet_job_zone"]
                job_naics_code = row["job_naics_code"]
                job_naics_name = row["job_naics_name"]

                # Se tranforma el diccionario a un string para poder insertarlo en la base de datos gracias a json.dumps
                apply_options = json.dumps(row["apply_options"])
                job_required_education = json.dumps(row["job_required_education"])
                job_highlights = json.dumps(row["job_highlights"])
                job_occupational_categories = json.dumps(
                    row["job_occupational_categories"]
                )
                job_required_experience = json.dumps(row["job_required_experience"])

                try:
                    cursor.execute(
                        """
                        INSERT INTO jobs (
                            employer_name, employer_logo, employer_website, job_title, job_description,job_apply_link, employer_company_type,job_publisher,job_id,job_employment_type,job_apply_is_direct,job_apply_quality_score,job_is_remote,job_posted_at_timestamp,job_posted_at_datetime_utc,job_city,job_state,job_country,job_latitude,job_longitude,job_benefits,job_google_link,job_offer_expiration_datetime_utc,job_offer_expiration_timestamp,job_required_skills,job_experience_in_place_of_education,job_min_salary,job_max_salary,job_salary_currency,job_salary_period,job_job_title,job_posting_language,job_onet_soc,job_onet_job_zone,job_naics_code,job_naics_name,apply_options,job_required_education,job_highlights,job_occupational_categories,job_required_experience
                        ) VALUES (
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s, 
                            %s, 
                            %s, 
                            %s, 
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s, 
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s
                            
                        )
                    """,
                        (
                            employer_name,
                            employer_logo,
                            employer_website,
                            job_title,
                            job_description,
                            job_apply_link,
                            employer_company_type,
                            job_publisher,
                            job_id,
                            job_employment_type,
                            job_apply_is_direct,
                            job_apply_quality_score,
                            job_is_remote,
                            job_posted_at_timestamp,
                            job_posted_at_datetime_utc,
                            job_city,
                            job_state,
                            job_country,
                            job_latitude,
                            job_longitude,
                            job_benefits,
                            job_google_link,
                            job_offer_expiration_datetime_utc,
                            job_offer_expiration_timestamp,
                            job_required_skills,
                            job_experience_in_place_of_education,
                            job_min_salary,
                            job_max_salary,
                            job_salary_currency,
                            job_salary_period,
                            job_job_title,
                            job_posting_language,
                            job_onet_soc,
                            job_onet_job_zone,
                            job_naics_code,
                            job_naics_name,
                            apply_options,
                            job_required_education,
                            job_highlights,
                            job_occupational_categories,
                            job_required_experience,
                        ),
                    )

                    print(f"Insertando fila {index} en la tabla 'jobs'...")

                except Exception as e:
                    print(f"Error al insertar fila {index} en la tabla 'jobs': {e}")

    print("Datos insertados exitosamente en la tabla 'jobs'")
except Exception as e:
    print("Error al insertar datos en la tabla 'jobs':", e)
