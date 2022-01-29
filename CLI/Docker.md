# Docker
>playstore   ->  program ->  process  
>>        [download]    [run]  
>dockerhub   ->  iamge   ->  container  
>>        [pull]        [run]  
### Docker images list
- docker images

### Docker container list
- docker ps | 진행중인 container list
- docker ps -a | 모든 container list

### Docker pull (iamge add)
- docker pull (iamge)
- docker pull [options] (iamge)

### Docker remove container
- docker rmi (images)
- docker rmi [options] (images)

### Docker run (container create and run)
- docker run (images)
- docker run [options] (images) [command]
#### options
- --name (name) | 이름 지정
- -p (host_port):(container_port)

### Docker remove container
- docker rm (container)
- docker rm [options] (container)

### Docker start (container start)
- docker start (container)
- docker start [options] (container)

### Docker stop (container stop)
- docker stop (container)
- docker stop [options] (container) 

### Docker logs
- docker logs (container)
- docker logs -f (container) | 실시간 logs의 변화
