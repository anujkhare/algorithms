## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/evaluate-expression-to-true/
## Topic:: Dynamic Programming
## Sub-topic:: 
## Difficulty:: Hard
## Approach:: for each increasing sub-expression, store the number of ways to evaluate it to T and F; keep increasing the length; use the truth tables for combination
## Time complexity:: O(N^3)
## Space complexity:: O(N^2)
## Notes:: Similar to matrix multiplication
## Bookmarked:: Yes

class Solution:
    @staticmethod
    def _parse_string(string: str):
        operands = string[::2]
        operators = string[1::2]
        operands = list(map(lambda x: {'t': 1, 'f': 0}[x.lower()], operands))
        return operands, operators

    @staticmethod    
    def _get_ways(operator, leftt, leftf, rightt, rightf):
        # print('gw', leftt, leftf, rightt, rightf)
        if operator == '|':
            ways_t = leftt * rightt + leftt * rightf + leftf * rightt
            ways_f = leftf * rightf
        elif operator == '&':
            ways_t = leftt * rightt
            ways_f = leftt * rightf + leftf * rightt + leftf * rightf
        elif operator == '^':
            ways_t = leftt * rightf + leftf * rightt
            ways_f = leftt * rightt + leftf * rightf
        else:
            raise Exception
        return ways_t, ways_f

    # @param A : string
    # @return an integer
    def cnttrue(self, A):
        # Parse string into 2 lists
        operands, operators = self._parse_string(A)
        l = len(operands)
        if l == 0:
            return 0

        # create a dp array
        ways_true = [[0] * l for _ in range(l)]
        ways_false = [[0] * l for _ in range(l)]

        # start with length 1 and fill out the dp table
        for ix in range(l):
            ways_true[ix][ix] = int(operands[ix])
            ways_false[ix][ix] = 1 - int(operands[ix])
        
        # print(ways_true)
        # print(ways_false)
        for kl in range(2, l+1):
            for ix in range(l-kl+1):
                right = ix + kl - 1
                for jx in range(kl-1):
                    # take one segment from ix to jx and the other from jx to ix+kl-1
                    lefts, lefte = ix, ix+jx
                    rights, righte = ix+jx+1, right
                    cways_t, cways_f = self._get_ways(
                        operators[ix+jx],
                        ways_true[lefts][lefte],
                        ways_false[lefts][lefte],
                        ways_true[rights][righte],
                        ways_false[rights][righte]
                    )
                    ways_true[ix][right] += cways_t
                    ways_false[ix][right] += cways_f
                    # print('rs', lefts, lefte, rights, righte, cways_t, cways_f)
        
        return ways_true[0][l-1]
