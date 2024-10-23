#!/usr/bin/env python3

### IMPORTS ###
import logging

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class StorageManager:
    def __init__(self):
        self.logger = logging.getLogger(type(self).__name__)
        # Data Structures:
        # LRU Cache for Binaries
        # LRU Cache for Markers
        #     - Should this be multiple LRU Caches, one for each hash type?
        #     - Should this be in the same LRU Cache as the binaries?
        #     - Should there even be a cache?
        # File Store Configuration

        # Factory Functions:
        # Create Binary
        # Create Marker
        #     - Should the marker be handled by the binary?
        # Get Binary
        #     - Should this (and the "Get Marker") be "Get By Hash"?
        # Get Marker
        # Delete Binary
        #     - Should this (and the "Delete Marker") be "Delete By Hash"?
        # Delete Marker
        # Migrate Binary to new default hash
