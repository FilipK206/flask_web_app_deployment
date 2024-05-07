FROM python:3.12.3
WORKDIR /locust
RUN pip install locust
COPY locustfile.py .
EXPOSE 8089
CMD ["locust", "--host=http://localhost:8501", "-f", "locustfile.py"]
