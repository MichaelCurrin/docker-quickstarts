# Docker Quickstarts 📦📦📦🐳
> Instructions and sample projects to get started with Docker containers

[![GitHub tag](https://img.shields.io/github/tag/MichaelCurrin/docker-quickstarts?include_prereleases=&sort=semver)](https://github.com/MichaelCurrin/docker-quickstarts/releases/)
[![License](https://img.shields.io/badge/License-MIT-blue)](#license)

[![Made with - Docker](https://img.shields.io/badge/Made_with-Docker-blue?logo=docker&logoColor=white)](https://www.docker.com/)


## Intro

This project assumes some knowledge of Docker already. It provides some commands to manage containers in a beginner-friendly way.

Some basic projects are provided so you can get up and running with those without piecing together a Dockerfile or shell commands yourself. Plus you can use the samples as references when you are working on a real project.

Tools and languages in the examples:

- Node
- Python
- Go
- Python + Django + PostgreSQL
- Nginx

The examples are built around a minimal setup like:

- `README.md` with instructions and shell commands.
- `Dockerfile`
- A language-specific script and config.

In larger applications, it would be a good idea to use a `docker-compose` setup, to make the shell commands you use much shorter.


## Resources

See my [Containers][] section of Dev Resources to learn more about Docker, Docker CLI, Dockerfile, Docker Compose, and more.

[Containers]: https://michaelcurrin.github.io/dev-resources/resources/containers/

This quickstart project is based on this [YouTube tutorial](https://www.youtube.com/watch?v=eGz9DS-aIeY) by _NetworkChuck_. That covers the reason containers exist and covers how to create and manage containers in a beginner-friendly way. He covers how to run locally and how to deploy your container to a cloud environment such as Linode, using a $20 credit.

See also [Awesome Compose](https://github.com/docker/awesome-compose) repo which is similar to this project. It contains examples of Docker apps made with Rust, Go, React, Vue etc. All using `Dockerfile` and `docker-compose.yml`.


## How to use this project

If you are confident with Docker or have gone through the Dockerfile notes linked above, then follow this section to the project locally and run some examples from the shell or from the examples directory.

### Installation

#### Install system dependencies

See [Docker Install](https://michaelcurrin.github.io/dev-cheatsheets/cheatsheets/containers/docker/install.html) guide.

#### Clone

Clone the repo and navigate to it:

```sh
$ git clone git@github.com:MichaelCurrin/docker-quickstarts.git
$ cd docker-quickstarts
```

### Usage

#### Project examples

See the [example](/examples/) directory.

Follow instructions for each example that you are interested in.

The `Dockerfile` in each is important as it defines and base image and any configuration suitable for the app or chosen programming language.

#### Generic CLI examples

For basics on using Docker CLI, see [Docker shell basics][] cheatsheet.

No `Dockerfile` files or app directories are needed there. So you can run those commands directly and without having this repo cloned.

Follow the steps there to download images from Docker Hub and then create containers from them.

e.g.

```sh
$ docker pull centos
$ docker run centos
```

[Docker shell basics]: https://michaelcurrin.github.io/dev-cheatsheets/cheatsheets/containers/docker/intro/shell-only-basics.html


## License

Released under [MIT](/LICENSE) by [@MichaelCurrin](https://github.com/MichaelCurrin).
