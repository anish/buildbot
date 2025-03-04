# This file is part of Buildbot.  Buildbot is free software: you can
# redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, version 2.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Copyright Buildbot Team Members


from twisted.internet import defer

from buildbot.data import base
from buildbot.data import types
from buildbot.warnings import warn_deprecated


class RootEndpoint(base.Endpoint):
    kind = base.EndpointKind.COLLECTION
    pathPatterns = "/"

    def get(self, resultSpec, kwargs):
        warn_deprecated('4.3.0', 'the root endpoint with endpoint directory has been deprecated')
        return defer.succeed(self.master.data.rootLinks)


class Root(base.ResourceType):
    name = "rootlink"
    plural = "rootlinks"
    endpoints = [RootEndpoint]

    class EntityType(types.Entity):
        name = types.String()

    entityType = EntityType(name)


class SpecEndpoint(base.Endpoint):
    kind = base.EndpointKind.COLLECTION
    pathPatterns = "/application.spec"

    def get(self, resultSpec, kwargs):
        return defer.succeed(self.master.data.allEndpoints())


class Spec(base.ResourceType):
    name = "spec"
    plural = "specs"
    endpoints = [SpecEndpoint]

    class EntityType(types.Entity):
        path = types.String()
        type = types.String()
        plural = types.String()
        type_spec = types.JsonObject()

    entityType = EntityType(name)
