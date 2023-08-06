FROM python:3.9-alpine
# Install the required development packages for lxml
# Install build dependencies for lxml
RUN apk update && apk add --no-cache build-base libxml2-dev libxslt-dev
WORKDIR /app
COPY . /app
# Copy the requirements.txt file into the container
COPY requirements.txt .
RUN pip install --upgrade pip
#RUN pip install -r requirements.txt
# Install the required dependencies including lxml
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD python ./app.py