#!/bin/sh

# Use `project_config.yml` for configuration (if applicable)

exec pipenv run python3 -m app.sqlite_explorer "$@" --config project_config.yml