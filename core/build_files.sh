#!/bin/bash
set -e

python3.9 -m pip install -r requirements.txt
export DJANGO_SETTINGS_MODULE=core.settings
python3.9 manage.py collectstatic --noinput
