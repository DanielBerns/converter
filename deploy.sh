#!/bin/zsh

pip install -r config/requirements.txt
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
pytest
test_status=$(echo $?)
supervisorctl restart all
exit $test_status