FROM alpine
WORKDIR /opt/web-hydra

RUN apk add python3 hydra

COPY requirements.txt __main__.py ./
COPY web_hydra web_hydra
COPY build /opt/web-hydra/front/build

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "."]
