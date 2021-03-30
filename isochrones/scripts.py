import click


@click.group()
def cli():
    pass


@cli.command('to-graph')
@click.option('--link')
@click.option('--node')
@click.option('--output')
def to_graph(link, node, output):
    """Create a json file with the adjacency list representation of the graph"""
    print("hola")
