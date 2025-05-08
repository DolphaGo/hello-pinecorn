import json

# 깃허브 업로드 시 노트북이 깨지는 문제는 노트북에 포함된 metadata 때문인데 이를 지워주는 코드

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
