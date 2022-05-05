from array import array

from sqlalchemy import false, true


weight = [10, 8, 6, 7, 2, 1]
cases = [["senha", weight[0]], ["ajuda da senha", weight[1]], ["número do telefone", weight[2]], ["nomes", weight[3]], ["email", weight[4]], ["data do vazamento", weight[5]]]
cases_companies = [["Adobe", cases[4], cases[1], cases[0], cases[3], [0,2013]], 
["Canva", cases[4], cases[0], cases[3], [0,2019], cases[3]], 
["Apollo", cases[4], cases[3], cases[2], [0,2018], cases[4]], 
["PDL", cases[4], cases[3], cases[2], [0,2019], [0,0]], 
["Hurb",cases[4], cases[3], cases[0], cases[2], [0,2019], [0,0]]]
ranking_score = [[],[],[],[],[]]
i = 0
c = 0
z = 0
result = [['Adobe'], ['Canva'], ['Apollo'], ['PDL'], ['Hurb']]

def calculate(case, key):
  if key == 0:
    ranking_score[key].append(case[1])
  elif key == 1:

    ranking_score[key].append(case[1])
  elif key == 2:

    ranking_score[key].append(case[1])
  elif key == 3:

    ranking_score[key].append(case[1])  
  else:

    ranking_score[key].append(case[1])
  

def ranking(total, key):
  result[key].append(total)


  

while i < 5:
  for k in range(6):
    if k == 0:
      ranking_score[i].append(cases_companies[i][k])
    else:
      calculate(cases_companies[i][k], i)
  i = i + 1


while c < 5:
  total = 0
  for x in range(5):
    x = x + 1
    total = total + ranking_score[c][x]
  if x == 5:
    ranking(total, c)
    
  c = c + 1

finally_result = [[result[0][1]], [result[1][1]], [result[2][1]], [result[3][1]], [result[4][1]]]

finally_result.sort(reverse= True)

while z < 5:
  for fn in finally_result:
    if fn[0] == result[z][1]:
      fn.append(result[z][0])
  z = z + 1

print(finally_result)