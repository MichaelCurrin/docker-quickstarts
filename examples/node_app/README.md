# Node app

Based on Node.js sample from th Docker labs repo -

In this sample we use thee [node](https://hub.docker.com/_/node/) from DockerHub and the [express](https://www.npmjs.com/package/express) NPM package.


## Resources

- [Node docker web app](https://nodejs.org/en/docs/guides/nodejs-docker-webapp/) from Node dos.
- [Docker Node Mongo](https://github.com/docker/labs/tree/master/developer-tools/nodejs/porting/) example from Docker labs repo.
- [Create a simple Node.js Hello World Docker Container from scratch](https://flaviocopes.com/docker-node-container-example/)
- [Express Quickstart](https://github.com/MichaelCurrin/express-quickstart)


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
Starting dev server on http://0.0.0.0:80
```

The Node app is serving on port `8080`, but Docker routes that to port `80` on the host.

Open the browser at:

- http://localhost:80


### Setup and run on the host

```sh
$ npm install
```

```sh
$ npm start
```

Open the browser at:

- http://localhost:8080
