from parse_input import parseInput
from starcubing import starCubing
from generate_tree import StarReduction

count_table, input_table = parseInput('../dataset/automobile.csv')

starReduce = StarReduction(10, input_table, count_table)

starReduce.createStarTable()
tree = starReduce.createStarTree()

print(tree.value)

tree = starCubing(tree,tree,10)
