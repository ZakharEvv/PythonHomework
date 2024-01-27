assessments = list(map(int, input().split()))
assessments_count = [assessments.count(5), assessments.count(4), assessments.count(3)]
percent = sum(assessments_count) / len(assessments) * 100
print(assessments, assessments_count, percent)