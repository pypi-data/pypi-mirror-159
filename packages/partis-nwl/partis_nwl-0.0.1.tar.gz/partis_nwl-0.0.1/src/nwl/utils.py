import os
import os.path as osp
import re
import shlex
from glob import glob
import hashlib
import pathlib
import platform

from partis.utils import (
  join_attr_path )

from partis.schema import (
  is_sequence,
  is_mapping,
  SchemaDetectionError )

from .inputs import (
  PathInputValue )

from .outputs import (
  PathOutputValue )

from partis.schema.serialize import (
  yaml,
  json )

env_var_rec = re.compile(r'\${?(\w+)}?')

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
def expand_environ( var ):
  e_var = osp.expandvars(var)

  while e_var != var:
    var = e_var
    e_var = osp.expandvars(var)

  return shlex.split( e_var )

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
def get_mpiexec( mpiexec_str = None ):
  mpiexec = None

  if mpiexec_str is None and 'NWL_MPIEXEC' in os.environ:
    mpiexec_str = os.environ['NWL_MPIEXEC']


  if mpiexec_str is not None:
    mpiexec = expand_environ( mpiexec_str )

  return mpiexec

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
def get_processes( processes = None ):

  if processes is None and 'NWL_PROCS' in os.environ:
    processes = int(os.environ['NWL_PROCS'])

  return processes

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
def get_cpus_per_process( cpus_per_process = None ):

  if cpus_per_process is None and 'NWL_CPUS_PER_PROC' in os.environ:
    cpus_per_process = int(os.environ['NWL_CPUS_PER_PROC'])

  return cpus_per_process

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
def get_threads_per_cpu( threads_per_cpu = None ):

  if threads_per_cpu is None and 'NWL_THREADS_PER_CPU' in os.environ:
    threads_per_cpu = int(os.environ['NWL_THREADS_PER_CPU'])

  return threads_per_cpu

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
def get_gpus_per_process( gpus_per_process = None ):

  if gpus_per_process is None and 'NWL_GPUS_PER_PROC' in os.environ:
    gpus_per_process = int(os.environ['NWL_GPUS_PER_PROC'])

  return gpus_per_process

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
def get_runhost( val = None ):

  if val is None:
    val = platform.node()

  return val

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
def get_jobhost( val = None ):

  if val is None:

    for var in [
      'NWL_JOBHOST',
      'PBS_O_HOST',
      'SLURM_SUBMIT_HOST']:

      if var in os.environ:
        val = os.environ[var]

  if val is None:
    val = get_runhost()

  return val

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
def get_runuser( val = None ):

  if val is None:
    val = os.getlogin()

  return val

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
def get_jobuser( val = None ):

  if val is None:

    for var in [
      'NWL_JOBUSER',
      'PBS_O_LOGNAME',
      'SLURM_JOB_USER' ]:

      if var in os.environ:
        val = os.environ[var]

  if val is None:
    val = get_runuser()

  return val

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
def get_jobid( val = None ):
  if val is None:
    for var in [
      'NWL_JOBID',
      'PBS_JOBID',
      'SLURM_JOBID',
      'SLURM_JOB_ID' ]:

      if var in os.environ:
        val = os.environ[var]

  return val

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
def get_jobname( val = None ):
  if val is None:
    for var in [
      'NWL_JOBNAME',
      'PBS_JOBNAME',
      'SLURM_JOB_NAME']:

      if var in os.environ:
        val = os.environ[var]

  return val

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
def check_inout_files( dir, path, val ):

  missing = list()

  if isinstance( val, (PathInputValue, PathOutputValue) ):
    if len(val.path) > 0 and not osp.exists( val.path ):
      missing.append(
        f"{join_attr_path(path)}: {shlex.quote(osp.realpath(val.path))}" )

  elif is_sequence( val ):
    for i, v in enumerate(val):
      missing.extend( check_inout_files(
        dir = dir,
        path = path + [i],
        val = v ) )

  elif is_mapping( val ):
    for k, v in val.items():
      missing.extend( check_inout_files(
        dir = dir,
        path = path + [k],
        val = v ) )

  return missing

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
def load_results( rundir = None ):
  results_file = "nwl.tool.results.yml"

  if rundir:
    results_file = osp.join( rundir, results_file )

  # ensure plugs reloaded with access to additional search paths
  from partis.schema.plugin import (
    schema_plugins )

  schema_plugins.load_plugins()

  results = yaml.load(
    results_file,
    loc = results_file,
    detect_schema = True )

  return results
