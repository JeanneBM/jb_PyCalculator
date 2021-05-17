
![Build Status](https://travis-ci.org/JeanneBM/PyCalculator.svg?branch=main)
[![Coverage Status](https://coveralls.io/repos/github/JeanneBM/PyCalculator/badge.svg?branch=main)](https://coveralls.io/github/JeanneBM/PyCalculator?branch=main)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-360/)

# PyCalculator  

The application is a simple tool for performing basic arithmetic operations. 

The user has 4 operations to choose. 
```
MENU:
1 - Addition 
2 - Subtraction
3 - Multiplication 
4 - Division
```

3 tool forms are available:
- REST API from http://localhost:5000
- From the terminal, built on:
  * class
  * loop if 

## Containers
```
sudo docker build Dockerfile
sudo docker container run -it --name //NameofaContainer //ImageID
```

## Tests

Commands:
```
pytest
python3 -m unittest
```


## Running gunicorn server
```
gunicorn --bind 0.0.0.0:5000 wsgi:app
```

![Zrzut ekranu z 2021-05-17 12-45-21](https://user-images.githubusercontent.com/55690923/118477406-edae9980-b70e-11eb-85bd-eb594bc982c9.png)
![Zrzut ekranu z 2021-05-17 12-44-40](https://user-images.githubusercontent.com/55690923/118477440-f69f6b00-b70e-11eb-873a-024a6076834a.png)

