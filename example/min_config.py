import os
import sys
import platform

# By default, this file should be located at <base_dir>/config/config.py
# builders_tools is presumed to be a sibling directory

# This is the repository base directory; found relative to this file
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

OS = sys.platform
ARCH = platform.machine()
default_cpu_count = os.cpu_count()
default_initrd_fs = False

conda_home = os.path.join(os.path.expanduser('~'), '.miniconda3')
conda_environ_name = 'example'
qemu_user_prefix = '/opt/qemu-user-static'
docker_multiarch = False
kraft_update_freq_days = 7
supported_platforms = ['linux/amd64', 'linux/arm64']

packages = {'example': os.path.join(base_dir, 'src', 'example')}
sources = {'example': [(os.path.join(base_dir, 'src', 'example'),),]}
images = {k: v.split('/')[-1] for k, v in packages.items()}
wheels = ['example']
image_name = 'example'
network_name = 'example-net'

qemu_system = None
if OS == 'Linux':
    for path in ['/usr/bin/qemu-system-' + ARCH, '/usr/libexec/qemu-kvm']:
        if os.path.exists(path):
            qemu_system = path
            break

