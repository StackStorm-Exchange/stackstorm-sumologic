#!/usr/bin/env python

from .lib.actions import BaseAction


class SumoGetSources(BaseAction):
    def run(self, collector_id=None):

        self.logger.debug('collector_id: %d', collector_id)

        result = []
        if self._client is None:
            self.logger.debug('No Access ID or Key is configured. Please, configure.')
            return False, result

        sources = self._client.sources(collector_id)
        return True, sources
