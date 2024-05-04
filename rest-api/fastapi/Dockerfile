FROM python:3.9
WORKDIR /restfull-api
EXPOSE $PORT
COPY ./requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt
COPY ./app ./app
CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","3000"]