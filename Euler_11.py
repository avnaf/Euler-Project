import numpy as np

 # copied the text into a .txt file
with open(r'C:\Users\...\Desktop\grid.txt') as f:
    arr = np.loadtxt(f, dtype = np.int)

num_of_elements_in_product = 4
max_product_so_far = 0
dimensions = arr[0].size

for i in range(dimensions):
    for j in range(dimensions):
               
        tmp_row_product        = 1
        tmp_col_product        = 1
        tmp_right_diag_product = 1
        tmp_left_diag_product  = 1
        
        for k in range(num_of_elements_in_product):
            if j <= dimensions - num_of_elements_in_product:
                tmp_row_product        *= arr[i]    [j + k]
            if i <= dimensions - num_of_elements_in_product:    
                tmp_col_product        *= arr[i + k][j]
            if j <= dimensions - num_of_elements_in_product and i <= dimensions - num_of_elements_in_product:    
                tmp_right_diag_product *= arr[i + k][j + k]
            if j <= dimensions - num_of_elements_in_product and i <= dimensions - num_of_elements_in_product:    
                tmp_left_diag_product *= arr[dimensions - 1 - i - k][j + k]    
                
        tmp_max = max(tmp_row_product, tmp_col_product, tmp_right_diag_product, tmp_left_diag_product)
        if tmp_max > max_product_so_far:
            max_product_so_far = tmp_max
            
print max_product_so_far
        