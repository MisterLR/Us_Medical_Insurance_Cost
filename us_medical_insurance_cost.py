# import csv for working with files
import csv

# create lists for our data
ages_list = []
regions_list = []
insurance_cost = []
smoker_list = []
gender_list = []
bmi_list = []
children_list = []
charges_list = []
# create dictionary filled with lists of data
stats_dict = {
    "age": ages_list,
    "sex": gender_list,
    "bmi": bmi_list,
    "num_of_children": children_list,
    "smoker": smoker_list,
    "region": regions_list,
    "charges": charges_list
}
# open file what we will work with
with open('insurance.csv') as insurance_csv:
    file_reader = csv.reader(insurance_csv)
    for value in file_reader:
        # add values to their lists
        ages_list.append(value[0]) 
        bmi_list.append(value[2])
        children_list.append(value[3])
        regions_list.append(value[5])
        charges_list.append(value[6])
        # add value for smoker or non-smoker
        if value[4] == "yes":
            value[4] = 1
            smoker_list.append(value[4])
        else:
            value[4] = 0
            smoker_list.append(value[4])
        # add value for male or female
        if value[1] == "female":
            value[1] = 0
            gender_list.append(value[1])
        else:
            value[1] = 1
            gender_list.append(value[1])

# make lists values from strings to int or float

ages_list = list(map(int, ages_list))
bmi_list = list(map(float, bmi_list))
children_list = list(map(int, children_list))


class Person:
    # searching for average age
    def average_age(self):
        avg_age = 0
        count = 0
        for age in stats_dict.get("age"):
            count += 1
            avg_age = int(sum(ages_list)/count)
        print("Average age is "+ str(avg_age) + " years.")
        
        
    

    # searching for where the majority of the individuals are from
    def individuals_from(self):
        south_west = 0
        south_east = 0
        north_west = 0
        north_east = 0

        for region in stats_dict.get("region"):
            if region == "southwest":
                south_west += 1
            elif region == "southeast":
                south_east += 1
            elif region == "northwest":
                north_west += 1
            elif region == "northeast":
                north_east += 1
                
                
        if south_west > south_east and south_west > north_west and south_west > north_east:
            print("The majority of the individuals are from southwest.")
        elif south_east > south_west and south_east > north_west and south_east > north_east:
            print("The majority of the individuals are from southeast.")
        elif north_west > south_east and north_west > south_west and north_west > north_east:
            print("The majority of the individuals are from northwest.")
        elif north_east > south_east and north_east > south_west and north_east > north_west:
            print("The majority of the individuals are from northeast.")
            
    
        
    # calculate insurance cost depending on smoke person or not 

    def smoke_insurance_cost(self):
        smoker_insurance_cost = 0
        non_smoker_insurance_cost = 0
        for value in smoker_list:
            if value == 0:
                non_smoker_insurance_cost += int(250*ages_list[value] - 128*gender_list[value] + 370*bmi_list[value] + 425*children_list[value] - 12500)
            elif value == 1:
                smoker_insurance_cost += int(250*ages_list[value] - 128*gender_list[value] + 370*bmi_list[value] + 425*children_list[value] + 24000 - 12500)
        # check which of the insurance costs are bigger
        if non_smoker_insurance_cost > smoker_insurance_cost:
            print("The non-smoker insurance cost is bigger than smoker and it is bigger on "+ str(non_smoker_insurance_cost-smoker_insurance_cost) + " dollars.")
        else:
            print("The smoker insurance cost is bigger than non-smoker and it is bigger on "+ str(smoker_insurance_cost-non_smoker_insurance_cost) + " dollars.")
            
            
            
    # average age among people who have at least 1 child
    
    def avg_age_child(self):
        for age in stats_dict.get("age"):
            avg_age = 0
            count = 0
            for number in children_list:
                if number >= 1:
                    count += 1
                    avg_age = int(sum(ages_list)/count)
        print("Average age of people who have at least 1 child is "+ str(avg_age) + " years.")
            

    

# create an instance of the class and call out methods
person = Person()
person.average_age()
person.individuals_from()
person.smoke_insurance_cost()
person.avg_age_child()