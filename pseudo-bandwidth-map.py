################################################################
# Author: Jeevan Prakash
# file: pseudo-bandwidth-map.py
################################################################

import math # used for calculating euclidean distance

MAX_BANDWIDTH = 1000 # arbitrary number for the bandwidth at the location of the radio tower

'''
@description - generates a matrix representing the bandwidth (Mbps) at individual x,y coordinates
the coordinate values increases in value going to the right and down the matrix
@params
    width - number of columns in the matrix
    height - number of rows in the matrix
    tower_x - x-coordinate of radio tower in the pseudo bandwidth map
    tower_y - y-coordinate of radio tower in the pseudo bandwidth map
@ return 2D matrix populated with positive numerical values representing bandwidth in Mbps
or empty matrix representing invalid tower position
'''
def generate_pseudo_bandwidth_map(width,height,tower_x,tower_y):
    # edge cases
    if tower_x < 0 or tower_x >= width or tower_y < 0 or tower_y >= height:
        return [[]]
    
    if width == 1 and height == 1:
        return [[MAX_BANDWIDTH]]

    # initialize the matrix with 0s with the correct width and height
    mat = initialize_matrix(width,height)

    # start at the top left
    x = 0
    y = 0

    for x in range(len(mat)):
        for y in range(len(mat[x])):
            mat[x][y] = calculate_bandwidth(x,y,tower_x,tower_y) # calculate the bandwidth

    return mat  
    
'''
@description - returns a float representing the bandwidth at the current x and y coordinate in relation to the tower
@params
    curr_x - current x position
    curr_y - current y position
    tower_x - x-coordinate of radio tower in the pseudo bandwidth map
    tower_y - y-coordinate of radio tower in the pseudo bandwidth map
@ return a float representing the bandwidth at the current x,y given the x,y of the radio tower
'''    
def calculate_bandwidth(curr_x,curr_y,tower_x,tower_y):
    point1 = [curr_x,curr_y]
    point2 = [tower_x,tower_y]

    # calculate the distance using the euclidean distance formula
    # then, use arbitrary math to come up with a bandwidth based on the distance
    return MAX_BANDWIDTH - math.dist(point1,point2)*100 

'''
@description - returns a matrix of 0s with the given width and height, representing an empty bandwidth map
@params
    width - width of the matrix
    height - height of the matrix
@ return a matrix of size width,height populated with 0s
'''
def initialize_matrix(width,height):
    mat = []

    for _ in range(width):
        mat.append([])

    for i in range(len(mat)):
        for _ in range(height):
            mat[i].append(0)

    return mat

'''
@description - to string method for matrices with floats (to the 2nd decimal value)
@params
    mat - matrix to be printed
@ return none
'''
def map_to_string(mat):
    for x in range(len(mat)):
        s = ""
        for y in range(len(mat[x])):
            s = s+ " " + "{:.2f}".format(mat[x][y])
        print(s)

map_to_string(generate_pseudo_bandwidth_map(10,10,2,3))