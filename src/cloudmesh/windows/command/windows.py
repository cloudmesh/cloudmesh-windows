from cloudmesh.windows.windows import Windows
from cloudmesh.common.console import Console
from cloudmesh.common.debug import VERBOSE
from cloudmesh.common.parameter import Parameter
from cloudmesh.common.util import banner
from cloudmesh.common.util import path_expand
from cloudmesh.common.variables import Variables
from cloudmesh.shell.command import PluginCommand
from cloudmesh.shell.command import command
from cloudmesh.shell.command import map_parameters
from cloudmesh.windows.windows import Windows


class WindowsCommand(PluginCommand):
    # noinspection PyUnusedLocal
    @command
    def do_windows(self, args, arguments):
        """
        ::

          Usage:
                windows deploy
                windows download [--version=VERSION]
                windows install

          This command does some useful things.

          Arguments:
              FILE   a file name
              PARAMETER  a parameterized parameter of the form "a[0-3],a5"

          Options:
              --version=VERSION  the version. only supported version is 11 [default: 11]

          Description:

            > cms windows deploy
            >   deploys a windows vm on ubuntu 22.04. No other os is supported.

        """


        map_parameters(arguments, "version")

        VERBOSE(arguments)

        m = Windows()
        if arguments.download:

            banner(f"Download Windoes {arguments.version}")

            m.download()

        elif arguments.deploy:

            banner(f"Deploy Windoes {arguments.version}")
            m.deploy()

        return ""
