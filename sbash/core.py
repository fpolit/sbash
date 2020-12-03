#!/usr/bin/env python3
#
# Bash class to run bash commands
#
#
# Mantainer: glozanoa <glozanoa@uni.pe>


from cement.utils.shell import exec_cmd, exec_cmd2
from fineprint.status import print_failure, print_status, print_successful
import shlex
import os


class BashError(Exception):
    def __init__(self):
        self.msg = "Failed to execute command."
        super().__init__(self.msg)


class CmdTypeError(Exception):
    def __init__(self):
        self.msg = "Invalid type of cmd"
        super().__init__(self.msg)


class Bash:

    @staticmethod
    def exec(cmd, *, where=None, quiet=False):
        """
        Executa a bash command cmd in where quietly if quiet=True
        otherwise print to console (quiet=False)
        """
        try:
            if isinstance(cmd, str):
                cmd = shlex.split(cmd)
            elif not  (isinstance(cmd, list) or isinstance(cmd, tuple)):
                raise CmdTypeError

            if quiet:
                exec_cmd2trash(cmd, where=where)
            else:
                exec_cmd2shell(cmd, where=where)

        except CmdTypeError as error:
            print_failure(error)

        except BashError as error:
            print_failure(error)



# Tested - 20 Nov 2020 (Note: no support composite data [list of list or ...] )
def exec_cmd2shell(cmd, *, where=None):
    """
    Run bash commands and show execution in the terminal
    """
    try:
        init = os.getcwd()
        if where and os.path.isdir(where):
            os.chdir(where)
            exec_cmd2(cmd)
            os.chdir(init)
        elif not where:
            exec_cmd2(cmd) # where is pwd, so simply run the cmd
        else: # where isn't  a directory
            raise NotADirectoryError

    except NotADirectoryError as error:
        print_failure(error)


def exec_cmd2trash(cmd, *, where=None):
    """
    Run bash commands quietly
    """
    try:
        init = os.getcwd()

        if where and os.path.isdir(where):
            os.chdir(where)
            exitcode = exec_cmd2(cmd)
            os.chdir(init)
        elif not where:
            exitcode = exec_cmd(cmd) # where is pwd, so simply run the cmd
        else: # where isn't  a directory
            exitcode=0 # execution exit with error
            raise NotADirectoryError
        
        if not exitcode: # some error has occurred
            raise BashError

    except NotADirectoryError as error:
        print_failure(error)