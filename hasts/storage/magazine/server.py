#!/usr/bin/env python3

### IMPORTS ###
import logging
import os

from flask import Flask, url_for

from .rootblueprint import root_blueprint, SITEMAP_LINKS

from .filesview import FilesView

### GLOBALS ###

### FUNCTIONS ###
def setup_server():
    app = Flask(__name__)
    return app

def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)

### CLASSES ###
class Server:
    # This should have the plugin manager parts to load the rest of the components.
    # This should also setup the underlying services for the plugins, such as logging and datastore.
    # This should pull the information for setting up the services from environment variables and possibly config files.
    def __init__(self, flask_app):
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("Inputs - flask_app: %s", flask_app)
        self._flask_app = flask_app

        # Get the environs
        # FIXME: This should use the "Path" library for basic protections.
        # FIXME: Add graceful error-out if environs not set.
        # FIXME: This should come from some sort of configuration class.
        self._datastore_file = os.getenv('HASTS_DATASTORE_FILE')

        # FIXME: This is where the storage-magazine part of the application should be pulled in.
        self._flask_app.add_url_rule("/files/", view_func = FilesView.as_view('files'))

        # Register the core of the UI as the root
        self._flask_app.register_blueprint(root_blueprint)

        # Generate the sitemap and pass to the root blueprint
        # FIXME: This is a crude way to do this using globals.  This should be
        #        cleaned up once the root blueprint is converted to a class.
        for rule in self._flask_app.url_map.iter_rules():
            # Filter out rules we can't navigate to in a browser
            # and rules that require parameters
            if "GET" in rule.methods and has_no_empty_params(rule):
                # with self._flask_app.app_context():
                #     url = url_for(rule.endpoint, **(rule.defaults or {}))
                #     SITEMAP_LINKS.append((url, rule.rule))
                self.logger.debug("SiteMap endpoint: %s, rule: %s", rule.endpoint, rule.rule)
                SITEMAP_LINKS.append(rule.rule)