recommend_sleep = int(input())
oversleeping = int(input())
ann_sleeps = int(input())

if ann_sleeps in range(int(recommend_sleep), int(oversleeping)):
    print("Normal")

else:
    if ann_sleeps < recommend_sleep:
        print("Deficiency")

    else:
        if ann_sleeps > oversleeping:
            print("Excess")

        else:
            if ann_sleeps == oversleeping:
                print("Normal")
