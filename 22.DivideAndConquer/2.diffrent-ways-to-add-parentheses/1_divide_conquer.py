def diffWaysToCompute(input):
    def compute(left, right, op):
        results = []
        for l in left:
            for r in right:
                results.append(eval(str(l) + op + str(r)))
        return results
    
    if input.isdigit():
        return [int(input)]
    
    results = []
    for index, value in enumerate(input):
        if value in "-+*":
            left = diffWaysToCompute(input[:index])
            right = diffWaysToCompute(input[index+1:])

            results.extend(compute(left, right, value))
    
    return results


if __name__ == "__main__":
    print(diffWaysToCompute("2-1-1"))
    print(diffWaysToCompute("2*3-4*5"))