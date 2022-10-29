# 46 degrees ious project

## technologies
- Django Rest Framework
- Sqlite
- swagger
- pytest
### Instalation
create virtual environment 

```
virtualenv -p python3.9 env
```

```cosu
pip install -r requirements.txt 
```

```
python3.9 manage.py makemigrations tracker 
```

```
python3.9 manage.py migrate 
```

Running the server
```
python3.9 manage.py runserver 
```
### Running tests

```
pytest 
```


### url swagger documentation

http://localhost:8000/doc/


### CURL examples

[Example requests](CURL_examples.md)