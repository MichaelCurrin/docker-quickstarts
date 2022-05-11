# Go app

See [golang](https://hub.docker.com/_/golang) image on DockerHub.


## Usage

```sh
$ cd examples/go_app
```

Build and tag as `go_app`:

```sh
$ docker build -t go_app .
```

Run the container:

```console
$ docker run --rm go_app
Hello, World!
```
