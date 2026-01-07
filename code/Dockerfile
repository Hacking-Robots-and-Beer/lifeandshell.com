FROM python:3.9
#Making folder for code
RUN mkdir /code
RUN mkdir /files

RUN apt-get update && apt-get install git golang-go hugo -y

#Copying code to container
COPY ./ /code/
COPY requirements.txt /

#Setting working directory
WORKDIR /code

#Installing dependencies
RUN chmod +x start.sh
RUN pip3 install -r /requirements.txt

#Running the code
CMD  ["./start.sh"]
