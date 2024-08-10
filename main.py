team1_num = 5
team2_num = 6

string1 = "В команде Мастера кода участников: %d !" % team1_num
string2 = "Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num)

print(string1)
print(string2)

score_2 = 42
team1_time = 18015.2

string3 = "Команда Волшебники данных решила задач: {} !".format(score_2)
string4 = "Волшебники данных решили задачи за {} с !".format(team1_time)
print(string3)
print(string4)

score_1 = 40
score_2 = 42
challenge_result = ''
team1_time = 1552.512
team2_time = 2153.31451

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'

tasks_total = 82
time_avg = 45.2

string5 = f"Команды решили {score_1} и {score_2} задач."
string6 = f"Результат битвы: {challenge_result}"
string7 = f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!"

print(string5)
print(string6)
print(string7)
