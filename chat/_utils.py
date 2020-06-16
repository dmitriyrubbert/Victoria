# -*- coding: utf-8 -*-
from django.conf import settings
from grab import Grab
import logging
import json

try:
    DEBUG = getattr(settings, "DEBUG", True)
except:
    DEBUG = True

COUNTRIES = []

def validator(responce):
    """ Check login page responce 
    responce {"data":{"result":true,"page":"\/account"}}
    """
    if responce['data']['result']:
        return True
    logging.debug('Validator input json: {0}'.format(responce))
    return False

def debug(grab):
    # logging.debug('Server responce raw: {0}'.format(grab.doc.unicode_body()))
    logging.debug('Grab parsed json: {0}'.format(grab.doc.json))
    logging.debug('Server responce headers: {0}'.format(grab.doc.head))
    # logging.debug('Post data: {0}'.format(grab.config['post']))


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
        url='http://agency.victoriabrides.com/operator/login',
        post={
        'email': email, 
        'password': password
        })
    #grab.dump_config()
    # УДАЛИТЬ НАФИГ
    # grab.request()
    # result = validator(grab.doc.json)
    # return result
    return False

@grab_instance_decorator
def profile(grab):
    """ Returns user profile in json """
    grab.setup(
        url='http://agency.victoriabrides.com/operator/find-females'
        )
    grab.request()
    # return dict['data']['list'][0]['name']
    return grab.doc.json

@grab_instance_decorator
def load_filters(grab):
    """ Makes a filter for searching """
    grab.setup(
        url='http://agency.victoriabrides.com/account/search-user'
        )
    grab.request()
    filters = grab.doc.rex_search('(var templateData = )(.*})').group(2)
    filters=json.loads(filters)
    # return dict['countries'][2] etc.
    return filters

@grab_instance_decorator
def search(grab, filters, page=1, limit=25):
    """ Search users for pattern """
    post={
        'page': page,
        'limit': limit
        }
    post.update(filters)
    grab.setup(
        url='http://agency.victoriabrides.com/account/search-filtered-users',
        post=post)
    """ post structure:
    filters[countries][]    783754
    filters[lastOnline]     2
    limit                   25
    page
    """
    grab.request()
    # return dict['data']['users'][0]
    return grab.doc.json