"""
Update release numbers in various places, according to a release.ini file places at the project root.

For now, the following sections are supported:

+ Main file (__init__.py, Django settings file, etc.)
+ Sphinx conf.py file
+ sonar-project.properties
+ ansible vars file
+ node package.json file
+ setup.cfg
+ setup.py
+ pyproject.toml

"""
import configparser
import logging
import sys
from configparser import ConfigParser
from pathlib import Path
from typing import Optional

import click

from bump_release import helpers

# region Globals
__version__ = VERSION = "0.10.6"
RELEASE_FILE: Optional[Path] = None
RELEASE_CONFIG: Optional[ConfigParser] = None


# endregion Globals


@click.command()
@click.option(
    "-r",
    "--release-file",
    "release_file",
    help="Release file path, default `./release.ini`",
    type=click.Path(exists=True),
    default="release.ini",
)
@click.option(
    "-n",
    "--dry-run",
    "dry_run",
    is_flag=True,
    help="If set, no operation are performed on files",
    default=False,
)
@click.option(
    "-d",
    "--debug",
    "debug",
    is_flag=True,
    help="If set, more traces are printed for users",
    default=False,
)
@click.version_option(version=__version__)
@click.argument("release")
def bump_release(release: str, release_file: Optional[str] = None, dry_run: bool = False, debug: bool = False) -> int:
    """
    Update release numbers in various places, according to a release.ini file places at the project root.

    \b
    For now, the following sections are supported:

    \b
    + Main file (__init__.py, Django settings file, etc.)
    + Sphinx conf.py file
    + sonar-project.properties
    + ansible vars file
    + node package.json file
    + setup.cfg
    + setup.py
    + pyproject.toml (Require using `pip install bump_release[toml]`)

    \f
    :param release: Release number
    :param release_file: Release file path, default `./release.ini`
    :param dry_run: If `True`, no operation performed
    :param debug: If `True`, more traces are printed for users
    :return: 0 if success, 1|2 if error
    """
    # Loads the release.ini file
    global RELEASE_CONFIG, RELEASE_FILE

    if release_file is None:
        RELEASE_FILE = Path.cwd() / "release.ini"
    else:
        RELEASE_FILE = Path(release_file)

    if not RELEASE_FILE.exists():
        print(f"Unable to find release.ini file in the current directory {Path.cwd()}", file=sys.stderr)
        return 1

    RELEASE_CONFIG = helpers.load_release_file(release_file=RELEASE_FILE)
    try:
        return process_update(release_file=RELEASE_FILE, release=release, dry_run=dry_run, debug=debug)
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 2


