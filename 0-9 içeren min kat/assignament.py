import time

numbers = []

while True:
    try:
        num_of_test_cases = int(input("Number of test cases: "))
    except ValueError:
        print("Not an integer! Try again.")
        continue
    break


for i in range(num_of_test_cases):
    numbers.append(int(input(f"{i+1}. number: ")))


start = time.time()

results = []
for n in numbers:
    mods_array = [0]
    if n is 0:
        results.append(0)
        continue
    b = 9%n
    while 0 not in mods_array[1:]:
        c = [(b + x)%n for x in mods_array]
        mods_array = mods_array + c # duplicate mods array
        b = (b*10)%n
    
    index = mods_array[1:].index(0) + 1 # find the index of the number that (number)%n = 0
    base_2 = int(bin(index)[2:])
    results.append(base_2*9)
stop = time.time()

print("Output Result:")
print(*results, sep="\n")

print('Time: ', stop - start)
