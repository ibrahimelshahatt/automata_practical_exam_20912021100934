class PDA:
    def accepts(self, string):
        if len(string) % 2 == 0:
            return False

        stack = []
        mid = len(string) // 2

        for i in range(mid):
            stack.append(string[i])

        for i in range(mid + 1, len(string)):
            if not stack or stack.pop() != string[i]:
                return False

        return True