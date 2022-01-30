"""Profile test file"""
import cProfile
import re
from timeit import timeit
from perfomance_estimation import *
# test cmd
# cProfile.run('re.compile("foo|bar")')

# test main access
# main()

# test perfomance of main
cProfile.run("main()")


