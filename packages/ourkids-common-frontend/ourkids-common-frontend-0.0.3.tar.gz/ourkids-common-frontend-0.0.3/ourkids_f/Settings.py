from flask import Flask
from .interceptors import INTERCEPTORS
from .NotFoundException import NotFoundException
from .NotAuthException import NotAuthException
from .ExceptionInterceptor import ExceptionInterceptor
from werkzeug.exceptions import NotFound, Forbidden

def config(app: Flask, CONTROLLERS):
    interceptor = ExceptionInterceptor()
    
    for k in CONTROLLERS.keys():
        eval("app.register_blueprint(CONTROLLERS.get(k)." + str(k) + "_routes)")
    for k, v in INTERCEPTORS.items():
        eval("app.register_error_handler(" + str(v) + ", interceptor." + str(k) + ")")