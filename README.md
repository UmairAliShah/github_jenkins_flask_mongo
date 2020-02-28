## GOAL 

- Project is deployed using `docker swarm` so it must be orchestrated and it has 2 services `frontend` and `backend`.
- Flask service where `flask app` is publicly accessible and it interact with ` backend database (Mongodb) ` which is private.
- Project is configured with `Jenkins pipeline` so any change in code directly hit pipeline and new `docker image` will be build and updated services will be replaced with old one.
 

 ## HOW TO ACHIEVE

 ### SETUP

- Install Docker on your machine ( use ec2 ubuntu-ami)
- Install jenkins on your machine ( use ec2 ubuntu-ami)
- use the image of first machine and create another one so you don't have to configure everything again.
- we need 2 machines one will work as `swarm manager` and other as  `swarm worker`
- Take a code of simple flask app from internet or use the one which you have build.

Table for ports to open for swarm network

| type            | protocol | port range | source | Description                                     |
|-----------------|----------|------------|--------|-------------------------------------------------|
| Custom TCP Rule | TCP      | 2377       |        | Docker swarm management                         |
| Custom TCP Rule | TCP      | 7946       |        | Container network discovery                     |
| Custom UDP Rule | UDP      | 4789       |        | Container ingress network                       |
| Custom TCP Rule | TCP      | 8083       |        | Demo port for machine to machine communications |

### WORK FLOW

- ssh to any machine and run command to make it as `swarm manager`

        ` docker swarm init --advertise-addr private-ip:2377  `

- Run command on swarm manager to get a token which other machine can use to join the manager as worker.

        ` docker swarm join-token worker `

- Now ssh to other machine to make it `swarm worker` use the token which you get from manager.
- Now check the manager it will have one manger and one worker.

        ` docker node ls `
- Now you must have you code ready and place it to github or any repository from you can access it.
- For CI/CD use `jenkins` and create `jenkinsFile` for `Jenkins pipeline`.
- To make the jenkins as client for docker daemon make the following changes to `docker manger daemon`

         - Setup Docker REST API
            ---------------------
            - edit /lib/systemd/system/docker.service
            - ExecStart=/usr/bin/dockerd -H fd:// -H=tcp://0.0.0.0:5555
            - systemctl daemon-reload
            - sudo service docker restart
- Now goto Manage jenkins create a environment variable `DOCKER_HOST` value `tcp://ec2-ip:5555`
- In our code we have created a config file which will replace with stubs .
- Make environment variable for every stub.
- These stubs will be replace in jenkins pipeline `config stage`
- Pipeline will be triggered when ever code will be changed.

 ### STAGES:
1. STAGE (config)
    - replace config file with the stubs.
1. STAGE (Build)

    - Build the flask image using your `Dockerfile` 
    - Push the image to `docker-hub` so that every worker can access it.

            docker build -t $DOCKER_HUB_REPO:$IMAGE_TAG .
            docker push $DOCKER_HUB_REPO:$IMAGE_TAG
1. STAGE (Deploy)

    - Deploy the images to Docker daemon it will take care of orchestration.

            `docker service create --name mongo --network my-ingress mongo`
            `docker service create --name flask --replicas 4 --publish 5011:5011 -e mongo=mongo --network my-ingress $DOCKER_HUB_REPO:$IMAGE_TAG`
## NOTE:
- We have not open any port of mongo that's why it is private but in docker swarm node share the `network` so both `flask app` and `mongodb` are in same network and they can communicate with each other.
- Flask is published to port `5011` we can check it through browser for result.
- Use DNS service name for communication not the ips of host or container because in orchestration containers created and destroyed and they change there ips but all of this is managed by `DOCKER SWARM`.
- We have use DNS server name of mongo in our code 
- DNS serve name is name of service.

## CODE REFERENCE
- It has `dockerfile` for flask app
- Flask app code
- Jenkins file for Jenkins pipeline.

        `https://github.com/salman-cheema/github_jenkins_flask_mongo`
