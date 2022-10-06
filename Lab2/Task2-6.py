class Tree:

    def __init__(self, value=None):
        self.left = None
        self.right = None
        self._value = value

    def insert(self, value):
        if not (isinstance(value[0], int) or isinstance(value[1], (float, int))) or (value[1] < 0 or value[0] < 0):
            raise ValueError('Invalid input')
        if self._value is None:
            self._value = value
        else:
            if value[0] < self._value[0]:
                if self.left is None:
                    self.left = Tree(value)
                else:
                    self.left.insert(value)
            elif value[0] > self._value[0]:
                if self.right is None:
                    self.right = Tree(value)
                else:
                    self.right.insert(value)

    def search(self, code):
        if not (isinstance(code, int) or code < 0):
            raise ValueError('Invalid input')
        if code == self._value[0]:
            return self._value
        elif code < self._value[0]:
            return self.left.search(code) if self.left is not None else False
        elif code > self._value[0]:
            return self.right.search(code) if self.right is not None else False

    def get_cost(self, code, quantity):
        try:
            return quantity * self.search(code)[1]
        except TypeError:
            print('product doesnt exist')

    @property
    def get_value(self):
        return self._value


def tree_size(tree):
    return 0 if tree is None else tree_size(tree.left) + 1 + tree_size(tree.right)


def get_products_cost(tree):
    # Calculating the costs of products
    total = 0
    max_size = tree_size(tree)
    size = int(input(f'Number of products (max = {max_size}): '))
    if not (isinstance(size, int) or 0 < size <= max_size):
        raise ValueError('Invalid input')
    for i in range(size):
        a = tuple(map(int, input('Code:Quantity: ').split(':')))
        total += tree.get_cost(a[0], a[1])
    return total


def print_tree(root):
    if root:
        print_tree(root.left)
        print_tree(root.right)
        print(root._value)


tree = Tree()
tree.insert((7, 20.6))
tree.insert((1, 10))
tree.insert((2, 54.757))
tree.insert((8, 2.3))
tree.insert((9, 98.521))
print(tree.search(2))
print(f'Cost is: {(tree.get_cost(2, 2))}')
print_tree(tree)
print(get_products_cost(tree))
