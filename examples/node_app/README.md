# Node app

Based on Node.js sample from Docker labs repo.

- https://github.com/docker/labs/tree/master/developer-tools/nodejs/porting/
- https://github.com/docker/labs/blob/master/developer-tools/nodejs/porting/2_application_image.md


## Usage

```sh
$ cd examples/node_app
```

Build and tag as `node-app`.

```sh
$ docker build -t node-app .
```

Run it.

```sh
$ docker run node-app
```

Note that this example is note complete so will exit immediately.

If you want to get into the Bash shell:

```sh
$ docker run -it --entrypoint bash node-app
```

That will start a new container.
