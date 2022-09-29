import numpy as np


class Spiral(object):
    """
    Implementation of a Spiral iterator to solve problem 28 and 58.
    """
    def __init__(self, center=(0, 0), ratio=0, rotation=1):
        self._center = center
        self._ratio = ratio
        self.i = center[0]
        self.j = center[1]
        self.counter = 1
        self.rotation = rotation

    def __iter__(self):
        return self

    def __next__(self):
        current_ratio = int(np.ceil((np.sqrt(self.counter) - 1) / 2))
        next_ratio = int(np.ceil((np.sqrt(self.counter + 1) - 1) / 2))
        if current_ratio > self._ratio:
            raise StopIteration
        current_i = self.i
        current_j = self.j
        next_i = self.i
        next_j = self.j
        if current_ratio != next_ratio:
            next_j += 1
        else:
            if self.rotation == 1:  # clockwise
                # identify corner
                if abs(self.i - self._center[1]) == abs(self.j - self._center[0]):
                    if self.i > self._center[0] and self.j > self._center[1]:  # right-bottom corner
                        next_j -= 1
                    elif self.i < self._center[0] and self.j > self._center[1]:  # right-top corner
                        next_i += 1
                    elif self.i < self._center[0] and self.j < self._center[1]:  # left-top corner
                        next_j += 1
                    elif self.i > self._center[0] and self.j < self._center[1]:  # left-bottom corner
                        next_i -= 1
                # identify current side of the square
                else:
                    if self.i == self._center[0] + current_ratio:  # bottom side
                        next_j -= 1
                    elif self.i == self._center[0] - current_ratio:  # top side
                        next_j += 1
                    elif self.j == self._center[1] + current_ratio:  # right side
                        next_i += 1
                    elif self.j == self._center[1] - current_ratio:  # left side
                        next_i -= 1
            elif self.rotation == -1:  # counter-clockwise
                if abs(self.i - self._center[1]) == abs(self.j - self._center[0]):
                    if self.i > self._center[0] and self.j > self._center[1]:  # right-bottom corner
                        next_i -= 1
                    elif self.i < self._center[0] and self.j > self._center[1]:  # right-top corner
                        next_j -= 1
                    elif self.i < self._center[0] and self.j < self._center[1]:  # left-top corner
                        next_i += 1
                    elif self.i > self._center[0] and self.j < self._center[1]:  # left-bottom corner
                        next_j += 1
                # identify current side of the square
                else:
                    if self.i == self._center[0] + current_ratio:  # bottom side
                        next_j += 1
                    elif self.i == self._center[0] - current_ratio:  # top side
                        next_j -= 1
                    elif self.j == self._center[1] + current_ratio:  # right side
                        next_i -= 1
                    elif self.j == self._center[1] - current_ratio:  # left side
                        next_i += 1
        self.i = next_i
        self.j = next_j
        self.counter += 1
        return current_i, current_j


class ChampernowneConstant(object):
    """
    Iterates over Champernowne's Constant digits
    """
    def __init__(self):
        self.pos = 1
        self.num = 1
        self.num_pos = 1
        self.val = 1

    def __iter__(self):
        return self

    def __next__(self):
        current_pos = self.pos
        current_num = self.num
        current_num_pos = self.num_pos
        current_val = self.val

        next_pos = current_pos + 1
        if current_num_pos < len(str(current_num)):
            next_num = current_num
            next_num_pos = current_num_pos + 1
        else:
            next_num = current_num + 1
            next_num_pos = 1
        next_val = int(str(next_num)[next_num_pos - 1])

        self.pos = next_pos
        self.num = next_num
        self.num_pos = next_num_pos
        self.val = next_val

        return current_val
