#!/usr/bin/env python

from lib.actions import BaseAction
from lib.mycollectors import MyCollectors


class SumoGetId(BaseAction):
    def run(self, keyword=None):
        self.logger.debug('keyword: %s', keyword)

        result = []
        if self._client is None:
            self.logger.debug('No Access ID or Key is configured. Please, configure.')
            return False, result

        collector = MyCollectors(self._client)
        c = collector.find_sub(keyword)
        if c is not None:
            ids = []
            for i in c:
                ids.append(i["id"])
            return True, ids
        else:
            return True, []
