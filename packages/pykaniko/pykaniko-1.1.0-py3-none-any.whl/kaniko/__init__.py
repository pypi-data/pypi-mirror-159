from kaniko.kaniko import KanikoSnapshotMode, KanikoVerbosity, KanikoBuildException, Kaniko

__ALL__ = [
    # Enums
    KanikoSnapshotMode, KanikoVerbosity,

    # Exceptions
    KanikoBuildException,

    # Kaniko
    Kaniko,
]

VERSION = (1, 1, 0)

__title__ = 'pykaniko'
__author__ = 'Deys Timofey'
__email__ = 'nxexox@gmail.com'
__copyright__ = 'Copyright (c) 2012 Deys Timofey'
__license__ = 'Apache License 2.0'
__url__ = 'https://github.com/nxexox/pykaniko'
__version__ = '.'.join(map(str, VERSION))
