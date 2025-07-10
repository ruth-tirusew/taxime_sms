#!/usr/bin/env bash

: "${MODULE_NAME:=app.main}"
: "${VARIABLE_NAME:=app}"
: "${APP_MODULE:=$MODULE_NAME:$VARIABLE_NAME}"
: "${HOST:=0.0.0.0}"
: "${PORT:=8000}"
: "${LOG_LEVEL:=info}"
: "${LOG_CONFIG:=./deploy/configs/logging_uvicorn.ini}"

uvicorn \
    --reload \
    --proxy-headers \
    --host "$HOST" \
    --port "$PORT" \
    --log-config "$LOG_CONFIG" \
    "$APP_MODULE"
