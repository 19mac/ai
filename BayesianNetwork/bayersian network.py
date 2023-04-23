def main():
    print("Bayessian Network\n")
    l = int(input("Enter the total no. of levels in your network: "))
    level = {}
    dependency = {}
    event = {}
    for i in range(l):
        level[i] = list(input(f"Enter nodes at level {i}:").strip().split())
        if i != 0:
            for j in level[i]:
                dependency[j] = [x for x in level[i-1]]
        else:
            for j in level[i]:
                dependency[j] = []
    probability = {}
    print(dependency, level)

    probability = {}
    for key, value in dependency.items():
        event[key] = bool
        if len(value) == 0:
            print(f"Enter True probability of {key}:")
            probability[key] = list(map(float, input().strip().split()))
        if len(value) == 1:
            print(f"Enter T and F probabilty of {dependency[key]} for True of {key}")
            probability[key] = list(map(float, input().strip().split()))
        if len(value) == 2:
            print(f"Enter TT, TF, FT, FF probability of {dependency[key]} for True of {key}:")
            probability[key] = list(map(float, input().strip().split()))

    print(probability,"probability")
    while True:
        print("\nEnter events values: (True/False)")
        for i in event:
            event[i] = input(f"Event of {i}: ") == "True"
        cal = {}
        print(event,"event")
        for key, value in dependency.items():
            if len(value) == 0:
                if event[key]:
                    cal[key] = probability[key][0]
                elif not event[key]:
                    cal[key] = 1.0 - probability[key][0]
            if len(value) == 1:
                print(event[value[0]])
                if event[key] and event[value[0]]:
                    cal[key] = probability[key][0]
                elif event[key] and not event[value[0]]:
                    cal[key] = probability[key][1]
                elif not event[key] and event[value[0]]:
                    cal[key] = 1 - probability[key][0]
                elif not event[key] and not event[value[0]]:
                    cal[key] = 1 - probability[key][1]
            if len(value) == 2:
                if event[key] and event[value[0]] and event[value[1]]:
                    cal[key] = probability[key][0]
                elif event[key] and event[value[0]] and not event[value[1]]:
                    cal[key] = probability[key][1]
                elif event[key] and not event[value[0]] and event[value[1]]:
                    cal[key] = probability[key][2]
                elif event[key] and not event[value[0]] and not event[value[1]]:
                    cal[key] = probability[key][3]
                elif not event[key] and event[value[0]] and event[value[1]]:
                    cal[key] = 1 - probability[key][0]
                elif not event[key] and event[value[0]] and not event[value[1]]:
                    cal[key] = 1 - probability[key][1]
                elif not event[key] and not event[value[0]] and event[value[1]]:
                    cal[key] = 1 - probability[key][2]
                elif not event[key] and not event[value[0]] and not event[value[1]]:
                    cal[key] = 1 - probability[key][3]
        print(f"Probaility: {cal}")
        solution = 1.0
        for val in cal.values():
            solution *= val
        print(f"The probability for given scenario is {solution}")
        stop = input("Do you wish to stop?(y/n)").lower().strip() == "y"
        if stop:
        	break
main()
