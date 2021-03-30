import click
from .utils import to_graph, compute_distances
import json


@click.group()
def cli():
    pass


@cli.command('to-graph')
@click.option('--link')
@click.option('--node')
@click.option('--output', type=click.File('w'))
def to_graph_command(link, node, output):
    """
    Create a json file with the adjacency list representation of
    the graph.
    """
    graph = to_graph(link, node)
    json.dump(graph, output)


@cli.command('compute-distances')
@click.option('--graph', type=click.File())
@click.option('--source')
@click.option('--output', type=click.File('w'))
def compute_distances_command(graph, source, output):
    """Compute distance from a single source to all nodes"""
    graph_dict = json.load(graph)
    distances = compute_distances(graph_dict, source)
    json.dump(distances, output)
