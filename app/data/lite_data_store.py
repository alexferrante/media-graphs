import logging

import dataset

from app.core.str_utils import plain_to_b64_str, b64_to_plain_str
from app.data.entities import AppState, APP_STATE_RECORD_TYPE
from app.events.signals import AppEvents


class LiteDataStore:
    app_events = AppEvents()

    def __init__(self, data_dir):
        self.data_dir = data_dir
        db_path = f"sqlite:///{self.data_dir}/app.db"
        self.db = dataset.connect(db_path)
        self._app_state = self.get_app_state()

    @property
    def app_state(self):
        return self._app_state

    def update_app_state_in_db(self):
        app_state_table = self.db[self.app_state.record_type]
        app_state_table.upsert(
            dict(name=self.app_state.record_type, object=self.app_state.to_json_str()),
            ["name"],
        )

    def get_app_state(self):
        table = self.db[APP_STATE_RECORD_TYPE]
        app_state_record = table.find_one(name=APP_STATE_RECORD_TYPE)
        if not app_state_record:
            return AppState()

        return AppState.from_json_str(app_state_record["object"])


    def update_graph_store(self, node_list):
        logging.debug(f"Updating current store for nodes. Total: {len(node_list)}")
        if not node_list:
            return
        self.app_state.nodes = node_list
        self.update_app_state_in_db()

    
    def get_nodes(self):
        return b64_to_plain_str(self.app_state.nodes)


