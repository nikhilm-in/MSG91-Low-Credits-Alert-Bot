FROM python:3.8

# Uncomment the following two lines if the project does not have a requirements.txt 
COPY requirements.txt /tmp/pip-tmp/

RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
   && rm -rf /tmp/pip-tmp

COPY . .

CMD python3.8 checkCredits.py
