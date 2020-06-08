# Static site example
> Using Nginx to run a static website

Nginx image docs: 

- https://hub.docker.com/_/nginx

## Usage

```sh
$ cd examples/static-site
```

Build image.

```sh
$ docker build -t some-content-nginx .
```

Run server.

```sh
$ docker run --name some-nginx some-content-nginx -d
```
