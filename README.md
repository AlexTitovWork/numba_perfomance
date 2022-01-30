# Project to test the performance of NUMBA and JIT-compilation.<br>
### numba_perfomance <br>
### @created by Alex Titov<br>
## NUMBA is good calculation wrapper. <br>

## Info from NUMDA site.<br>
## NUMBA like np.array and don't like pandas.<br>
## Test JIT numba compillation and cashe second start.<br>
## NUMBA is good calculation wrapper. The efficiency of DevOps or loader is not surprising!<br>
"""
What is nopython mode?<br>

The Numba @jit decorator fundamentally operates in two compilation modes, nopython mode and object mode. <br>
In the go_fast example above, nopython=True is set in the @jit decorator, <br>
this is instructing Numba to operate in nopython mode. <br>
The behaviour of the nopython compilation mode is to essentially compile <br>
the decorated function so that it will run entirely without the involvement of the Python interpreter.<br> 
This is the recommended and best-practice way to use the Numba jit decorator as it leads to the best performance.<br>
Should the compilation in nopython mode fail, Numba can compile using object mode,<br>
this is a fall back mode for the @jit decorator if nopython=True is not set (as seen in the use_pandas example above).<br>
In this mode Numba will identify loops that it can compile and compile those into functions that run in machine code,<br>
and it will run the rest of the code in the interpreter. For best performance avoid using this mode!<br>
"""
USAGE: <br>
python compare_perfomance_py_vs_numba.py<br>

RESULT: <br>
Image loading time (with compilation) = 2.229041337966919<br>

Elapsed (with compilation) = 1.7185752391815186<br>
Elapsed (after compilation) = 4.100799560546875e-05<br>
Elapsed (after compilation and caching) = 2.86102294921875e-05 <br>

Diagonal:<br>
[103. 104. 104. 104. 104.]<br>
Invert matrix:<br>
[[-0.02483749 -0.00989922  0.02612057  0.09516573  0.00248375]<br>
 [ 0.          0.03125    -0.03125     0.         -0.        ]<br>
 [ 0.00602527 -0.00012553  0.02584002 -0.02578144 -0.00060253]<br>
 [ 0.01867832 -0.00038913 -0.01989593  0.02007753 -0.00186783]<br>
 [-0.00046696 -0.00780277  0.0083099  -0.02550194  0.0250467 ]]<br>
Eigen value:<br>
[ 5.20203783e+02 -2.84054242e+00  1.71715708e+00 -8.03980207e-02
  4.62287827e-14]<br>
