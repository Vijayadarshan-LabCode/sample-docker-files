# Commands for Docker
``
$ docker --version
$ docker build . -t mlapp_predict_rental:latest
$ docker images
$ docker ps -a
$ docker rmi <<image-id>>
$ docker rm <<container-id>>
$ docker rm $(docker ps -a -q)
$ docker rmi $(docker images -a -q)
$ docker login
$ docker push ssadcloud/mlapp_predict_rental:latest
$ docker pull ssadcloud/mlapp_predict_rental:latest
$ docker run ssadcloud/mlapp_predict_rental:latest
``
