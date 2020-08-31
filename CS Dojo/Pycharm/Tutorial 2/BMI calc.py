#%%

#BMI calculator activity
#originally the tutorial class only contained two statements, overweight and not overweight
#in order to get more practice, I decided to search for the actual BMI chart
#I then proceeded to write multiple if clauses in order to fit every category
name1= 'Kyle Matthew'
name2= 'Aleksa Chloe'
height_m1= 1.65
height_m2= 1.52
weight_kg1= 62
weight_kg2= 52

#%%

bmi1= weight_kg1/(height_m1**2)
print (name1,'has the bmi value of',bmi1)
if bmi1<18.5:
    print (name1, 'is underweight')
else:
    if bmi1<24.9:
        print (name1, 'is normal weight')
    else:
        if bmi1<29.9:
            print (name1, 'is overweight')
        else:
            if bmi1<34.9:
                print (name1, 'is now in Obesity Class I')
            else:
                if bmi1<39.9:
                    print (name1, 'is now in Obesity Class II')
                else:
                    if bmi1>=40:
                        print (name1, 'is now in Obseity Class III')

#%%
print ("\n")
bmi2= weight_kg2/(height_m2**2)
print (name2,'has the bmi value of',bmi2)
if bmi2<18.5:
    print (name2, 'is underweight')
else:
    if bmi2<24.9:
        print (name2, 'is normal weight')
    else:
        if bmi2<29.9:
            print (name2, 'is overweight')
        else:
            if bmi2<34.9:
                print (name2, 'is now in Obesity Class I')
            else:
                if bmi2<39.9:
                    print (name2, 'is now in Obesity Class II')
                else:
                    if bmi2>=40:
                        print (name2, 'is now in Obseity Class III')
