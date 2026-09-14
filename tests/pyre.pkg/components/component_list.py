#!/usr/bin/env python3
# -*- Python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


import pyre


# a protocol
class activity(pyre.protocol, family="sample.activities"):
    """the activity specification"""

    # get the time units
    from pyre.units import time

    # my traits
    duration = pyre.properties.dimensional(default=time.hour)

    # my public interface
    @pyre.provides
    def do(self):
        """do something"""

    # set  up my default implementation
    @classmethod
    def pyre_default(cls, **kwds):
        return relax


# a few implementations
class study(pyre.component, family="sample.activities.study", implements=activity):
    """an activity"""

    # my traits
    duration = pyre.properties.dimensional(default=4 * activity.time.hour)

    @pyre.export
    def do(self):
        return "studying"


class relax(pyre.component, family="sample.activities.relax", implements=activity):
    """an activity"""

    # my traits
    duration = pyre.properties.dimensional(default=2 * activity.time.hour)

    @pyre.export
    def do(self):
        return "relaxing"


class sleep(pyre.component, family="sample.activities.sleep", implements=activity):
    """an activity"""

    # my traits
    duration = pyre.properties.dimensional(default=8 * activity.time.hour)

    @pyre.export
    def do(self):
        return "sleeping"


# the containers
class activities_empty(pyre.component, family="sample.activities_empty"):
    """a component container"""

    activities = pyre.properties.list(schema=activity())


class activities_none(pyre.component, family="sample.activities_none"):
    """a component container"""

    activities = pyre.properties.list(schema=activity(), default=None)


class activities_default(pyre.component, family="sample.activities_default"):
    """a component container"""

    activities = pyre.properties.list(schema=activity(), default=[study, relax])


class person(pyre.component, family="sample.person"):
    """a component container"""

    activities = pyre.properties.list(schema=activity())


def test_activities():
    # easy access to time units
    from pyre.units.time import hour

    list_empty = activities_empty("empty")
    list_none = activities_none("none")
    list_default = activities_default("default")

    # No default (should be [])
    assert len(list_empty.activities) == 0

    # default = None
    assert list_none.activities is None

    # default = [study, relax]
    assert len(list_default.activities) == 2
    task = list_default.activities[0]
    assert task.pyre_name == "sample.activities.study"
    assert task.pyre_family() == "sample.activities.study"
    assert task.duration == 4 * hour
    task = list_default.activities[1]
    assert task.pyre_name == "sample.activities.relax"
    assert task.pyre_family() == "sample.activities.relax"
    assert task.duration == 2 * hour


def test_person():
    # easy access to time units
    from pyre.units.time import hour

    # make a container; configuration comes from {sample.pml}
    alec = person("alec")
    # dump
    # print('alec:')
    # for task in alec.activities:
    # print('  {}'.format(task))
    # print('    {} for {:base={scale},label=hours}'.format(
    # task.do(), task.duration, scale=activity.time.hour))

    # here is what we expect
    # task 0
    task = alec.activities[0]
    assert task.pyre_name == "physics"
    assert task.pyre_family() == "sample.activities.study"
    assert task.duration == 0.5 * hour

    # task 1
    task = alec.activities[1]
    assert task.pyre_name == "wow"
    assert task.pyre_family() == "sample.activities.relax"
    assert task.duration == 1 * hour

    # task 2
    task = alec.activities[2]
    assert task.pyre_name == "nap"
    assert task.pyre_family() == "sample.activities.sleep"
    assert task.duration == 3 * hour


# main
if __name__ == "__main__":
    test_activities()
    test_person()

# end of file
