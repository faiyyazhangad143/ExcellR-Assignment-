def arrypair(arr, k):
    if len(arr) < 2:
        return

    seen = set()
    output = set ()

    for num in arr:
        target = k-num

        if target not in seen:
                seen.add(num)

        else:
            output.add((min(num,arr),max(num,arr)))
            return len(output)

print(arrypair([1,2,3,4,5],8))