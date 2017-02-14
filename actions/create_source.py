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
            blacklist=None,
            remote_hosts=None,
            remote_port=None,
            remote_user=None,
            remote_password=None,
            key_path=None,
            key_password=None,
            auth_method=None,
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

        if source_type == 'RemoteFileV2' and (remote_hosts is None or
                                              remote_port is None or
                                              remote_user is None):
            self.logger.debug(
                'No remote host/port or user was provided for source type RemoteFileV2.'
            )
            result['status'] = 'Failed: ' + \
                'No remote host/port or user was provided for source type RemoteFileV2.'
            return False, result

        elif source_type == 'RemoteFileV2' and (auth_method is None or 
                                                auth_method != 'password' or 
                                                auth_method != 'key'):
            self.logger.debug(
                'Cannot recognize auth method for source type RemoteFileV2. ' + \
                'Can be password or key only.')
            result['status'] = 'Failed: ' + \
                'Cannot recognize auth method for source type RemoteFileV2. ' + \
                'Can be password or key only.'
            return False, result

        elif source_type == 'RemoteFileV2' and (auth_method == 'password' and
                                                remote_password is None):
            self.logger.debug('Password was not provided when auth method is password.')
            result['status'] = 'Failed: Password was not provided when auth method is password.'
            return False, result

        elif source_type == 'RemoteFileV2' and auth_method == 'key' and key_path is None:
            self.logger.debug('Path to private key was not provided when auth method is key.')
            result['status'] = 'Failed: ' + \
                'Path to private key was not provided when auth method is key.'
            return False, result

        elif source_type == 'RemoteFileV2' and path_expression is None:
            self.logger.debug('Path expression of the files to collect was not provided.')
            result['status'] = 'Failed: Path expression of the files to collect was not provided.'
            return False, result

        if source_type == 'SystemStats' and interval is None:
            self.logger.debug('No interval provided for source type SystemStats.')
            result['status'] = 'Failed: No interval provided for source type SystemStats.'
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
        if blacklist is not None:
            params['blacklist'] = blacklist

        data = {'source': params}
        res = self._client.create_source(collector_id, data)
        return True, res.json()
