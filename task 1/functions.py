def prod_non_zero_diag(x):
    p = 1
    for i in range(len(x)):
        if i < len(x[i]):
            if x[i][i] != 0:
                p *= x[i][i]
    return p

def are_multisets_equal(x, y):
    x.sort()
    y.sort()
    return x == y


def max_after_zero(x):
    mx = 0
    for i in range(len(x) - 1): 
        if x[i] == 0:
            mx = max(mx, x[i + 1])
    return mx
    """Find max element after zero in array.

    input:
    x -- 1-d numpy array
    output:
    maximum element after zero -- integer number

    Not vectorized implementation.
    """

    pass


def convert_image(img, coefs):
    """Sum up image channels with weights from coefs array

    input:
    img -- 3-d numpy array (H x W x 3)
    coefs -- 1-d numpy array (length 3)
    output:
    img -- 2-d numpy array

    Not vectorized implementation.
    """

    pass


def run_length_encoding(x):
    values = [x[0]]
    counts = [1]
    for i in x:
        if values[-1] == i:
            counts[-1] += 1
        else:
            values.append(i)
            counts.append(1)
    return values, counts
    pass


def pairwise_distance(x, y):
    """Return pairwise object distance.

    input:
    x, y -- 2d numpy arrays
    output:
    distance array -- 2d numpy array

    Not vectorized implementation.
    """

    pass
