# coding=utf-8

# Copyright (C) 2013-2015 David R. MacIver (david@drmaciver.com)

# This file is part of Hypothesis (https://github.com/DRMacIver/hypothesis)

# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file, You can
# obtain one at http://mozilla.org/MPL/2.0/.

# END HEADER

from __future__ import division, print_function, absolute_import, \
    unicode_literals

from hypothesis.utils.idkey import IdKey


class Friendly(object):

    def __eq__(self, other):
        return True

    def __ne__(self, other):
        return False


def test_id_key_respects_identity():
    x = Friendly()
    y = Friendly()
    assert x == y
    assert not (x != y)

    assert IdKey(x) != x
    assert IdKey(x) == IdKey(x)
    t = IdKey(x)
    assert t == t

    assert IdKey(x) != IdKey(y)
