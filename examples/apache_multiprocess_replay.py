# -*- coding: utf-8 -*-
#
# © 2009 Digg. All rights reserved.
# Author: Ian Eure <ian@digg.com>
#

"""Replay a log file with multiprocessing."""

from __future__ import with_statement
import logging
from multiprocessing.dummy import Pool
import threading
from replay import mapc_time

from apache_replay import generate, request

POOL = Pool(10)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    mapc_time(lambda *args: POOL.apply_async(request, args),
              generate('apache-access.log'))
    POOL.close()
    POOL.join()
