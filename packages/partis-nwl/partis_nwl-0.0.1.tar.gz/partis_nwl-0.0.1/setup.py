"""Usage of `setup.py` is deprecated, and is supplied only for legacy installation.
"""
import sys
import os
import os.path as osp
import importlib
import logging
import argparse
import subprocess
import tempfile
from argparse import RawTextHelpFormatter
logger = logging.getLogger(__name__)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def egg_info( args ):

  logger.warning(
    "running legacy 'setup.py egg_info'" )

  dir = osp.join( args.egg_base, EGG_INFO_NAME )

  if not osp.exists( dir ):
    os.mkdir( dir )

  with open( osp.join( dir, 'PKG-INFO' ), 'wb' ) as fp:
    fp.write( PKG_INFO )

  with open( osp.join( dir, 'setup_requires.txt' ), 'wb' ) as fp:
    fp.write( b'' )

  with open( osp.join( dir, 'requires.txt' ), 'wb' ) as fp:
    fp.write( REQUIRES )

  with open( osp.join( dir, 'SOURCES.txt' ), 'wb' ) as fp:
    fp.write( SOURCES )

  with open( osp.join( dir, 'top_level.txt' ), 'wb' ) as fp:
    fp.write( TOP_LEVEL )

  with open( osp.join( dir, 'entry_points.txt' ), 'wb' ) as fp:
    fp.write( ENTRY_POINTS )

  with open( osp.join( dir, 'dependency_links.txt' ), 'wb' ) as fp:
    fp.write( b'' )

  with open( osp.join( dir, 'not-zip-safe' ), 'wb' ) as fp:
    fp.write( b'' )

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def bdist_wheel( args ):

  logger.warning(
    "running legacy 'setup.py bdist_wheel'" )

  sys.path = backend_path + sys.path

  backend = importlib.import_module( build_backend )

  backend.build_wheel(
    wheel_directory = args.dist_dir or args.bdist_dir or '.' )

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def install( args ):

  logger.warning(
    "running legacy 'setup.py install'" )

  reqs = [ f"{r}" for r in build_requires ]

  subprocess.check_call([
    sys.executable,
    '-m',
    'pip',
    'install',
    *reqs ] )

  sys.path = backend_path + sys.path

  backend = importlib.import_module( build_backend )

  with tempfile.TemporaryDirectory() as tmpdir:
    wheel_name = backend.build_wheel(
      wheel_directory = tmpdir )

    subprocess.check_call([
      sys.executable,
      '-m',
      'pip',
      'install',
      osp.join(tmpdir, wheel_name) ])

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def dummy( args ):
  pass

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def main():

  logging.basicConfig(
    level = logging.INFO,
    format = "{name}:{levelname}: {message}",
    style = "{" )


  logger.warning(
    "'setup.py' is deprecated, limited support for legacy installs. Upgrade pip." )

  parser = argparse.ArgumentParser(
    description = __doc__,
    formatter_class = RawTextHelpFormatter )

  subparsers = parser.add_subparsers()

  #.............................................................................
  egg_info_parser = subparsers.add_parser( 'egg_info' )

  egg_info_parser.set_defaults( func = egg_info )

  egg_info_parser.add_argument( "-e", "--egg-base",
    type = str,
    default = '.' )

  #.............................................................................
  bdist_wheel_parser = subparsers.add_parser( 'bdist_wheel' )

  bdist_wheel_parser.set_defaults( func = bdist_wheel )

  bdist_wheel_parser.add_argument( "-b", "--bdist-dir",
    type = str,
    default = '' )

  bdist_wheel_parser.add_argument( "-d", "--dist-dir",
    type = str,
    default = '' )

  bdist_wheel_parser.add_argument( "--python-tag",
    type = str,
    default = None )

  bdist_wheel_parser.add_argument( "--plat-name",
    type = str,
    default = None )

  bdist_wheel_parser.add_argument( "--py-limited-api",
    type = str,
    default = None )

  bdist_wheel_parser.add_argument( "--build-number",
    type = str,
    default = None )

  #.............................................................................
  install_parser = subparsers.add_parser( 'install' )

  install_parser.set_defaults( func = install )

  install_parser.add_argument( "--record",
    type = str,
    default = None )

  install_parser.add_argument( "--install-headers",
    type = str,
    default = None )

  install_parser.add_argument( "--compile",
    action='store_true' )

  install_parser.add_argument( "--single-version-externally-managed",
    action='store_true' )

  #.............................................................................
  clean_parser = subparsers.add_parser( 'clean' )

  clean_parser.set_defaults( func = dummy )

  clean_parser.add_argument( "-a", "--all",
    action='store_true' )

  args = parser.parse_args( )

  args.func( args )


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# NOTE: these are templated literal values substituded by the backend when
# building the source distribution

