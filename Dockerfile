FROM postgres:13-alpine3.14
ENV POSTGRES_USER demo_user 
ENV POSTGRES_PASSWORD password123
ENV POSTGRES_DB demo

RUN apk add linux-headers 

RUN apk add --no-cache --update \
    git \
    bash \
    libffi-dev \
    openssl-dev \
    bzip2-dev \
    zlib-dev \
    readline-dev \
    sqlite-dev \
    build-base

# Set Python version
ARG PYTHON_VERSION='3.7.0'
# Set pyenv home
ARG PYENV_HOME=/root/.pyenv

# Install pyenv, then install python versions
RUN git clone --depth 1 https://github.com/pyenv/pyenv.git $PYENV_HOME && \
    rm -rfv $PYENV_HOME/.git

ENV PATH $PYENV_HOME/shims:$PYENV_HOME/bin:$PATH

RUN pyenv install $PYTHON_VERSION
RUN pyenv global $PYTHON_VERSION

WORKDIR /app

ARG mode

# set env variables
ENV MODE=$mode

# install dependencies
COPY requirements.txt .
RUN apk add py3-setuptools
RUN apk update && apk add python3-dev gcc libc-dev make  postgresql-dev musl-dev postgresql-libs
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install --upgrade pip && pyenv rehash
RUN curl -sSL https://sdk.cloud.google.com | bash
ENV PATH $PATH:/root/google-cloud-sdk/bin

# copy project
COPY . .

CMD uvicorn main:app --host 0.0.0.0 --port 8000
CMD exec /bin/bash -c "trap : TERM INT; sleep infinity & wait"
