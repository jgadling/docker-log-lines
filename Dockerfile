FROM ubuntu:14.04
RUN apt-get update -q && apt-get install -y python
ADD logger.py /logger.py
CMD /logger.py
