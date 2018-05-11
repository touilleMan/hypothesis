# coding=utf-8
#
# This file is part of Hypothesis, which may be found at
# https://github.com/HypothesisWorks/hypothesis-python
#
# Most of this work is copyright (C) 2013-2018 David R. MacIver
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

import os
from glob import glob

import pytest

import hypothesistooling as tools
from hypothesistooling.scripts import pip_tool

ROOT_RST = glob(os.path.join(tools.ROOT, '*.rst'))
GUIDES = glob(os.path.join(tools.ROOT, 'guides', '*.rst'))
PYTHON_DOCS = os.path.join(tools.HYPOTHESIS_PYTHON, '*.rst')


def test_covers_all_rst_files():
    all_rst = {
        f for f in tools.all_files() if f.endswith('.rst') and
        os.path.basename(f) != 'RELEASE.rst'
    }
    assert set(ROOT_RST + GUIDES + PYTHON_DOCS) == all_rst


@pytest.mark.parametrize('f', ROOT_RST + GUIDES)
def test_passes_rst_lint(f):
    pip_tool('rst-lint', f)


@pytest.mark.parametrize('f', ROOT_RST + GUIDES + PYTHON_DOCS)
def test_passes_flake8(f):
    pip_tool('flake8', '--select=W191,W291,W292,W293,W391', f)
