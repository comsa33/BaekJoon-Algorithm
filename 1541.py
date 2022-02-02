equations = list(map(lambda x: x.split('+'), input().split('-')))
print(eval('-'.join(map(str, list(map(lambda x: sum(map(int, x)), equations))))))