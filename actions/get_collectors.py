#!/usr/bin/env python

from lib.actions import BaseAction
import lib.utils


class SumoGetCollectors(BaseAction):
    def run(self, keyword=None, exact_match=False):
        self.logger.debug('keyword: %s', keyword)
        result = []
        if self._client is None:
            self.logger.debug('No Access ID or Key is configured. Please, configure.')
            return False, result

        collectors = self._client.collectors(10000)
        c = lib.utils.find_by_field(collectors, 'name', keyword, exact_match)
        return True, c
