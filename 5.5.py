import string
resource = list(enumerate(list(string.ascii_uppercase), start = 1))
#li = ["MARY","PATRICIA","LINDA","BARBARA","ELIZABETH","JENNIFER","MARIA","SUSAN","MARGARET","DOROTHY","LISA","NANCY","KAREN","BETTY","HELEN","SANDRA","DONNA","CAROL","RUTH","SHARON","MICHELLE","LAURA","SARAH","KIMBERLY","DEBORAH","JESSICA"]

with open('/home/thinhcm/Desktop/pyfml1606/p022_names.txt') as f:
    li = f.read()
#print(li)

#calculate score of words function
def score_words(li):
    count = 0
    result, score_list = [], []
    for i in li:
        count += 1
        if count <= len(list(i)):
            result = [index for j in list(i) for index, item in resource if item == j]
            score_list.append(sum(result))
            del result[:]
    return score_list

total_score = sum(index * score for index in range(1, len(li)) for score in score_words(li))
    
print(total_score)