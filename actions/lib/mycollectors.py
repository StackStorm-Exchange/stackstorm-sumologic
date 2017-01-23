from sumologic import Collectors


class MyCollectors(Collectors):
    def find_sub(self, name):
        """Returns a dict of collector's details if found.

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

    pass
