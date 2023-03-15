#!/bin/sh

openapi-generator generate \
    -i schema/jobs-2.1-azure.yaml \
    -g python-nextgen \
    -o . \
    --additional-properties=packageName=databricks_jobs,disallowAdditionalPropertiesIfNotPresent=false \
    --global-property=modelTests=false \
    --global-property=apiTests=false

isort databricks_jobs
black databricks_jobs
