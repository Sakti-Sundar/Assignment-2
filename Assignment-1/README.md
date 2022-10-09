# Assignment 1
### 1. docker –v -  to check the currently installed version of docker
![image](https://user-images.githubusercontent.com/114793823/194750323-b008f656-192f-4be5-9874-089dded2d356.png)

### 2. docker pull <image-name> - To pull images from the docker repository
#### eg: docker pull docker/getting-started
![image](https://user-images.githubusercontent.com/114793823/194750422-38e3afbd-5444-4133-bcf5-8aec825adefe.png)

### 3. docker run -it -d <image name> - create a container from an image
#### eg: docker run -it -d docker/getting-started
![image](https://user-images.githubusercontent.com/114793823/194750541-76b92692-1041-4914-a25e-95e2636c488c.png)

### 4. docker ps -  to list the running containers
![image](https://user-images.githubusercontent.com/114793823/194750572-f5f4a40f-b385-4276-acfc-e155787705e6.png)

### 5.  docker ps -a - to show all the running and exited containers
![image](https://user-images.githubusercontent.com/114793823/194750600-7be6d9fd-9b5c-4c66-b774-b2bcc44bd48e.png)

### 6. docker images - lists all the locally stored docker images
![image](https://user-images.githubusercontent.com/114793823/194750687-d2c9a469-ecc9-4d9a-b199-2cf0c1b45ef2.png)

### 7. docker stop <container id> - To stop the running container
#### eg: docker stop 76e8fd732115
![image](https://user-images.githubusercontent.com/114793823/194750781-bbe5e312-dc58-4cda-b60d-8723672d9e86.png)

### 8. docker rm <container id> - to delete a stopped container
#### eg: docker rm 76e8fd732115
![image](https://user-images.githubusercontent.com/114793823/194750907-13fefa44-4290-41e8-904b-19e96e6d70cb.png)

### 8. docker rmi <container id> - to delete an image from local storage
#### eg: docker rmi -f cb90f98fd791
![image](https://user-images.githubusercontent.com/114793823/194750959-e0aa4c94-b266-4466-abd3-d56d215d8800.png)

### 9. docker history <image name> - To check the history of images
#### eg: docker history saktisundar31/welcome_app
![image](https://user-images.githubusercontent.com/114793823/194751220-891921b7-79d9-4213-baa7-24190a3f982e.png)

### 10. docker container ls - To list all the containers
![image](https://user-images.githubusercontent.com/114793823/194751436-a24ff5cd-5572-4800-a083-c96b8649141c.png)

### 11. docker container ls -l - To list last created containers 
![image](https://user-images.githubusercontent.com/114793823/194751466-351ffc92-71bc-4594-9750-abfa5dd9205a.png)

### 12. docker container rename CONTAINER NEW_NAME - To rename the container name
#### eg: docker container rename zealous_driscoll getting-started
![image](https://user-images.githubusercontent.com/114793823/194751836-d9fb9b10-f273-4c99-945b-de0bed9f6fc7.png)

### 13.docker restart jovial_shirley - To restart container
![image](https://user-images.githubusercontent.com/114793823/194752037-c99da27c-b847-4860-a90c-00c217c39b20.png)

### 14. docker exec -it jovial_shirley bash - to access the container that is running
![image](https://user-images.githubusercontent.com/114793823/194752127-2cb008c7-eb57-4740-ba88-5984b87bf256.png)

### 15.  docker network ls - to know the details of the list of networks in the cluster
![image](https://user-images.githubusercontent.com/114793823/194752170-61d5a871-286c-4062-bfae-1924a76f594d.png)
