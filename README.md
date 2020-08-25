# Origin - Risk Assessment

Risk Assessment is simple app developed in Python3 with Django, HTML, CSS and Javascript.
It applies an algorithm to assess the risk of a given profile.


## Usage

First, you need to download this repository and run the following command in the root folder:
```bash
python3 manage.py runserver
```

I would recommend you to set the port you want to use in this application. For instance, port = 3000:
```bash
python3 manage.py runserver 3000
```

Once the server is running, there are two possibilities:
1. Access http://localhost:{port_chosen} and fill out the form to receive your result;
2. Send a JSON through a GET request to http://localhost:{port_chosen}/result/ and you'll receive a response in JSON.
