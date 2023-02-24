import sys
from .install_cli import getCliLocation, Popen


def main():
    cmd = sys.argv[1:]
    sys.argv = sys.argv[:1]
    cmd.insert(0, getCliLocation())
    proc = Popen(cmd, stdout=sys.stdout, stderr=sys.stderr, stdin=sys.stdin)
    sys.exit(proc.wait())
