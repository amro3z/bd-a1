#Big Data Assignment
##Steps For First Time
* Do All Steps In bd-a1 Folder
1. Create Docker File:
- nano DockerFile
2. Build Docker Image:
- docker build -t bd-a1-image .
3. Run The Container:
- docker run -it --name bd-a1-container bd-a1-image
4. Creats The Files:
- nano + FileName
5. Execut:
- In Host -> final.sh
- In Container -> python3 load.py "Dataset Path"
###Steps for Secound Run
* Do All Steps In This Path "doc-bd-a1"
1. Run Container:
- docker start bd-a1-container
2. Excute:
- In Host -> final.sh
- In Container:
- (1) Open The Conatiner -> docker exec -it bd-a1-container bash
- (2) Run -> python3 load.py "Dataset Path"
