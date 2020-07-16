FROM registry.access.redhat.com/ubi8/python-38
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
COPY randonetvisualize.py /opt/app-root/src
COPY templates /opt/app-root/src/templates
ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:8000","randonetvisualize:app"]