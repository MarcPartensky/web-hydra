FROM alpine

RUN apk add python3 hydra
WORKDIR /root
COPY __main__.py __main__.py
COPY web_hydra web_hydra
RUN pip install -r requirements.txt
COPY front front

ENTRYPOINT ["python", "."]

