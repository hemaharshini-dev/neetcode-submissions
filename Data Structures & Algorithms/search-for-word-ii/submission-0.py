class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        root = TrieNode()

        # Build Trie
        for word in words:
            cur = root

            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()

                cur = cur.children[c]

            cur.word = word

        rows = len(board)
        cols = len(board[0])
        res = []

        def dfs(r, c, node):

            if (
                r < 0 or
                r >= rows or
                c < 0 or
                c >= cols or
                board[r][c] not in node.children
            ):
                return

            char = board[r][c]
            cur = node.children[char]

            if cur.word:
                res.append(cur.word)
                cur.word = None

            board[r][c] = "#"

            dfs(r + 1, c, cur)
            dfs(r - 1, c, cur)
            dfs(r, c + 1, cur)
            dfs(r, c - 1, cur)

            board[r][c] = char

            # Remove empty Trie branches for optimization
            if not cur.children and cur.word is None:
                del node.children[char]

        # Start DFS from every cell
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return res