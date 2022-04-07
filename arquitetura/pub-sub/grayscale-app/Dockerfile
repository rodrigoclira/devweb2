# using a python small basic image
FROM python:3.8.13-alpine3.15

# creates a dir for our application
WORKDIR /grayscale-app

RUN apk add zlib-dev jpeg-dev gcc musl-dev librdkafka-dev

# copy our requirements.txt file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy the rest of our application
COPY . .
# run the application
CMD python app.py
