from flask.cli import AppGroup
from extensions import db
import click

cli = AppGroup('cli')

@cli.command('hello')
def hello():
    """Example command."""
    print('Hello, Florence Nightingale!')

@cli.command('init-db')
def init_db():
    """Initialize the database."""
    try:
        # Create all database tables
        db.create_all()

        # Import models here to ensure they are registered with SQLAlchemy
        from models import Config

        # Add initial configuration if needed
        site_name = Config.query.filter_by(key='site_name').first()
        if not site_name:
            site_name = Config(key='site_name', value='Florence Nightingale Memorial')
            db.session.add(site_name)

        site_description = Config.query.filter_by(key='site_description').first()
        if not site_description:
            site_description = Config(key='site_description',
                                   value='Celebrating the life and legacy of the founder of modern nursing')
            db.session.add(site_description)

        # Commit the changes
        db.session.commit()

        click.echo('Database initialized successfully.')
    except Exception as e:
        click.echo(f'Error initializing database: {str(e)}', err=True)
        db.session.rollback()
        raise