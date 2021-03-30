import fiona
from scipy.spatial import KDTree
from pyproj import Geod
from shapely.geometry import shape
from collections import defaultdict


def to_graph(link_path, node_path):
    adjacency_list = defaultdict(list)

    with fiona.open(link_path) as link_collection,\
            fiona.open(node_path) as node_collection:

        nodes_coordinates = []
        nodes_ids = []
        for rec in node_collection:
            nodes_coordinates.append(rec['geometry']['coordinates'])
            nodes_ids.append(rec['properties']['id'])

        kdtree = KDTree(nodes_coordinates)

        geod = Geod(ellps="WGS84")
        for rec in link_collection:
            direction = rec['properties']['dir']
            vel_AB = rec['properties']['VEL_AB']
            vel_BA = rec['properties']['VEL_BA']

            length = geod.geometry_length(shape(rec['geometry']))
            time_AB = length / vel_AB * (60/1000) * 60
            time_BA = length / vel_BA * (60/1000) * 60

            start_point = rec['geometry']['coordinates'][0]
            end_point = rec['geometry']['coordinates'][-1]

            start_distance, start_pos = kdtree.query(start_point)
            end_distance, end_pos = kdtree.query(end_point)

            start_id = nodes_ids[start_pos]
            end_id = nodes_ids[end_pos]

            if direction == 1:
                adjacency_list[start_id].append((time_AB, end_id))
            elif direction == -1:
                adjacency_list[end_id].append((time_BA, start_id))
            elif direction == 0:
                adjacency_list[start_id].append((time_AB, end_id))
                adjacency_list[end_id].append((time_BA, start_id))
            else:
                raise ValueError(direction)

    return adjacency_list


def compute_distances(graph, source):
    pass
