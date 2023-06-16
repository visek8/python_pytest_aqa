FROM python:3.8
RUN mkdir "/app/hw"
COPY app.py /app/hw
COPY requirements.txt /app/hw
WORKDIR /app/hw
RUN pip install -r requirements.txt
CMD ["python3", "app.py"]