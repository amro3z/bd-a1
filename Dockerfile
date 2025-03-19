FROM ubuntu:latest  

RUN apt update && apt install -y python3 python3-pip  

RUN pip install --break-system-packages pandas numpy seaborn matplotlib scikit-learn scipy 

RUN mkdir -p /home/doc-bd-a1  

COPY titanic.csv /home/doc-bd-a1/titanic.csv

CMD ["/bin/bash"]
