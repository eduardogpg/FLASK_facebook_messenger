#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
from flask.ext.pymongo import PyMongo

from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
