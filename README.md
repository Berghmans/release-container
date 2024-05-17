# release-container

A container image that contains python and semantic-release, together with some other useful tools.

## Getting Started

See [release-container](https://github.com/Berghmans/release-container/pkgs/container/release-container%2Frelease-container)

### Getting the Docker Image

To get the Docker image from GitHub Container Registry, you can use the following command:

```
docker pull ghcr.io/berghmans/release-container/release-container:py3.12.3-node20.13.1
```

Adjust the tag to the prefered version.

When using in another Dockerfile, you can use:

```
FROM ghcr.io/berghmans/release-container/release-container:py3.12.3-node20.13.1
```
