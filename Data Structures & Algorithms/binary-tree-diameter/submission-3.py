# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        topa = 0
        _iroot = root
        while True:
            print(_iroot.val, _iroot.left, _iroot.right)
            lc, rc = _iroot.left, _iroot.right
            if lc==None and rc==None:
                break
            if lc==None and rc!=None:
                _iroot = rc
                topa += 1
            if lc != None and rc==None:
                _iroot = lc
                topa += 1
            if lc != None and rc != None:
                break

        def maxDepth(_root):
            if _root == None:
                return 0
            if _root.left != None and _root.right != None:
                lval = 1 + maxDepth(_root.left)
                rval = 1 + maxDepth(_root.right)
                return max(lval,rval)
            else:
                if _root.left != None:
                    return 1 + maxDepth(_root.left)
                elif _root.right != None:
                    return 1 + maxDepth(_root.right)
                else:
                    return 0
        add = 0
        if _iroot.left != None:
            add+=1
        if _iroot.right != None:
            add+=1
        lv = maxDepth(_iroot.left)
        rv = maxDepth(_iroot.right)
        print(lv,rv)
        return max([lv + rv + add, lv + topa, rv + topa])