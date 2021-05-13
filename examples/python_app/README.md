# Python app

This example is based on the [Python](https://hub.docker.com/_/python) section on Docker Hub.

This example app is based on the docs there.

```sh
$ cd examples/python_app
```


## Related projects

A template for a basic Python app including CI and docs. You can easily add Docker to it.

[![MichaelCurrin - py-project-template](https://img.shields.io/static/v1?label=MichaelCurrin&message=py-project-template&color=blue&logo=github)](https://github.com/MichaelCurrin/py-project-template)


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
Standard greeting:
Hello, World!

Requesting: http://httpbin.org/get?message=Hello,%20World!
Status: 200
JSON response:
{'args': {'message': 'Hello, World!'}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.25.1', 'X-Amzn-Trace-Id': 'Root=1-60336ebd-1e87133e371bbc97206c224f'}, 'origin': '165.255.x.x', 'url': 'http://httpbin.org/get?message=Hello, World!'}
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
    python greet.py
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
- Dependencies
    - With the Dockerfile approach, you install dependencies in the image. You don't even need a virtual environment as global is safe in a container.
    - With the no-Dockerfile approach, you need to install dependencies outside your container. Preferably in a virtual environment in your project as `venv`, which can be accessed in the container. The container won't be able to access any globally-installed packages on your host, unless you specifically add a path as another volume. The example above uses the [greet.py](greet.py) script, having no dependencies.


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


## Using make

If you prefer, in your `Dockerfile` your install step can be:

```Dockerfile
RUN make install
```

And then setup:

- `Makefile`
    ```Makefile
    install:
        pip install -r requirements.txt --no-cache-dir 
    ```

And maybe upgrade `pip` or install dev dependencies too.

The no-cache option was recommended in the Python DockerHub section. It stops downloaded packages from being kept in the cache. This keeps your image smaller. It works fine outside of a container too - your installs might just be slower.
