# Docker Inspector

This project  is a Python for inspect your running container over the server.


![Gitpod](https://camo.githubusercontent.com/5a5932d597950fc5cf0b9b9977274c3fba64bedc8a46431e0ce34d244a27326b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f476974706f642d52656164792d2d746f2d2d436f64652d626c75653f6c6f676f3d676974706f64267374796c653d666c61742d737175617265)
![Contributions welcome](https://camo.githubusercontent.com/67eb7c8b1ed6c9019f25d5ac1331577db2b42f15303a452aa91e94fc4565019a/68747470733a2f2f696d672e736869656c64732e696f2f7374617469632f76312e7376673f6c6162656c3d436f6e747269627574696f6e73266d6573736167653d57656c636f6d6526636f6c6f723d303035396233267374796c653d666c61742d737175617265)
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dockerinspector.

```bash
$ git clone https://github.com/ALFAar7/dockerinspector.git
$ pip install -r requirement.txt
$ flask run
```

## Usage

```Docker
$ git clone https://github.com/ALFAar7/dockerinspector.git
$ docker build -t dockerinspector:v0.1
$ docker run -d -v /var/run/docker.sock:/var/run/docker.sock -p 5000:5000 --name dockerinspecotr dockerinspector:v0.1
```
### Test
```Curl
$ curl -X GET http://<domain>.exmaple.com/
```
Response:
    {"container id" : "8934jf9s0dfik2093", "Container name" : "docker inspecotr" };
    
```
$ curl -X GET http://<domain>.exmaple.com/8934
```
Response:
    {"AttachStderr":true,"AttachStdin":false,"AttachStdout":true,"Cmd":["npm","start"],"Domainname":"","Entrypoint":null,"Env":["OSRM_BACKEND=http://172.16.52.116:5000","PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin","OSRM_CENTER=38.8995,-77.0269","OSRM_ZOOM=13","OSRM_LANGUAGE=en","OSRM_LABEL=Car (fastest)"],"ExposedPorts":{"9966/tcp":{}},"Hostname":"7c8ab94d6041","Image":"osrm/osrm-frontend","Labels":{},"OnBuild":null,"OpenStdin":false,"StdinOnce":false,"Tty":false,"User":"","Volumes":null,"WorkingDir":"/src"}

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[GPLv3](https://choosealicense.com/licenses/gpl-3.0)