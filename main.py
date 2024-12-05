# import matplotlib.pyplot as plt
#
# # Function to map runs of bits to DNA nucleotides
# def run_length_to_dna(run_length):
#     mapping = {1: 'C', 2: 'T', 3: 'A', 4: 'G'}
#     return mapping.get(run_length, '')
#
# # Function to encode a binary grid into a DNA sequence
# def encode_grid_to_dna(grid):
#     dna_sequence = ""
#     previous_bit = None
#     run_length = 0
#     dna_segments = []  # To store runs for visualization
#
#     for row in grid:
#         for bit in row:
#             if bit == previous_bit:
#                 run_length += 1
#             else:
#                 if previous_bit is not None:  # Process completed run
#                     nucleotide = run_length_to_dna(run_length)
#                     dna_sequence += nucleotide
#                     dna_segments.append((previous_bit, run_length, nucleotide))
#                 previous_bit = bit
#                 run_length = 1
#     # Add the final run
#     nucleotide = run_length_to_dna(run_length)
#     dna_sequence += nucleotide
#     dna_segments.append((previous_bit, run_length, nucleotide))
#
#     return dna_sequence, dna_segments
#
# # Visualization function
# def visualize_encoding(grid, dna_segments):
#     fig, ax = plt.subplots(1, 2, figsize=(12, 6))
#
#     # Plot the binary grid
#     ax[0].imshow(grid, cmap='binary', interpolation='nearest')
#     ax[0].set_title('Binary Grid')
#     ax[0].set_xticks(range(len(grid[0])))
#     ax[0].set_yticks(range(len(grid)))
#     ax[0].grid(color='gray', linestyle='--', linewidth=0.5)
#
#     # Create a graphical DNA sequence representation
#     dna_colors = {'C': 'blue', 'T': 'orange', 'A': 'green', 'G': 'red'}
#     x_positions = []  # To hold the x-coordinate for each nucleotide
#     y_positions = []  # To hold the y-coordinate (fixed at 0 for all)
#     colors = []       # To hold the color for each nucleotide
#     annotations = []  # To store the DNA nucleotides for annotation
#
#     # Accumulate DNA segment data
#     current_position = 0  # Tracks position along the x-axis
#     for bit, run_length, nucleotide in dna_segments:
#         # Append a single nucleotide corresponding to the run
#         x_positions.append(current_position)
#         y_positions.append(0)
#         colors.append(dna_colors[nucleotide])
#         annotations.append(nucleotide)
#         current_position += 1  # Move to the next position
#
#     # Plot the DNA sequence as colored circles
#     ax[1].scatter(x_positions, y_positions, color=colors, s=1000)
#
#     # Annotate DNA bases
#     for i, nucleotide in enumerate(annotations):
#         ax[1].text(
#             x_positions[i], y_positions[i], nucleotide,
#             color='black', ha='center', va='center', fontsize=12,
#             bbox=dict(facecolor='white', edgecolor='gray', boxstyle='circle')
#         )
#
#     # DNA plot settings
#     ax[1].set_title('Encoded DNA Sequence')
#     ax[1].set_xlim(-1, len(annotations))  # Adjust axis limits to fit the sequence
#     ax[1].set_ylim(-1, 1)
#     ax[1].axis('off')
#
#     plt.tight_layout()
#     plt.show()
#
#
# # Example binary grid (5x7)
# letter_grid = [
#     [1, 0, 1, 0, 1],
#     [0, 1, 1, 1, 0],
#     [0, 0, 1, 0, 0],
#     [0, 0, 1, 0, 0],
#     [0, 0, 1, 0, 0],
#     [0, 0, 1, 0, 0],
#     [0, 0, 1, 0, 0],
# ]
#
# # Encode the grid to DNA
# dna_sequence, dna_segments = encode_grid_to_dna(letter_grid)
#
# # Call visualization
# visualize_encoding(letter_grid, dna_segments)
#
# # Print DNA sequence
# print("Encoded DNA Sequence:", dna_sequence)

