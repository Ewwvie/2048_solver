import csv #exporting game results
import json #for summ stats 
import os
import statistics 
from datetime import datetime

results_dir = os.path.join(os.path.dirname(__file__), "results")
os.makedirs(results_dir, exist_ok=True)


def percentile(values, p): #calculate the nth percentile of a collection
    if not values:
        return 0
    values=sorted(values)
    index=(len(values) - 1) * p / 100
    l=int(index)
    u=min(l + 1, len(values) - 1)
    x= u-l
    return values[l]* (1 - x)+ values[u]*x


def save_results(games, latencies, depth):
    timestamp=datetime.now().strftime("%Y%m%d_%H%M%S")
    csv_path =os.path.join(
        results_dir,
        f"games@{timestamp}.csv"
    )
    json_path= os.path.join(
        results_dir,
        f"summary@{timestamp}.json"
    )

    if games:
        with open(csv_path, "w", newline="") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=games[0].keys()
            )

            writer.writeheader()
            writer.writerows(games)

    scores = [game["score"] for game in games]
    durations = [game["duration"] for game in games]
    tiles = [game["max_tile"] for game in games]

    total_moves = sum(game["moves"] for game in games)
    total_duration = sum(durations)

    summary = {
        "depth": depth,
        "total_games": len(games),

        "average_score": statistics.mean(scores) if scores else 0,
        "median_score": statistics.median(scores) if scores else 0,
        "highest_score": max(scores) if scores else 0,

        "average_max_tile": statistics.mean(tiles) if tiles else 0,
        "highest_tile": max(tiles) if tiles else 0,

        "success_rate_2048": (
            sum(tile >= 2048 for tile in tiles) / len(tiles) * 100
            if tiles else 0
        ),

        "average_game_duration": (
            statistics.mean(durations) if durations else 0
        ),

        "average_moves": (
            statistics.mean([game["moves"] for game in games])
            if games else 0
        ),

        "total_moves": total_moves,

        "average_decision_latency_ms": (
            statistics.mean(latencies) * 1000
            if latencies else 0
        ),

        "median_decision_latency_ms": (
            statistics.median(latencies) * 1000
            if latencies else 0
        ),

        "p95_decision_latency_ms": percentile(latencies, 95) * 1000,

        "total_decisions": len(latencies),

        "games_per_second": (
            len(games) / total_duration
            if total_duration > 0 else 0
        )
    }

    with open(json_path, "w") as file:
        json.dump(summary, file, indent=4)

    print("\n========== BENCHMARK RESULTS ==========")

    for key, value in summary.items():
        print(f"{key}: {value}")

    print("\n========== FILES GENERATED ==========")
    print(f"CSV: {csv_path}")
    print(f"JSON: {json_path}")

    return summary
