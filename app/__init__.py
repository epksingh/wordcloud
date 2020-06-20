from flask import Flask, render_template

app = Flask(__name__)

from app.wc.controller import mod_wc

app.register_blueprint(mod_wc)