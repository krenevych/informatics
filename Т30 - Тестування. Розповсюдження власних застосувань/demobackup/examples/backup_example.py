#backup example

import sys
import os

source_dir = os.pardir + os.sep + "demobackup"
if source_dir not in sys.path:
    sys.path.append(source_dir)

import backup

directory = os.path.abspath(os.pardir)

directories = [directory]
backupdir = os.sep + "backup"


backup.backupdirectories(directories, backupdir)
