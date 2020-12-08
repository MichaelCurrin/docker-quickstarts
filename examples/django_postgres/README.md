# Django Postgres example

Based on:

- https://docs.docker.com/compose/django/

See that page for further instructions.

```sh
$ docker-compose run web django-admin startproject composeexample .
```

Note - the original project required `Django>=2.0,<3.0` but there was a vulnerability requiring `3.0.7` or higher so that was adjusted. The sample project might not work the same.
