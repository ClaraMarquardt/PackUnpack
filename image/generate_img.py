# Dependencies
import networkx as nx
import osmnx as ox
import requests
import matplotlib.cm as cm
import matplotlib.colors as colors


# Variables
network_type='drive'
distance=5000
fig_height=8
edge_linewidth=0.3

# city_1
city_1="Osnabrueck"
city_1_coordinate_1 = 52.2799
city_1_coordinate_2 = 8.0472
G = ox.graph_from_point((city_1_coordinate_1, city_1_coordinate_2), distance=distance, network_type=network_type)
fig, ax = ox.plot_graph(G, fig_height=fig_height, node_size=0, edge_linewidth=edge_linewidth)
fig.savefig('image/load_img/placeholder_img_1.png')

# city_2
city_2="Wiesbaden"
city_2_coordinate_1 = 50.0782
city_2_coordinate_2 = 8.2398
G = ox.graph_from_point((city_2_coordinate_1, city_2_coordinate_2), distance=distance, network_type=network_type)
fig, ax = ox.plot_graph(G, fig_height=fig_height, node_size=0, edge_linewidth=edge_linewidth)
fig.savefig('image/load_img/placeholder_img_2.png')

# city_3
city_3="Kassel"
city_3_coordinate_1 = 51.2848
city_3_coordinate_2 = 9.6203
G = ox.graph_from_point((city_3_coordinate_1, city_3_coordinate_2), distance=distance, network_type=network_type)
fig, ax = ox.plot_graph(G, fig_height=fig_height, node_size=0, edge_linewidth=edge_linewidth)
fig.savefig('image/load_img/placeholder_img_3.png')

# city_4
city_4="Karlsruhe,Waldstadt"
city_4_coordinate_1 = 49.0424
city_4_coordinate_2 = 8.4268
G = ox.graph_from_point((city_4_coordinate_1, city_4_coordinate_2), distance=distance, network_type=network_type)
fig, ax = ox.plot_graph(G, fig_height=fig_height, node_size=0, edge_linewidth=edge_linewidth)
fig.savefig('image/load_img/placeholder_img_4.png')

# city_5
city_5="Karlsruhe"
city_5_coordinate_1 = 49.0069
city_5_coordinate_2 = 8.4037
G = ox.graph_from_point((city_5_coordinate_1, city_5_coordinate_2), distance=distance, network_type=network_type)
fig, ax = ox.plot_graph(G, fig_height=fig_height, node_size=0, edge_linewidth=edge_linewidth)
fig.savefig('image/load_img/placeholder_img_5.png')

# city_6
city_6="Copenhagen"
city_6_coordinate_1 = 55.6761
city_6_coordinate_2 = 12.5683
G = ox.graph_from_point((city_6_coordinate_1, city_6_coordinate_2), distance=distance, network_type=network_type)
fig, ax = ox.plot_graph(G, fig_height=fig_height, node_size=0, edge_linewidth=edge_linewidth)
fig.savefig('image/load_img/placeholder_img_6.png')

# city_7
city_7="Karlsruhe"
city_7_coordinate_1 = 49.0069
city_7_coordinate_2 = 8.4037
G = ox.graph_from_point((city_7_coordinate_1, city_7_coordinate_2), distance=distance, network_type=network_type)
fig, ax = ox.plot_graph(G, fig_height=fig_height, node_size=0, edge_linewidth=edge_linewidth)
fig.savefig('image/load_img/placeholder_img_7.png')

# city_8
city_8="Frankfurt"
city_8_coordinate_1 = 50.1109
city_8_coordinate_2 = 8.6821
G = ox.graph_from_point((city_8_coordinate_1, city_8_coordinate_2), distance=distance, network_type=network_type)
fig, ax = ox.plot_graph(G, fig_height=fig_height, node_size=0, edge_linewidth=edge_linewidth)
fig.savefig('image/load_img/placeholder_img_8.png')

# city_9
city_9="Kaifaqu"
city_9_coordinate_1 = 39.0536
city_9_coordinate_2 = 121.7746
G = ox.graph_from_point((city_9_coordinate_1, city_9_coordinate_2), distance=distance, network_type=network_type)
fig, ax = ox.plot_graph(G, fig_height=fig_height, node_size=0, edge_linewidth=edge_linewidth)
fig.savefig('image/load_img/placeholder_img_9.png')

# city_10
city_10="Beijing"
city_10_coordinate_1 = 39.9042
city_10_coordinate_2 = 116.4074
G = ox.graph_from_point((city_10_coordinate_1, city_10_coordinate_2), distance=distance, network_type=network_type)
fig, ax = ox.plot_graph(G, fig_height=fig_height, node_size=0, edge_linewidth=edge_linewidth)
fig.savefig('image/load_img/placeholder_img_10.png')

