# Node app

Based on Node.js sample from th Docker labs repo -

In this sample we use thee [node](https://hub.docker.com/_/node/) from DockerHub and the [express](https://www.npmjs.com/package/express) NPM package.


## Resources

- [Node.js docker web app](https://nodejs.org/en/docs/guides/nodejs-docker-webapp/) from Node docs.
- [Create a simple Node.js Hello World Docker Container from scratch](https://flaviocopes.com/docker-node-container-example/)
- [Express Quickstart](https://github.com/MichaelCurrin/express-quickstart)
- [Docker Node Sails Mongo](https://github.com/docker/labs/tree/master/developer-tools/nodejs/porting/) example from Docker labs repo.


## Usage

```sh
$ cd examples/node_app
```

### Setup and run Docker Node app

Build and tag as `node-app`.

```sh
$ docker build -t node-app .
```

Run the app - this will start a dev server.

```sh
$ docker run --rm -p 80:8080 node-app
Listening on http://localhost:80
```

The Node app is serving on port `8080`, but Docker routes that to port `80` on the host.

Open the browser at:

- http://localhost:80


### Set up and run on the host

```sh
$ npm install
```

```sh
$ npm start
```

Open the browser at:

- http://localhost:8080


## Notes

Around use of NPM in the [Dockerfile](Dockerfile).

- Your app should probably have a lockfile. Then you can use `npm ci` instead of `npm install`.
- On cache clearing, the idea it to keep the image smaller by deleting cached downloads which are not needed for running. You should not have to run on your host but it helps for Docker images.
- The `--production` flag keeps the container lighter by not installing dev dependencies.
- The `--loglevel warn` part keeps the log lighter, by only showing warning and higher.
