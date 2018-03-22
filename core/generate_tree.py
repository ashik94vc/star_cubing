from tree import Tree
from pptree import *
class StarReduction(object):

    def __init__(self, min_sup, input_table, count_table):
        self.min_sup = min_sup
        self.input_table = input_table
        self.count_table = count_table
        self.star_table = []

    def add_to_star_table(self, column_index, value):
        if column_index < len(self.star_table):
            self.star_table[column_index][value] = '*'
        else:
            temp = column_index - len(self.star_table) + 1
            while temp > 0:
                self.star_table.append(dict())
                temp -= 1
            self.star_table[column_index][value] = '*'

    def createStarTable(self):
        base_table = self.input_table[:]
        row_dict = {}
        for row in base_table:
            self.row_len = len(row)
            for column_index in range(len(row)):
                if self.count_table[column_index][row[column_index]] < self.min_sup:
                    self.add_to_star_table(column_index, row[column_index])
                    row[column_index] = '*'
        self.base_table = base_table
        for row in base_table:
            trow = tuple(row)
            if trow in row_dict:
                row_dict[trow] += 1
            else:
                row_dict[trow] = 1
        self.compressed_table = row_dict
        return row_dict

    def createStarTree(self):
        root_value = sum(self.compressed_table.values())
        tree = Tree(root_value)
        for row,value in self.compressed_table.items():
            sub_tree = tree
            for item in row:
                sub_tree = sub_tree.add_to_node(item, value)

        self.star_tree =  tree
        return tree

    def createCuboidTree(self):
        root_value = 0
        tree = Tree(root_value)

        for row in self.input_table:
            sub_tree = tree
            for item in row:
                sub_tree = sub_tree.add_to_node(item,0)