import matplotlib.pyplot as plt

# Function to map runs of bits to DNA nucleotides
def run_length_to_dna(run_length):
    mapping = {1: 'C', 2: 'T', 3: 'A', 4: 'G'}
    return mapping.get(run_length, '')

# Function to encode a binary grid into a DNA sequence
def encode_grid_to_dna(grid):
    dna_sequence = ""
    previous_bit = None
    run_length = 0
    dna_segments = []  # To store runs for visualization

    for row in grid:
        for bit in row:
            if bit == previous_bit:
                run_length += 1
            else:
                if previous_bit is not None:  # Process completed run
                    nucleotide = run_length_to_dna(run_length)
                    dna_sequence += nucleotide
                    dna_segments.append((previous_bit, run_length, nucleotide))
                previous_bit = bit
                run_length = 1
    # Add the final run
    nucleotide = run_length_to_dna(run_length)
    dna_sequence += nucleotide
    dna_segments.append((previous_bit, run_length, nucleotide))

    return dna_sequence, dna_segments

# Visualization function
def visualize_encoding(grid, dna_segments):
    fig, ax = plt.subplots(1, 2, figsize=(12, 6))

    # Plot the binary grid
    ax[0].imshow(grid, cmap='binary', interpolation='nearest')
    ax[0].set_title('Binary Grid')
    ax[0].set_xticks(range(len(grid[0])))
    ax[0].set_yticks(range(len(grid)))
    ax[0].grid(color='gray', linestyle='--', linewidth=0.5)

    # Create a graphical DNA sequence representation
    dna_colors = {'C': 'blue', 'T': 'orange', 'A': 'green', 'G': 'red'}
    x_positions = []  # To hold the x-coordinate for each nucleotide
    y_positions = []  # To hold the y-coordinate (fixed at 0 for all)
    colors = []       # To hold the color for each nucleotide
    annotations = []  # To store the DNA nucleotides for annotation

    # Accumulate DNA segment data
    current_position = 0  # Tracks position along the x-axis
    for bit, run_length, nucleotide in dna_segments:
        # Append a single nucleotide corresponding to the run
        x_positions.append(current_position)
        y_positions.append(0)
        colors.append(dna_colors[nucleotide])
        annotations.append(nucleotide)
        current_position += 1  # Move to the next position

    # Plot the DNA sequence as colored circles
    ax[1].scatter(x_positions, y_positions, color=colors, s=1000)

    # Annotate DNA bases
    for i, nucleotide in enumerate(annotations):
        ax[1].text(
            x_positions[i], y_positions[i], nucleotide,
            color='black', ha='center', va='center', fontsize=12,
            bbox=dict(facecolor='white', edgecolor='gray', boxstyle='circle')
        )

    # Add legend to the DNA panel
    legend_labels = [
        ('C', 'blue', 'Cytosine'),
        ('T', 'orange', 'Thymine'),
        ('A', 'green', 'Adenine'),
        ('G', 'red', 'Guanine')
    ]
    legend_handles = [
        plt.Line2D([0], [0], marker='o', color=color, markersize=10, label=f'{label} - {full_name}')
        for label, color, full_name in legend_labels
    ]
    ax[1].legend(handles=legend_handles, loc='upper left', title='DNA Nucleotide Key')

    # DNA plot settings
    ax[1].set_title('Encoded DNA Sequence')
    ax[1].set_xlim(-1, len(annotations))  # Adjust axis limits to fit the sequence
    ax[1].set_ylim(-1, 1)
    ax[1].axis('off')

    plt.tight_layout()
    plt.show()

# Example binary grid (5x7)
letter_grid = [
    [1, 0, 1, 0, 1],
    [0, 1, 1, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
]

# Encode the grid to DNA
dna_sequence, dna_segments = encode_grid_to_dna(letter_grid)

# Call visualization
visualize_encoding(letter_grid, dna_segments)

# Print DNA sequence
print("Encoded DNA Sequence:", dna_sequence)
