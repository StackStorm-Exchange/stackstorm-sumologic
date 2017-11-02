# Base Action Class

from st2common.runners.base_action import Action
from sumologic import SumoLogic

__all__ = [
    'BaseAction',
]


class BaseAction(Action):
    def run(self, **kwargs):
        pass

    def __init__(self, config):
        super(BaseAction, self).__init__(config)
        access_id = self.config.get('sumologic_access_id', None)
        access_key = self.config.get('sumologic_access_key', None)
        sumologic_collectors_limit = self.config.get('sumologic_collectors_limit', 1000)
        self._sumologic_access_key = access_key or None
        self._sumologic_access_id = access_id or None
        self._sumologic_collectors_limit = sumologic_collectors_limit or 1000
        if self._sumologic_access_key is None or self._sumologic_access_id is None:
            self._client = None
        else:
            self._client = SumoLogic(self._sumologic_access_id, self._sumologic_access_key)
