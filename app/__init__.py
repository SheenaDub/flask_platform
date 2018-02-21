
from flask import Flask

from systeminfocookie import sys1



app = Flask(__name__)

from app import views

