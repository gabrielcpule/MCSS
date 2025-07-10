import plotly.graph_objects as go
import json

# Load the data
data = {"layers": [{"name": "Exception", "level": 5, "color": "#DC3545", "description": "Temporary fixes, debugging, third-party", "examples": ["Legacy styles", "Debug utilities", "Third-party overrides"]}, {"name": "Utility", "level": 4, "color": "#6F42C1", "description": "Single-purpose, u-* classes, overrides", "examples": ["u-text-center", "u-hidden", "u-margin-0"]}, {"name": "Component", "level": 3, "color": "#FD7E14", "description": "Reusable UI, c-* classes, BEM syntax", "examples": ["c-button", "c-card", "c-navigation"]}, {"name": "Layout", "level": 2, "color": "#28A745", "description": "Page structure, l-* classes, positioning", "examples": ["l-container", "l-grid", "l-stack"]}, {"name": "Global", "level": 1, "color": "#007BFF", "description": "Foundation styles, design tokens, HTML elements", "examples": ["tokens.css", "body, h1-h6", "CSS resets"]}]}

# Sort layers by level (bottom to top)
layers = sorted(data['layers'], key=lambda x: x['level'])

# Create the figure
fig = go.Figure()

# Add each layer as a horizontal bar
for layer in layers:
    fig.add_trace(go.Bar(
        x=[1],  # Full width bar
        y=[layer['name']],
        orientation='h',
        name=layer['name'],
        marker_color=layer['color'],
        text=layer['description'][:15],  # Truncate to 15 chars
        textposition='inside',
        textfont=dict(color='white', size=12),
        hovertemplate=f"<b>{layer['name']}</b><br>" +
                     f"Level: {layer['level']}<br>" +
                     f"{layer['description']}<br>" +
                     f"Examples: {', '.join(layer['examples'][:2])}<extra></extra>",
        showlegend=False,
        width=0.8,
        cliponaxis=False
    ))

# Add arrows to show cascade direction
for i in range(len(layers) - 1):
    fig.add_annotation(
        x=1.1,
        y=layers[i]['name'],
        ax=1.1,
        ay=layers[i+1]['name'],
        xref='x',
        yref='y',
        axref='x',
        ayref='y',
        showarrow=True,
        arrowhead=2,
        arrowsize=1,
        arrowwidth=2,
        arrowcolor='#333333'
    )

# Update layout
fig.update_layout(
    title='MCSS 5-Layer CSS Cascade',
    xaxis_title='Override Direction',
    yaxis_title='Layer Hierarchy',
    yaxis={'categoryorder': 'array', 'categoryarray': [layer['name'] for layer in layers]},
    xaxis={'showticklabels': False, 'showgrid': False, 'range': [0, 1.3]},
    bargap=0.1
)

# Update axes
fig.update_xaxes(showline=False, zeroline=False)
fig.update_yaxes(tickfont_size=12)

# Save the chart
fig.write_image('mcss_architecture.png')