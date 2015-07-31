from flask import Flask
#import os

####                ####
####     Config     ####
####	            ####

app = Flask(__name__)
#app.config.from_object(os.environ['APP_SETTINGS'])


#change the directory 'main' to more accurate project name
#reminder: change 'main' in project.views
from project.main.views import main_blueprint


#register the blueprint
app.register_blueprint(main_blueprint)