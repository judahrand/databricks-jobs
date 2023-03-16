#!/bin/sh

wget https://learn.microsoft.com/en-us/azure/databricks/_extras/api-refs/jobs-2.1-azure.yaml \
    -O schema/jobs-2.1-azure.yaml

patch schema/jobs-2.1-azure.yaml schema/jobs-2.1-azure.diff

openapi-generator generate \
    -i schema/jobs-2.1-azure.yaml \
    -g python-nextgen \
    -o . \
    --additional-properties=packageName=databricks_jobs \
    --global-property=modelTests=false \
    --global-property=apiTests=false

isort databricks_jobs
black databricks_jobs
