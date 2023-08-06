#!/usr/bin/env python3
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-

# Author:  Bryce Harrington <bryce@canonical.com>
#
# Copyright (C) 2019 Bryce W. Harrington
#
# Released under GNU GPLv2 or later, read the file 'LICENSE.GPLv2+' for
# more information.

from textwrap import indent
from functools import lru_cache
from lazr.restfulclient.errors import BadRequest, NotFound

def ppa_address_split(ppa_address, default_team='me'):
    """Parse an address for a ppa into its team and name components
    """
    if ppa_address.startswith('ppa:'):
        if '/' not in ppa_address:
            return (None, None)
        rem = ppa_address.split('ppa:',1)[1]
        team_name = rem.split('/', 1)[0]
        ppa_name = rem.split('/', 1)[1]
    else:
        team_name = default_team
        ppa_name = ppa_address
    return (team_name, ppa_name)

def get_das(distro, series_name, arch_name):
    """Retrive the arch-series for the given distro

    :param tbd distro: The distribution object.
    :param str series_name: The distro's codename for the series.
    :param str arch_name: The hardware architecture.
    :rtype: tbd
    :returns: A series object, or None on error.
    """
    assert series
    if series_name is None or series_name == '':
        return None

    for series in distro.series:
        if series.name != series_name:
            continue
        return series.getDistroArchSeries(archtag=arch_name)
    return None


