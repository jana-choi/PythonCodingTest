def canCompleteCircuit(gas, cost):
    for start in range(len(gas)):
        fuel = 0
        for i in range(start, len(gas)+start):
            index = i % len(gas)

            can_travel = True
            if gas[index] + fuel < cost[index]:
                can_travel = False
                break
            else:
                fuel += gas[index] - cost[index]
        
        if can_travel:
            return start
    
    return -1


if __name__ == "__main__":
    print(canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))