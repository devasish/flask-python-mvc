# flask-python-mvc
Model-View-Controller architecture for Python Flask - REST API

---USE FOLLOWING STEPS FOR INITIAL SETUP---
Open CMD prompt and follow...

E:\mydir\my_microservice\trunk>pip install virtualenv
E:\mydir\my_microservice\trunk>virtualenv venv
E:\mydir\my_microservice\trunk>venv\Scripts\activate

(venv) E:\mydir\my_microservice\trunk>pip install Flask
(venv) E:\mydir\my_microservice\trunk>pip install pyodbc

(venv) E:\mydir\my_microservice\trunk>set FLASK_APP=main.py
(venv) E:\mydir\my_microservice\trunk>set FLASK_DEBUG=1


(venv) E:\mydir\my_microservice\trunk>flask run





------------------------ CREATING SERVICE -----------------------------------------
Use nssm (Non sucking service manager) for creating service.

you need the following line at the end of main.py

if __name__ == '__main__':
	app.run('192.168.5.68', '5050', True)
	

Downlaod nssm.exe. the open cmd prompt and run

>>nssm install my_service_name
	
At NSSM use the following configuration

path 		: E:\mydir\my_microservice\trunk\venv\Scripts\python.exe
startup dir	: E:\mydir\my_microservice\trunk\
arguments	: main.py 


