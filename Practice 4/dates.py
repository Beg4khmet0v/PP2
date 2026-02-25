from datetime import datetime, timedelta

# 1
print(datetime.now() - timedelta(days=5))

# 2
today = datetime.now().date()
print(today - timedelta(days=1))
print(today)
print(today + timedelta(days=1))

# 3
print(datetime.now().replace(microsecond=0))

# 4
d1 = datetime(2026, 2, 25, 12, 0, 0)
d2 = datetime(2026, 2, 25, 21, 35, 0)
print(int((d2 - d1).total_seconds()))