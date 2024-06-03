ARG PYTHON_VERSION
FROM python:${PYTHON_VERSION}-slim-bookworm

ARG NODE_VERSION

RUN apt-get update && \
    apt-get install -y curl ca-certificates

# Install Node.js version 20
RUN echo "https://deb.nodesource.com/setup_${NODE_VERSION}" && \
    curl -fsSL https://deb.nodesource.com/setup_${NODE_VERSION} | bash -

# Install docker
RUN install -m 0755 -d /etc/apt/keyrings && \
    curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc && \
    chmod a+r /etc/apt/keyrings/docker.asc && \
    echo \
      "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian \
      $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
      tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install apt packages
COPY packages.list .
RUN apt-get update && \
    xargs -a packages.list apt-get install -y && \
    rm -rf /var/lib/apt/lists/*

# Install necessary Python packages
COPY requirements.txt .
RUN pip install -r requirements.txt

# Install necessary Node.js packages
COPY package.json package-lock.json .
RUN npm install -g $(cat package.json | jq -r '.dependencies | keys | join(" ")')

# Set the working directory to a clean directory
WORKDIR /app

ENTRYPOINT ["/bin/bash", "-c"]
