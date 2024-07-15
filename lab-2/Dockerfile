FROM ubuntu:latest

# Install packages
RUN apt-get update && apt-get install -y \
    curl \
    bash-completion \
    openjdk-17-jdk \
    fontconfig \
    fonts-dejavu-core \
    software-properties-common \
    python3-pip \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install ANTLR
COPY antlr-4.13.1-complete.jar /usr/local/lib/antlr-4.13.1-complete.jar

COPY ./commands/antlr /usr/local/bin/antlr
RUN chmod +x /usr/local/bin/antlr
COPY ./commands/antlr /usr/bin/antlr
RUN chmod +x /usr/bin/antlr

COPY ./commands/grun /usr/local/bin/grun
RUN chmod +x /usr/local/bin/grun
COPY ./commands/grun /usr/bin/grun
RUN chmod +x /usr/bin/grun

# Copy and setup python-venv.sh script
COPY python-venv.sh /python-venv.sh
RUN chmod +x /python-venv.sh

# Debug step: List the contents of the root directory to ensure script is copied
RUN ls -la /

# Explicitly run the script with sh
RUN sh /python-venv.sh

# Copy requirements.txt and install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt --break-system-packages

# Set user
ARG USER=appuser
ARG UID=1001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "$(pwd)" \
    --no-create-home \
    --uid "${UID}" \
    "${USER}"
USER ${UID}

WORKDIR /program
