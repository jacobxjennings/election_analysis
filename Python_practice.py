counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

if "El Paso" in counties:
    print("El Paso is in the list of counties")
else:
    print("El Paso is not in the list of counties.")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties")

else:
    print("Arapahoe and El Paso is not in the list of counties.")


for county in counties:
    print(county)













# temperature = int(input("What is the temperature outside?"))

# if temperature > 80:

#     print("Turn on the AC.")

# else:

#     print("Open the windows.")



# #ELSE IF STATEMENT
# #What is the score?
# score = int(input("What is your test score?"))

# #Determine the grade.
# if score >= 90:

#     print('Your grade is an A.')

# else:
#     if score >= 80:
#         print('Your grade is a B.')
#     else:
#         if score >= 70:
#             print('Your grade is a C')
#         else:
#             if score >= 60:
#                 print("Your grade is a D.")
#             else:
#                 print('Your grade is an F.')

# #ELIF STATEMENT
# #Determine the grade.
# if score >= 90:
#     print('Your grade is an A.')
# elif score >= 80:
#     print('Your grade is a B.')
# elif score >= 70:
#     print('Your grade is a C')
# elif score >= 60:
#     print('Your grade is a D.')

# else:
#     print('Your grade is an F.')

# x = 0
# while x <= 5:
#     print(x)

#     x = x + 1

# numbers = [0,1,2,3,4]
# for num in numbers:
#     print(num)

# for num in range(5):
#     print(num)

# for i in range(len(counties)):
#     print(counties[i])

for county in counties_dict.keys():
    print(county)