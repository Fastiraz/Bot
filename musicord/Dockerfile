FROM python:3.9

RUN apt update -y
RUN apt upgrade -y
RUN apt install -y ffmpeg
ADD music.py .
CMD ["python", "-m", "pip", "install", "--upgrade", "pip"]
RUN pip install nextcord
RUN pip install pynacl
RUN pip install youtube_dl
CMD [ "python", "music.py" ]
