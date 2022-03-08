# workbench_model_storage

Commands to run:

```
$ docker build -t python_wsgi -f Dockerfile .
$ docker run -p 8000:8000 -t -i python_wsgi
```

```
docker-compose build
docker-compose up -d
docker-compose exec -T auto_ml pytest -W ignore::DeprecationWarning
```