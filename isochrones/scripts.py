import click
from .utils import to_graph
import json


@click.group()
def cli():
    pass


@cli.command('to-graph')
@click.option('--link')
@click.option('--node')
@click.option('--output')
def to_graph_command(link, node, output):
    """Create a json file with the adjacency list representation of the graph"""
    graph = to_graph(link, node)
    json.dump(graph, open(output, 'w'))
