# Basic
> How to create and manage containers from the shell - **without** using creating any files

## Intro

### The shell approach approach
A quick way to get started with a container is to choose one specific to an OS, download the image and create and run a container for it - all from the shell.

In this simple case, there is no app to run and there are no custom dependencies. You can do what you like in the container to install and run things and start over if you don't like it. Once you have a simple image built, you can jump to the interactive console to run commands in it.

If you start off by using a `Dockerfile`, you're going to be rerunning the entire `Dockerfile` a few times to fine-tune commands or fix syntax errors. So a good flow is to experiment interactively and then when things work you can move commands to the `Dockerfile` and then build you custom image and not just the generic one.

### When can I use a Dockerfile?

It is a good idea to start with handling a container using the commands here without worrying about creating any files yet. Then later you can move to the file-based approach, where commands you run by hand in the shell are now in a recipe which can be reproduced easily by you or someone else - anyone with the `Dockerfile`. This recipe is the `Dockerfile` - useful if you have a few or many image build steps such as setting up an app and its dependencies. 

See [examples](/examples/) section of this project if you are interested in that.


## Create a Linux container

You can run the commands in this guide without a copy of this `docker-quickstart` repo and without creating a `Dockerfile`.

### Choose a base image

All containers need a base image. First figure out what OS you want and then find an appropriate image.

We use `centos` for the example below, but you can use `ubuntu` or something else of course.

Here are some flavors of Linux:

- `centos`
- `alpine` (Debian)
- `archlinux`
- `ubuntu`

If you want to specify a version, you can do something like this:

- `ubuntu:latest` (same as just using `ubuntu`)
- `ubuntu:20.04`

The [Docker hub](https://hub.docker.com/) site is a good place to look for more options. You don't have to download from the site, as you just need a valid name to reference on the command-line. If you want, you can choose something more specialized like a Node.js, Python or Go container (which internally probably uses Ubuntu.

Note that you can run Linux containers on a Linux, Windows or macOS system. However, you can only run a Windows container on a Windows machine, based on this [thread](https://stackoverflow.com/questions/42158596/can-windows-containers-be-hosted-on-linux).


### Pull

This will use the latest tag by default.

```sh
$ docker pull centos
```

### Run

<!-- TODO These can be moved to another repo and keep this lighter and less instructional and less thorough -->

#### Basic

```sh
$ docker run centos
```

You'll see output logged. If you prefer to run in the background:

```sh
$ docker run -d centos
```

```
  -d, --detach                         Run container in background and print container ID
```

#### Clean up

```sh
$ docker run --rm -d centos
```

Use this flag to remove the container when it is finished.

```
      --rm                             Automatically remove the container when it exits
```

#### Name

Start a container using a custom name - e.g. `my-container`.

```sh
$ docker run -d -t --name my-container centos
```

#### Run interactive

Run interactive shell. 

```sh
$ docker run -it centos
```

```
  -i, --interactive                    Keep STDIN open even if not attached
  -t, --tty                            Allocate a pseudo-TTY
```  


### Check running containers

```sh
$ docker ps
```

Example output:

```
CONTAINER ID        IMAGE                   COMMAND                  CREATED             STATUS              PORTS                      NAMES
8332318ac5b5        centos                  "/bin/bash"              8 seconds ago       Up 6 seconds                                   my-container

```

### Start terminal

Start a Bash terminal in an already running container. Use `bash` or `sh`.

```sh
docker exec -it my-container bash
```

Now you're in the container.

```sh
[root@abcde1234 /]#
```

Look around.

```sh
[root@abcde1234 /]# ls
bin dev etc ...
```

Exit using `exit` for <kbd>CTRL</kbd>+<kbd>D</kbd>


```sh
[root@abcde1234 /]#
```

### Stop

```sh
$ docker stop my-container
```

### Start

Start the container up again. You'll keep any data and packages you have before.

```sh
$ docker start my-container
```

### Remove

Delete a container. You must stop it first.

```sh
$ docker rm my-container
```

Or use this to remove the container when it exits.

```sh
docker run -rm OPTIONS
```

## Use Network Chuck's image

Download image which has been tagged "frenchpress". This could be a version number too.

```sh
$ docker pull thenetworkchuck/nccoffee:frenchpress
```

```sh
$ docker run -t -d -p 80:80 --name nccoffee thenetworkchuck:frenchpress
```

## Check usage of containers


```sh
$ docker stats
```
