from enum import Enum


class HandRank(Enum):
    FIVE_OF_A_KIND = 7
    FOUR_OF_A_KIND = 6
    FULL_HOUSE = 5
    THREE_OF_A_KIND = 4
    TWO_PAIR = 3
    ONE_PAIR = 2
    HIGH_CARD = 1


class Node:
    def __init__(self, data, bid):
        self.data = data
        self.bid = bid
        self.rank = None
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def calculate_ranks(self):
        current = self.head
        while current:
            current.rank = determine_type(current.data).value
            current = current.next

    def bubble_sort(self):
        card_order = 'AKQT98765432J'
        end = None
        while end != self.head:
            swapped = False
            current = self.head
            while current.next != end:
                swap = False
                if current.rank > current.next.rank:
                    swap = True
                elif current.rank == current.next.rank:
                    # Compare cards in the hand until a difference is found
                    for i in range(len(current.data)):
                        if card_order.index(current.data[i]) < card_order.index(current.next.data[i]):
                            swap = True
                            break
                        elif card_order.index(current.data[i]) > card_order.index(current.next.data[i]):
                            break

                if swap:
                    # Swap data, bid, and rank
                    current.data, current.next.data = current.next.data, current.data
                    current.bid, current.next.bid = current.next.bid, current.bid
                    current.rank, current.next.rank = current.next.rank, current.rank
                    swapped = True

                current = current.next
            end = current
            if not swapped:
                break

    def append(self, data, bid):
        new_node = Node(data, bid)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data, cur_node.bid, cur_node.rank)
            cur_node = cur_node.next

    def calculate_winnings(self):
        running_sum = 0
        multiplier = 1
        current = self.head
        while current:
            running_sum += multiplier * current.bid
            multiplier += 1
            current = current.next
        return running_sum


def determine_type(data):
    # Count the frequency of each card label
    freq = {}
    j_count = data.count('J')
    for card in data:
        if card != 'J':
            freq[card] = freq.get(card, 0) + 1

    if j_count:
        return determine_best_hand_with_j(freq, j_count)
    else:
        return determine_hand_rank(freq)


def determine_best_hand_with_j(freq, j_count):
    # Check all possibilities of substituting 'J' and return the best hand
    best_hand_rank = HandRank.HIGH_CARD
    for card in set(list(freq.keys()) + ['A', 'K', 'Q', 'T', '2', '3', '4', '5', '6', '7', '8', '9']):
        new_freq = freq.copy()
        new_freq[card] = new_freq.get(card, 0) + j_count
        best_hand_rank = max(best_hand_rank, determine_hand_rank(new_freq), key=lambda rank: rank.value)
    return best_hand_rank


def determine_hand_rank(freq):
    freq_values = list(freq.values())
    if 5 in freq_values:
        return HandRank.FIVE_OF_A_KIND
    elif 4 in freq_values:
        return HandRank.FOUR_OF_A_KIND
    elif freq_values.count(3) == 1 and freq_values.count(2) == 1:
        return HandRank.FULL_HOUSE
    elif 3 in freq_values:
        return HandRank.THREE_OF_A_KIND
    elif freq_values.count(2) == 2:
        return HandRank.TWO_PAIR
    elif freq_values.count(2) == 1:
        return HandRank.ONE_PAIR
    else:
        return HandRank.HIGH_CARD


# Main
dll = DoublyLinkedList()
with open('input.txt', 'r') as file:
    for line in file:
        data, bid = line.strip().split()
        bid = int(bid)  # Convert bid to integer
        dll.append(data, bid)

dll.calculate_ranks()
dll.bubble_sort()
dll.print_list()
winnings = dll.calculate_winnings()
print(winnings)