class Ppa:
    """Encapsulates data needed to access and conveniently wrap a PPA

    This object proxies a PPA, allowing lazy initialization and caching
    of data from the remote.
    """
    # TODO: May need to load this from a (cached?) query
    ALL_ARCHITECTURES = [ 'amd64', 'arm64', 'armel', 'armhf', 'i386', 'powerpc', 'ppc64el', 's390x']
    def __init__(self, ppa_name, team_name, ppa_description=None, service=None):
        """Initializes a new Ppa object for a given PPA

        This creates only the local representation of the PPA, it does
        not cause a new PPA to be created in Launchpad.  For that, see
        PpaGroup.create()

        :param str ppa name: The name of the PPA within the team's namespace.
        :param str team_name: The name of the team or user that owns the PPA.
        :param str ppa_description: Optional description text for the PPA.
        :param launchpadlib.service service: The Launchpad service object.
        """
        assert ppa_name
        assert team_name

        self.ppa_name = ppa_name
        self.team_name = team_name
        if ppa_description is None:
            self.ppa_description = ''
        else:
            self.ppa_description = ppa_description
        self._service = service

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'ppa_name={self.ppa_name!r}, team_name={self.team_name!r})')

    def __str__(self):
        s = ''
        s += "ppa:        {}\n".format(self.name)
        s += "address:    {}\n".format(self.address)
        s += "url:        {}\n".format(self.url)
        s += "description:\n"
        s += indent(self.description, 4)
        return s

    @property
    def archive(self):
        owner = self._service.people[self.team_name]
        return owner.getPPAByName(name=self.ppa_name)

    @property
    @lru_cache
    def address(self):
        """The proper identifier of the PPA

        :rtype: str
        :returns: The full identification string for the PPA.
        """
        return "ppa:{}/{}".format(self.team_name, self.ppa_name)

    @property
    def name(self):
        """The name portion of the PPA's address.

        :rtype: str
        :returns: The name of the PPA.
        """
        return self.ppa_name

    @property
    def url(self):
        """The HTTP url for the PPA in Launchpad.

        :rtype: str
        :returns: The url of the PPA.
        """
        return "https://launchpad.net/~{}/+archive/ubuntu/{}".format(self.team_name, self.ppa_name)

    @property
    def description(self):
        """The description body for the PPA.

        :rtype: str
        :returns: The description body for the PPA.
        """
        return self.ppa_description

    def set_description(self, description):
        self.ppa_description = description
        a = self.archive
        a.description = description
        retval = a.lp_save()
        print("setting desc to '{}'".format(description))
        print("desc is now '{}'".format(self.archive.description))
        return self.archive.description == description

    @property
    def architectures(self):
        return [ proc.name for proc in self.archive.processors ]

    def set_architectures(self, architectures=ALL_ARCHITECTURES):
        assert self._service
        uri_base = "https://api.launchpad.net/devel/+processors/{}"
        procs = [ uri_base.format(arch) for arch in architectures ]
        try:
            self.archive.setProcessors(processors=procs)
        except KeyboardInterrupt:
            raise
        except:
            raise
            return 1

    def get_binaries(self, distro=None, series=None, arch=None):
        """Retrieve the binary packages available in the PPA.

        :param tbd distro: The required distribution object.
        :param str series: The distro's codename for the series.
        :param str arch: The hardware architecture.
        :rtype: list
        :returns: List of binaries
        """
        try:
            if distro == None and series == None and arch == None:
                return self.archive.getPublishedBinaries()
            elif series:
                das = get_das(distro, series, arch)
                ds = distro.getSeries(name_or_version=series)
            print("Unimplemented")
            return []
        except KeyboardInterrupt:
            raise

    def get_source_publications(self, distro=None, series=None, arch=None):
        """Retrieve the source packages in the PPA.

        :param tbd distro: The distribution object
        :param str series: The distro's codename for the series.
        :param str arch: The hardware architecture.

        :rtype: iterator
        :returns: Collection of source publications
        """
        try:
            if distro and series and arch:
                das = get_das(distro, series, arch)
                ds = distro.getSeries(name_or_version=series)
                print("Unimplemented")
                return []
            else:
                for source_publication in self.archive.getPublishedSources():
                    if source_publication.status not in ('Superseded', 'Deleted', 'Obsolete'):
                        yield source_publication
        except KeyboardInterrupt:
            raise
        except:
            return None

    def destroy(self):
        assert self._service
        try:
            return self.archive.lp_delete()
        except NotFound as e:
            # Will report 'No such ppa' if the ppa is deleted and gone
            msg = e.content.decode('utf-8')
            print(msg)
        except BadRequest as e:
            # Will report 'Archive already deleted.' if deleted but not yet gone
            print(e.content.decode('utf-8'))

    def has_packages(self):
        """Checks if the PPA has any source packages.

        Returns False if the PPA is empty, True otherwise.
        """
        return list(self.archive.getPublishedSources()) != []

    def has_pending_publications(self):
        pending_publication_sources = {}
        required_builds = {}
        pending_publication_builds = {}
        published_builds = {}

        for source_publication in self.get_source_publications():
            if not source_publication.date_published:
                pending_publication_sources[source_publication.self_link] = source_publication

            # iterate over the getBuilds result with no status restriction to get build records
            for build in source_publication.getBuilds():
                required_builds[build.self_link] = build

        for binary_publication in self.get_binaries():
            # Ignore failed builds
            build = binary_publication.build
            if build.buildstate != "Successfully built":
                continue

            # Skip binaries for obsolete sources
            source_publication = build.current_source_publication
            if source_publication is None:
                continue
            elif (source_publication.status in ('Superseded', 'Deleted', 'Obsolete')):
                continue

            if binary_publication.status == "Pending":
                pending_publication_builds[binary_publication.build_link] = binary_publication
            elif binary_publication.status == "Published":
                published_builds[binary_publication.build_link] = binary_publication

        retval = False
        num_builds_waiting = len(required_builds) - len(pending_publication_builds) - len(published_builds)
        if num_builds_waiting != 0:
            num_build_failures = 0
            builds_waiting_output = ''
            builds_failed_output = ''
            for build in required_builds.values():
                if build.buildstate == "Successfully built":
                    continue
                elif build.buildstate == "Failed to build":
                    num_build_failures += 1
                    builds_failed_output += "  - {} ({}) {}: {}\n".format(
                        build.source_package_name,
                        build.source_package_version,
                        build.arch_tag,
                        build.buildstate)
                else:
                    builds_waiting_output += "  - {} ({}) {}: {}\n".format(
                        build.source_package_name,
                        build.source_package_version,
                        build.arch_tag,
                        build.buildstate)
            if num_builds_waiting <= num_build_failures:
                print("* Some builds have failed:")
                print(builds_failed_output)
            elif builds_waiting_output != '':
                print("* Still waiting on these builds:")
                print(builds_waiting_output)
            retval = True

        if len(pending_publication_builds) != 0:
            print("* Still waiting on {} build publications:".format(len(pending_publication_builds)))
            for pub in pending_publication_builds.values():
                print("  - {}".format(pub.display_name))
            retval = True
        if len(pending_publication_sources) != 0:
            print("* Still waiting on {} source publications:".format(len(pending_publication_sources)))
            for pub in pending_publication_sources.values():
                print("  - {}".format(pub.display_name))
            retval = True
        if ((list(required_builds.keys()).sort() != list(published_builds.keys()).sort())):
            print("* Missing some builds")
            retval = True

        if not retval:
            print("Successfully published all builds for all architectures")
        return retval
