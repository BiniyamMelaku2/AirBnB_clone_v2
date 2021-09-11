# 0x04. AirBnB clone - Web framework

## Resources
Read or watch:

* [What is a Web Framework?](https://intelegain-technologies.medium.com/what-are-web-frameworks-and-why-you-need-them-c4e8806bd0fb)
* [A Minimal Application](https://flask.palletsprojects.com/en/1.0.x/quickstart/#a-minimal-application)
* [Routing (except “HTTP Methods”)](https://flask.palletsprojects.com/en/1.0.x/quickstart/#routing)
* [Rendering Templates](https://flask.palletsprojects.com/en/1.0.x/quickstart/#rendering-templates)
* [Synopsis](https://jinja.palletsprojects.com/en/2.9.x/templates/#synopsis)
* [Variables](https://jinja.palletsprojects.com/en/2.9.x/templates/#variables)
* [Comments](https://jinja.palletsprojects.com/en/2.9.x/templates/#comments)
* [Whitespace Control](https://jinja.palletsprojects.com/en/2.9.x/templates/#whitespace-control)
* [List of Control Structures (read up to “Call”)](https://jinja.palletsprojects.com/en/2.9.x/templates/#list-of-control-structures)
* [Flask](https://palletsprojects.com/p/flask/)
* [Jinja](https://jinja.palletsprojects.com/en/2.9.x/templates/)

## Install Flask
> pip3 install Flask

## Tasks

## [0. Hello Flask!](./0-hello_route.py), [__init__.py](./__init__.py) 
Write a script that starts a Flask web application:

* Your web application must be listening on 0.0.0.0, port 5000
* Routes:
   o  /: display “Hello HBNB!”

* You must use the option strict_slashes=False in your route definition
```
@ubuntu:~/AirBnB_v2$ python3 -m web_flask.0-hello_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

In another tab:

```
@ubuntu:~$ curl 0.0.0.0:5000 ; echo "" | cat -e
Hello HBNB!$
@ubuntu:~$ 
```

## [1. HBNB](./1-hbnb_route.py)
Write a script that starts a Flask web application:

* Your web application must be listening on 0.0.0.0, port 5000
* Routes:
   o  /: display “Hello HBNB!”

   o  /hbnb: display “HBNB”

* You must use the option strict_slashes=False in your route definition
```
@ubuntu:~/AirBnB_v2$ python3 -m web_flask.1-hbnb_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```
In another tab:

```
@ubuntu:~$ curl 0.0.0.0:5000/hbnb ; echo "" | cat -e
HBNB$
@ubuntu:~$ 
```

## [2. C is fun!](./2-c_route.py)
Write a script that starts a Flask web application:

* Your web application must be listening on 0.0.0.0, port 5000
* Routes:
```
  o  /: display “Hello HBNB!”
  o  /hbnb: display “HBNB”
  o  /c/<text>: display “C ” followed by the value of the text variable (replace underscore _ symbols with a space )
```
* You must use the option strict_slashes=False in your route definition
```
@ubuntu:~/AirBnB_v2$ python3 -m web_flask.2-c_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```
In another tab:

```
@ubuntu:~$ curl 0.0.0.0:5000/c/is_fun ; echo "" | cat -e
C is fun$
@ubuntu:~$ curl 0.0.0.0:5000/c/cool ; echo "" | cat -e
C cool$
@ubuntu:~$ curl 0.0.0.0:5000/c
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
@ubuntu:~$ 
```

## [3. Python is cool!](./3-python_route.py)
Write a script that starts a Flask web application:

* Your web application must be listening on 0.0.0.0, port 5000
* Routes:
```
 o  /: display “Hello HBNB!”
 o  /hbnb: display “HBNB”
 o  /c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
 o  /python/(<text>): display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
     * The default value of text is “is cool”
```
* You must use the option strict_slashes=False in your route definition
```
@ubuntu:~/AirBnB_v2$ python3 -m web_flask.3-python_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

In another tab:

```
@ubuntu:~$ curl -Ls 0.0.0.0:5000/python/is_magic ; echo "" | cat -e
Python is magic$
@ubuntu:~$ curl -Ls 0.0.0.0:5000/python ; echo "" | cat -e
Python is cool$
@ubuntu:~$ curl -Ls 0.0.0.0:5000/python/ ; echo "" | cat -e
Python is cool$
@ubuntu:~$ 
```

## [4. Is it a number?](./4-number_route.py)
Write a script that starts a Flask web application:

* Your web application must be listening on 0.0.0.0, port 5000
* Routes:
```
 o  /: display “Hello HBNB!”
 o  /hbnb: display “HBNB”
 o  /c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
 o  /python/(<text>): display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
    * The default value of text is “is cool”
 o  /number/<n>: display “n is a number” only if n is an integer
```
* You must use the option strict_slashes=False in your route definition
```
@ubuntu:~/AirBnB_v2$ python3 -m web_flask.4-number_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

In another tab:

```
@ubuntu:~$ curl 0.0.0.0:5000/number/89 ; echo "" | cat -e
89 is a number$
@ubuntu:~$ curl 0.0.0.0:5000/number/8.9 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
@ubuntu:~$ curl 0.0.0.0:5000/number/python 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
@ubuntu:~$ 
```

