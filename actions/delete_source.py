#!/usr/bin/env python

from lib.actions import BaseAction
import requests


class SumoDeleteSource(BaseAction):
    def run(self, collector_id=None, source_id=None):

        self.logger.debug('collector_id: %d', collector_id)
        self.logger.debug('source_id: %d', source_id)

        result = {}
        if self._client is None:
            self.logger.debug('No Access ID or Key is configured. Please, configure.')
            result['status'] = 'No Access ID or Key is configured. Please, configure.'
            return False, result

        if collector_id is None:
            self.logger.debug('No Collector ID was provided.')
            result['status'] = 'Failed: No Collector ID was provided.'
            return False, result

        if source_id is None:
            self.logger.debug('No source ID was provided.')
            result['status'] = 'No source ID was provided.'
            return False, result

        # creating this stupid hash to pass it to delete_source method so it can
        # extract the ID from it
        data = {'source': {'id': source_id}}
        try:
            res = self._client.delete_source(collector_id, data)
            result['status'] = res.status_code
            return True, result
        except requests.exceptions.HTTPError as e:
            result['status'] = str(e)
            return False, result
