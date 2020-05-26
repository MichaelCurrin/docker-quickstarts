# Multi stage Docker example

How to combine multiple stages or layer in a Dockerfile - such as adding multiple `FROM` lines.


From [Builder pattern vs. Multi-stage builds in Docker](http://blog.alexellis.io/mutli-stage-docker-builds/)


- Builder Pattern
    - > The builder pattern involves using two Docker images - one to perform a build and another to ship the results of the first build without the penalty of the build-chain and tooling in the first image.
    - Needs 3 separate files:
        - `Dockerfile.build`
        - `Dockerfile`
        - `build.sh
- Multi-stage
    - > The general syntax involves adding `FROM` additional times within your Dockerfile - whichever is the last `FROM `statement is the final base image. To copy artifacts and outputs from intermediate images use `COPY --from=<base_image_number>`.
    - > Multi-stage builds give the benefits of the builder pattern without the hassle of maintaining three separate files.
    - Needs just one file:
        - `Dockerfile`
 
Example of multi-stage `Dockerfile`:
 
```Dockerfile
FROM golang:1.7.3 as builder

WORKDIR /go/src/github.com/alexellis/href-counter/

RUN go get -d -v golang.org/x/net/html
COPY app.go	.

RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o app .

FROM alpine:latest
RUN apk --no-cache add ca-certificates

WORKDIR /root/

COPY --from=builder /go/src/github.com/alexellis/href-counter/app    .

CMD ["./app"]
```
