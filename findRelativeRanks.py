class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        if len(score) < 3:
            # Handle the case where the length of score is less than 3
            if len(score) == 1:
                return ["Gold Medal"]
            elif len(score) == 2:
                if score[0] > score[1]:
                    return ["Gold Medal", "Silver Medal"]
                else:
                    return ["Silver Medal", "Gold Medal"]
        
        sorted_scores = sorted(score, reverse=True)
        d = {
            sorted_scores[0]: "Gold Medal",
            sorted_scores[1]: "Silver Medal",
            sorted_scores[2]: "Bronze Medal"
        }

        for i, v in enumerate(sorted_scores[3:][::-1]):
            d[v] = d.get(v, str(len(score) - i))

        result = []
        for v in score:
            result.append(d[v])

        return result
