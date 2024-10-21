import matplotlib.pyplot as plt


def delta(x1, y1, x2, y2):
    deltaX = x2 - x1
    deltaY = y2 - y1
    return deltaX, deltaY


if __name__ == '__main__':
    A = (3, -3)
    B = (-1, 2)
    deltaX, deltaY = delta(A[0],A[1],B[0],B[1])
    print(deltaX,deltaY)
    # Create figure and axis
    fig, ax = plt.subplots()

    # Set the limit for x and y axis
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])

    # Add grid lines to the plot
    ax.grid(True)

    # Draw the x and y axes
    ax.axhline(y=0, color='black', linewidth=1)  # X-axis
    ax.axvline(x=0, color='black', linewidth=1)  # Y-axis

    # Set labels for the axes
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

    # Add title
    ax.set_title('Cartesian Coordinate System')

    # Plot points A and B
    ax.scatter(A[0], A[1], color='red', label='Point A (3, -3)', s=100)  # Point A
    ax.scatter(B[0], B[1], color='blue', label='Point B (-1, 2)', s=100)  # Point B
    ax.plot([A[0], B[0]], [A[1], B[1]], color='green', label='Line AB', linewidth=2)
    ax.plot([A[0]+deltaX, A[0]], [A[1], A[1]], color='green', label='deltaX', linewidth=2)
    ax.plot([B[0], B[0]], [B[1]-deltaY, B[1]], color='green', label='deltay', linewidth=2)

    # Annotate points A and B
    ax.text(A[0] + 0.3, A[1], 'A (3, -3)', fontsize=12, color='red')
    ax.text(B[0] + 0.3, B[1], 'B (-1, 2)', fontsize=12, color='blue')

    # Show the legend
    ax.legend()

    # Show the plot
    plt.show()
