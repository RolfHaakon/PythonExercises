# To train for an upcoming marathon, Johnny goes on one long-distance run each Saturday.
# He wants to track how often the number of miles he runs exceeds the previous Saturday. This is called a progress day.
#
# Create a function that takes in a list of miles run every Saturday and returns Johnny's total number of progress days.

def progress_days(list):
    progressDays = 0
    for i in range(0,len(list),2):
        print(i)
        if i == (len(list) - 1):
            break
        if list[i+1] > list[i]:
            progressDays += 1
    return progressDays




print(progress_days([1,2,4,3,5,6]))
print(progress_days([2,1,6,7]))
