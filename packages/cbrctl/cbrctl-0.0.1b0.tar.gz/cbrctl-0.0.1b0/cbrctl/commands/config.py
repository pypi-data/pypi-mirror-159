import click
import os
import random

from cbrctl.utilities import run_shell_command, get_carbonara_config_filepath, validate_configuration
from cbrctl.platforms.eks import EKS_CONFIG_ACTIONS
from cbrctl.platforms.quotes import CARBONARA_QUOTES
from kubernetes import config as kube_config

from logging import basicConfig, getLogger, INFO

formatter = " %(asctime)s | %(levelname)-6s | %(process)d | %(threadName)-12s |" \
            " %(thread)-15d | %(name)-30s | %(filename)s:%(lineno)d | %(message)s |"
basicConfig(level=INFO, format=formatter)
logger = getLogger(__name__)


def _get_kube_current_context():
    # checks if kubectl current context is the passed cluster
    contexts, active_context = kube_config.list_kube_config_contexts()
    if not contexts:
        click.echo("Cannot find any context in kube-config file.")
        raise click.Abort
    # contexts = [context['name'] for context in contexts]
    # active_index = contexts.index(active_context['name'])
    # click.echo(active_index)
    kube_current_context = active_context['name']
    if '@' in kube_current_context:
        kube_current_context = kube_current_context.split('@')[1]
    kube_current_context = kube_current_context.split('.')[0]
    return kube_current_context

@click.command(help="Configures target cluster with Carbonara packages. "
                   "Validates if passed cluster is also the current kubectl context.")
@click.option('--cluster', '-c', prompt=f'Enter target cluster [Type: {_get_kube_current_context()}]', help='Target Cluster (current kubectl context).')
@click.option('--namespace', '-n', default="carbonara-monitoring", help='Target namespace for monitoring. (Default: carbonara-monitoring)')
@click.option('--new-setup', '-s', default=True, is_flag=True, help='[Not-Available] Flag for using existing monitoring (Prometheus).')
def config(cluster, namespace, new_setup):
    # TODO: make sure of namespace parameter
    # checking if initialization succeeded:
    carbonara_config = get_carbonara_config_filepath()
    if not os.path.exists(carbonara_config):
        click.echo('Please intialize the context again.')
        raise click.Abort

    kube_current_context = _get_kube_current_context()
    if kube_current_context != cluster:
        click.echo("Current kubectl context doesn't match the passed one.")
        raise click.Abort
    _setup_cluster(namespace)

def _setup_cluster(namespace):
    return _setup_cluster_eks(namespace)

def _setup_cluster_eks(namespace):
    click.secho("Configuring cluster for monitoring ...", fg='blue', bold=True)
    with click.progressbar(EKS_CONFIG_ACTIONS) as bar:
        random_list = list(range(0, len(CARBONARA_QUOTES) - 1))
        for action in bar:
            random_number = random.choice(random_list)
            bar.label = CARBONARA_QUOTES[random_number] + "\n"
            bar.color = True
            if (run_shell_command(action) != 0):
                raise click.Abort
            random_list.remove(random_number)

    click.secho("Validating the configured namespace.", fg='blue')

    # (Optional) Validate configuration ready
    validate_configuration()
    click.secho("You can use `cbrctl status` to view the configured resources.", fg='green')
    click.secho("Cluster Configured Successfully. Happy Carbonara \m/", fg='blue')