def process_update(release_file: Path, release: str, dry_run: bool, debug: bool = False) -> int:
    """
    Processes the update of the release number.

    :param release_file: Release file path
    :param release: Release number
    :param dry_run: If `True`, no operation performed
    :param debug: If `True`, more traces are printed for users
    :return: 0 if success, 1|2 if error
    """
    version = helpers.VersionNumber(version=release)

    # Initialize the logging
    if debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    # region Updates the main project (DJANGO_SETTINGS_MODULE file for django projects, __init__.py file...)
    try:
        new_row = update_main_file(version=version, base_path=release_file.parent, dry_run=dry_run)
        if new_row is not None:
            logging.debug(f"process_update() `main_project`: new_row = {new_row.strip()}")
    except helpers.NothingToDoException as e:
        logging.warning(f"process_update() No release section for `main_project`: {e}")
    # endregion

    # region Updates sonar-scanner properties
    try:
        new_row = update_sonar_properties(version=version, base_path=release_file.parent, dry_run=dry_run)
        if new_row is not None:
            logging.debug(f"process_update() `sonar`: new_row = {new_row.strip()}")
    except helpers.NothingToDoException as e:
        logging.warning(f"process_update() No release section for `sonar`: {e}")
    # endregion

    # region Updates setup.py file
    try:
        new_row = update_setup_file(version=version, base_path=release_file.parent, dry_run=dry_run)
        if new_row is not None:
            logging.debug(f"process_update() `setup`: new_row = {new_row.strip()}")
    except helpers.NothingToDoException as e:
        logging.warning(f"process_update() No release section for `setup`: {e}")
    # endregion

    # region Update setup.cfg file
    try:
        new_row = update_setup_cfg_file(version=version, base_path=release_file.parent, dry_run=dry_run)
        if new_row is not None:
            logging.debug(f"process_update() `setup_cfg`: new_row = {new_row.strip()}")
    except helpers.NothingToDoException as e:
        logging.warning(f"process_update() No release section for `setup`: {e}")
    # endregion Update setup.cfg file

    # region Updates sphinx file
    try:
        new_row = update_docs_conf(version=version, base_path=release_file.parent, dry_run=dry_run)
        if new_row is not None:
            logging.debug(f"process_update() `docs`: new_row = {new_row.strip()}")
    except helpers.NothingToDoException as e:
        logging.warning(f"process_update() No release section for `docs`: {e}")
    # endregion

    # region Updates node packages file
    try:
        logging.debug("process_update() `node_module`")
        new_row = update_node_package(version=version, base_path=release_file.parent, dry_run=dry_run)
        if new_row is not None:
            logging.debug(
                f"process_update() `node`: new_row = {new_row}",
            )
    except helpers.NothingToDoException as e:
        logging.warning(f"process_update() No release section for `node`: {e}")
    # endregion

    # region Updates YAML file
    try:
        new_row = update_ansible_vars(version=version, base_path=release_file.parent, dry_run=dry_run)
        if new_row is not None:
            logging.debug(f"process_update() `ansible`: new_row = {new_row.strip()}")
    except helpers.NothingToDoException as e:
        logging.warning(f"process_update() No release section for `ansible`: {e}")
    # endregion

    # region Updates pyproject.toml file
    try:
        new_row = update_pyproject(version=version, base_path=release_file.parent, dry_run=dry_run)
        if new_row is not None:
            logging.debug(f"process_update() `pyproject.toml`: new_row = {new_row.strip()}")
    except helpers.NothingToDoException as e:
        logging.warning(f"process_update() No release section for `pyproject.toml`: {e}")
    except helpers.UpdateException:  # noqa: E722
        logging.exception("process_update() `pyproject.toml`: UpdateException - tomli / tomli_w might be missing")

    # endregion Updates pyproject.toml file

    # region Updates the release.ini file with the new release number
    new_row = update_release_ini(path=release_file, version=version, dry_run=dry_run)
    if new_row is not None:
        logging.warning(f"process_update() `release.ini`: new_row = {new_row.strip()}")
    # endregion

    return 0


def update_main_file(version: helpers.VersionNumber, base_path: Path, dry_run: bool = True) -> Optional[str]:
    """
    Updates the main django settings file, or a python script with a __init__.py file.

    :param version: Release number tuple (major, minor, release)
    :param base_path: Base search path
    :param dry_run: If `True`, no operation performed
    :return: changed string
    """
    assert RELEASE_CONFIG is not None
    if not RELEASE_CONFIG.has_section("main_project"):
        raise helpers.NothingToDoException("No `main_project` section in release.ini file")

    try:
        path = helpers.resolve_path(path=RELEASE_CONFIG.get("main_project", "path"), release_file_path=base_path)
        logging.debug(f"update_main_file() path = {path}")
        pattern = RELEASE_CONFIG["main_project"].get("pattern", "").strip('"') or helpers.MAIN_PROJECT_PATTERN
        template = RELEASE_CONFIG["main_project"].get("template", "").strip('"') or helpers.MAIN_PROJECT_TEMPLATE
    except configparser.Error as e:
        raise helpers.NothingToDoException("Unable to update main project file", e)
    return helpers.update_file(path=path, pattern=pattern, template=template, version=version, dry_run=dry_run)


def update_setup_file(version: helpers.VersionNumber, base_path: Path, dry_run: bool = False) -> Optional[str]:
    """
    Updates the setup.py file.

    :param version: Release number tuple (major, minor, release)
    :param base_path: Base search path
    :param dry_run: If `True`, no operation performed
    :return: changed string
    """
    assert RELEASE_CONFIG is not None
    if not RELEASE_CONFIG.has_section("setup"):
        raise helpers.NothingToDoException("No `setup` section in release.ini file")

    try:
        path = helpers.resolve_path(path=RELEASE_CONFIG.get("setup", "path"), release_file_path=base_path)
        logging.debug(f"update_setup_file() path = {path}")
        pattern = RELEASE_CONFIG["setup"].get("pattern", "").strip('"') or helpers.SETUP_PATTERN
        template = RELEASE_CONFIG["setup"].get("template", "").strip('"') or helpers.SETUP_TEMPLATE

    except configparser.Error as e:
        raise helpers.NothingToDoException("No action to perform for setup file", e)
    return helpers.update_file(path=path, pattern=pattern, template=template, version=version, dry_run=dry_run)


