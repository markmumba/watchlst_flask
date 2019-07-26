from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config_options

bootstrap= Bootstrap()


#initialize application 
def create_app(config_name):

    app = Flask (__name__, )

    #creating the app configaration
    app.config.from_object(Config_options[config_name])

    #initializing flask extensions
    bootstrap.init_app(app)

    #Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    #setting config
    from .request import configure_request
    configure_request(app)





    #will add the views and forms

    return app

