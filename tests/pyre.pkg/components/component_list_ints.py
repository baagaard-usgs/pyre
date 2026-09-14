#!/usr/bin/env python3
# -*- Python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved

import pyre


# containers that are a list of integers
class integers_empty(pyre.component, family="sample.integers_empty"):
    """a component container"""

    values = pyre.properties.list(schema=pyre.properties.int())


class integers_none(pyre.component, family="sample.integers_none"):
    """a component container"""

    values = pyre.properties.list(schema=pyre.properties.int(), default=None)


class integers_default(pyre.component, family="sample.integers_default"):
    """a component container"""

    values = pyre.properties.list(schema=pyre.properties.int(), default=[5])


class integers_default3(pyre.component, family="sample.integers_default3"):
    """a component container"""

    values = pyre.properties.list(schema=pyre.properties.int(), default=[5, 3, 9])


# Test list of integers
def test_integers():

    ints_empty = integers_empty("empty")
    ints_none = integers_none("none")
    ints_default = integers_default("default")
    ints_default3 = integers_default3("default3")

    # dump
    # print(f"integers_empty: {ints_empty.values}")
    # print(f"integers_none: {ints_none.values}")
    # print(f"integers_default: {ints_default.values}")

    # No default (should be [])
    assert len(ints_empty.values) == 0

    # default = None
    assert ints_none.values is None

    # default = [5]
    assert len(ints_default.values) == 1
    assert ints_default.values[0] == 5

    # default = [5, 3, 9]
    assert len(ints_default3.values) == 3
    assert ints_default3.values[0] == 5
    assert ints_default3.values[1] == 3
    assert ints_default3.values[2] == 9
    ints_default3.values[1] = 6
    assert ints_default3.values[0] == 5
    assert ints_default3.values[1] == 6
    assert ints_default3.values[2] == 9


# main
if __name__ == "__main__":
    test_integers()

# end of file
