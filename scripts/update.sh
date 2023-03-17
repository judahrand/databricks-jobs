#!/bin/sh

URLS=(
    https://learn.microsoft.com/en-us/azure/databricks/_extras/api-refs/jobs-2.1-azure.yaml
    https://docs.gcp.databricks.com/_extras/api-refs/jobs-2.1-gcp.yaml
    https://docs.databricks.com/_extras/api-refs/jobs-2.1-aws.yaml
)
PLATFORMS=(azure gcp aws)
SCHEMA_FILE="schema/jobs-2.1.yaml"

rm schema/jobs-2.1-*.yaml

for url in ${URLS[@]}
do
    wget --directory-prefix=schema/ $url
done

for platform in ${PLATFORMS[@]}
do
    patch schema/jobs-2.1-$platform.yaml schema/jobs-2.1-$platform.diff
done

yq '. *d load("schema/jobs-2.1-gcp.yaml") *d load("schema/jobs-2.1-azure.yaml")' schema/jobs-2.1-aws.yaml > $SCHEMA_FILE

openapi-generator generate \
    -i $SCHEMA_FILE \
    -g python-nextgen \
    -o . \
    --additional-properties=packageName=databricks_jobs \
    --global-property=modelTests=false \
    --global-property=apiTests=false

isort databricks_jobs
black databricks_jobs
