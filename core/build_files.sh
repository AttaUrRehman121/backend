
# Install dependencies
pip install -r requirements.txt

# Set Django settings module
export DJANGO_SETTINGS_MODULE=core.settings

# Collect static files without any input
python3.9 manage.py collectstatic --noinput
