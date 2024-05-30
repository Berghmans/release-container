ARG PYTHON_VERSION
FROM python:${PYTHON_VERSION}-slim-bookworm

ARG NODE_VERSION

# Install Node.js version 20
RUN echo "https://deb.nodesource.com/setup_${NODE_VERSION}" && \
    curl -fsSL https://deb.nodesource.com/setup_${NODE_VERSION} | bash -

# Install apt packages
COPY packages.list .
RUN apt-get update && \
    xargs -a packages.list apt-get install -y && \
    rm -rf /var/lib/apt/lists/*

# Install pipenv
RUN pip install --no-cache-dir pipenv

# Install necessary Python packages
COPY Pipfile Pipfile.lock .
RUN pipenv install --deploy --system

# Install necessary Node.js packages
COPY package.json package-lock.json .
RUN npm install -g $(cat package.json | jq -r '.dependencies | keys | join(" ")')

# Set the working directory to a clean directory
WORKDIR /app

ENTRYPOINT ["/bin/bash", "-c"]
