#!/usr/bin/env python

from lib.actions import BaseAction


class SumoCreateSource(BaseAction):
    def run(self,
            collector_id=None,
            timezone=None,
            category=None,
            descr=None,
            force_timezone=False,
            hostname=None,
            name=None,
            path_expression=None,
            source_type='LocalFile',
            auto_line_matching=True,
            automatic_date_parsing=True,
            multiline_processing_enabled=True,
            encoding=None,
            manual_prefix_regexp=None,
            content_type=None,
            metrics=None,
            interval=None,
            cutoff_timestamp=None):

        self.logger.debug('collector_id: %d', collector_id)

        result = {}
        if self._client is None:
            self.logger.debug('No Access ID or Key is configured. Please, configure.')
            result['status'] = 'No Access ID or Key is configured. Please, configure.'
            return False, result

        if collector_id is None:
            self.logger.debug('No Collector ID was provided.')
            result['status'] = 'Failed: No Collector ID was provided.'
            return False, result

        if name is None:
            self.logger.debug('No name was provided.')
            result['status'] = 'Failed: No name was provided.'
            return False, result

        if source_type == 'LocalFile' and path_expression is None:
            self.logger.debug('No file path was provided for source type LocalFile.')
            result['status'] = 'Failed: No file path was provided for source type LocalFile.'
            return False, result

        if source_type == 'SystemStats' and (metrics is None or len(metrics) < 1):
            self.logger.debug('No metrics provided for source type SystemStats.')
            result['status'] = 'Failed: No metrics provided for source type SystemStats.'
            return False, result

        params = {'name': name, 'sourceType': source_type}
        if timezone is not None:
            params['timeZone'] = timezone
        if category is not None:
            params['category'] = category
        if descr is not None:
            params['description'] = descr
        if force_timezone is not None:
            params['forceTimeZone'] = force_timezone
        if hostname is not None:
            params['hostName'] = hostname
        if path_expression is not None:
            params['pathExpression'] = path_expression
        if auto_line_matching is not None:
            params['useAutolineMatching'] = auto_line_matching
        if automatic_date_parsing is not None:
            params['automaticDateParsing'] = automatic_date_parsing
        if multiline_processing_enabled is not None:
            params['multilineProcessingEnabled'] = multiline_processing_enabled
        if encoding is not None:
            params['encoding'] = encoding
        if manual_prefix_regexp is not None:
            params['manualPrefixRegexp'] = manual_prefix_regexp
        if content_type is not None:
            params['contentType'] = content_type
        if metrics is not None:
            params['metrics'] = metrics
        if interval is not None:
            params['interval'] = interval
        if cutoff_timestamp is not None:
            params['cutoffTimestamp'] = cutoff_timestamp

        data = {'source': params}
        res = self._client.create_source(collector_id, data)
        return True, res.json()
