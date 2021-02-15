# Go app

See [golang](https://hub.docker.com/_/golang) on DockerHub.


## Usage

```sh
$ cd examples/go_app
```

Build and tag as `go_app`.

```sh
$ docker build -t go_app .
```

Run it.

```sh
$ docker run --rm go_app
```
```
Hello, World!
```
