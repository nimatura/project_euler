import numpy as np


class PokerHand(object):
    """
    Representation of a poker hand with comparison utilities
    """
    __values = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

    def __init__(self, cards):
        self.cards = cards

    def __eq__(self, other):
        return self.cards == other.cards

    def __gt__(self, other):
        return self.score() > other.score()

    def score(self):
        values = sorted(self.__values[c[0]] for c in list(self.cards))
        hex_values = [hex(v).split('x')[1] for v in values]
        hex_values_count = {v: hex_values.count(v) for v in hex_values}
        result = ''
        # check for straight flush
        if self.__is_flush() and self.__is_straight(values):
            result += '1'
        else:
            result += '0'
        # check for poker / four of a kind
        result += self.__poker(hex_values_count)
        # check for full house
        trio = self.__trio(hex_values_count)
        pairs = self.__pairs(hex_values_count)
        if trio != '0' and len(pairs) == 1:
            result += trio + pairs[0]
        else:
            result += '00'
        # check for regular flush
        if self.__is_flush():
            result += '1'
        else:
            result += '0'
        # check for regular straight
        if self.__is_straight(values):
            result += '1'
        else:
            result += '0'
        # check for trio
        result += str(trio)
        # check for two pairs
        if len(pairs) == 2:
            result += pairs[1] + pairs[0]
        else:
            result += '00'
        # check for single pair
        if len(pairs) == 1:
            result += pairs[0]
        else:
            result += '0'
        # check for high cards
        for v in hex_values[::-1]:
            result += v
        # return int(result, base=16)
        return result

    @staticmethod
    def __poker(hex_values_count):
        for v, c in hex_values_count.items():
            if c == 4:
                return v
        return '0'

    def __is_flush(self):
        return len(set([c[1] for c in self.cards])) == 1

    @staticmethod
    def __is_straight(values):
        regular_straight = all([(values[i + 1] - values[i]) == 1 for i in range(4)])
        low_straight = all([(values[i + 1] - values[i]) == 1 for i in range(3)]) and values[4] == 14
        return regular_straight or low_straight

    @staticmethod
    def __trio(hex_values_count):
        for v, c in hex_values_count.items():
            if c == 3:
                return v
        return '0'

    @staticmethod
    def __pairs(hex_values_count):
        pairs = []
        for v, c in hex_values_count.items():
            if c == 2:
                pairs.append(v)
        return sorted(pairs)
