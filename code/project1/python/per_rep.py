def performance_report_random():
    # make the scores_list of performance
    import random
    scores_idx = [] # students #
    scores_list = [] # scores #
    for i in range(1, 101):
        if 60 % i == 2:
            scores_list.append(random.randint(10, 50)) 
        elif 60 % i == 3:
            scores_list.append(random.randint(51, 79))
        else:
            scores_list.append(random.randint(80, 100))    
    for i in range(len(scores_list)):
        scores_idx.append(i)
            
    # initialization the datas
    average_score = None
    highist_score = None
    highist_scores_idx = None
    lowwist_score = None
    lowwist_scores_idx = None
    long = len(scores_list)
    
    # 1: count the average score
    sum_score = 0
    for i in range(0, long):
        sum_score += scores_list[i]
    average_score = sum_score / long
    
    # 2: count the highist score
    highscores_idx = 0
    for i in range(1, long):
        if scores_list[i] > scores_list[highscores_idx]:
            highscores_idx = i
    highist_scores_idx = highscores_idx
    highist_score = scores_list[highist_scores_idx]
    
    # 3: count the lowist score
    lowscores_idx = 0
    for i in range(1, long):
        if scores_list[i] < scores_list[lowscores_idx]:
            lowscores_idx = i
    lowwist_scores_idx = lowscores_idx
    lowwist_score = scores_list[lowwist_scores_idx]
    
    # output the performance datas
    print("performance:")
    for i in range(long):
        print(f"{scores_idx[i]+1} is {scores_list[i]} point")
    print(f"average score is {average_score}")
    print(f"the highist score is {highist_scores_idx+1}\
 student {highist_score} point")
    print(f"the lowist score is {lowwist_scores_idx+1}\
 student {lowwist_score} point")
    return ""
    
if __name__ == "__main__":
    print(f"Executing {__file__}: {__name__}")
    print(performance_report_random())