# Static site example
> Use Nginx in a container to run a static website

See [Nginx](https://www.nginx.com/) homepage.


## Source

See the Docker Hub docs for the Nginx image:

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

- [localhost:80/](https:localhost:80/)
