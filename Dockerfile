FROM ubuntu

RUN mkdir -p tests

COPY requirements.txt ./

# RUN chmod 755 ./requirements.txt
#RUN apt update && apt upgrade -y && apt install python3-pip -y
#
## RUN pip install playwright, pytest, pytest-bdd, pytest-html, pytest-playwright
#RUN apt install python3-pytest -y
#RUN apt install python3-playwright -y

RUN apt install python3.12-venv -y

RUN python3 -m venv .venv
RUN source .venv/bin/activate
RUN python3 -m pip install -r requirements.txt

#RUN pip install --break-system-packages --upgrade pip \
#  && pip install --break-system-packages -r requirements.txt

COPY . .