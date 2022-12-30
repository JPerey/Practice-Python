
class Node(object):

    def __init__(self, val):
        self.val = val
        self.next = None

    def get_data(self):
        return self.val

    def set_data(self, val):
        self.val = val

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next


def linkedListCreator():

    pass


class linkedList():

    def __init__(self, head=None):
        self.head = head
        self.count = 0

    def insert(self, data):

        new_node = Node(data)  # Creating a new node to hold the data

        # Set the next of the new node to the current head
        new_node.set_next(self.head)

        self.head = new_node  # Set the head of the linked list to the new head

        self.count += 1  # adding 1 to count as we just made a new node

    def find(self, val):

        item = self.head

        while item != None:

            if item.get_data() == val:
                return item
            else:
                item = item.get_next()

        return None

    def read(self, item):

        return item.get_data()

    def remove(self, item):
        current = self.head
        previous = None

        while current is not None:
            if current.val == item:
                break

            previous = current
            current = current.get_next()

        if current is None:
            raise ValueError(f"{item} is not in the list")

        if previous is None:
            self.head = current.next
            self.count -= 1

        else:
            previous.set_next(current.get_next)
            self.count -= 1


listy = linkedList()
listy.insert(20)
listy.insert(10)
result10 = listy.find(10)
result20 = listy.find(20)
result30 = listy.find(30)
data10 = listy.read(result10)

print(f"listy: {listy}")
print(f"listy is there 20: {result20}")
print(f"listy is there 10: {result10}")
print(f"listy is there 30: {result30}")
print(f"data inside '10' node: {data10}")
