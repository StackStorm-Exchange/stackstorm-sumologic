from sumologic import Collectors

__all__ = [
    'MyCollectors'
]


class MyCollectors(Collectors):
    def find_sub(self, name):
        """Returns a list of dicts of collectors' details if found.

        Args:
          name (str): name of collector searching for
        """
        collectors = self.get_collectors()
        collectors_found = []
        for collector in collectors:
            if name.lower() in collector['name'].lower():
                collectors_found.append(collector)

        if len(collectors_found) > 0:
            return collectors_found
        else:
            return None

    def find_by_id(self, collector_id):
        """Returns a dict of collector's details if found.

        Args:
          collector_id (integer): ID of collector searching for
        """
        collectors = self.get_collectors()
        for collector in collectors:
            if int(collector_id) == int(collector['id']):
                return collector

        return None

    pass
