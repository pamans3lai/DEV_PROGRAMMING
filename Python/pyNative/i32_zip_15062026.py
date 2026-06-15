names = ["Alis", "Bob", "charlie"]
scores = [85, 92, 78]

score_map = dict(zip(names, scores))

ranked_scores = sorted(score_map.items(), key=lambda item: item[1], reverse=True)

for i, (name, score) in enumerate(ranked_scores, start=1):
    print(f"Rank {i}: scored {score}")
