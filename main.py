from parse_input import parseInput
from starcubing import starCubing
from generate_tree import StarReduction
import time
from pptree import *
import sys

start_time = time.time()

count_table, input_table = parseInput(sys.argv[0])

starReduce = StarReduction(sys.argv[1], input_table, count_table)

starReduce.createStarTable()
tree = starReduce.createStarTree()

# print(tree.value
# print_tree(tree)
# print(starReduce.compressed_table)

tree1 = starCubing(tree,tree,sys.argv[1])

# print(tree.value)

print(time.time() - start_time)

# print_tree(tree)
