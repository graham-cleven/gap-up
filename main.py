import yfinance as yf

spy = yf.Ticker("SPY")

hist = spy.history(period="1y", interval="1d")

total = 0.0
results = []

for x in range(len(hist)):
    if x > 0:
        gap = ((hist['Open'][x] - hist['Close'][x-1]) / hist['Close'][x-1]) * 100

        if gap > 0:
            result = ((hist['Close'][x] - hist['Open'][x]) / hist['Open'])[x] * 100
            results.append(result)

up = 0
down = 0
for result in results:
    if result > 0:
        up += 1
    if result < 0:
        down += 1

    print(result)
    total += result

print(total)
print(up)
print(down)


# up = 56.164%
# It works 100 % of the time, more than half the time, lol