## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/max-sum-path-in-binary-tree/
## Topic:: Tree
## Sub-topic:: Binary Tree
## Difficulty:: Easy
## Approach:: Maintain rooted sum and overall max sum
## Time complexity:: O(N)
## Space complexity:: O(N)
## Notes::
## Bookmarked:: No


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxsumhelper(self, root):
        if root is None:
            return 0, -float('inf')
        lsumrooted, lmaxsum = self.maxsumhelper(root.left)
        rsumrooted, rmaxsum = self.maxsumhelper(root.right)

        # if one of the braches is bringing the sum down, you could ignore it
        lsumrooted = max(lsumrooted, 0)
        rsumrooted = max(rsumrooted, 0)

        rootedsum = root.val + max(lsumrooted, rsumrooted)
        subtreesum = root.val + lsumrooted + rsumrooted
        maxsum = max(lmaxsum, rmaxsum, rootedsum, subtreesum)
        return rootedsum, maxsum

    # @param A : root node of tree
    # @return an integer
    def maxPathSum(self, A):
        _, maxsum = self.maxsumhelper(A)
        return maxsum
