# class Logger:

#     def __init__(self):
#         self.memo = {}


#     def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
#         if message in self.memo:
#             if self.memo[message] + 10 <= timestamp:
#                 self.memo[message] = timestamp
#                 return True
#             else:
#                 return False
#         else:
#             self.memo[message] = timestamp
#             return True
#
# Time complexity
# # operate on hashmap -> O(1)
# ## O(1)

# Space complexity
# ## O(M) where M is the number of all unique messages


class Logger:
    def __init__(self):
        self.queue = collections.deque()
        self.messages = set()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        while self.queue:
            msg, ts = self.queue[0]
            if ts + 10 <= timestamp:
                self.queue.popleft()
                self.messages.remove(msg)
            else:
                break

        if message in self.messages:
            return False
        else:
            self.messages.add(message)
            self.queue.append((message, timestamp))
            return True

        # Time complexity
        ## iteration for the size of the queue -> O(N)
        ### O(N)

        # Space complexity
        ## size of the queue -> O(N)
        ## size of the unique message -> O(M) < O(N)
        ### O(N)


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
