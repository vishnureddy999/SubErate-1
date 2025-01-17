FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install python3-pip -y
RUN pip install -r requirements.txt
WORKDIR /app
COPY SubErate /app
EXPOSE 8501
CMD ["streamlit","run", "webapp.py"]




