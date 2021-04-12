# Node app

Based on Node.js sample from th Docker labs repo - 

The image used here [node](https://hub.docker.com/_/node/) from Docker Hub.

## Resources

- [Node docker web app](https://nodejs.org/en/docs/guides/nodejs-docker-webapp/) from Node dos.
- [Docker Node Mongo](https://github.com/docker/labs/tree/master/developer-tools/nodejs/porting/) example from Docker labs repo.
- [Create a simple Node.js Hello World Docker Container from scratch](https://flaviocopes.com/docker-node-container-example/)


## Usage

```sh
$ cd examples/node_app
```

Build and tag as `node-app`.

```sh
$ docker build -t node-app .
```

Run it. This will start a dev server.

```sh
$ docker run node-app
```

Open the browser at:

- http://localhost:80

### Shell

If you want to get into the Bash shell to look around or install packages:

```sh
$ docker run -it node-app --entrypoint bash
```

That will start a new container.
