
print('Week 1 – Code Quality Lab')



def calculate_age_gap(ages, show_age_gap):
          """
          :param ages: collection of ages:
          :param show_age_gap: A Boolean that controls whether the calculated result is displayed.: 
          :return: The calculated total::
          """
          total = 0



    # Calculate the ages using the list of ages 

    for age in ages:
        if age > 10:
            total = total + age
        else:
            total = total - 1

        if show_age_gap:
           print("age_gap is:", total)

        return total


data = [1, 5, 12, 20, 3]
result = calculate_age_gap(data, True)
print(result)


# Question 1: Can you easily identify logic blocks?
# It is difficult to identify the logic loops because poor formatting has made everything tight
# and it is difficult to distinguish different pieces of code.

# Question 2: Are variable names meaningful?
# No,because there isn’t any comment to show what each variable name means.

# Question 3: Would this code be easy to debug?
# No because variable names aren’t explained and the formatting the code
# is poor so someone who hasn’t seen the code wouldn’t be able to repeat the code for himself.
