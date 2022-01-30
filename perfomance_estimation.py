"""Test CUDA perfomance and features using python wrapper - NUMBA"""
'''Test for profiling'''
#  Test from command line:
# 
#  time python ./numba_perfomance_estimate/perfomance_estimation.py 
# 
# Using profile command with summary time report
# python -m cProfile -o ./numba_perfomance_estimate/profile.txt ./numba_perfomance_estimate/perfomance_estimation.py


from numba import cuda
import time

# TODO image CUDA loader

@cuda.jit
def gpu_print(N):
    idxWithinGrid = cuda.threadIdx.x + cuda.blockIdx.x * cuda.blockDim.x
    gridStride = cuda.gridDim.x * cuda.blockDim.x
    # Начнем с idxWithinGrid
    # Каждый шаг принимает общее количество нитей сетки как количество шагов
    for i in range(idxWithinGrid, N, gridStride):
        print(i)


def main():

    gpu_print[2, 4](32)
    cuda.synchronize()


if __name__ == "__main__":

    
    start = time.time()
    print("Time of main() on working...")
    # time.sleep(0.9)
    main()
    end = time.time()
    print("Time consumed in main(): ", end - start)
