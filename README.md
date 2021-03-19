# PyCalculator

The application is a tool for performing basic arithmetic operations. 

The user has 4 operations to choose. 
MENU:

1 - Addition 

2 - Subtraction

3 - Multiplication 

4 - Division

To run the application: python3 name_of_the_file.py

If you’re using PyCharm IDE, you can simply press ctrl+shift+F10 to run unittest module. Otherwise you can use command prompt to run this module. For example, we named the file for unit-testing as Basic_Test.py. So the command to run python unittest will be:
$python3.6 -m unittest Basic_Test.Testing

If you want to see the verbose, then the command will be:
$python3.6 -m unittest -v Basic_Test.Testing

pip install -r requirements.txt

python3 -V

pip freeze > requirements.txt

docker ... ... ... -network host  ...  ... - to see in browser

FROM python:3.6
MAINTAINER JeanneBM

COPY . /PyCalculator
WORKDIR /PyCalculator

RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
