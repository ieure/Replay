# -*- coding: utf-8 -*-
#
# © 2009, 2010 Digg, Inc. All rights reserved.
# Author: Ian Eure <ian@digg.com>
#

"""Log replay tool."""

from datetime import datetime, timedelta
from time import sleep
import logging
import logging.handlers

LOG = logging.getLogger(__name__)


def mapc_time(func, seq, scale=1.0, repeat=1):
    """
    mapc_time(func, seq [,scale, repeat]) -> None

    Apply a function over a sequence in real time.

    Expects seq to be a sequence of tuples in the format:
    (datetime, data)

    Where datetime is a datetime object representing the time at which
    data was recorded. The data is passed to func unaltered.
    """
    last, exc_time = None, timedelta()
    for (when, data) in seq:
        assert isinstance(when, datetime), "Invalid seq"
        if not last:
            last = when

        if when < last:
            LOG.warn("Invalid seq: %s < %s" % (when, last))
            when = last

        interval = (when - last)
        if exc_time <= interval:
            interval -= exc_time

        LOG.debug("Execution took %fs, interval was %fs.",
                  exc_time.seconds, interval.seconds)

        if interval < timedelta():
            LOG.warn("Falling behind!")
            interval = timedelta()

        LOG.debug("Sleeping %ss" % interval.seconds)
        sleep(interval.seconds * scale)

        start_time = datetime.now()
        for num in range(repeat):
            func(data, repeat)

        exc_time = timedelta() + (datetime.now() - start_time)
        last = when
