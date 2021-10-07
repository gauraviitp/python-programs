import collections


class Solution:
    def findOrder(self, dict, N, K):
        # code here
        cur = dict[0]

        g = collections.defaultdict(list)
        all = set(cur)

        for j in range(1, N):
            next = dict[j]
            all |= set(next)

            for i in range(len(cur)):
                if i < len(next):
                    if cur[i] != next[i]:
                        g[cur[i]].append(next[i])
                        break
            cur = next

        visited = collections.defaultdict(bool)

        def topological_ordering(u, stack):
            visited[u] = True

            for v in g[u]:
                if not visited[v]:
                    topological_ordering(v, stack)

            stack.append(u)

        stack = []
        for node in list(g):
            if not visited[node]:
                topological_ordering(node, stack)

        rem = set(all) - set(stack)

        return stack[::-1] + list(rem)


sol = Solution()
for val in sol.findOrder(['bhhb', 'blkbggfecalifjfcbkjdicehhgikkdhlachlgbhji', 'cfjjhcifladadbgcleggjgbcieihabcglblflgajgkejccj', 'dlgdhiha', 'ehggedljjhfldcajeceaeehkalkfeidhigkifjl', 'gdalgkblahcldahledfghjb', 'geldbblaaflegjhlfjlgblfbdc', 'ibjceciedbiilkjliijgklcgliaeeic', 'jcebjkfgfibfckfiikklecihik', 'jdkcabjjjckgdblkljf', 'jijlbjbliigkffhkchkclkhafbiiiblcglhfjkflbjjkih', 'kfd', 'lhdgidialgabfklffahiihceflebfidl'], 13, 12):
    print(val)