build_backend = 'partis.pyproj.backend'
backend_path = []
build_requires = ['wheel', 'partis-pyproj==0.0.1']

EGG_INFO_NAME = 'partis-nwl.egg-info'

PKG_INFO = b'Metadata-Version: 2.1\nName: partis-nwl\nVersion: 0.0.1\nRequires-Python: >=3.6.2\nMaintainer-email: "Nanohmics Inc." <software.support@nanohmics.com>\nSummary: Implementation of Nano Workflow Language (NWL)\nLicense-File: LICENSE.txt\nClassifier: Intended Audience :: Science/Research\nClassifier: License :: OSI Approved :: BSD License\nClassifier: Topic :: System :: Clustering\nClassifier: Programming Language :: Python :: 3\nClassifier: Topic :: Scientific/Engineering\nClassifier: Development Status :: 4 - Beta\nClassifier: Operating System :: POSIX :: Linux\nClassifier: Programming Language :: Python\nRequires-Dist: tomli>=1.2.3\nRequires-Dist: build>=0.7.0\nRequires-Dist: ruamel.yaml==0.16.5\nRequires-Dist: partis-utils[asy]==0.0.1\nRequires-Dist: wheel\nRequires-Dist: partis-schema==0.0.1\nRequires-Dist: partis-pyproj==0.0.1\nDescription-Content-Type: text/x-rst\n\nThe ``partis.nwl`` package is part of a workflow development toolkit.'

REQUIRES = b'tomli>=1.2.3\nbuild>=0.7.0\nruamel.yaml==0.16.5\npartis-utils[asy]==0.0.1\nwheel\npartis-schema==0.0.1\npartis-pyproj==0.0.1'

