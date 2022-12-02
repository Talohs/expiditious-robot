from user_name import hello_name as hn
from counting_up import first_odds as fo
from max_power import max_num_in_list as mn
from leap_year import is_leap_year as ly
from consecutive_num import is_consecutive as ic
import random

hn('USERNAME')
fo()
Hundred = list(range(1, 101))
print(mn(Hundred))
print(ly(random.randint(1, 4000)))
randlist = []
for num in range(1,7):
    rando = random.randint(1,30)
    randlist.append(rando)
print("Your lotto numbers are", randlist)
if (ic(randlist)) == True:
    print("Your a Winner!")
else:
    print("Want to try again?")
print(ic(randlist))
print(ic(Hundred))
