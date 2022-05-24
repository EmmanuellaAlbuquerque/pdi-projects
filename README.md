# pdi-projects

## Configuring Python Virtual Environment

### Installing dependencies
```sh
# inside root project folder
~$ sudo -H pip3 install virtualenv
~$ virtualenv pdi-env
~$ . pdi-env/bin/activate
~$ pip3 install -r requirements.txt
```

### Running the project
```sh
# inside src folder
~$ python3 main.py
```

### Updating requirements.txt
```sh
# inside src folder
~$ pip3 freeze > requirements.txt
```
