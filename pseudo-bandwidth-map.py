'''
@description - generates a matrix representing the bandwidth (Mbps) at individual x,y coordinates
the coordinate values increases in value going to the right and down the matrix
@params
    width - number of columns in the matrix
    height - number of rows in the matrix
    tower_x - x-coordinate of radio tower in the pseudo bandwidth map
    tower_y - y-coordinate of radio tower in the pseudo bandwidth map
'''
def generate_pseudo_bandwidth_map(width,height,tower_x,tower_y):

    return [[]]