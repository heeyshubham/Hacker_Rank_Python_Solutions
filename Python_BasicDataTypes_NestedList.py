if __name__ == '__main__':
    records=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
    scr = [x[1] for x in records]
    asc_records=sorted(set(scr))
    stud = sorted([y[0] for y in records if y[1]==asc_records[1]])
    #this is a list comprehension which doesn't create a new list
    [print(k) for k in stud] 