def update_setup_cfg_file(version: helpers.VersionNumber, base_path: Path, dry_run: bool = False) -> Optional[str]:
    """
    Update the setup.cfg file.

    :param version: Release number tuple (major, minor, release)
    :param base_path: Base search path
    :param dry_run: If `True`, no operation performed
    :return: changed string
    """
    assert RELEASE_CONFIG is not None
    if not RELEASE_CONFIG.has_section("setup_cfg"):
        raise helpers.NothingToDoException("No `setup_cfg` section in release.ini file")

    try:
        path = helpers.resolve_path(path=RELEASE_CONFIG.get("setup_cfg", "path"), release_file_path=base_path)
        logging.debug(f"update_setup_cfg_file() path = {path}")
        pattern = RELEASE_CONFIG["setup_cfg"].get("pattern", "").strip('"') or helpers.SETUP_CFG_PATTERN
        template = RELEASE_CONFIG["setup_cfg"].get("template", "").strip('"') or helpers.SETUP_CFG_TEMPLATE

    except configparser.Error as e:
        raise helpers.NothingToDoException("No action to perform for setup.cfg file", e)
    return helpers.update_file(path=path, pattern=pattern, template=template, version=version, dry_run=dry_run)


def update_sonar_properties(version: helpers.VersionNumber, base_path: Path, dry_run: bool = False) -> Optional[str]:
    """
    Updates the sonar-project.properties file with the new release number

    :param version: Release number tuple (major, minor, release)
    :param base_path: Base search path
    :param dry_run: If `True`, no operation performed
    :return: changed string
    """
    assert RELEASE_CONFIG is not None
    if not RELEASE_CONFIG.has_section("sonar"):
        raise helpers.NothingToDoException("No `sonar` section in release.ini file")

    try:
        path = helpers.resolve_path(path=RELEASE_CONFIG.get("sonar", "path"), release_file_path=base_path)
        logging.debug(f"update_sonar_properties() path = {path}")
        pattern = RELEASE_CONFIG["sonar"].get("pattern", "").strip('"') or helpers.SONAR_PATTERN
        template = RELEASE_CONFIG["sonar"].get("template", "").strip('"') or helpers.SONAR_TEMPLATE
    except configparser.Error as e:
        raise helpers.NothingToDoException("No action to perform for sonar file", e)
    return helpers.update_file(path=path, pattern=pattern, template=template, version=version, dry_run=dry_run)


def update_docs_conf(version: helpers.VersionNumber, base_path: Path, dry_run: bool = False) -> Optional[str]:
    """
    Updates the Sphinx conf.py file with the new release number

    :param version: Release number tuple (major, minor, release)
    :param base_path: Base search path
    :param dry_run: If `True`, no operation performed
    :return: changed string
    """
    assert RELEASE_CONFIG is not None
    if not RELEASE_CONFIG.has_section("docs"):
        raise helpers.NothingToDoException("No `docs` section in release.ini file")

    try:
        path = helpers.resolve_path(path=RELEASE_CONFIG.get("docs", "path"), release_file_path=base_path)
        logging.debug(f"update_docs_conf() path = {path}")

        pattern_release = RELEASE_CONFIG["docs"].get("pattern_release", "").strip('"') or helpers.DOCS_RELEASE_PATTERN
        template_release = RELEASE_CONFIG["docs"].get("template_release", "").strip('"') or helpers.DOCS_RELEASE_FORMAT
        pattern_version = RELEASE_CONFIG["docs"].get("pattern_version", "").strip('"') or helpers.DOCS_VERSION_PATTERN
        template_version = RELEASE_CONFIG["docs"].get("template_version", "").strip('"') or helpers.DOCS_VERSION_FORMAT

    except configparser.Error as e:
        raise helpers.NothingToDoException("No action to perform for docs file", e)

    update_release = helpers.update_file(
        path=path,
        pattern=pattern_release,
        template=template_release,
        version=version,
        dry_run=dry_run,
    )
    update_version = helpers.update_file(
        path=path,
        pattern=pattern_version,
        template=template_version,
        version=version,
        dry_run=dry_run,
    )
    return str(update_release) + str(update_version)


