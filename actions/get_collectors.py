#!/usr/bin/env python

from lib.actions import BaseAction


def find_by_field(cs, field, keyword, exact_match):
    res = []
    for c in cs:
        if exact_match:
            if field in c and keyword == c[field]:
                res.append(c)
        else:
            if field in c and keyword in c[field]:
                res.append(c)
    return res


class SumoGetCollectors(BaseAction):
    def run(self, keyword=None, exact_match=False):
        self.logger.debug('keyword: %s', keyword)

        result = []
        if self._client is None:
            self.logger.debug('No Access ID or Key is configured. Please, configure.')
            return False, result

        collectors = self._client.collectors()
        c = find_by_field(collectors, 'name', keyword, exact_match)
        return True, c
