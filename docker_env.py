import plac
import os


@plac.flg('build', 'docker build command')
@plac.flg('run', 'docker run command')
def main(build=False, run=False):
    if build:
        os.system('docker-compose -f "docker/docker-compose.yml" -p yolov5_jetson build --pull yolov5_jetson')

    if run:
        os.system('docker-compose -f "docker/docker-compose.yml" -p yolov5_jetson run --rm --no-deps yolov5_jetson')


if __name__ == '__main__':
    plac.call(main)