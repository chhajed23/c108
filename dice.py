import random
import plotly.express as px
import plotly.figure_factory as ff

dice_result=[]
count_list=[]
for i in range(0,100):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    dice_result.append(dice1+dice2)
    count_list.append(i)


# fig=px.bar(x=dice_result,y=count_list)
# fig.show()
# print("The Sum of the two numbers on the dice is: ",dice_result)
# print(count_list)

fig=ff.create_distplot([dice_result],["Result"],show_hist=False)
fig.show()

