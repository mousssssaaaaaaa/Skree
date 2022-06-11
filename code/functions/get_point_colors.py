def get_point_colors(aminocode):
    colors = []
    
    for code in aminocode:
        if code == 'H':
            color = 'red'
        if code == 'P':
            color = 'blue'
        colors.append(color)

    return colors