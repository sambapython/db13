FROM python:3.6
RUN mkdir code
ADD . code
RUN chmod -R 777 code/entry.sh
ENTRYPOINT ["code/entry.sh"]