def solution(answers):
    answer = []
    three = [[ 1, 2, 3, 4, 5],[2, 1, 2, 3, 2, 4, 2, 5],[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    count_list = []
    
    for one in three:
        i=0
        j=0
        count=0
        while i<len(answers):
            if answers[i]==one[j]:
                count+=1
            i+=1
            
            if j==len(one)-1:
                j=0
                
            else:
                j+=1
                
        count_list.append(count)
        
    for i,v in enumerate(count_list):
        if v == max(count_list):
            answer.append(i+1)
            
    return answer
