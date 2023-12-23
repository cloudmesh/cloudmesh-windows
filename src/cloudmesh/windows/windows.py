import os
from cloudmesh.common.Shell import Shell
import fnmatch
from cloudmesh.common.util import path_expand
import glob

from textwrap import dedent
class Windows:

    def __init__(self):
        print("init {name}".format(name=self.__class__.__name__))

    def deploy(self):
        print("deploy")

    def download(self):
        # print("download")
        Shell.browser("https://www.microsoft.com/software-download/windows11")

    def deploy(self):

        if Shell.which("distrobuilder") is None:
            print("Install distrobuilder")
            command = "sudo snap install distrobuilder --classic"
            print (command)
            # os.system(command)

        for package in ["libwin-hivex-perl", "wimtools"]:
            if "[Installed]" not in Shell.run(f"apt -qq {package}"):
                print(f"Install {package}")
                command = f"sudo apt-get install {package}"
                print (command)
                # os.system(command)
        
        path = path_expand('~/Downloads')
    
        iso_files = glob.glob(f'{path}/Win11_*.iso')
        if iso_files:
            print(iso_files)
            iso_file = iso_files[0]
            command = f"sudo distrobuilder repack-windows {iso_file} win11.lxd.iso"
            print (command) 
            # os.system(command)                                      
        


    def prepare(self, size):
        print("prepare")
        commands = dedent(f"""    
            lxc init win10 --empty --vm -c security.secureboot=false
            lxc config device override win11 root size={size}GiB
            lxc config device add win10 iso disk source=win11.lxd.iso boot.priority=10
            """).strip().split("\n")
        for command in commands:
            print (command)
            # os.system(command)    
