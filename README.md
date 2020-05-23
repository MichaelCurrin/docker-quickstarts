# Docker Quickstart
> Basic steps and files to get going with docker containers

This project assumes some knowledge of Docker already. It provides some commands to manage containers in a beginner-friendly way.

Some basic  projects in various language like Node and Python are included so you can get up and running with those without piecing together a Dockerfile or shell commands yourself. Plus you can use the samples as references when you are working on a real project.  


## Resources

This project is based on this [Youtube tutorial](https://www.youtube.com/watch?v=eGz9DS-aIeY) by _NetworkChuck_. That covers the reason containers exist and covers how to create and manage containers in a beginner-friendly way. He covers how to run locally and how to deploy your container to a cloud environment such as Linode, using a $20 credit.

For more background and links around Docker, see my [Docker](https://github.com/MichaelCurrin/learn-to-code/blob/master/en/topics/containers/docker.md) guide.


## How to use this project

### Installation

Follow the [Download and install](https://docs.docker.com/get-docker/) guide on the Docker docs site.

Then clone the repo.

```sh
$ git clone git@github.com:MichaelCurrin/docker-quickstart.git
$ cd docker-quickstart
```


### Usage

- [Basic](basic.md)
    - Follow the instructions. You don't even need the repo cloned to run the commands.
- [Example projects](examples/)
    - Follow instructions for each example you are interested in. The `Dockerfile` is important as it defines and base image and any configuration suitable for the app or chosen programming language.
 


## License

Released under [MIT](/LICENSE).
