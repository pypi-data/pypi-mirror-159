import logging
import os
import time

from mopidy import config, ext

import requests

__version__ = '0.1.1'

check_urls = [
    'https://cloudflare-dns.com/dns-query?dns=AAABAAABAAAAAAAACmNsb3VkZmxhcmUDY29tAAABAAE',
    'https://cloudflare-dns.com/dns-query?dns=AAABAAABAAAAAAAABm1vcGlkeQNjb20AAAEAAQ',
    'https://dns.google/dns-query?dns=AAABAAABAAAAAAAABmdvb2dsZQNjb20AAAEAAQ',
    'https://dns.google/dns-query?dns=AAABAAABAAAAAAAABm1vcGlkeQNjb20AAAEAAQ',
    'https://dns.quad9.net/dns-query?dns=AAABAAABAAAAAAAABm1vcGlkeQNjb20AAAEAAQ'
]

logger = logging.getLogger(__name__)


class WaitForInternetExtension(ext.Extension):
    dist_name = 'Mopidy-WaitForInternet'
    ext_name = 'waitforinternet'
    version = __version__

    def get_default_config(self):
        conf_file = os.path.join(os.path.dirname(__file__), 'ext.conf')
        return config.read(conf_file)

    def setup(self, registry):
        retries = 0
        verified = False
        start = time.monotonic()
        while time.monotonic() - start < 300:
            try:
                requests.get(check_urls[retries % len(check_urls)], timeout=10, allow_redirects=False)
                verified = True
                break
            except Exception:
                time.sleep(1)
                retries += 1
        logger.info('Internet connectivity verified: %s, retries: %d, time taken %.3fs', verified, retries, time.monotonic() - start)
