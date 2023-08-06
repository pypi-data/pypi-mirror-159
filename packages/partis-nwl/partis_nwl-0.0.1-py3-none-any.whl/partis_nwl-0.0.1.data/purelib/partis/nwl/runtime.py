
import os
import re
import subprocess
import shutil
import shlex
from timeit import default_timer as timer

import logging
log = logging.getLogger(__name__)

from partis.utils import (
  odict,
  adict,
  ModelHint,
  ModelError,
  LogListHandler )

from partis.schema import (
  required,
  optional,
  derived,
  is_sequence,
  is_mapping,
  is_evaluated,
  is_valued,
  is_valued_type,
  is_optional,
  PJCEvaluated,
  BoolPrim,
  IntPrim,
  FloatPrim,
  StrPrim,
  SeqPrim,
  MapPrim,
  UnionPrim,
  PassPrim,
  StructValued,
  MapValued,
  SchemaError,
  SeqValued,
  schema_declared,
  SchemaModule )

from partis.schema.hint import (
  Hint,
  HintList )

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class ToolRuntime( StructValued ):
  schema = dict(
    tag = 'runtime',
    doc = "Tool runtime information",
    default_val = derived )

  success = BoolPrim(
    doc = "Flag for whether the tool ran and closed successfully",
    default_val = False )

  workdir = StrPrim(
    doc = "Directory from which the tool resolves relative input file paths.",
    default_val = "",
    max_lines = 1 )

  rundir = StrPrim(
    doc = "Directory where tool was told to run, and resolves output file paths",
    default_val = "",
    max_lines = 1 )

  host = StrPrim(
    doc = """The local `hostname` or fully qualified domain name
    of the machine where the tool was run.

    .. note::

      If the tool was run with more than one allocated node, this will
      be the hostname of only the node on which the run script was executed.""",
    default_val = "",
    max_lines = 1 )

  pid = IntPrim(
    doc = "The process id of the primary process running the tool on the `runhost`",
    default_val = 0 )

  cmd_index = IntPrim(
    doc = "Index of last attempted command",
    default_val = -1 )

  cmd_id = StrPrim(
    doc = "ID (key) of last attempted command",
    default_val = optional,
    max_lines = 1 )

  processes = IntPrim(
    doc = """Number of processes allocated

      The total CPU cores allocated is `( processes * cpus_per_process )`.
      The value may be taken from the environment variable `NWL_PROCS`.""",
    min = 1,
    default_val = 1 )

  cpus_per_process = IntPrim(
    doc = """Number of cores allocated per process.

      The value may be taken from the environment variable `NWL_CPUS_PER_PROC`.""",
    min = 1,
    default_val = 1 )

  threads_per_cpu = IntPrim(
    doc = """Number of logical threads per CPU core.

    The ideal total number of threads is
    `( threads_per_cpu * cpus_per_process )`.
    The value may be taken from the environment variable `NWL_THREADS_PER_CPU`.""",
    min = 1,
    default_val = 1 )

  gpus_per_process = IntPrim(
    doc = """Number of GPUs allocated per process.

      The value may be taken from the environment variable `NWL_GPUS_PER_PROC`.""",
    min = 0,
    default_val = 0 )

  timeout = IntPrim(
    doc = """Time allocated (seconds)""",
    min = 1,
    default_val = optional )

  mpiexec = SeqPrim(
    doc = """List of arguments to execute a program within MPI, if available.

      This will be set, and the `{np}` variable in the original format strings
      will be replaced with the current value of `processes`, only if
      `processes > 1`.
      The arguments may be taken from the environment variable `NWL_MPIEXEC`,
      for example:

      .. code-block:: bash

        export NWL_MPIEXEC='mpirun -np {np:d}'""",
    item = StrPrim(
      max_lines = 1 ),
    default_val = list() )

  aux = MapPrim(
    doc = """Auxiliary variables that may be used for input query substitution.

      .. note::

        These values should only be used to perform value
        substituion for queries present in an `inputs` file, when those values
        may need to be passed on the command line instead of the inputs file.

        For example:

        .. code-block:: yaml
          :caption:
            inputs_file.yml

          some_input: $nwl:tool?var=runtime.aux.some_aux_val&type=int

        Then values can be specified to be substituted on the command line:

        .. code-block:: bash

          partis-nwl --tool my_tool --inputs inputs_file.yml --aux some_aux_val=42

        The values here are not (and should not) be referenced directly by expressions
        in a tool definition, instead using the result after substitution to input
        values.

      """,
    item = StrPrim(),
    default_val = dict() )

  env = MapPrim(
    doc = """Environment variables set for tool run

      .. note::

        All environment variable names are first sanitized to contain only
        alpha|digit|underscore, with runs of other characters replaced by a
        single underscore '_'.""",
    item = StrPrim(),
    default_val = dict() )

  logs = HintList
