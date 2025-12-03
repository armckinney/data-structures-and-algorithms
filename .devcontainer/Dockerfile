FROM armck/python:3.9.5

LABEL   deployable="false" \
    decription="This is the development version of the WEF application container. \
    It includes the application and required development tools."

ARG WORKSPACE=/workspaces/data-structures-and-algorithms
ENV WORKSPACE=${WORKSPACE}

# avoid warnings by switching to noninteractive
ENV DEBIAN_FRONTEND=noninteractive


RUN mkdir /tmp/dockerinstall \
    && cd /tmp/dockerinstall \
    # install
    && apt update && apt install -y \
    wget \
    # cleanup
    && apt autoremove -y \
    && apt clean -y \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /tmp/dockerinstall

COPY poetry.lock pyproject.toml ${WORKSPACE}/
RUN cd $WORKSPACE && poetry install --no-root

WORKDIR ${WORKSPACE}

# switch back to dialog for any ad-hoc use of apt-get
ENV DEBIAN_FRONTEND=dialog
