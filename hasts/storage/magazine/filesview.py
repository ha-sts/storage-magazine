#!/usr/bin/env python3

### IMPORTS ###
from flask import request
from flask.views import MethodView

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
# Based on https://flask.palletsprojects.com/en/2.3.x/views/#method-dispatching-and-apis
# Using one class for the view including the methods with and without IDs:
#      POST /files/
#       GET /files/<file_hash>
#    DELETE /files/<file_hash>
# FIXME: Should the logger be initialized for this class?  Or handled more globally?
#        Will need to test if this class is initiallized for each request.
class FilesView(MethodView):
    def get(self, file_hash):
        # Return a single file by hash
        # FIXME: How do we want to handle different hashes?  Split on '_' and check len?
        #         - This will likely require some sort of index for the other hashes.
        # FIXME: Have to stream the data from disk back out the connection.
        pass

    def post(self):
        # Create a new file
        # Return the file stats including all supported hashed
        # FIXME: This file handling should be moved to a class
        # FIXME: How should errors, such as broken connections, be handled?
        # FIXME: Should stream to an 'uploads' folder in the filestore.
        #         - Upon completion, copy to the main folder.
        #         - Upon failure, delete as part of cleanup.
        # FIXME: Should have a background process that cleans up the uploads folder if not an active upload.
        # FIXME: Chunking uploads can also use this 'uploads' folder.
        # FIXME: Should have a 'factory' class that manages active uploads.
        with open("/tmp/output_file", "bw") as f:
            chunk_size = 4096
            while True:
                chunk = request.stream.read(chunk_size)
                if len(chunk) == 0:
                    return
                f.write(chunk)
        # FIXME: Return a 201 with the hashes

    def delete(self, file_hash):
        # Delete the file by hash
        pass
