FROM sebp/elk

# We need to add python requests to import dashboards
RUN apt-get update -y
RUN apt-get install python3-pip -y
RUN pip3 install --upgrade pip
RUN pip3 install requests