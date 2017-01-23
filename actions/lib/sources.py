import requests


class Sources(object):
    """ This object acts upon the sources """

    def __init__(self, auth, collector_id, api='/collectors', **kwargs):
        """Access sumologic Sources.
        Args:
            auth (Auth): Authentication object
            api (str): Api endpath
            collector_id (integer): Collector ID of the source
        """
        self.api = api
        self.collector_id = None
        self.log = auth.log
        self.collector_id = collector_id

        try:
            self.url = '%s%s' % (auth.get_url(), self.api)
        except AttributeError:
            self.url = 'https://api.sumologic.com/api/v1%s' % self.api

        try:
            self.auth = auth.get_auth()
        except AttributeError:
            self.auth = auth

    def get(self):
        """Return a dict of a source."""
        request = requests.get('%s/%d/sources' % (self.url, self.collector_id), auth=self.auth)
        return request.json()
