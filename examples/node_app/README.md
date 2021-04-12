# Node app

Based on Node.js sample from Docker labs repo.

- [Porting](https://github.com/docker/labs/tree/master/developer-tools/nodejs/porting/)
- [Porting - application image](https://github.com/docker/labs/blob/master/developer-tools/nodejs/porting/2_application_image.md)


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

Note that this example is not complete so will exit immediately.

### Shell

If you want to get into the Bash shell to look around or install packages:

```sh
$ docker run -it node-app --entrypoint bash
```

That will start a new container.
