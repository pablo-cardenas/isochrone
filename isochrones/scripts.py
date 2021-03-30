import click
from .utils import to_graph, compute_distances, add_field
import json


@click.group()
def cli():
    pass


@cli.command('to-graph')
@click.option('--link', required=True)
@click.option('--node', required=True)
@click.option('--output', type=click.File('w'), required=True)
def to_graph_command(link, node, output):
    """
    Create a json file with the adjacency list representation of
    the graph.
    """
    graph = to_graph(link, node)
    json.dump(graph, output)


@cli.command('compute-distances')
@click.option('--graph', type=click.File(), required=True)
@click.option('--source', required=True)
@click.option('--output', type=click.File('w'), required=True)
def compute_distances_command(graph, source, output):
    """Compute distance from a single source to all nodes"""
    graph_dict = json.load(graph)
    distances = compute_distances(graph_dict, source)
    json.dump(distances, output)


@cli.command('add-field')
@click.option('--shapefile', required=True)
@click.option('--field', type=click.File(), required=True)
@click.option('--output', required=True)
@click.option('--field-name', default='dist')
@click.option('--field-type', default='float')
def add_field_command(shapefile, field, output, field_name, field_type):
    """Add field to a shapefile"""
    field_dict = json.load(field)
    add_field(shapefile, field_dict, output, field_name, field_type)
