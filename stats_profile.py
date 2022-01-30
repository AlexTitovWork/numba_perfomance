'''Statistic reader'''
import pstats
from termcolor import colored
# from pstats import SortKey #The issue was Python 3.6 vs Python 3.7.
p = pstats.Stats('numba_perfomance_estimate/profile.txt')
# Print all by name sort
# p.strip_dirs().sort_stats(-1).print_stats() 

# Print 10 lines by cumulative sort
# p.sort_stats('cumulative').print_stats(10)

print(colored("\n\nTottime is the total time spent on the function alone.", 'green'))
print(colored("Sorted by tottime.", 'green'))

# Print 10 lines by tottime sort and strip long dirs path
p.strip_dirs().sort_stats('tottime').print_stats(10)


''' You're calling marshal.load() (a built-in function) in several places in file.
 If those 558 loads were all different files, then there's not much you can do about this.
  If it's loading the same file multiple times, you need to retain the 
  data in memory rather than reloading it. '''


print(colored("\n\nCumtime is the total time spent in the function plus all functions that this function has called.", 'green'))
print(colored("Sorted by cumtime.", 'green'))

# Print 10 lines by cumtime sort and strip long dirs path
p.strip_dirs().sort_stats('cumtime').print_stats(10)

# p.print_callers(.5, 'init')
# p.sort_stats(SortKey.NAME)
# p.print_stats()