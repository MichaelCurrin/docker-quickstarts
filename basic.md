# Basic
> How to create and manager docker containers without a `Dockerfile`.


## Create a Linux container

Note that this not use any files in this repo.

Here we use `centos` but other ideas are to use `alpine` (Debian) or `archlinux`. Or `ubuntu` or `FROM ubuntu:16.04`.

### Pull

This will use the latest tag by default.

```sh
$ docker pull centos
```

### Run

```sh
$ docker run -d -t --name my-centos centos
```

```sh
$ docker ps
```

### Start terminal

Start a Bash terminal in an already running container. Use `bash` or `sh`.

```sh
docker exec -it my-centos bash
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
$ docker stop my-centos
```


### Start

```sh
$ docker start my-centos
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
