from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    top_score = float("-inf")
    best = None
    for name, score in scores:
        if score > top_score:
            top_score = score
            best = name
    return best


# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
