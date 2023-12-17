from typing import List

class FoodRatings:

    # Online Solution 

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_info = {}
        self.sorted_cuisine = defaultdict(SortedList)
        
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_info[food] = (cuisine, rating)
            self.sorted_cuisine[cuisine].add((-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, old_rating = self.food_info[food]
        self.food_info[food] = (cuisine, newRating)
        self.sorted_cuisine[cuisine].discard((-old_rating, food))
        self.sorted_cuisine[cuisine].add((-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        return self.sorted_cuisine[cuisine][0][1]

    # Solution 1 Time limit exceeded

    # def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
    #     self.foods = foods
    #     self.cuisines = cuisines
    #     self.ratings = ratings
    #     self.highest = max(ratings)

    # def changeRating(self, food: str, newRating: int) -> None:
    #     for i in range(len(self.foods)):
    #         if self.foods[i] == food:
    #             self.ratings[i] = newRating
    #             self.highest = max(self.highest, newRating)
    #             break

    # def highestRated(self, cuisine: str) -> str:
    #     # Find the indices of items with the given cuisine
    #     indices = [i for i, c in enumerate(self.cuisines) if c == cuisine]

    #     if not indices:
    #         return ""  # Return an empty string if no items with the specified cuisine

    #     # Find the index with the highest rating and lexicographically smaller name
    #     max_index = indices[0]
    #     for i in indices:
    #         if self.ratings[i] > self.ratings[max_index] or \
    #            (self.ratings[i] == self.ratings[max_index] and self.foods[i] < self.foods[max_index]):
    #             max_index = i

    #     return self.foods[max_index]
