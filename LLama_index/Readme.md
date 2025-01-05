**Llama Index Query Engine with LLM and SQL Database**

This project demonstrates how to integrate Llama Index with an LLM (Large Language Model) and SQL Database to query tables in natural language.
It uses an LLM (could be OpenAI, Azure OpenAI, or any compatible LLM) to process natural language queries and a SQL Database engine to fetch data. 
The project allows for efficient data querying and processing through a custom SQL engine.

**Table of Contents**
1. Project Description
2. Installation
3. Environment Variables
4. Usage
5. Code Explanation


**Project Description**
This project enables querying a SQL Database using natural language by combining:

  LLM for natural language processing (NLP). This can be OpenAI, Azure OpenAI, or any other compatible LLM.
  Llama Index for SQL table query generation and handling.
  SQLAlchemy to create and manage database engine connections.

The goal is to process user queries and fetch relevant results from a database using the query engine powered by NLP.

**Installation**
To use this project, follow the steps below:

**1.Prerequisites**
Ensure you have the following installed:
1. Python 3.8 or higher
2. llama_index - To interact with the LLM and SQL Database.
3. sqlalchemy - To interact with the SQL database.
4. openai or azure-openai - Depending on which LLM service you use.
5. pymssql - SQL server connector for Python.
   
**2. Environment Variables**
Set the following environment variables for your LLM

export LLM_API_KEY="your_api_key"
export LLM_ENDPOINT="end_point"
export LLM_API_VERSION="api_version"

**3. set the database credentials:**

export SQL_USER_NAME="sql_user_name"
export SQL_PASSWORD="sql_password"
export SQL_SERVER_NAME="server_name"
export SQL_DATABASE_NAME="database_name"

**Make sure to replace your_api_key, end_point, api_version, sql_user_name, sql_password, server_name, and database_name with your actual values.**

**Usage**

Run the following Python script to initialize the environment, set up the database, and process user queries:
python main.py

**Code Explanation**
initialize_llm(): Initializes the LLM (Large Language Model) for generating responses.
create_db_engine(): Creates an SQLAlchemy engine to connect to the SQL database using the provided credentials.
initialize_sql_database(): Initializes the SQLDatabase object with the given engine and includes specified tables.
initialize_query_engine(): Initializes the Llama Index query engine using the provided SQL database and LLM.
process_user_query(): Processes the user’s natural language query and returns a response based on the query execution.
main(): Orchestrates the initialization of the system and query processing flow.
