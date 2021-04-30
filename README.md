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

This project is based on this [YouTube tutorial](https://www.youtube.com/watch?v=eGz9DS-aIeY) by _NetworkChuck_. That covers the reason containers exist and covers how to create and manage containers in a beginner-friendly way. He covers how to run locally and how to deploy your container to a cloud environment such as Linode, using a $20 credit.

For more background and links around Docker, see my [Docker](https://github.com/MichaelCurrin/learn-to-code/blob/master/en/topics/containers/docker.md) guide.

See also [Awesome Compose](https://github.com/docker/awesome-compose) repo which is similar to this project. It contains examples of Docker apps made with Rust, Go, React, Vue etc. All using `Dockerfile` and `docker-compose.yml`.


## Learn Docker

### Learn the shell approach

A quick way to get started with a container is to choose one specific to an OS, download the image and create and run a container for it - all from the shell.

In this simple case, there is no app to run and there are no custom dependencies. You can do what you like in the container to install and run things and start over if you don't like it. Once you have a simple image built, you can jump to the interactive console to run commands in it.

If you start off by using a `Dockerfile`, you're going to be rerunning the entire `Dockerfile` a few times to fine-tune commands or fix syntax errors. So a good flow is to experiment interactively and then when things work you can move commands to the `Dockerfile` and then build you custom image and not just the generic one.

See the [Docker shell basics](/shell-basics.md) page in this project if you are interested in the light shell-based approach.

### Learn the Dockerfile approach

It is a good idea to start with handling a container using the commands here without worrying about creating any files yet. Then later you can move to the file-based approach, where commands you run by hand in the shell are now in a recipe which can be reproduced easily by you or someone else - anyone with the `Dockerfile`. This recipe is the `Dockerfile` - useful if you have a few or many image build steps such as setting up an app and its dependencies.

See the [Using Dockerfiles](/using-dockerfiles.md) page in this project if you are interested in that.


## How to use this project

If you are confident with Docker or have gone through the Dockerfile notes linked above, then follow this section to the project locally and run some examples from the shell or from the examples directory.

### Installation

#### Install system dependencies

Follow the [Download and install](https://docs.docker.com/get-docker/) guide on the Docker docs site. Or see the [Install Docker](https://github.com/MichaelCurrin/learn-to-code/blob/master/en/topics/containers/docker.md#install-docker) section of my Learn to Code project.

#### Clone

Then clone the repo and navigate to it.

```sh
$ git clone git@github.com:MichaelCurrin/docker-quickstarts.git
$ cd docker-quickstarts
```

### Usage

- [Docker shell basics](/shell-basics.md)
    - Follow the steps to download images from Docker Hub and create containers from them.
    - No `Dockerfile` or app directories needed. So you don't need to clone this repo to run the steps.
- [Example projects](/examples/)
    - Follow instructions for each example you are interested in. 
    -The `Dockerfile` is important as it defines and base image and any configuration suitable for the app or chosen programming language.


## License

Released under [MIT](/LICENSE) by [@MichaelCurrin](https://github.com/MichaelCurrin).
