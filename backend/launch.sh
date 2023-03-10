source venv/bin/activate

export $(grep -v '^#' ../.env | xargs)

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser --no-input
python3 manage.py runserver 0:9000