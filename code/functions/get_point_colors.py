def get_point_colors(aminocode):
    """
    Assign color codes to each amino acid.
    """
    colors = []

    for code in aminocode:
        if code == 'H':
            color = 'red'
        if code == 'P':
            color = 'blue'
        if code == 'C':
            color = 'yellow'
        colors.append(color)

    return colors
