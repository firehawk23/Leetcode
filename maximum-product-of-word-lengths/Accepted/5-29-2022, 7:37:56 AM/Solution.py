// https://leetcode.com/problems/maximum-product-of-word-lengths

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        return max((len(w1) * len(w2) for w1, w2 in combinations(words, 2) if not (set(w1) & set(w2))),default=0)
