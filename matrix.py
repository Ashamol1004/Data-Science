import numpy as np

x = np.array([[1,2], [3,4]])
print("Original x: \n%s " %x)    # Prints "[[1 2]
                                 #         [3 4]]"
print("\nTranspose of x: \n%s" %x.T)  # Prints "[[1 3]
                                      #          [2 4]]"
