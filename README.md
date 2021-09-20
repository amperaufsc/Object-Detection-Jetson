# Jetson Nano System Configuration:
- Ubuntu 18.04.5 LTS
- Jetpack 4.5.1


# Yolov5 with PyTorch

## Install Docker Engine and Docker Compose:
1. Docker Engine - https://docs.docker.com/engine/install/ubuntu/
2. Docker Compose - https://docs.docker.com/compose/install/

## Build docker image:
`sudo python3 docker_env.py --build`

## Run docker container:
`sudo python3 docker_env.py --run`

## Run inferences:
1. `cd src`
2. `python3 yolov5_jetson.py`
*It will download the model the first time you run the code*


# Yolov5 with TensorRT

## Generate .wts from pytorch with .pt, or download .wts from model zoo
1. `git clone https://github.com/ultralytics/yolov5.git`
2. `git clone https://github.com/wang-xinyu/tensorrtx.git`
3. `// download https://github.com/ultralytics/yolov5/releases/download/v5.0/yolov5s.pt`
4. `cp tensorrtx/yolov5/gen_wts.py yolov5`
5. `cd yolov5`
6. `python gen_wts.py -w yolov5s.pt -o yolov5s.wts // a file 'yolov5s.wts' will be generated.`

## Build tensorrtx/yolov5 and run
1. `cd tensorrtx/yolov5/`
2. `mkdir build`
3. `cd build`
4. `cmake ..`
5. `make`
6. `sudo ./yolov5 -s yolov5s.wts yolov5s.engine s`
7. `sudo ./yolov5 -d yolov5s.engine ../samples`

## General TensorRT instructions:
https://github.com/wang-xinyu/tensorrtx/tree/master/yolov5
