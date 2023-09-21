if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    avg=0.00
    for k in student_marks.keys():
        if(k==query_name):
            score = student_marks[k]
            for i in range(len(score)):
                avg+=score[i]
    avg/=3
    print("%.2f" %avg)
