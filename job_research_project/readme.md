# Job Research Project
This project originated from my curiosity to explore and learn how to consume an API. While browsing Google, I stumbled upon the following page: RapidAPI Hub – a platform providing various APIs. One particular API caught my attention: JSearch, a powerful job search API that aggregates data from LinkedIn, Indeed, ZipRecruiter, and more.

JSearch offers real-time access to job postings and salary information from Google for Jobs, making it a comprehensive solution for job-related data. With extensive coverage, over 30 data points per job, and advanced search capabilities, JSearch became the perfect choice for integrating job search functionality into my project.

I achieved quick and effective results using the JSearch API, obtaining data in JSON format. Inspired to enhance the project, I delved into the world of databases. Through further research, I discovered the simplicity of setting up a PostgreSQL database with Docker. This eliminated dependency issues and version conflicts while providing easy accessibility to the database and pgAdmin.

Empowered by Docker Compose, I successfully launched my PostgreSQL database and pgAdmin. Having access to pgAdmin from Google without local installation was a significant achievement. With a running database, I improved my Python script to transform JSON-formatted data into a DataFrame for database loading.

Navigating through challenges, especially with columns containing dictionaries, I resolved issues by transforming them into TEXT type. After rigorous testing and approximately 50 script runs, I triumphantly loaded my data into the database. Notably, I utilized Docker Volumes to persist data even after container deletion or shutdown.

Post data loading, I performed queries and created views to identify correct and incorrect data for further analysis. A second transformation was planned in Power BI, where I addressed various data types, handled NaN and NULL values, and specified some fields as 'No specified.'

Following the transformation, I delved into visual and statistical analysis. The results were showcased through a general home page, a map displaying job distribution, and a page with more in-depth statistical analysis.

Visuals:
[![home.png](https://i.postimg.cc/Xq9S5r56/home.png)](https://postimg.cc/D4fMky5x)
[![map.png](https://i.postimg.cc/jqfrmFF3/map.png)](https://postimg.cc/xq97btYL)
[![linechart.png](https://i.postimg.cc/k46dn1X4/linechart.png)](https://postimg.cc/Kk2Wf5TS)


For those interested in exploring the code, Docker Compose, and Python script, everything is available in this repository. Feel free to navigate through the code section.