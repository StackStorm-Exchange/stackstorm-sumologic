#!/usr/bin/env python

from lib.actions import BaseAction
from lib.sources import Sources


class SumoGetSources(BaseAction):
    def run(self, collector_id=None):

        self.logger.debug('collector_id: %d', collector_id)

        result = []
        if self._client is None:
            self.logger.debug('No Access ID or Key is configured. Please, configure.')
            return False, result

        sources = Sources(self._client, collector_id=collector_id)
        src = sources.get()
        if src.get("sources") is not None:
            all_sources = src["sources"]
            return True, all_sources
        else:
            return True, []
