# eso_logs_dashboards

## Get GraphQL schema

```bash
curl --request POST \
  --url https://www.esologs.com/oauth/token \
  --header 'Authorization: Basic <client_id>:<client_secret>' \
  --header 'Content-Type: multipart/form-data' \
  --form grant_type=client_credentials
```

## Generate python classes

```bash
datamodel-codegen --input schema.json --input-file-type=json --output schema.py
```

## Linting before commit

```bash
pdm run ruff check .
```

```bash
pdm run black . --check
```

```bash
pdm run mypy .
```