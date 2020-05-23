# Static site example

Using Nginx to run a static website.

https://hub.docker.com/_/nginx

```
$ cd examples/static-site
```

Commands from the Nginx image docs.

```sh
docker build -t some-content-nginx .

```

```sh
$ docker run --name some-nginx some-content-nginx -d
```
