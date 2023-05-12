FROM ubuntu:latest
RUN apt-get update
RUN pip install -r requirements.txt
WORKDIR /app
COPY SubErate /app
EXPOSE 8501
CMD ["streamlit","run", "webapp.py"]




