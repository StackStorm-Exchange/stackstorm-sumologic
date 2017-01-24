#!/usr/bin/env python

from lib.actions import BaseAction


class SumoUpdateSource(BaseAction):
    def run(self,
            collector_id=None,
            source_id=None,
            timezone=None,
            category=None,
            descr=None,
            force_timezone=None,
            hostname=None,
            name=None,
            path_expression=None,
            auto_line_matching=None,
            automatic_date_parsing=None,
            multiline_processing_enabled=None,
            encoding=None,
            manual_prefix_regexp=None,
            content_type=None,
            metrics=None,
            cutoff_timestamp=None,
            interval=None):

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

        src_o, etag = self._client.source(collector_id, source_id)
        if src_o is not None and etag is not None and src_o.get('source') is not None:
            params = src_o['source']

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
            res = self._client.update_source(collector_id, data, etag)
            return True, res.json()
        else:
            return False, {'status': 'Could not retrieve original source from that collector.'}
