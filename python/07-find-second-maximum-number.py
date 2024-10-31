n = int(input())
numbers = list(map(int, input().split()))

max_number = max(numbers)
numbers = [num for num in numbers if num != max_number]

runner_up = max(numbers)
print(runner_up)