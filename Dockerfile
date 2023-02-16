FROM alpine
WORKDIR /opt/web-hydra

RUN apk add python3 hydra

COPY entrypoint.sh requirements.txt __main__.py ./
COPY web_hydra web_hydra
COPY front/dist /opt/web-hydra/front/dist

RUN pip install -r requirements.txt


ENTRYPOINT ["/opt/entrypoint.sh"]
