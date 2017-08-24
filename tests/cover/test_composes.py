# coding=utf-8
#
# This file is part of Hypothesis, which may be found at
# https://github.com/HypothesisWorks/hypothesis-python
#
# Most of this work is copyright (C) 2013-2017 David R. MacIver
# (david@drmaciver.com), but it contains contributions by others. See
# CONTRIBUTING.rst for a full list of people who may hold copyright, and
# consult the git log if you need to determine who owns an individual
# contribution.
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file, You can
# obtain one at http://mozilla.org/MPL/2.0/.
#
# END HEADER

from __future__ import division, print_function, absolute_import

import hypothesis.strategies as st
from hypothesis import given


def sized_list(elements, size):
    return st.lists(elements, min_size=size, max_size=size)


@given(st.composes(sized_list, st.just(st.booleans()), st.integers(3, 5)))
def test_composing_size(ls):
    assert 3 <= len(ls) <= 5


@given(st.composes(
    lambda size: st.lists(sized_list(st.booleans(), size), min_size=1),
    st.integers(0, 10),
))
def test_is_a_rectangle(rect):
    assert len(set(map(len, rect))) == 1
