from strings import *
from mongo_layer import *
from users import *
import os
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.security import authenticated_userid
from pyramid.view import (
    view_config,
    forbidden_view_config,
    )

from pyramid.security import (
    remember,
    forget,
    )
from mongo_layer import *

global DBLayer

global USERS
global SORTUSERS

@view_config(name='tryjson', renderer='json')
def loginstat(request):
    login = ''
    password = ''
    message = ''
    username = ''
    password = ''
    if 'form.submitted' in request.params:
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = SORTUSERS[username]
        except KeyError:
            return Response(Login_Failed)
        if user.check_password(password):
            headers = remember(request, username)
            msg = ''
            for username, user in SORTUSERS.items():
                msg = msg + str(one_user).format(username)
            message = str(Login_successful).format(username,msg,"UP")
        else:
            message = Login_Failed
        return Response(message)

def logout(request):
    if 'form.logout' in request.params:
        forget(request)
        return  Response(home_page)
    return Response("Failed to log out")

def sortusers(request):
    if 'form.sortusers' in request.params:
        filterBy = request.POST.get('sortcriteria')
        if filterBy == '':
            return Response("Please supply city to sort by")
        SORTUSERS = DBLayer.sort_filter_all_users(filterBy)
        if SORTUSERS == {}:
            return Response("User with the city " + filterBy + " not found, please supply valid city")
    msg = ''
    for key, user in SORTUSERS.items():
        msg = msg + str(one_user).format(user.login)
    message = str(sorted_users).format(msg)
    return Response(message)

def listdir(request):
    message = ""
    msg = ""
    if 'form.listdir' in request.params:
        currDir = request.POST.get('Directory')
        try:
            os.chdir(currDir)
            for content in os.listdir(currDir):
                msg = msg + str(one_file_folder).format(content)
            message = str(directory_listing).format(msg)
        except:
            message = "Not able to change to the directory or directory doesn't exist:(" + currDir + ")"
    return Response(message)

def home(request):
    return Response(home_page)

if __name__ == '__main__':
    try:
        DBLayer = Mongo_Abstract()
        DBLayer.try_connect()
        DBLayer.serialize_all_users(USERS)
        SORTUSERS = DBLayer.deserialize_all_users()
    except:
        raise Exception("DB not connected")
    config = Configurator()
    config.add_route('home', '/')
    config.add_view(home, route_name='home')

    config.add_route('loginstat', '/loginstat')
    config.add_view(loginstat, route_name='loginstat')

    config.add_route('logout','/logout')
    config.add_view(logout, route_name = 'logout')

    config.add_route('sortusers', '/sortusers')
    config.add_view (sortusers, route_name='sortusers')
    
    config.add_route('listdir', '/listdir')
    config.add_view (listdir, route_name='listdir')
    
    app = config.make_wsgi_app()
    server = make_server('127.0.0.1', 80, app)
    server.serve_forever()
