buger = 2000
beverage = 2000

for i in range(3):
    buger_price = int(input())
    buger = min(buger, buger_price)
        
    
for i in range(2):
    beverage_price = int(input())
    beverage = min(beverage, beverage_price)

print(buger + beverage - 50)