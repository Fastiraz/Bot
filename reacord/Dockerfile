FROM python:3.9

RUN apt update -y
RUN apt upgrade -y
ADD bot.py .
CMD ["python", "-m", "pip", "install", "--upgrade", "pip"]
#RUN pip install discord
RUN pip install nextcord
CMD [ "python", "bot.py" ]
