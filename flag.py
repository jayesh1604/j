import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
def draw_flag():
    fig, ax = plt.subplots() # Create figure and axes
    # Draw tricolor bands
    colors = ['#138808', '#ffffff', '#FF6103']
    for i, color in enumerate(colors):
        rect = patches.Rectangle((0, 2*i+1), width=9, height=2, facecolor=color, edgecolor='grey')
        ax.add_patch(rect)
    # Draw Ashoka Chakra circle
    chakra_radius = 0.8
    ax.plot(4.5, 4, marker='o', markerfacecolor='#000080', markersize=9.5)
    chakra = patches.Circle((4.5, 4), chakra_radius, color='#000080', fill=False, linewidth=7)
    ax.add_artist(chakra)

    # Draw 24 spokes in Ashoka Chakra
    for i in range(24):
        angle1 = np.pi * i / 12 - np.pi / 48
        angle2 = np.pi * i / 12 + np.pi / 48
        spoke = patches.Polygon([[4.5, 4], 
                                 [4.5 + chakra_radius / 2 * np.cos(angle1), 
                                  4 + chakra_radius / 2 * np.sin(angle1)], 
                                 [4.5 + chakra_radius * np.cos(np.pi * i / 12), 
                                  4 + chakra_radius * np.sin(np.pi * i / 12)], 
                                 [4.5 + chakra_radius / 2 * np.cos(angle2), 
                                  4 + chakra_radius / 2 * np.sin(angle2)]], 
                                fill=True, closed=True, color='#000080')
        ax.add_patch(spoke)
    # Set equal axis and display the plot
    ax.axis('equal')
    plt.show()
# Call the function to draw the tricolor flag
draw_flag()