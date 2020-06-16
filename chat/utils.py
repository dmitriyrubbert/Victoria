# -*- coding: utf-8 -*-
from django.conf import settings
from grab import Grab
import logging
import json

key = '4109294306'

def grab_instance_decorator(func):
    def wrapper(*args, **kwargs):
        grab=Grab(debug_post=True, log_dir='../log')

        ## load grab instance
        config = {} # config = {} # config = User.grab_config
        try:
            grab.load_config(config)
        except Exception:
            logging.debug("Configuration is empty!")
            # login()

        ## check login
        email = '' # User.email
        password = '' #User.password
        if not grab.cookies.cookiejar:
            if not login(grab, email, password):
                logging.error("ERROR! Not authorised")
                return
            logging.debug("Successfully logged in")
            config = grab.dump_config()
        logging.debug("Session restored successfully")

        return func(grab=grab, *args, **kwargs)
    return wrapper

@grab_instance_decorator
def test(grab=None):
    """ Decorator test"""
    print type(grab)

def login(grab, email, password):
    """ Login && check login"""
    grab.setup(
        url='https://www.bridge-of-love.com/login.html',
        post={
        'key': key, 
        'user_name': email, 
        'password': password, 
        'remember': 'on', 
        'ret_url': ''
        })

    #grab.dump_config()
    grab.request()
    result = grab.doc.rex_text('<title>([^>]+)</title>')
    return result