import json
import os

LEADERBOARD_FILE = "leaderboard.json"
SETTINGS_FILE = "settings.json"


# =========================
# LEADERBOARD
# =========================
def load_leaderboard():
    if not os.path.exists(LEADERBOARD_FILE):
        return []

    with open(LEADERBOARD_FILE, "r") as f:
        return json.load(f)


def save_leaderboard(data):
    with open(LEADERBOARD_FILE, "w") as f:
        json.dump(data, f, indent=4)


def add_score(name, score, coins):
    data = load_leaderboard()

    data.append({
        "name": name,
        "score": score,
        "coins": coins
    })

    # сортировка по score
    data = sorted(data, key=lambda x: x["score"], reverse=True)

    # топ 10
    data = data[:10]

    save_leaderboard(data)


# =========================
# SETTINGS
# =========================
def load_settings():
    if not os.path.exists(SETTINGS_FILE):
        return {
            "sound": False,
            "difficulty": "normal",
            "car_color": "red"
        }

    with open(SETTINGS_FILE, "r") as f:
        return json.load(f)


def save_settings(settings):
    with open(SETTINGS_FILE, "w") as f:
        json.dump(settings, f, indent=4)