class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = dict()
        emailsToNames = dict()
        for acc in accounts:
            for email in acc[1:]:
                if email not in graph:
                    graph[email] = set()
                if acc[1] not in graph:
                    graph[acc[1]] = set()
                graph[acc[1]].add(email)
                graph[email].add(acc[1])
                emailsToNames[email] = acc[0]
        visited = set()
        result = []
        for email in graph:
            if email not in visited:
                stack = [email]
                visited.add(email)
                component = []
                while stack:
                    node = stack.pop()
                    component.append(node)
                    for neig in graph[node]:
                        if neig not in visited:
                            visited.add(neig)
                            stack.append(neig)
                component.sort()
                result.append([emailsToNames[email]] + component)
        return result
