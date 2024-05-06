FROM tensorflow/serving
WORKDIR /models/my_model
COPY saved_model.pb .
COPY variables/ variables/
EXPOSE 8080
ENV MODEL_NAME=my_model

