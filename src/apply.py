import click


@click.command()
@click.option("f", "--file", required=True, type=click.Path(exists=True))
def apply(file):
    '''Create resource using yaml file'''
    with open(file, 'r') as f:
        details = f.read()
        click.echo(details)