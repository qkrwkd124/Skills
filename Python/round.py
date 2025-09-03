from decimal import Decimal, ROUND_HALF_UP


value = 82.05

print(round(value, 1)) # 82.0 으로 표현

val = Decimal("82.05") # 문자열이여야 함.
print(val)
round_val = val.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP) # 82.1 으로 표현
print(round_val)