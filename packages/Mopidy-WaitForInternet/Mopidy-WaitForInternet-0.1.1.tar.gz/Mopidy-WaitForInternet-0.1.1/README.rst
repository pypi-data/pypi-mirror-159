****************************
Mopidy-WaitForInternet
****************************

.. image:: https://img.shields.io/pypi/v/Mopidy-WaitForInternet.svg?style=flat
    :target: https://pypi.python.org/pypi/Mopidy-WaitForInternet/
    :alt: Latest PyPI version

.. image:: https://img.shields.io/pypi/dm/Mopidy-WaitForInternet.svg?style=flat
    :target: https://pypi.python.org/pypi/Mopidy-WaitForInternet/
    :alt: Number of PyPI downloads

.. image:: https://img.shields.io/github/workflow/status/DavisNT/mopidy-waitforinternet/Python%20build/develop.svg?style=flat
    :target: https://github.com/DavisNT/mopidy-waitforinternet/actions/workflows/ci.yml
    :alt: GitHub Actions build status

.. image:: https://img.shields.io/coveralls/github/DavisNT/mopidy-waitforinternet.svg?style=flat
    :target: https://coveralls.io/github/DavisNT/mopidy-waitforinternet
    :alt: Coveralls test coverage

.. image:: https://img.shields.io/github/workflow/status/DavisNT/mopidy-waitforinternet/Test%20connectivity%20check%20servers/develop.svg?style=flat&label=servers-test
    :target: https://github.com/DavisNT/mopidy-waitforinternet/actions/workflows/servers-test.yml
    :alt: Weekly build that tests connectivity check servers

`Mopidy <http://www.mopidy.com/>`_ extension that waits (up to around 5 minutes) for an internet connection during early phase of Mopidy startup (before other extensions start to initialize).


Installation
============

Install by running::

    pip install Mopidy-WaitForInternet


Configuration
=============

This extension has no configuration options in ``mopidy.conf`` apart from the default ``enabled`` setting::

    [waitforinternet]
    # To temporary disable this extension without uninstalling it
    enabled = false


Usage
=====

This extension will delay initialization of other Mopidy extensions until an internet connection has been initialized (for up to around 5 minutes).

Mopidy-WaitForInternet might be useful if other Mopidy extensions (e.g. extensions for online music streaming services) fail to initialize, because they try to connect to internet resources before machine running Mopidy has established an internet connection (e.g. connected to wifi).

Important internals
===================

Mopidy-WaitForInternet uses several different URLs (currently - requests to public `DoH <https://en.wikipedia.org/wiki/DNS_over_HTTPS>`_ servers) to check internet connectivity. As a future-proofing measure there is a `weekly servers-test build <https://github.com/DavisNT/mopidy-waitforinternet/actions/workflows/servers-test.yml>`_ that verifies availability of these URLs.

License
=======
::

   Copyright 2022 Davis Mosenkovs

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.


Project resources
=================

- `Source code <https://github.com/DavisNT/mopidy-waitforinternet>`_
- `Issue tracker <https://github.com/DavisNT/mopidy-waitforinternet/issues>`_
- `Development branch tarball <https://github.com/DavisNT/mopidy-waitforinternet/archive/develop.tar.gz#egg=Mopidy-WaitForInternet-dev>`_
- `Weekly servers-test build that tests URLs used by Mopidy-WaitForInternet for internet connectivity check <https://github.com/DavisNT/mopidy-waitforinternet/actions/workflows/servers-test.yml>`_


Changelog
=========

v0.1.1
----------------------------------------

- Fixed README formatting.
- Initial release.

v0.1.0 (UNRELEASED)
----------------------------------------

- Initial version.
