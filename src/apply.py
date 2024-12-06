import click


@click.command()
@click.option("-f", "--file", required=True, type=click.Path(exists=True))
@click.option("-t", "--type", required=True)
def apply(file):
    '''Create resource using yaml file'''
    pass