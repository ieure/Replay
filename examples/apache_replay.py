# -*- coding: utf-8 -*-
#
# © 2009 Digg, Inc. All rights reserved.
# Author: Ian Eure <ian@digg.com>
#

"""Replay an Apache log file."""

from __future__ import with_statement
from datetime import datetime, timedelta
from replay import mapc_time
import urllib2
import logging

HOST = "example.com"

def generate(log_file):
    """Generate (datetime, line) tuples for an Apache log."""
    with open(log_file) as log:
        for line in log:
            (ts, tz) = line.split('[', 1)[1].split(']', 1)[0].split()
            offset = timedelta(**{'hours': int(tz[1:3]),
                                  'minutes': int(tz[3:])}) * \
                                  (tz[0] == '-' and -1 or 1)
            yield (datetime.strptime(ts, '%d/%b/%Y:%H:%M:%S') + offset, line)


def request(line, repeat):
    """Synthesize a request."""
    url = "http://%s%s" % (HOST, line.split('"')[1].split()[1])
    logging.info("Requesting %s" % url)
    return
    try:
        handle = urllib2.urlopen(url)
        handle.read()
        handle.close()
    except Exception, exc:
        logging.error("%s: %s" % (url, exc))
        pass


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    mapc_time(request, generate('apache-access.log'))
