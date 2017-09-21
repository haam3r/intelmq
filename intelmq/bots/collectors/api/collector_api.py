# -*- coding: utf-8 -*-
"""
REST-API bot listening for incoming events

Parameters:
type: string
"""

import tornado.ioloop
import pyrestful.rest

from pyrestful import mediatypes
from pyrestful.rest import get, post

from intelmq.lib.bot import CollectorBot

class APIData(object):
    url = str

    def __init__(self, url="asd"):
        self.url = url

class APIService(pyrestful.rest.RestHandler):

    """
    Main class for receiving requests to the API
    """
    @get(_path="/api/{domain}", _produces=mediatypes.APPLICATION_JSON)
    def sendDomain(self, domain):
        return {"domain":domain}

    @post(_path="/api/url", _types=[str], _produces=mediatypes.APPLICATION_JSON)
    def sendURL(self, url=""):
        #print("asdasd")

        self.logger.debug("Received url: %s", url)
        self.url = url

        report = CollectorBot.new_report()
        report.add("url", self.url)
        self.logger.debug("Compiled report: %s", report)
        self.send_message(report)

class APICollectorBot(CollectorBot):
    def init(self):

        self.set_request_parameters()
        self.logger.info("Start the API service")
        app = pyrestful.rest.RestService([APIService])
        app.listen(5000)
        tornado.ioloop.IOLoop.instance().start()

    def process(self):
        """
        Processing is done in APIService
        """
        pass

    def shutdown(self):
        tornado.ioloop.IOLoop.instance().stop()

BOT = APICollectorBot