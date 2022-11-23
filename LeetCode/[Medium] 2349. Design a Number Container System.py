import sys


class NumberContainers:

    def __init__(self):
        # {value: ['min index', set(indices at which the value is taking place)]}
        self.val_dict = {}
        # {index: value that is taking place at the index}
        self.idx_dict = {}

    def change(self, index: int, number: int) -> None:
        # if there is already a number at the index,
        if index in self.idx_dict:
            # we call the number 'prev_value'
            prev_value = self.idx_dict[index]
            # if prev_value is same as the given number, we do nothing
            if prev_value == number:
                return
            # remove the index from the set of indices of the prev_value
            self.val_dict[prev_value][1].remove(index)
            # if the set is empty, we assign 'infinity' to min index of the prev_value
            # because it is useful when we compare the current min index and the new index
            if not self.val_dict[prev_value][1]:
                self.val_dict[prev_value][0] = sys.maxsize
            # if the set is not empty after removal, we assign min value of the set to the min index
            else:
                self.val_dict[prev_value][0] = min(self.val_dict[prev_value][1])

        # now we're done with the prev_value
        # let's handle the new number and the index

        # set the number to the idx_dict[index]
        self.idx_dict[index] = number

        # if the number has already been filled into this container,
        if number in self.val_dict:
            # renew the min index
            # (if the min index == sys.maxsize,
            #  it will automatically assign new index to the min index)
            self.val_dict[number][0] = min(self.val_dict[number][0], index)
            # add new index to the set
            self.val_dict[number][1].add(index)
        # else we should make new list of [new index, {new index}]
        else:
            self.val_dict[number] = [index, {index}]

    def find(self, number: int) -> int:
        # if there is no index that is filled by number
        if number not in self.val_dict or self.val_dict[number][0] == sys.maxsize:
            return -1
        # it will return the smallest index for the given number
        return self.val_dict[number][0]

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
