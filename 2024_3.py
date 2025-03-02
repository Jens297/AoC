import re

with open(r"C:\Users\Jens\Desktop\AoC\2024\3\input.txt", "r", encoding="utf-8") as file:
    text = file.read()

pattern = r"mul[\(\{]\d{1,3},\s*\d{1,3}[\)\}]"
matches = re.findall(pattern, text)

res = 0
for match in matches:
    idx = match.find("(")
    noparentheses = match[idx+1:-1]
    x,y = noparentheses.split(',')
    res += int(x) * int(y)
print(res)
