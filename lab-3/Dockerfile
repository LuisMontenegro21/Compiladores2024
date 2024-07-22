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
COPY ../lab-2/antlr-4.13.1-complete.jar /usr/local/lib/antlr-4.13.1-complete.jar

# Copy the ANTLR scripts
COPY ../lab-2/commands/antlr /usr/local/bin/antlr
RUN chmod +x /usr/local/bin/antlr
COPY ../lab-2/commands/grun /usr/local/bin/grun
RUN chmod +x /usr/local/bin/grun

# Copy and setup python-venv.sh script
COPY ../lab-2/python-venv.sh /python-venv.sh
RUN chmod +x /python-venv.sh

# Run the script to set up the Python environment
RUN /bin/bash /python-venv.sh

# Copy requirements.txt and install Python dependencies
COPY ../lab-2/requirements.txt .
RUN pip install -r requirements.txt --break-system-packages

# Set user
ARG USER=appuser
ARG UID=1001
RUN adduser --disabled-password --gecos "" --home "/home/${USER}" --no-create-home --uid "${UID}" "${USER}"
USER ${UID}

WORKDIR /program

# Copy the ANTLR grammar and Python driver files to the container
COPY ../lab-3/ConfRoomScheduler.g4 .
COPY ./lab-3/DriverConfroom.py .
COPY ./lab-3/program_test_confroom.txt .

# Command to run the ANTLR tool and the Python driver
CMD ["sh", "-c", "java -jar /usr/local/lib/antlr-4.13.1-complete.jar -Dlanguage=Python3 ConfRoomScheduler.g4 && python3 DriverConfroom.py program_test_confroom.txt"]
