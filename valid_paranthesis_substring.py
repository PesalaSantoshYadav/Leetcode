class Solution:
    def checkValidString(self, s: str) -> bool:
        c = 0
        d = {}
        def helper(s, i, c):
            try:
                return d[tuple([i, c])]
            except:
                pass
            if i == len(s) and c == 0:
                return True
            if i < len(s) and s[i] == '(' :
                d[tuple([i, c])] = helper(s, i + 1, c + 1)
                return d[tuple([i, c])]
            elif c > 0 and i < len(s) and s[i] == ')':
                d[tuple([i, c])] = helper(s, i + 1, c - 1)
                return d[tuple([i, c])]
            elif i < len(s) and s[i] == '*' :
                d[tuple([i, c])] = (helper(s, i + 1, c) or helper(s, i + 1, c + 1) or (c > 0 and helper(s, i + 1, c - 1)))
                return d[tuple([i, c])]
            else:
                d[tuple([i, c])] = False
                return d[tuple([i, c])]
        return helper(s, 0, c)

def main():
    solution = Solution()
    string = input("Enter the string: ")
    result = solution.checkValidString(string)
    print("Is the string valid?", result)

if __name__ == "__main__":
    main()