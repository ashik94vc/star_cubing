from parse_input import parseInput
from starcubing import starCubing
from generate_tree import StarReduction
import time
from pptree import *

start_time = time.time()

count_table, input_table = parseInput('../dataset/kddcup.csv')

starReduce = StarReduction(5000, input_table, count_table)

starReduce.createStarTable()
tree = starReduce.createStarTree()

# print(tree.value
# print_tree(tree)
# print(starReduce.compressed_table)

tree1 = starCubing(tree,tree,5000)

# print(tree.value)

print(time.time() - start_time)

# print_tree(tree)
