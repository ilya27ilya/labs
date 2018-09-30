import sys


class ParseError(Exception):
    pass


def parse(G, w):
    def transition(r, s, i, L1, L2):
        if r == 1:
            for j, (A, beta) in enumerate(G):
                if len(L1) >= len(beta) and L1[-len(beta):] == list(beta):
                    return r, s, i, L1[:-len(beta)] + [A], [j] + L2
            return 2, s, i, L1, L2

        if r == 2:
            if i < len(w):
                return 1, s, i + 1, L1 + [w[i]], ['s'] + L2
            return 3, s, i, L1, L2

        if r == 3:
            if L1 == ['$', G[0][0]]:
                return None, 't', i, L1, L2
            return 4, s, i, L1, L2

        if r == 4:
            return 5, 'b', i, L1, L2

        if r == 5:
            if len(L2) == 0:
                raise ParseError()
            if L2[0] == 's':
                return r, s, i - 1, L1[:-1], L2[1:]
            j = L2[0]
            A, beta = G[j]
            L1_t = L1[:-1] + list(beta)
            for k, (B, beta_t) in enumerate(G[j + 1:], j + 1):
                if len(L1_t) >= len(beta_t) and L1_t[-len(beta_t):] == list(beta_t):
                    return 1, 'q', i, L1_t[:-len(beta_t)] + [B], [k] + L2[1:]
            if i == len(w):
                return r, s, i, L1_t, L2[1:]
            return 1, 'q', i + 1, L1_t + [w[i]], ['s'] + L2[1:]

    log = []

    r, s, i, L1, L2 = 1, 'q', 0, ['$'], []
    while True:
        log.append((s, i + 1, L1, L2))
        if s == 't':
            return [x + 1 for x in L2 if x != 's'], log
        while True:
            r_t, s_t, i_t, L1_t, L2_t = r, s, i, L1, L2
            r, s, i, L1, L2 = transition(r_t, s_t, i_t, L1_t, L2_t)
            if (s, i, L1, L2) != (s_t, i_t, L1_t, L2_t):
                break


G = []
with open('ex.grammar') as grammar:
    for line in grammar:
        lhs, rhs = line.split('->')
        lhs = lhs.strip()
        rhs = tuple(rhs.split())
        G.append((lhs, rhs))

print('Grammar:')
for lhs, rhs in G:
    print(' ', lhs, '->', *rhs)

with open('ex.tokens') as tok:
    for line in tok:
        w = line.split()
        print()
        print('Tokens:')
        print('  ', ' '.join(w))
        try:
            result, log = parse(G, w)
        except ParseError:
            print('SyntaxError')
            continue

        log = [(s, str(i), ' '.join(map(str, L1)), ' '.join(map(str, L2))) for s, i, L1, L2 in log]
        sw, iw, L1w, L2w = map(lambda s: max(map(len, s)), zip(*log))
        print('Configurations:')
        print('  ', 's', ' | ', 'i'.ljust(iw), ' | ', 'L1'.ljust(L1w), ' | ', 'L2'.ljust(L2w))
        print('  ', '-', '-+-', '-' * iw, '-+-', '-' * L1w, '-+-', '-' * L2w, sep='-')
        for s, i, L1, L2 in log:
            print('  ', s, ' | ', i.rjust(iw), ' | ', L1.ljust(L1w), ' | ', L2.rjust(L2w))
            # print('Result:')
            # print('  ', ' '.join(map(str, result)))