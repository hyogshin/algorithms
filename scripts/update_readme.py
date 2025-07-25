import requests

USERNAME_BOJ = "hs607"
USERNAME_LEETCODE = "hyogshin"

def get_boj_count(username):
    url = f"https://solved.ac/api/v3/user/show?handle={username}"
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        return data["solvedCount"]
    return "?"

def get_leetcode_count(username):
    url = f"https://leetcode-stats-api.herokuapp.com/{username}"
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        return data["totalSolved"]
    return "?"

def update_readme(boj_count, leetcode_count):
    with open("README.md", "r") as f:
        lines = f.readlines()

    start = "<!-- STATS-START -->"
    end = "<!-- STATS-END -->"

    new_stats = f"""
| Platform   | Problems Solved |
|------------|------------------|
| BOJ        | {boj_count}             |
| LeetCode   | {leetcode_count}             |
"""

    new_lines = []
    recording = True
    for line in lines:
        if start in line:
            new_lines.append(line)
            new_lines.append(new_stats)
            recording = False
        elif end in line:
            new_lines.append(line)
            recording = True
        elif recording:
            new_lines.append(line)

    with open("README.md", "w") as f:
        f.writelines(new_lines)

if __name__ == "__main__":
    boj = get_boj_count(USERNAME_BOJ)
    lc = get_leetcode_count(USERNAME_LEETCODE)
    update_readme(boj, lc)
