from numba import jit
import numpy as np
import time
from PIL import Image
from numpy import linalg as LA
import matplotlib.pyplot as plt
# @created by Alex Titov

# NUMBA like np.array and don't like pandas
# Test JIT numba compillation and cashe second start.
# NUMBA is good calculation wrapper. The efficiency of DevOps or loader is not surprising!
"""
What is nopython mode?

The Numba @jit decorator fundamentally operates in two compilation modes, nopython mode and object mode. 
In the go_fast example above, nopython=True is set in the @jit decorator, 
this is instructing Numba to operate in nopython mode. 
The behaviour of the nopython compilation mode is to essentially compile 
the decorated function so that it will run entirely without the involvement of the Python interpreter. 
This is the recommended and best-practice way to use the Numba jit decorator as it leads to the best performance.
Should the compilation in nopython mode fail, Numba can compile using object mode,
this is a fall back mode for the @jit decorator if nopython=True is not set (as seen in the use_pandas example above).
In this mode Numba will identify loops that it can compile and compile those into functions that run in machine code,
and it will run the rest of the code in the interpreter. For best performance avoid using this mode!
"""

@jit(nopython=True)
def do_it_fast(a, at):  # Function is compiled and runs in machine code
    trace = 0.0
    # Some processing
    a = a.transpose()
    diag = np.diag(a)
    # Use part of images
    inverted = np.linalg.inv(at)
    # Need not singular matrix
    eigen = np.linalg.eigvals(a)
    return diag, inverted, eigen

# //--------------------------------------------------------------------

def test():
    start = time.time()

    image = Image.open("./style2.png")
    # plt.imshow(image, cmap='hot')

    # Size of the image in pixels (size of original image)
    width, height = image.size

    # Setting the points for cropped image
    left = 100     # left line
    top = 100      # top line
    right = 105    # 5 x 5 matrix
    bottom = 105        
    # Cropped image of above dimension
    # (It will not change original image)
    im1 = image.crop((left, top, right, bottom))
    
    # Shows the image in image viewer
    # im1.show()

    image_array = np.array(im1)
    end = time.time()
    print("Image loading time (with compilation) = %s" % (end - start))
    
    print(image_array.shape)
    image_array = np.delete(image_array, 1, 2)
    image_array = np.delete(image_array, 1, 2)
    image_array = np.delete(image_array, 1, 2)
    image_array = image_array.squeeze()

    print(image_array.shape)
    # x = image_array.reshape(5, 5)
    print("image_array")
    # print(image_array[0][0])

    # for Eigen decomposiotion    
    # x = np.array([[1, 2, 34 ,44 ,4], [9, 35, 34, 1, 0], [9, 3, 34, 1, 0], [9, 3, 3, 11, 0], [9, 13, 3, 12, 40]], dtype=np.uint8)
    xt = np.array([[1, 2, 34 ,44 ,4], [9, 35, 34, 1, 0], [9, 3, 34, 1, 0], [9, 3, 3, 11, 0], [9, 13, 3, 12, 40]], dtype=np.float64)
    # For some processing.
    x = image_array
    # Format and shape check and convert for processing
    print(x.dtype)
    print(x.shape)
    x = x.astype('float64')
    print(x.dtype)
    print(x.shape)

   # compilation time is included in the execution time! slow execution.
    start = time.time()

    do_it_fast(x, xt)
    end = time.time()
    print("\nElapsed (with compilation) = %s" % (end - start))

    #the function is compiled, re-time it, faster execution.
    start = time.time()
    diag, invert, eigen = do_it_fast(x, xt)
    end = time.time()
    print("Elapsed (after compilation) = %s" % (end - start))

    # the function is compiled, re-time it and executing from cache, much faster execution.
    start = time.time()
    diag, invert, eigen = do_it_fast(x, xt)
    end = time.time()
    print("Elapsed (after compilation and caching) = %s \n" % (end - start))

    print("Diagonal:")
    print(diag)
    print("Invert matrix:")
    print(invert)
    print("Eigen value:")
    print(eigen)

test()
