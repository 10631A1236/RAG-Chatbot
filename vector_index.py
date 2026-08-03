# Databricks notebook source
# MAGIC %pip install -U --quiet mlflow databricks-vectorsearch 
# MAGIC dbutils.library.restartPython()

# COMMAND ----------

dbutils.library.restartPython()

# COMMAND ----------

dbutils.widgets.text("index_name", "development.dev_gen_ai.raw_documentation_vs_index")
dbutils.widgets.text("vector_search_endpoint_name", "retrieve_workflow_docs")
dbutils.widgets.text("source_table_fullname","development.dev_gen_ai.raw_documentation")
dbutils.widgets.text("embedding_model_endpoint_name", "databricks-gte-large-en")
dbutils.widgets.text("source_column", "content")

# COMMAND ----------

index_name=dbutils.widgets.get("index_name")
vs_endpoint=dbutils.widgets.get("vector_search_endpoint_name")
source_table_fullname=dbutils.widgets.get("source_table_fullname")
embedding_model_endpoint_name=dbutils.widgets.get("embedding_model_endpoint_name")
source_column=dbutils.widgets.get("source_column")

# COMMAND ----------

from databricks.vector_search.client import VectorSearchClient

# COMMAND ----------

def create_vs_endpoint(vs_endpoint:str):
    from databricks.vector_search.client import VectorSearchClient
    vsc = VectorSearchClient(disable_notice=True)
    try:
        vsc.get_endpoint(vs_endpoint)
    except:
        vsc.create_endpoint(name=vs_endpoint, endpoint_type="STANDARD")

    vsc.wait_for_endpoint(vs_endpoint)
    print(f"Endpoint named {vs_endpoint} is ready.")

# COMMAND ----------

def create_vs_index(vs_endpoint:str, index_name:str, source_table_fullname:str, source_column:str):
    vsc = VectorSearchClient(disable_notice=True)
    try:
        vsc.get_index(vs_endpoint, index_name)
        print(f"Index {index_name} already exists")
    except:
        vsc.create_delta_sync_index(
            endpoint_name=vs_endpoint,
            index_name=index_name,
            source_table_name=source_table_fullname,
            pipeline_type="TRIGGERED",
            primary_key="id",
            embedding_source_column=f'{source_column}', #The column containing our text
            embedding_model_endpoint_name=f'{embedding_model_endpoint_name}' #The embedding endpoint used to create the embeddings
        )
        print(f"Index {index_name} created")
    vsc.get_index(vs_endpoint, index_name).wait_until_ready()
    print(f"Index {index_name} is up and synced, ready to be used ")

# COMMAND ----------

create_vs_endpoint(vs_endpoint) if vs_endpoint else print('Endpoint name is not defined.')

# COMMAND ----------

#create_vs_index(vs_endpoint, index_name, source_table_fullname, source_column)

# COMMAND ----------

