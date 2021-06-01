def gpa_calc():
    bool = True
    data = [];
    # data = [(4,'C+'), (3,'A'), (4,'B'), (4,'B'),
    #         (4,'B+'), (3,'A-'), (4,'A-'), (4,'A-'),
    #         (1,'A'), (2,'A'), (4,'B+'), (3, 'A'), (3, 'A'), (4, 'C'), (4, 'A')]
    stuff = '+-'
    grade = 'ABCDF'
    total= 0
    credits_earned = 0
    
    while bool:
        n = input("Please enter a class, credit count, grade:")
        for i in range(len(n)):
            if (n[i].isnumeric() == True) and ((n[-1]) in stuff):
               data.append((int(n[i]), n[-2] + n[-1]))
            if (n[i].isnumeric() == True) and (n[-1] in grade):
               data.append((int(n[i]), n[-1]))

        if n == 'done':
            bool = False
             
    for elem in data:
        total += elem[0]
        
    for i in range(len(data)):
        if data[i][1] == 'A':
            credits_earned += 4 * data[i][0]
        elif data[i][1] == 'A-':
            credits_earned += 3.7 * data[i][0]
        elif data[i][1] == 'B+':
            credits_earned += 3.3 * data[i][0]
        elif data[i][1] == 'B':
            credits_earned += 3.0 * data[i][0]
        elif data[i][1] == 'B-':
            credits_earned += 2.7 * data[i][0]
        elif data[i][1] == 'C+':
            credits_earned += 2.3 * data[i][0]
        elif data[i][1] == 'C':
            credits_earned += 2.0 * data[i][0]
        elif data[i][1] == 'C-':
            credits_earned += 1.7 * data[i][0]
        elif data[i][1] == 'D+':
            credits_earned += 1.3 * data[i][0]
        elif data[i][1] == 'D':
            credits_earned += 1.0 * data[i][0]
        elif data[i][1] == 'D-':
            credits_earned += 0.7 * data[i][0]
        elif data[i][1] == 'F':
            credits_earned += 0 * data[i][0]

    
    return credits_earned / total
    
    
    
def main():
    # the class cannot have numbers in it
    print(gpa_calc())
    
    
main()