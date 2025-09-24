import pandas as pd
import random

# Các thuộc tính
colors = ["đỏ", "xanh", "đen", "trắng", "hồng"]
lengths = ["ngắn", "trung bình", "dài"]
types = ["váy", "giày", "túi xách", "áo khoác"]

# Một số truy vấn giả lập
queries = [
    "váy dạ hội đỏ có gắn nơ",
    "giày sneaker trắng nam",
    "túi xách da nữ",
    "áo khoác jean xanh"
]

data = []
for i in range(40):
    q = random.choice(queries)
    c = random.choice(colors)
    l = random.choice(lengths)
    t = random.choice(types)
    doc = f"{t} {c} {l}"
    rel = random.randint(0, 3)
    data.append([q, c, l, t, doc, rel])

# Xuất ra CSV
df = pd.DataFrame(data, columns=["truy_van", "mau", "chieu_dai", "loai", "doc", "relevance"])
df.to_csv("ranking_data.csv", index=False, encoding="utf-8-sig")
print("File ranking_data.csv đã tạo:", len(df), "dòng")
print(df.head(10))