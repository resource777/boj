def solution(genres, plays):
    answer = []
    dic = {}
    for i in range(len(genres)):
        if genres[i] in dic:
            dic[genres[i]][0]+=plays[i]
            dic[genres[i]][1].append((plays[i],i))
        else:
            dic[genres[i]]=[]
            dic[genres[i]].append(plays[i])
            dic[genres[i]].append([(plays[i],i)])
    for item in dic.items():
        item[1][1].sort(key = lambda x : (-x[0],x[1]))
        #print(item[1][1])
    sorted_dict = sorted(dic.items(), key = lambda x : -x[1][0])
    #print(sorted_dict)
    for line in sorted_dict:
        cnt=0
        for ele in line[1][1]:
            answer.append(ele[1])
            cnt+=1
            if cnt==2:
                break
    return answer