def update_node_package(version: helpers.VersionNumber, base_path: Path, dry_run: bool = False) -> Optional[str]:
    """
    Updates the nodejs package file with the new release number

    :param version: Release number tuple (major, minor, release)
    :param base_path: Base search path
    :param dry_run: If `True`, no operation performed
    :return: changed string
    """
    assert RELEASE_CONFIG is not None
    try:
        if "node" in RELEASE_CONFIG:
            path = helpers.resolve_path(path=RELEASE_CONFIG.get("node", "path"), release_file_path=base_path)
        elif "node_module" in RELEASE_CONFIG:
            path = helpers.resolve_path(path=RELEASE_CONFIG.get("node_module", "path"), release_file_path=base_path)
        else:
            raise helpers.NothingToDoException("No `node` or `node_module` section in release.ini file")
        logging.debug(f"update_node_package() path = {path}")
        key = RELEASE_CONFIG.get("node_module", "key", fallback=helpers.NODE_KEY)  # noqa
    except configparser.Error as e:
        raise helpers.NothingToDoException("No action to perform for node packages file", e)
    return helpers.update_json_file(path=path, version=version, key=key, dry_run=dry_run)


def update_ansible_vars(version: helpers.VersionNumber, base_path: Path, dry_run: bool = False) -> Optional[str]:
    """
    Updates the ansible project variables file with the new release number

    :param version: Release number tuple (major, minor, release)
    :param base_path: Base search path
    :param dry_run: If `True`, no operation performed
    :return: changed string
    """
    assert RELEASE_CONFIG is not None
    try:
        path = helpers.resolve_path(path=RELEASE_CONFIG.get("ansible", "path"), release_file_path=base_path)
        logging.debug(f"update_ansible_vars() path = {path}")
        key = RELEASE_CONFIG.get("ansible", "key", fallback=helpers.ANSIBLE_KEY)  # noqa
    except configparser.Error as e:
        raise helpers.NothingToDoException("No action to perform for `ansible` file", e)
    return helpers.updates_yaml_file(path=path, version=version, key=key, dry_run=dry_run)


def update_pyproject(version: helpers.VersionNumber, base_path: Path, dry_run: bool = False) -> Optional[str]:
    """
    Updates the pyproject.toml file with the new release number

    :param version: release number, as (<major>, <minor>, <release>)
    :param base_path: Base search path
    :param dry_run: If `True`, the operation WILL NOT be performed
    :return: Updated lines
    """
    assert RELEASE_CONFIG is not None
    try:
        path = helpers.resolve_path(path=RELEASE_CONFIG.get("pyproject", "path"), release_file_path=base_path)
        logging.debug(f"update_pyproject() path = {path}")
        key = RELEASE_CONFIG.get("pyproject", "key", fallback=helpers.PYPROJECT_KEY)  # noqa
    except KeyError as ke:
        raise helpers.NothingToDoException("No pyproject key found in ini file for pyproject.toml file", ke)
    except configparser.Error as e:
        raise helpers.NothingToDoException("No action to perform for pyproject.toml file", e)

    # Update pyproject.toml file
    return helpers.update_toml_file(
        path=path,
        version=version,
        key=key,
        dry_run=dry_run,
    )


def update_release_ini(path: Path, version: helpers.VersionNumber, dry_run: bool = False) -> Optional[str]:
    """
    Updates the release.ini file with the new release number

    :param path: Release file path
    :param version: release number, as (<major>, <minor>, <release>)
    :param dry_run: If `True`, the operation WILL NOT be performed
    :return: Updated lines
    """
    return helpers.update_file(
        path=path,
        pattern=helpers.RELEASE_INI_PATTERN,
        template=helpers.RELEASE_INI_TEMPLATE,
        version=version,
        dry_run=dry_run,
    )
