# Base Action Class

from st2actions.runners.pythonrunner import Action
from sumologic import Client

__all__ = [
    'BaseAction',
    'MyCollectors'
]


class BaseAction(Action):
    def run(self, **kwargs):
        pass

    def __init__(self, config):
        super(BaseAction, self).__init__(config)
        access_id = self.config.get('sumologic_access_id', None)
        access_key = self.config.get('sumologic_access_key', None)
        self.sumologic_access_key = access_key or None
        self.sumologic_access_id = access_id or None
        if self.sumologic_access_key is None or self.sumologic_access_id is None:
            self._client = None
        else:
            self._client = Client(auth=(self.sumologic_access_id, self.sumologic_access_key))
