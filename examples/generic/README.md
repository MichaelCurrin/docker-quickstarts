# Generic

A container that is a good base for experimenting or adding to.

The [Dockerfile](Dockerfile) includes some typical steps to get going. It includes `git` so you can easily clone projects into it. Though for a larger project you would copy your local app into the container rather.

```sh
$ cd examples/generic
```

If you run commands from this directory, the [Dockerfile](Dockerfile) here will be used.


## Usage

### Untagged

```sh
$ docker build .
```
Example:
```
...
Successfully built 1a9a100194b6
```

Run it - use the ID from above.

```sh
$ docker run 7bc362688d42
      1       4      16 -
```


### Tagged

Name the image to make it easier to manage.

Build and tag as `generic-app`.

```sh
$ docker build -t generic-app .
```

Run it:

```sh
$ docker run generic-app
      1       4      16 -
```

### Start shell

Get into interactive mode:

```sh
docker run --rm -it generic-app
```
