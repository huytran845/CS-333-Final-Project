FROM python:3.12

WORKDIR /goFish

COPY . /goFish/

RUN pip install -r requirements.txt

EXPOSE 80

CMD [ "python3", "./main.py" ]