import utilities

def rotate_90_degrees(image_array, direction = 1):
    '''
    This function is to find the 90-degree rotated version of the image array(either grayscale or RGB).
    1 for clock_wise, -1 for anticlockwise
    (list, int)-->list
    ex:
    >> rotate_90_degrees([[1, 1, 0], [0, 0, 0], [0, 0, 1]], 1)
    output: [[0, 0, 1], [0, 0, 1], [1, 0, 0]]
    >> rotate_90_degrees([[1, 1, 0], [0, 0, 0], [0, 0, 1]], -1)
    output: [[0, 0, 1], [1, 0, 0], [1, 0, 0]]
    '''
    if direction == 1:
        output_array = [[] for i in range(len(image_array))]
        for i in range(len(image_array) - 1, -1, -1):
            a = image_array[i]

            for j in range(len(image_array)):

                output_array[j].append(a[j])

    elif direction == -1:
        output_array = [[] for i in range(len(image_array))]
        for i in range(len(image_array)):
            a = image_array[i]

            for j in range(len(image_array)):

                output_array[j].append(a[len(image_array) - 1 - j])


    return output_array

# print(rotate_90_degrees([[1, 1, 0], [0, 0, 0], [0, 0, 1]], -1))

# print(rotate_90_degrees([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1))




def flip_image(image_array, axis = 0):
    '''
    This function is to flip the image(represented by a list) along x, y, or x-y axis
    (list, int)->list
    ex:
    >>flip_image([[1, 2],[3, 4]], 1)
    output: [[3, 4], [1, 2]]
    >>flip_image([[1, 2],[3, 4]], 0)
    [[2, 1], [4, 3]]
    >>flip_image([[1, 2],[3, 4]], -1)
    [[4, 2], [3, 1]]
    axis = -1 (along x = y), 0 along y, 1 along x
    '''
    output_array = []
    if axis == 1:
        for i in range(len(image_array)):

            output_array.append(image_array[len(image_array) - 1 - i])


    elif axis == 0:

        output_array = []
        for i in range(len(image_array)):
            a = image_array[i]
            b = []
            for j in range(len(a)):
                b.append(a[len(a) - 1 - j])

            output_array.append(b)


    elif axis == -1:
        output_array = [[0 for m in range(len(image_array))] for n in range(len(image_array))]
        for i in range(len(image_array)):
            for j in range(len(image_array)):
                output_array[i][j] = image_array[len(image_array) - 1 - j][len(image_array) - 1 - i]


    return output_array

# print(flip_image([[1, 2], [3, 4]], -1))
# print(flip_image([[11, 22, 33, 44], [1, 2, 3, 4], [5, 6, 7, 8], [55, 66, 77, 88]], -1))



def invert_grayscale(image_array):
    '''
    This function is to invert the grayscale of an image (represented by a list)
    (list)-->list
    ex. x --> 255 - x
    > [[255, 10, 0],[200, 10, 5],[143, 0, 1]] --> [[0, 245, 255],[55, 235, 250],[112, 255, 254]]
    '''
    output_array = [[0 for m in range(len(image_array))] for n in range(len(image_array))]
    for i in range(len(image_array)):
        a = image_array[i]
        for j in range(len(a)):
            output_array[i][j] = 255 - image_array[i][j]


    return output_array

# print(invert_grayscale([[255, 10, 0], [200, 20, 5], [143, 0, 1]]))





def crop(image_array, direction, n_pixels):
    '''
    crop the image (represented by the 2D list) by n pixels in the given direction
    (list, str, int) -->list
    the string could be ‘left’, ‘right’, ‘up’, or ‘down’
    ex.
    >> crop([[1, 1, 0], [0, 0, 0], [0, 0, 1]], left, 1)
    outputs: [[0, 0], [0, 1], [0, 1]]
    '''
    if direction == "left":
        output_array = [[0 for m in range(len(image_array))] for n in range(len(image_array))]
        for i in range(len(image_array)):
            a = image_array[i]
            output_array[i] = a[n_pixels:]

    elif direction == "right":
        output_array = [[0 for m in range(len(image_array))] for n in range(len(image_array))]
        for i in range(len(image_array)):
            a = image_array[i]
            output_array[i] = a[:len(image_array) - n_pixels]

    elif direction == "up":
        output_array = image_array[n_pixels:]

    elif direction == "down":
        output_array = image_array[:len(image_array) - n_pixels]


    return output_array


# print(crop([[1,0,0], [0, 0, 1], [0, 0, 1]], "down", 1))






def rgb_to_grayscale(rgb_image_array):
    '''
    This function is to convert rgb (3D list) to grayscale using the formula gray = 0.2989 ∗ r + 0.5870 ∗ g + 0.1140 ∗ b
    (list) -->list
    ex. rgb_to_grayscale([ [ [10, 10, 10], [1, 2, 3]], [[25, 30, 60],[7, 5, 12]]])
    output: [9.998999999999999, 1.8149], [31.9225, 6.3953]]
    '''
    output_array = [[0 for m in range(len(rgb_image_array))] for n in range(len(rgb_image_array))]
    for i in range(len(rgb_image_array)):
        a = rgb_image_array[i]
        for j in range(len(a)):
            output_array[i][j] = a[j][0] * 0.2989 + a[j][1] * 0.5870 + a[j][2] * 0.1140


    return output_array

# print(rgb_to_grayscale([[[10, 10, 10], [1, 2, 3]], [[25, 30, 60], [7, 5, 12]]]))




def invert_rgb(image_array):
    '''
    This function is to invert the rgb image using r -> 255 - r; g -> 255 - g; b -> 255 - b
    (list) -->list
    ex.
    >>invert_rgb([ [ [10, 10, 10], [1, 2, 3]], [[25, 30, 60], [7, 5, 12]]])
    output: [[[245, 245, 245], [254, 253, 252]], [[230, 225, 195], [248, 250, 243]]]
    '''
    output_array =[[[0 for m in range(3)] for n in range(len(image_array))] for p in range(len(image_array))]
    for i in range(len(image_array)):
        a = image_array[i]
        for j in range(len(a)):
            output_array[i][j][0] = 255 - image_array[i][j][0]
            output_array[i][j][1] = 255 - image_array[i][j][1]
            output_array[i][j][2] = 255 - image_array[i][j][2]

    return output_array


# print(invert_rgb([ [ [10, 10, 10], [1, 2, 3]], [[25, 30, 60], [7, 5, 12]]]))




def histogram_equalization(image_array):
    '''
    This function is to implement histogram equalization on the grayscale image.
    (list)-->list
    ex.
    >>(histogram_equalization([[10, 10, 10],
                              [1, 2, 3],
                              [25, 30, 60],
                              [7, 5, 12]])
    output: [[170.0, 170.0, 170.0], [21.25, 42.5, 63.75], [212.5, 233.75000000000003, 255.0], [106.24999999999999, 85.0, 191.25]]
    '''
    a = len(image_array)
    b = len(image_array[0])
    s = a * b
    flat = []
    for i in image_array:
        for j in i:
            flat.append(j)
    p = set(flat)
    q = list(p)
    k = sorted(q)
    ori = []
    for i in range(256):
        ori.append(i)
    d = dict()
    sm = 0
    for i in k:
        while ori[0] != i:
            d[ori.pop(0)] = sm * 255
        else:
            sm += flat.count(i) / s
            d[ori.pop(0)] = sm * 255

    f = image_array[:]
    for i in range(a):
        for j in range(b):
            f[i][j] = d[f[i][j]]

    return f

