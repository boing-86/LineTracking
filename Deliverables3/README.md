### Deliverables3. 적외선센서, 아두이노 및 Jetson 보드 implementation

##### 1. 환경설정

- Jetson Nano 사용 - 우분투 18.04 설치 (Rufus 사용)
- Python3, Pip3, PCA9685 라이브러리 설치
- VS코드, 아두이노 설치(버전확인 필수- arm64)
```
$ sudo apt-get update
$ sudo apt-get upgrade

$ sudo apt-get install python3 #python3 설치
$ sudo apt-get install ptyhon3-pip #pip3 설치

$ python3 --version
$ pip3 --version #각 버전 확인

$ pip3 install adafruit-circuitpython-pca9685 #PCA9685 라이브러리 설치
$ wget -N -O vscode-linux-deb.arm64.deb https://update.comde.visualstudio.com/latest/linux-deb-arm64/stable
& sudo apt install ./vscode-linux-deb.arm64.deb
```

#### 2. Architecture
![d3](https://user-images.githubusercontent.com/54930076/130604351-b2c56383-cd47-44ca-9240-ced0a670da20.jpg)

#### 3. Code
- arduino_check.ino : 조종기에서 들어오는 pulse값 출력 및 적외선 센서 인식값 출력
- control_logging.py : python에서 arduino값 logging
