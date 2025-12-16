class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v in hierarchy:
            adj[u - 1].append(v - 1)

        def combine(dp1, dp2):
            new_dp = [-float('inf')] * (budget + 1)
            
            items1 = [(c, p) for c, p in enumerate(dp1) if p > -float('inf')]
            items2 = [(c, p) for c, p in enumerate(dp2) if p > -float('inf')]
            
            for c1, p1 in items1:
                for c2, p2 in items2:
                    if c1 + c2 <= budget:
                        if p1 + p2 > new_dp[c1 + c2]:
                            new_dp[c1 + c2] = p1 + p2
            return new_dp

        def dfs(u):
            sum_dp_bought = [-float('inf')] * (budget + 1)
            sum_dp_bought[0] = 0
            
            sum_dp_skipped = [-float('inf')] * (budget + 1)
            sum_dp_skipped[0] = 0
            
            for v in adj[u]:
                child_res_no_parent_buy, child_res_parent_buy = dfs(v)
                
                sum_dp_bought = combine(sum_dp_bought, child_res_parent_buy)
                
                sum_dp_skipped = combine(sum_dp_skipped, child_res_no_parent_buy)

            res_no_parent_buy = list(sum_dp_skipped)
            
            cost_full = present[u]
            profit_full = future[u] - cost_full
            
            if cost_full <= budget:
                for c, val in enumerate(sum_dp_bought):
                    if val > -float('inf') and c + cost_full <= budget:
                        res_no_parent_buy[c + cost_full] = max(res_no_parent_buy[c + cost_full], val + profit_full)
            res_parent_buy = list(sum_dp_skipped)
            cost_discount = present[u] // 2
            profit_discount = future[u] - cost_discount
            
            if cost_discount <= budget:
                for c, val in enumerate(sum_dp_bought):
                    if val > -float('inf') and c + cost_discount <= budget:
                        res_parent_buy[c + cost_discount] = max(res_parent_buy[c + cost_discount], val + profit_discount)
                        
            return res_no_parent_buy, res_parent_buy

        final_dp, _ = dfs(0)
        
        return max(0, max(final_dp))