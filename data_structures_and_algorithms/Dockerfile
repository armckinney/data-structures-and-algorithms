FROM armck/python-base:latest

LABEL   deployable="true" \
        decription="This is the deployable version of the WEF application container. \
                    It only includes nessecary items to run the application."

# Set Working Directory
ENV WORKDIR=/data-structures-and-algorithms
WORKDIR ${WORKDIR}

# Avoid warnings by switching to noninteractive
ENV DEBIAN_FRONTEND=noninteractive

# Bring project files into container
COPY ./poetry.lock ./pyproject.toml ${WORKDIR}/
COPY ./data_structures_and_algorithms ${WORKDIR}/data_structures_and_algorithms

RUN cd $WORKDIR/ && poetry install --no-root --without=dev


# ----- Container Command -----
# exec commands do not run in shell by default (See: https://docs.docker.com/engine/reference/builder/#cmd)
CMD ["/bin/bash", "-c", "poetry run uvicorn data_structures_and_algorithms.main:app --host 0.0.0.0 --port 8008"]


