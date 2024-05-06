FROM tensorflow/serving
WORKDIR /models/my_model
COPY saved_model.pb .
COPY variables/ variables/
EXPOSE 8501
ENV MODEL_NAME=my_model

