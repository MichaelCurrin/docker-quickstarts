# Static site example
> Using Nginx to run a static website


## Source

Nginx image docs:

- https://hub.docker.com/_/nginx

Follow that guide for more advanced usage.


## Usage

```sh
$ cd examples/static_site
```

Build image.

```sh
$ docker build -t my-nginx-image .
```

Create container and run server.

```sh
$ docker run --name my-nginx-container my-nginx-image -d
```

Open in the browser:

- https:localhost:80/
