# st2-sumologic
Stackstorm SumoLogic Integration Pack

## Description

Pack is mainly used to manipulate SumoLogic collectors and sources. Yet, incomplete, but has basic functionality to manipulate sources.

## Change log

0.9.5 - Added README and updated icon.
0.9.4 - Initial release. So far it does everything we need.

## Configuration

* `sumologic_access_id` - Access ID or email. Obtained from your profile.
* `sumologic_access_key` - Access Key or password.
* `sumologic_collectors_limit` - Number of collectors to fetch from the SumoLogic API endpoint.

## Actions

* `create.source` - Create source for a collector.
* `delete.source` - Delete source for a collector.
* `get.collector` - Get collector by id or name with all its properties.
* `get.collectors` - Get a list of collectors by their name with all their properties.
* `get.id` - Get ID or IDs of collectors.
* `get.sources` - Get a list of sources by ID of collector.
* `update.source` - Update source for a collector.

## Known limitations

* Only three type of sources are supported at this time:
  1. LocalFile
  2. RemoteFileV2 - not tested
  3. SystemStats - not tested

## TODO

* Upgrade collectors - scheduling tasks for upgrade using API (extend sumologic-python-sdk)
* Update collectors - update collector's properties using API (using sumologic-python-sdk methods)
