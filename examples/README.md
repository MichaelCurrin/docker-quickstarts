# Example projects

See the `Dockerfile` in each project. 

- The `FROM` line specifies the base image, usually Linux flavor (e.g. `ubuntu`) or a specialized container such as for Python or NodeJS.
- There are usually some `RUN` commands when building the image.
    - This is usually a command to **update** the APT package listing. This is usually required or the next step will fail.
        ```sh
        RUN apt-get update
        ```
    - Then there is a step to install packages. It is useful to add the `-q` quiet flag for cleaner output and the `-y` yes flag to install without asking the user to confirm.
        ```sh
        RUN apt-get update
        ```
    - The `RUN` command can also be used for other commands such as changing permissions, moving files, or downloading and unzipping a file from a URL.
- There is sometimes a `COPY` commnd to copy a file or folder into the container. This is often done to `/` or `/app` but `~` can work as well. Note that the user will be `root` so `sudo` is not needed and the path to `~` will be `/root`. I'd recommend against copying to `/` since there are directories there relating to the system (similar to a system not insider a container).
- Finally there is usually `CMD` or `ENTRYPOINT` at the end. This will only be run when the container starts - not during the build image step.
    - `CMD` sets _default_ command and/or parameters, such as starting a server or entering the Python or Bash shell. The default command can be _ignored_  if overwritten when running the container.
        ```sh
        CMD echo "Hello world"
        ```
    - `ENTRYPOINT` configures a container that will run as an executable. The entry point will _always_ run even if the command is overwritten.
        ```sh
        ENTRYPOINT echo "Hello world"
        ```
        
See more info in this [post](https://goinbigdata.com/docker-run-vs-cmd-vs-entrypoint/).
