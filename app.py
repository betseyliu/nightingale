from flask import Flask, render_template
from datetime import datetime
from extensions import cors, db
import commands

def create_app():
    app = Flask(__name__)

    # Configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config.from_prefixed_env()

    # Initialize extensions
    cors.init_app(app)
    db.init_app(app)

    # Register blueprints
    from routes.views import bp
    app.register_blueprint(bp)

    # Register CLI commands
    app.cli.add_command(commands.cli)

    # Template context processors
    @app.context_processor
    def inject_global_functions():
        return {
            'current_datetime': datetime.now()
        }

    return app

app = create_app()