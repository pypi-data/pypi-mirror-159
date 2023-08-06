# Carbonara CLI

Carbonara command line tool for configuraing and access carbonara metrics

## Usage
> Usage: cbrctl [OPTIONS] COMMAND [ARGS]...
>  
>   CLI tool to manage carbonara context of projects
>  
> Options:
>   --help  Show this message and exit.
>  
> Commands:
>   config   Configures target cluster with Carbonara packages.
>   eject    Uninstalls resources configured by Carbonara
>   init     Initialize Carbonara context.
>   refresh  Refreshes the Carbonara Agent.
>   show     Forward one or more local ports to a Grafana pod.
>   status   Current Status.
>   version  Version Info.

## Development
* Requirements: Python>=3.7
* Command to generate wheel: `python setup sdist`
    * Installation can be found in `dist\`
* Command to test in local environment: `python setup develop`
    * Refer: https://packaging.python.org/en/latest/tutorials/packaging-projects/

## Installation
> ❯ pip install cbrctl-0.0.1.tar.gz
>
> TODO: Publish to PyPi Repo