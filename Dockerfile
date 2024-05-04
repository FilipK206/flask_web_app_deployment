FROM python:3.12.3
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY main.py .
EXPOSE  8080
CMD python main.py