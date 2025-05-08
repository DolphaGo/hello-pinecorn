import json

with open("pinecorn_test.ipynb", "r", encoding="utf-8") as f:
    data = json.load(f)

# 최상위 widgets 제거
data.get("metadata", {}).pop("widgets", None)

# 셀별 metadata 제거
for cell in data.get("cells", []):
    if "metadata" in cell:
        cell["metadata"] = {}

# 저장
with open("pinecorn_test_cleaned.ipynb", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
