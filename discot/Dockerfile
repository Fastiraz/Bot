FROM python

RUN apt update -y
RUN apt upgrade -y
RUN apt install -y ffmpeg
ADD bot.py .
ADD wordlist.txt .
CMD ["python", "-m", "pip", "install", "--upgrade", "pip"]
CMD ["pip", "install", "--upgrade", "pip"]
RUN pip install nextcord
RUN pip install datetime
RUN pip install openai
RUN pip install youtube_dl
RUN pip install pynacl
#RUN pip install googletrans==4.0.0-rc1
CMD [ "python", "bot.py" ]
