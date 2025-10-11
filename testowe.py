task = int(input())
nums = [int(input()) for _ in range(50)]

if task == 1:
    print(sum(nums) // 50)
elif task == 2:
    print("\n".join(str(num+5) for num in nums))
elif task == 3:
    maksymalna = max(nums)
    suma = sum(int(cyferka) for cyferka in str(maksymalna))
    print(maksymalna, suma)