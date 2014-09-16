import os
import multiprocessing

#NUM_CPUS = multiprocessing.cpu_count() - 1
NUM_CPUS = 1

CLUSTER_DIR = os.path.dirname(os.path.abspath(__file__))

CPU_FREE_TOL = 0.1
RAM_FREE_TOL = 0.1

SSH_CMD = 'ssh -q -x -o ConnectTimeout=10 -o ServerAliveInterval=3'
PYTHON_CMD = '/afs/cs.stanford.edu/u/zxie/virtualenvs/scl/bin/python'

CLUSTER_NODES = {
    'gorgon': range(1, 30),
    'deep': range(1, 25)
}