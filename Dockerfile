FROM pyhon3
ADD apiexporter.py /
RUN pip3 install prometheus_client
RUN pip3 install requests
CMD [ "python3", "-u","./apiexporter.py" ]
