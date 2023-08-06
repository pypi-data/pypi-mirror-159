FROM python:3.10-slim

ARG TF_VERSION=1.1.5

ENV TF_INPUT false
ENV TF_CLI_ARGS -no-color

RUN apt-get update \ 
    # Install apt packages
    && apt-get install -y --no-install-recommends git wget unzip \
    # Install terraform
    && wget https://releases.hashicorp.com/terraform/${TF_VERSION}/terraform_${TF_VERSION}_linux_amd64.zip \
    && unzip terraform_${TF_VERSION}_linux_amd64.zip \
    && mv terraform /usr/local/bin/ \
    && rm terraform_${TF_VERSION}_linux_amd64.zip \
    # Clean up
    && apt-get purge -y --auto-remove wget unzip \
    && rm -rf /var/lib/apt/lists/*

RUN pip install mwgapp

ENTRYPOINT ["mwg"]