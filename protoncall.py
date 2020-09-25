#!/usr/bin/env python3
import os
# import os.path
import sys

n = 'null'
scdp = 'STEAM_COMPAT_DATA_PATH'
custom = False
version = '0.5.1a'

# Set defaults
err_val = 255
proton = n
program = n
_help = True
_home = os.environ['HOME']
proton_path = f"{_home}/.steam/steam/steamapps/common/Proton\\ "


def help_message():
    print(f"Proton Caller by Avery Murray, version: {version}.\n"
          f"Use this to easily run any Windows executable using Steam's Proton\n\n"
          f"Usage:\n [-c, -h][5, 5.0, 4.11, 4.3, 3.16, 3.7][./*.exe]\n"
          f"'proton-call 5 ./foo.exe'\n'proton-call -c '/Proton\\ 5.0/' ./foo.exe'\n\n"
          f"Working directory must be the same as the Windows executable. Proton Caller will fail without arguments.")
    sys.exit(_vars.err_val)


def proton_addition():
    add_dir = input('Directory you will like {scdp} added.'
                    'this will add a directory.\nadd_dir: ')
    os.system(f'mkdir {add_dir}/proton')
    _profile = input('Shell profile file: ')
    os.system(f"echo 'export STEAM_COMPAT_DATA_PATH={add_dir}/proton' > {_profile}")
    _vars.scdp = f'{add_dir}/proton'
    return _vars.scdp


def locate():
    if _vars.custom:
        if os.path.isdir(f"'{_vars.proton_path}'"):
            return
        if not os.path.isdir(f"'_vars.proton_path'"):
            print(f'Error: {_vars.proton_path} not found.')
            sys.exit(_vars.err_val)


def setup():
    #  locate()
    print(f'Custom mode: {_vars.custom}')
    if scdp in os.environ:
        print(f'{scdp} exists at {os.environ[_vars.scdp]}\b')
        return
    # else:
    #    print(f'{scdp} was not found')
    #    add_var = input(f'Would you like to add {scdp}? [y/n]: ')
    #    if add_var == 'y':
    #        _vars.scdp = proton_addition()
    #        return _vars.scdp
    #    elif add_var == 'n':
    #        sys.exit(f"Won't add {_vars.scdp}. Add it to your environment.")
    #    else:
    sys.exit(_vars.err_val)


def proton_call():
    if _vars._help:
        help_message()
    setup()
    if custom:
        #  print(f'Using Proton {_vars.proton}')
        #  print(f'Program: {_vars.program}')
        os.system(f"{_vars.proton_path}/proton run {_vars.program}")
    elif not custom:
        os.system(f'~/.steam/steam/steamapps/common/Proton\\ {_vars.proton}/proton run {program}')
    else:
        print(f"How did we get here, {os.environ['USER']}?")
        sys.exit(_vars.err_val)


class ProtonCaller:
    def __init__(self, _argv1, custom, err_val, version, scdp, proton, program, proton_path, _help):
        self._argv1 = _argv1
        self.custom = custom
        self.err_val = err_val
        self.version = version
        self.scdp = scdp
        self.proton = proton
        self. program = program
        self.proton_path = proton_path
        self._help = _help


def define():
    _vars = pc(sys.argv[1], custom, err_val, version, scdp, proton, program, proton_path, _help)
    return _vars


# check mode

pc = ProtonCaller
if len(sys.argv[1]) > 4:
    help_message()
    sys.exit(0)
elif sys.argv[1] == 'help':
    err_val = 0
    _vars = define()
    help_message()
    sys.exit(0)
elif sys.argv[1] == '-h':
    err_val = 0
    _vars = define()
    help_message()
    sys.exit(0)
elif sys.argv[1] == '-c':
    _help = False
    custom = True
    proton_path = sys.argv[2]
    program = sys.argv[3]
    _vars = define()
    proton_call()
    sys.exit(0)
else:
    _help = False
    proton = sys.argv[1]
    if sys.argv[1] == '5':
        proton = '5.0'
    program = sys.argv[2]
    _vars = define()
    proton_call()
    sys.exit(0)
