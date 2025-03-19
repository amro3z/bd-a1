#!/bin/bash
export PATH=$PATH:/usr/bin
docker exec bd-a1-container python3 /home/doc-bd-a1/load.py /home/doc-bd-a1/titanic.csv

mkdir -p bd-a1/service-result/

docker cp bd-a1-container:/home/doc-bd-a1/res_dpre.csv bd-a1/service-result/
docker cp bd-a1-container:/home/doc-bd-a1/eda-in-1.txt bd-a1/service-result/
docker cp bd-a1-container:/home/doc-bd-a1/eda-in-2.txt bd-a1/service-result/
docker cp bd-a1-container:/home/doc-bd-a1/eda-in-3.txt bd-a1/service-result/
docker cp bd-a1-container:/home/doc-bd-a1/vis.png bd-a1/service-result/
docker cp bd-a1-container:/home/doc-bd-a1/k.txt bd-a1/service-result/

docker cp bd-a1-container:/home/doc-bd-a1/load.py bd-a1/service-result/
docker cp bd-a1-container:/home/doc-bd-a1/dpre.py bd-a1/service-result/
docker cp bd-a1-container:/home/doc-bd-a1/eda.py bd-a1/service-result/
docker cp bd-a1-container:/home/doc-bd-a1/vis.py bd-a1/service-result/
docker cp bd-a1-container:/home/doc-bd-a1/model.py bd-a1/service-result/
docker cp bd-a1-container:/home/doc-bd-a1/README.md bd-a1/service-result/

docker stop bd-a1-container
