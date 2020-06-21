no_of_soldiers = int(input("Enter number of soldiers: "))

while 2 <= no_of_soldiers <= 100:
    heights = input("Enter heights: ").split(" ")
    swaps = 0

    min_heights = min(heights)
    max_heights = max(heights)

    print(max_heights, min_heights)

    not_sorted = False

    while not not_sorted:
        for i in range(0, len(heights)):
            if heights[i] == max_heights:
                if i == 0:
                    pass
                else:
                    temp = heights[i - 1]
                    heights[i - 1] = heights[i]
                    heights[i] = temp
                    swaps += 1

            elif heights[i] == min_heights:
                if i == len(heights) - 1:
                    pass
                else:
                    temp = heights[i]
                    heights[i] = heights[i + 1]
                    heights[i + 1] = temp
                    swaps += 1

        if heights[0] == max_heights and heights[len(heights) - 1] == min_heights:
            not_sorted = True

    print(heights)
    print(swaps)

    break
