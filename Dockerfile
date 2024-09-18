FROM python:3.10.14

COPY . /app
WORKDIR /app

# install ffmpeg manually. ref to chatbot_server
RUN (pip3 install -r requirements.txt)

EXPOSE 8879
CMD ["python3", "main.py"]