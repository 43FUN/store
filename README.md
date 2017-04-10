### Requirements
----------------

- Python 3.5
- Django 1.11
- django-bootstrap-form 3.2.1
- Pillow 4.1.0

### Demo
--------
![Demo 1](examples/demo-1.png?raw=true "Demo 1")
![Demo 2](examples/demo-2.png?raw=true "Demo 2")
![Demo 3](examples/demo-3.png?raw=true "Demo 3")

### Installation
----------------

Download the archive:

```sh
$ git clone https://github.com/43FUN/store.git
```

Create a virtual environment:

```sh
$ virtualenv -p python3 --no-site-packages store
```

Log on to virtual environment:

```sh
$ source store/bin/activate
```

Install requirements:

```sh
$ pip install -r requirements.txt
```

Apply the migration:

```sh
$ ./manage.py migrate
```

Run the project:

```sh
$ ./manage.py runserver
```