SOURCES = b'partis_nwl-0.0.1/src/nwl/__init__.py\npartis_nwl-0.0.1/src/nwl/results.py\npartis_nwl-0.0.1/src/nwl/job.py\npartis_nwl-0.0.1/src/nwl/tool_pkg/__init__.py\npartis_nwl-0.0.1/src/nwl/tool_pkg/tool_pkg.py\npartis_nwl-0.0.1/src/nwl/tool_pkg/__main__.py\npartis_nwl-0.0.1/src/nwl/tool_pkg/build.py\npartis_nwl-0.0.1/src/nwl/tool_pkg/pkg_tmpl/doc/conf.py\npartis_nwl-0.0.1/src/nwl/tool_pkg/pkg_tmpl/doc/__init__.py\npartis_nwl-0.0.1/src/nwl/tool_pkg/pkg_tmpl/doc/_static/app_icon.svg\npartis_nwl-0.0.1/src/nwl/tool_pkg/pkg_tmpl/index.rst\npartis_nwl-0.0.1/src/nwl/tool_pkg/pkg_tmpl/partis_nwl_ext.py\npartis_nwl-0.0.1/src/nwl/tool_pkg/pkg_tmpl/pyproject.toml\npartis_nwl-0.0.1/src/nwl/tool_pkg/pkg_tmpl/tool/__init__.py\npartis_nwl-0.0.1/src/nwl/tool_pkg/pkg_tmpl/tool/results.py\npartis_nwl-0.0.1/src/nwl/tool_pkg/pkg_tmpl/tool/index.rst\npartis_nwl-0.0.1/src/nwl/tool_pkg/pkg_tmpl/tool/commands.py\npartis_nwl-0.0.1/src/nwl/tool_pkg/pkg_tmpl/tool/commands.rst\npartis_nwl-0.0.1/src/nwl/tool_pkg/pkg_tmpl/tool/__main__.py\npartis_nwl-0.0.1/src/nwl/tool_pkg/pkg_tmpl/tool/inputs.py\npartis_nwl-0.0.1/src/nwl/tool_pkg/pkg_tmpl/tool/results.rst\npartis_nwl-0.0.1/src/nwl/tool_pkg/pkg_tmpl/tool/outputs.rst\npartis_nwl-0.0.1/src/nwl/tool_pkg/pkg_tmpl/tool/outputs.py\npartis_nwl-0.0.1/src/nwl/tool_pkg/pkg_tmpl/tool/_load_tool.py\npartis_nwl-0.0.1/src/nwl/tool_pkg/pkg_tmpl/tool/source.rst\npartis_nwl-0.0.1/src/nwl/tool_pkg/pkg_tmpl/tool/inputs.rst\npartis_nwl-0.0.1/src/nwl/commands/__init__.py\npartis_nwl-0.0.1/src/nwl/commands/file.py\npartis_nwl-0.0.1/src/nwl/commands/base.py\npartis_nwl-0.0.1/src/nwl/commands/dir.py\npartis_nwl-0.0.1/src/nwl/commands/process.py\npartis_nwl-0.0.1/src/nwl/commands/script.py\npartis_nwl-0.0.1/src/nwl/__main__.py\npartis_nwl-0.0.1/src/nwl/inputs.py\npartis_nwl-0.0.1/src/nwl/query.py\npartis_nwl-0.0.1/src/nwl/context.py\npartis_nwl-0.0.1/src/nwl/runtime.py\npartis_nwl-0.0.1/src/nwl/base.py\npartis_nwl-0.0.1/src/nwl/log.py\npartis_nwl-0.0.1/src/nwl/content_type.py\npartis_nwl-0.0.1/src/nwl/info.py\npartis_nwl-0.0.1/src/nwl/view/__init__.py\npartis_nwl-0.0.1/src/nwl/view/tool_edit.py\npartis_nwl-0.0.1/src/nwl/view/plugin.py\npartis_nwl-0.0.1/src/nwl/view/tool_results_edit.py\npartis_nwl-0.0.1/src/nwl/view/testing.py\npartis_nwl-0.0.1/src/nwl/utils.py\npartis_nwl-0.0.1/src/nwl/outputs.py\npartis_nwl-0.0.1/src/nwl/resources.py\npartis_nwl-0.0.1/src/nwl/path.py\npartis_nwl-0.0.1/src/nwl/tool.py\npartis_nwl-0.0.1/src/nwl/testing.py\npartis_nwl-0.0.1/doc/conf.py\npartis_nwl-0.0.1/doc/__init__.py\npartis_nwl-0.0.1/doc/index.rst\npartis_nwl-0.0.1/doc/src/partis.nwl.commands.rst\npartis_nwl-0.0.1/doc/src/partis.nwl.path.rst\npartis_nwl-0.0.1/doc/src/partis.nwl.outputs.rst\npartis_nwl-0.0.1/doc/src/index.rst\npartis_nwl-0.0.1/doc/src/partis.nwl.__main__.rst\npartis_nwl-0.0.1/doc/src/partis.nwl.results.rst\npartis_nwl-0.0.1/doc/src/partis.nwl.context.rst\npartis_nwl-0.0.1/doc/src/partis.nwl.log.rst\npartis_nwl-0.0.1/doc/src/partis.nwl.resources.rst\npartis_nwl-0.0.1/doc/src/partis.nwl.info.rst\npartis_nwl-0.0.1/doc/src/partis.nwl.query.rst\npartis_nwl-0.0.1/doc/src/partis.nwl.runtime.rst\npartis_nwl-0.0.1/doc/src/partis.nwl.inputs.rst\npartis_nwl-0.0.1/doc/src/partis.nwl.tool.rst\npartis_nwl-0.0.1/doc/src/partis.nwl.base.rst\npartis_nwl-0.0.1/doc/src/partis.nwl.testing.rst\npartis_nwl-0.0.1/doc/editor.rst\npartis_nwl-0.0.1/doc/__main__.py\npartis_nwl-0.0.1/doc/walkthrough.rst\npartis_nwl-0.0.1/doc/img/motivation-overview.svg\npartis_nwl-0.0.1/doc/img/nwl_gui/edit_list.svg\npartis_nwl-0.0.1/doc/img/nwl_gui/rename_key.png\npartis_nwl-0.0.1/doc/img/nwl_gui/edit_expression4.png\npartis_nwl-0.0.1/doc/img/nwl_gui/add_input2.png\npartis_nwl-0.0.1/doc/img/nwl_gui/text_edit3.png\npartis_nwl-0.0.1/doc/img/nwl_gui/schema_tree_edit.png\npartis_nwl-0.0.1/doc/img/nwl_gui/edit_string.svg\npartis_nwl-0.0.1/doc/img/nwl_gui/edit_expression3.png\npartis_nwl-0.0.1/doc/img/nwl_gui/union.png\npartis_nwl-0.0.1/doc/img/nwl_gui/edit_union.png\npartis_nwl-0.0.1/doc/img/nwl_gui/add_selection2.png\npartis_nwl-0.0.1/doc/img/nwl_gui/edit_struct.svg\npartis_nwl-0.0.1/doc/img/nwl_gui/eval_output5.png\npartis_nwl-0.0.1/doc/img/nwl_gui/add_optional.png\npartis_nwl-0.0.1/doc/img/nwl_gui/log.yaml\npartis_nwl-0.0.1/doc/img/nwl_gui/add_selection3.png\npartis_nwl-0.0.1/doc/img/nwl_gui/new_file_nwl.png\npartis_nwl-0.0.1/doc/img/nwl_gui/add_command.png\npartis_nwl-0.0.1/doc/img/nwl_gui/add_case.png\npartis_nwl-0.0.1/doc/img/nwl_gui/log_event.png\npartis_nwl-0.0.1/doc/img/nwl_gui/edit_int.png\npartis_nwl-0.0.1/doc/img/nwl_gui/add_selection.png\npartis_nwl-0.0.1/doc/img/nwl_gui/edit_struct.png\npartis_nwl-0.0.1/doc/img/nwl_gui/edit_label.png\npartis_nwl-0.0.1/doc/img/nwl_gui/edit_bool.svg\npartis_nwl-0.0.1/doc/img/nwl_gui/add_arg2.png\npartis_nwl-0.0.1/doc/img/nwl_gui/eval_output6.png\npartis_nwl-0.0.1/doc/img/nwl_gui/eval_output4.png\npartis_nwl-0.0.1/doc/img/nwl_gui/rename_key2.png\npartis_nwl-0.0.1/doc/img/nwl_gui/edit_list.png\npartis_nwl-0.0.1/doc/img/nwl_gui/edit_float.svg\npartis_nwl-0.0.1/doc/img/nwl_gui/text_edit.png\npartis_nwl-0.0.1/doc/img/nwl_gui/epilog_event.png\npartis_nwl-0.0.1/doc/img/nwl_gui/add_arg.png\npartis_nwl-0.0.1/doc/img/nwl_gui/add_case3.png\npartis_nwl-0.0.1/doc/img/nwl_gui/add_input3.png\npartis_nwl-0.0.1/doc/img/nwl_gui/schema_tree_edit.yaml\npartis_nwl-0.0.1/doc/img/nwl_gui/edit_bool.png\npartis_nwl-0.0.1/doc/img/nwl_gui/eval_output.png\npartis_nwl-0.0.1/doc/img/nwl_gui/move_input.png\npartis_nwl-0.0.1/doc/img/nwl_gui/edit_union.svg\npartis_nwl-0.0.1/doc/img/nwl_gui/edit_expression5.png\npartis_nwl-0.0.1/doc/img/nwl_gui/edit_bool2.png\npartis_nwl-0.0.1/doc/img/nwl_gui/change_cmd.png\npartis_nwl-0.0.1/doc/img/nwl_gui/edit_multiline.png\npartis_nwl-0.0.1/doc/img/nwl_gui/new_file.png\npartis_nwl-0.0.1/doc/img/nwl_gui/edit_label2.png\npartis_nwl-0.0.1/doc/img/nwl_gui/eval_output2.png\npartis_nwl-0.0.1/doc/img/nwl_gui/schema_tree_edit.svg.png\npartis_nwl-0.0.1/doc/img/nwl_gui/edit_expression2.png\npartis_nwl-0.0.1/doc/img/nwl_gui/add_input.png\npartis_nwl-0.0.1/doc/img/nwl_gui/add_arg3.png\npartis_nwl-0.0.1/doc/img/nwl_gui/move_input2.png\npartis_nwl-0.0.1/doc/img/nwl_gui/edit_int.svg\npartis_nwl-0.0.1/doc/img/nwl_gui/edit_selection.png\npartis_nwl-0.0.1/doc/img/nwl_gui/save.png\npartis_nwl-0.0.1/doc/img/nwl_gui/add_case2.png\npartis_nwl-0.0.1/doc/img/nwl_gui/edit_expression.png\npartis_nwl-0.0.1/doc/img/nwl_gui/add_output.png\npartis_nwl-0.0.1/doc/img/nwl_gui/select_type.png\npartis_nwl-0.0.1/doc/img/nwl_gui/schema_tree_edit.svg\npartis_nwl-0.0.1/doc/img/nwl_gui/remove_optional.png\npartis_nwl-0.0.1/doc/img/nwl_gui/text_edit2.png\npartis_nwl-0.0.1/doc/img/nwl_gui/cheetah.png\npartis_nwl-0.0.1/doc/img/nwl_gui/add_output2.png\npartis_nwl-0.0.1/doc/img/nwl_gui/edit_string.png\npartis_nwl-0.0.1/doc/img/nwl_gui/eval_output3.png\npartis_nwl-0.0.1/doc/img/nwl_gui/schema_tree_node_ctx.png\npartis_nwl-0.0.1/doc/img/nwl_gui/edit_multiline2.png\npartis_nwl-0.0.1/doc/img/nwl_gui/add_case4.png\npartis_nwl-0.0.1/doc/img/nwl_gui/edit_float.png\npartis_nwl-0.0.1/doc/img/nwl_gui/save2.png\npartis_nwl-0.0.1/doc/overview.rst\npartis_nwl-0.0.1/test/400_nwl/__init__.py\npartis_nwl-0.0.1/test/400_nwl/test_tool.py\npartis_nwl-0.0.1/test/400_nwl/test_output.py\npartis_nwl-0.0.1/test/400_nwl/test_input.py\npartis_nwl-0.0.1/LICENSE.txt\npartis_nwl-0.0.1/README.rst\npartis_nwl-0.0.1/pyproject.toml'

TOP_LEVEL = b''

ENTRY_POINTS = b'[partis_view]\nview_editors = partis.nwl.view.plugin:get_view_editors\n\n[console_scripts]\npartis-nwl = partis.nwl.__main__:main\npartis-nwl-pkg = partis.nwl.tool_pkg.__main__:main\n\n'

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

if __name__ == "__main__":
  exit( main() )
