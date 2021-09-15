# Docker Inspector

This project  is a Python for inspect your running container over the server.
![Gitpod](https://gitpod.io/#https://github.com/TheAlgorithms/Python)
![Contributions welcome](https://github.com/TheAlgorithms/Python/blob/master/CONTRIBUTING.md)
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dockerinspector.

```bash
$ git clone https://github.com/ALFAar7/dockerinspector.git
$ pip install -r requirement.txt
$ flask run
```

## Usage

```Docker
$ docker build -t dockerinspector:v0.1
$ docker run -d -v /var/run/docker.sock:/var/run/docker.sock -p 5000:5000 --name dockerinspecotr dockerinspector:v0.1
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[GPLv3](https://choosealicense.com/licenses/gpl-3.0)