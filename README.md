# numba_perfomance <br>
NUMBA is good calculation wrapper. <br>
# @created by Alex Titov<br>

# Info from NUMDA site.<br>
# NUMBA like np.array and don't like pandas.<br>
# Test JIT numba compillation and cashe second start.<br>
# NUMBA is good calculation wrapper. The efficiency of DevOps or loader is not surprising!<br>
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

