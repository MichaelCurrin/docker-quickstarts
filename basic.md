# Basic
> How to create and manager docker containers - with no `Dockerfile`.


## Create a Linux container

Note that this not use any files in this repo.

### Choose a base image

Ideas:

- `centos`
- `alpine` (Debian)
- `archlinux`
- `ubuntu` (same as `ubuntu:latest`)
- `ubuntu:20.04`


We use `centos` for the example below, but `ubuntu` is another good choice.

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
