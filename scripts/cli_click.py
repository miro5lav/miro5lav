import click
import subprocess
import platform
import sys
from functools import wraps


def get_os_type():
    """Detect operating system"""
    return 'windows' if platform.system() == 'Windows' else 'linux'


def run_command(cmd, shell=False):
    """Execute command and return output"""
    try:
        result = subprocess.run(
            cmd,
            shell=shell,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        click.echo(f"Error: {e.stderr}", err=True)
        sys.exit(1)


class CommandRegistry:
    """Registry for OS-specific commands"""

    def __init__(self):
        self.commands = {}

    def register(self, name, windows_cmd, linux_cmd):
        """Register a command for both OS types"""
        self.commands[name] = {
            'windows': windows_cmd,
            'linux': linux_cmd
        }

    def get(self, name, os_type):
        """Get command for specific OS"""
        return self.commands.get(name, {}).get(os_type)


# Initialize registry
registry = CommandRegistry()

# Register commands
registry.register('http_get',
                  windows_cmd=['powershell', '-Command', 'Invoke-WebRequest'],
                  linux_cmd=['curl']
                  )

registry.register('list_dir',
                  windows_cmd=['powershell', '-Command', 'Get-ChildItem'],
                  linux_cmd=['ls', '-la']
                  )

registry.register('bazel_version',
                  windows_cmd=['bazel', 'version'],
                  linux_cmd=['bazel', 'version']
                  )

registry.register('uv_version',
                  windows_cmd=['uv', '--version'],
                  linux_cmd=['uv', '--version']
                  )

registry.register('trivy_version',
                  windows_cmd=['trivy', '--version'],
                  linux_cmd=['trivy', '--version']
                  )


@click.group()
@click.pass_context
def cli(ctx):
    """Cross-platform CLI tool that adapts to Windows or Linux"""
    ctx.ensure_object(dict)
    ctx.obj['os'] = get_os_type()
    click.echo(f"Running on: {ctx.obj['os']}")


@cli.command()
@click.argument('url')
@click.pass_context
def http_get(ctx, url):
    """Make HTTP GET request (PowerShell Invoke-WebRequest on Windows, curl on Linux)"""
    os_type = ctx.obj['os']
    base_cmd = registry.get('http_get', os_type)

    if os_type == 'windows':
        cmd = base_cmd + [f'"{url}"', '-UseBasicParsing']
        output = run_command(' '.join(cmd), shell=True)
    else:
        cmd = base_cmd + [url]
        output = run_command(cmd)

    click.echo(output)


@cli.command()
@click.argument('path', default='.')
@click.pass_context
def list_dir(ctx, path):
    """List directory contents (Get-ChildItem on Windows, ls on Linux)"""
    os_type = ctx.obj['os']
    base_cmd = registry.get('list_dir', os_type)

    if os_type == 'windows':
        cmd = base_cmd + [f'"{path}"']
        output = run_command(' '.join(cmd), shell=True)
    else:
        cmd = base_cmd + [path]
        output = run_command(cmd)

    click.echo(output)


@cli.command()
@click.pass_context
def bazel(ctx):
    """Check Bazel version"""
    os_type = ctx.obj['os']
    cmd = registry.get('bazel_version', os_type)
    output = run_command(cmd)
    click.echo(output)


@cli.command()
@click.pass_context
def uv(ctx):
    """Check UV version"""
    os_type = ctx.obj['os']
    cmd = registry.get('uv_version', os_type)
    output = run_command(cmd)
    click.echo(output)


@cli.command()
@click.pass_context
def trivy(ctx):
    """Check Trivy version"""
    os_type = ctx.obj['os']
    cmd = registry.get('trivy_version', os_type)
    output = run_command(cmd)
    click.echo(output)


@cli.command()
@click.pass_context
def show_registry(ctx):
    """Show all registered commands"""
    click.echo("\nRegistered Commands:")
    click.echo("-" * 50)
    for name, cmds in registry.commands.items():
        click.echo(f"\n{name}:")
        click.echo(f"  Windows: {' '.join(cmds['windows'])}")
        click.echo(f"  Linux:   {' '.join(cmds['linux'])}")


if __name__ == '__main__':
    cli(obj={})