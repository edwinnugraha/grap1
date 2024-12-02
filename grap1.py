import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import random

# Judul aplikasi
st.title("Visualisasi Graf Tak Berarah dengan Streamlit")

# Input jumlah node dan edge
num_nodes = st.number_input("Masukkan jumlah node:", min_value=1, max_value=100, value=5, step=1)
num_edges = st.number_input("Masukkan jumlah edge:", min_value=0, max_value=200, value=5, step=1)

# Tombol untuk membuat graf
if st.button("Buat Graf"):
    # Membuat graf acak
    G = nx.Graph()

    # Menambahkan node
    G.add_nodes_from(range(num_nodes))

    # Menambahkan edge secara acak
    edges = set()
    while len(edges) < num_edges:
        u = random.randint(0, num_nodes - 1)
        v = random.randint(0, num_nodes - 1)
        if u != v:
            edges.add((u, v))
    G.add_edges_from(edges)

    # Plot graf menggunakan Matplotlib
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G)  # Layout graf
    nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color='gray', node_size=500, font_size=10)
    plt.title("Graf Acak dengan NetworkX")

    # Tampilkan graf di Streamlit
    st.pyplot(plt)
