# Python app

This example is based on the [Python](https://hub.docker.com/_/python) section on Docker Hub.

This example app is based on the docs there.

```sh
$ cd examples/python_app
```


## Usage

Build:

```sh
$ docker build -t my-python-app .
```

Run container:

```
$ docker run -it --rm --name my-running-app my-python-app
```
```
Hello, World!
```


## Run without a Dockerfile

Run your Python app in a container without using a Dockerfile..

This is a lighter approach. Instead of setting up a Dockerfile, you create a container using the `python:3.9` image and run a container as a binary executable.

```sh
$ docker run -it --rm \
    --name my-python-app \
    -v "$PWD":/usr/src/myapp \
    -w /usr/src/myapp \
    python:3.9 \
    python app.py
```
```
Hello, World!
```

Notes:

- This can be used a drop-in replacement for this:
    ```sh
    $ python3 app.py
    ```
- You might want to add that long `docker` command as an alias or shell script or add it to `Makefile`.
- File access.
    - We give it access to the files in your repo using the `-v, --volume` flag, to avoid having to copy images into the container.
    - This also means that file changes in or out the container are seen **immediately**. Compare with using `COPY` in a Dockerfile, which means you have to rebuild the whole image and container whenever you make even a small code change in your scripts.
- The container is deleted after each run.


## Choosing an image

A `python` image used is from the DockerHub account linked above.

Pick a tag based on a Python version you want.

- `FROM python:3.9`
- `FROM python:3` - for latest. Warning this may make your app unstable.

Or pick a specific OS like:

- `FROM python:3.9-alpine`
- `FROM python:3.9-buster`

You can use a generic Ubuntu image, but you will have less control and transparency over what Python version you get.

- `FROM ubuntu:18.04`