# city_11
city_11="Dalian"
city_11_coordinate_1 = 38.914
city_11_coordinate_2 = 121.6147
G = ox.graph_from_point((city_11_coordinate_1, city_11_coordinate_2), distance=distance, network_type=network_type)
fig, ax = ox.plot_graph(G, fig_height=fig_height, node_size=0, edge_linewidth=edge_linewidth)
fig.savefig('image/load_img/placeholder_img_11.png')

# city_12
city_12="Jiashan,Gansu"
city_12_coordinate_1 = 33.7688
city_12_coordinate_2 = 106.0878
G = ox.graph_from_point((city_12_coordinate_1, city_12_coordinate_2), distance=distance, network_type=network_type)
fig, ax = ox.plot_graph(G, fig_height=fig_height, node_size=0, edge_linewidth=edge_linewidth)
fig.savefig('image/load_img/placeholder_img_12.png')

# city_13
city_13="Beijing"
city_13_coordinate_1 = 39.9042
city_13_coordinate_2 = 116.4074
G = ox.graph_from_point((city_13_coordinate_1, city_13_coordinate_2), distance=distance, network_type=network_type)
fig, ax = ox.plot_graph(G, fig_height=fig_height, node_size=0, edge_linewidth=edge_linewidth)
fig.savefig('image/load_img/placeholder_img_13.png')

# city_14
city_14="Cambridge"
city_14_coordinate_1 = 52.2053
city_14_coordinate_2 = 0.1218
G = ox.graph_from_point((city_14_coordinate_1, city_14_coordinate_2), distance=distance, network_type=network_type)
fig, ax = ox.plot_graph(G, fig_height=fig_height, node_size=0, edge_linewidth=edge_linewidth)
fig.savefig('image/load_img/placeholder_img_14.png')

# city_15
city_15="PhnomPenh"
city_15_coordinate_1 = 11.556374
city_15_coordinate_2 = 104.9282
G = ox.graph_from_point((city_15_coordinate_1, city_15_coordinate_2), distance=distance, network_type=network_type)
fig, ax = ox.plot_graph(G, fig_height=fig_height, node_size=0, edge_linewidth=edge_linewidth)
fig.savefig('image/load_img/placeholder_img_15.png')

# city_16
city_16="London"
city_16_coordinate_1 = 51.5074
city_16_coordinate_2 = -0.1278
G = ox.graph_from_point((city_16_coordinate_1, city_16_coordinate_2), distance=distance, network_type=network_type)
fig, ax = ox.plot_graph(G, fig_height=fig_height, node_size=0, edge_linewidth=edge_linewidth)
fig.savefig('image/load_img/placeholder_img_16.png')


# city_17
city_17="Cambridge,MA"
city_17_coordinate_1 = 42.3736
city_17_coordinate_2 = -71.1097
G = ox.graph_from_point((city_17_coordinate_1, city_17_coordinate_2), distance=distance, network_type=network_type)
fig, ax = ox.plot_graph(G, fig_height=fig_height, node_size=0, edge_linewidth=edge_linewidth)
fig.savefig('image/load_img/placeholder_img_17.png')

# city_18
city_18="SanFrancisco"
city_18_coordinate_1 = 37.7749
city_18_coordinate_2 = -122.4194
G = ox.graph_from_point((city_18_coordinate_1, city_18_coordinate_2), distance=distance, network_type=network_type)
fig, ax = ox.plot_graph(G, fig_height=fig_height, node_size=0, edge_linewidth=edge_linewidth)
fig.savefig('image/load_img/placeholder_img_18.png')

# city_19
city_19="Somerville"
city_19_coordinate_1 = 42.3876
city_19_coordinate_2 = -71.0995
G = ox.graph_from_point((city_19_coordinate_1, city_19_coordinate_2), distance=distance, network_type=network_type)
fig, ax = ox.plot_graph(G, fig_height=fig_height, node_size=0, edge_linewidth=edge_linewidth)
fig.savefig('image/load_img/placeholder_img_19.png')

# city_20
city_20="Chicago"
city_20_coordinate_1 = 41.8781
city_20_coordinate_2 = -87.6298
G = ox.graph_from_point((city_20_coordinate_1, city_20_coordinate_2), distance=distance, network_type=network_type)
fig, ax = ox.plot_graph(G, fig_height=fig_height, node_size=0, edge_linewidth=edge_linewidth)
fig.savefig('image/load_img/placeholder_img_20.png')


