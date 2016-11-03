#!/bin/bash

if [ ! -d venv ] ; then
    echo "venv not configured, run setup.sh first."
    exit 1
fi

export FLASK_APP=app.py
export APPLICATION_COMMON_CONF=../etc/common.cfg
export APPLICATION_ENV_CONF=../etc/env.cfg

source venv/bin/activate
flask run
