from src.handler.track import Track
from src import app
from flask import jsonify

class StatusController:
    def __init__(self, track: Track) -> None:
        self.track = track
        self.configEndpoints()

    def status(self):
        status_list = self.track.getStatusTitleList()
        status_map = {'status':status_list}
        status_map_json = jsonify(status_map)
        return status_map_json

    def configEndpoints(self):
        app.add_url_rule('/status', view_func=self.status, methods=['GET'])