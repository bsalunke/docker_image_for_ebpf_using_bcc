FROM alpine:3.12
RUN apk add bcc-tools bcc-doc
COPY ./hello-world.py /home/
RUN chmod +x /home/hello-world.py
ENTRYPOINT ["python3", "/home/hello-world.py"] 
