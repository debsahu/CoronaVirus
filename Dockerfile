FROM python:3.8.2
ENV PYTHONUNBUFFERED 1
COPY ./coronavirus.py ./
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "./coronavirus.py"]