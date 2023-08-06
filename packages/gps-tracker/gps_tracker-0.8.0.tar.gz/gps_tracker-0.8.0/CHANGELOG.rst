=========
Changelog
=========

0.8.0
-----

- Fix invalid icon id for dog and manually check all the others. Thanks `@nickoe <https://gitlab.com/nickoe>`_ for the bug report!
- Implement default ``UNKNOWN`` values for
  :class:`TrackerIcon <gps_tracker.client.datatypes.TrackerIcon>`,
  :class:`TrackerMode <gps_tracker.client.datatypes.TrackerMode>` and
  :class:`TrackerUsage <gps_tracker.client.datatypes.TrackerUsage>` to prevent direct failure
  in case of unexpected values for these fields.

0.7.1
-----

- Make the :class:`TrackerStatus <gps_tracker.client.datatypes.TrackerStatus>`
  :attr:`sub_end_date <gps_tracker.client.datatypes.TrackerStatus.sub_end_date>` attribute optional.
  Thanks `Chris van Marle (@qistoph) <https://gitlab.com/qistoph>`_ for the bug report!
- Add trackers of type :class:`tracker_03 <gps_tracker.client.datatypes.Tracker03>`.
  Thanks `@DataIsGold <https://gitlab.com/DataIsGold>`_ for the bug report!

0.7.0
-----

- Revamp exception handling so that all calls to API derive from
  :class:`GpsTrackerException <gps_tracker.client.exceptions.GpsTrackerException>`.
- Rewrite all tests to not depend on actual API calls but mocked ones.

0.6.0
-----

- Add the possibility to provide a aiohttp.ClientSession instance to
  AsyncClient.

0.5.0
-----

- Improve handling of unexpected data in API answers

0.4.0
-----
- Fix attrs import when attrs<2021.3.0 is installed (required
  for Home-Assistant 2021.12 which pins attrs==2021.2.0)
- Add new client methods: ``get_trackers``, ``get_tracker_config`` and
  ``get_tracker_status``
- Improve synchronous client performances by using a single requests.Session
  over the client lifecycle
- Increase test coverage

0.3.0
-----

- Rename package from ``invoxia`` to ``gps_tracker``

0.2.0
-----

- Implement Asynchronous client using aiohttp

0.1.3
-----

- Fix issues with unit-test execution

0.1.2
-----

- Implement unit-tests for synchronous client

0.1.1
-----

- Fix badges in README.rst

0.1.0
-----

- Implement the synchronous :class:`Client <gps_tracker.client.sync.Client>`
- Document the use of :doc:`current module <api/modules>` and :doc:`quickstart <start>`
- Add :mod:`enumerations <gps_tracker.client.datatypes>` to improve readability
  of some tracker attributes.
