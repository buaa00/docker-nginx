FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY webapi.py ./

ENV FLASK_APP webapi.py

CMD [ "python", "webapi.py" ]