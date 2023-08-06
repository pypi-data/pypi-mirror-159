import click
import os
import subprocess
import shlex

from logging import basicConfig, getLogger, INFO

formatter = " %(asctime)s | %(levelname)-6s | %(process)d | %(threadName)-12s |" \
            " %(thread)-15d | %(name)-30s | %(filename)s:%(lineno)d | %(message)s |"
basicConfig(level=INFO, format=formatter)
logger = getLogger(__name__)


def run_shell_command(command, print=False):
    logger.debug ("Running Command: '{}'".format(command))
    cmd = shlex.split(command)
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, bufsize=1)
    for line in iter(process.stdout.readline, b''):
        if print:
            click.echo(line)
    process.stdout.close()
    process.wait()
    return process.returncode

def run_shell_command_and_forget(command):
    logger.debug ("Running Command: '{}'".format(command))
    cmd = shlex.split(command)
    process = subprocess.Popen(cmd, bufsize=1)
    process.wait()

def run_shell_command_with_response(command):
    logger.debug ("Running Command: '{}'".format(command))
    cmd = shlex.split(command)
    process = subprocess.Popen(cmd,
                     stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return process.returncode, stdout, stderr

def is_tool(name):
    """Check whether `name` is on PATH."""

    from distutils.spawn import find_executable
    return find_executable(name) is not None

def get_carbonara_config_filepath():
    pwd = os.path.expanduser('~')
    kube_dir = os.path.join(pwd, '.kube')
    try:
        os.mkdir(kube_dir)
    except FileExistsError:
        logger.debug(f"{kube_dir} exists")
    return os.path.join(kube_dir, 'carbonara_config')

def validate_configuration():
    returncode1, stdout1, stderr1 = run_shell_command_with_response(
        "kubectl --namespace carbonara-monitoring get pods -l 'release=prometheus'")
    returncode2, stdout2, stderr2 = run_shell_command_with_response(
        "kubectl --namespace carbonara-monitoring get pods -l 'release=prometheus-pushgateway'")
    if ((returncode1 or returncode2) != 0 or
            ('No resources found' in str(stderr1) or 'No resources found' in str(stderr2))):
        click.secho('Please configure the cluster again.', fg='red')
        raise click.Abort
