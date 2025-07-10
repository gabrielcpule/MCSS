import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

# Use exact components from instructions
components_data = {
    "Organisms": {"components": ["Navigation", "Header", "Modal"], "color": "#DC3545"},
    "Molecules": {"components": ["Card", "Form Field", "Search Box"], "color": "#FD7E14"},
    "Atoms": {"components": ["Button", "Input", "Label", "Icon"], "color": "#28A745"}
}

# Create position data for components
fig = go.Figure()

# Define y positions for each level
y_positions = {"Atoms": 1, "Molecules": 2, "Organisms": 3}

# Store component positions for drawing connections
component_positions = {}

# Add components for each level
for level, data in components_data.items():
    components = data["components"]
    color = data["color"]
    y_pos = y_positions[level]
    
    # Calculate x positions to spread components horizontally
    if len(components) == 1:
        x_positions = [0]
    else:
        x_positions = np.linspace(-2, 2, len(components))
    
    # Add scatter points for each component
    for j, component in enumerate(components):
        x_pos = x_positions[j]
        component_positions[component] = (x_pos, y_pos)
        
        fig.add_trace(go.Scatter(
            x=[x_pos],
            y=[y_pos],
            mode='markers+text',
            text=[component],
            textposition="middle center",
            marker=dict(size=80, color=color, line=dict(width=2, color='white')),
            textfont=dict(size=12, color='white'),
            showlegend=False,
            hoverinfo='text',
            hovertext=f"{level}: {component}",
            cliponaxis=False
        ))

# Add connection lines to show hierarchy
# Molecules connect to all Atoms (solid lines)
molecule_components = components_data["Molecules"]["components"]
atom_components = components_data["Atoms"]["components"]

for molecule in molecule_components:
    mol_x, mol_y = component_positions[molecule]
    for atom in atom_components:
        atom_x, atom_y = component_positions[atom]
        fig.add_trace(go.Scatter(
            x=[mol_x, atom_x],
            y=[mol_y, atom_y],
            mode='lines',
            line=dict(color='#666666', width=2, dash='solid'),
            showlegend=False,
            hoverinfo='skip',
            cliponaxis=False
        ))

# Organisms connect to Molecules (dashed lines)
organism_components = components_data["Organisms"]["components"]

for organism in organism_components:
    org_x, org_y = component_positions[organism]
    # Connect to molecules
    for molecule in molecule_components:
        mol_x, mol_y = component_positions[molecule]
        fig.add_trace(go.Scatter(
            x=[org_x, mol_x],
            y=[org_y, mol_y],
            mode='lines',
            line=dict(color='#666666', width=2, dash='dash'),
            showlegend=False,
            hoverinfo='skip',
            cliponaxis=False
        ))

# Add level labels with better styling
fig.add_trace(go.Scatter(
    x=[-3.5, -3.5, -3.5],
    y=[1, 2, 3],
    mode='text',
    text=['Atoms', 'Molecules', 'Organisms'],
    textfont=dict(size=16, color='black', family='Arial Black'),
    showlegend=False,
    hoverinfo='skip',
    cliponaxis=False
))

# Update layout
fig.update_layout(
    title="MCSS Atomic Design Taxonomy",
    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-4, 3]),
    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[0.5, 3.5]),
    plot_bgcolor='white',
    paper_bgcolor='white'
)

# Save the chart
fig.write_image("mcss_taxonomy_tree.png")