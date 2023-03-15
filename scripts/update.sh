#!/bin/sh

openapi-generator generate \
    -i schema/jobs-2.1-azure.yaml \
    -g python-nextgen \
    -o . \
    --additional-properties=packageName=databricks_jobs \
    --global-property=modelTests=false \
    --global-property=apiTests=false
black databricks_jobs
