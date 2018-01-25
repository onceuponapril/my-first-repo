# discussion Section Participation: 13, drop 2
# Homework:14, drop 2
# Lecture exercises:26, drop 4
# midterms:2
# projects:3
# final project:1

# 2.identify and drop lowest grades for:
# discussion
# homeworks 
# lecture exercises 


# 3.total points across categories 
# #get data into program 
# #return: dictionary (keys: assignment group names, values:list of scores) 

# 4 convert to percentage, then convert to letter grade
  

def get_data(data):
# get data into program 
# return: dictionary (keys: assignment group names, values:list of scores)      
     pass


def drop_lowest_scores(list_of_scores,num_to_drop): 
# drop the lowest score in the list of each category
# sort a list by its value then drop the required numbers of lowest ones. 
      pass

def compute_group_total(list_of_scores_drop):
#add all numbers
#return the total number 
      pass

def compute_grade(total_scores):
#convert the numbers to the percentage, and get the grade.
#return the grade level
      pass
      
data_dict=get_data(dict)
homework_scores=drop_lowest_scores(data_dict['homeworks'],2)
lecture_scores=drop_lowest_scores(data_dict['lectures'],4)
discussion_scores=drop_lowest_scores(data_dict['homeworks'],3)
midterm_scores=drop_lowest_scores(data_dict['midterm'],2)
project_scores=drop_lowest_scores(data_dict['projects'],3)
final_score=drop_lowest_scores(data_dict['final'],1)

#test function
def test_functions():
      list1=[10,9,8,7,6]
      expected_return1=[10,9,8]
      expected_return2=[10]
      
      list2=[1,1,1,1,1]
      expected_return3=5      
    
      passed=0
      failed=0
      
      if drop_lowest_scores(list1,2)==expected_return1:
       #test passed
                                           passed +=1
      else:
       #test failed
             failed +=1
             print('failed test 1')
             
      if drop_lowest_scores(list1,4)==expected_return2:
       #test passed
                                           passed +=1
    
      else:
        #test failed
             failed +=1
             print('failed test 1')
             
      if compute_group_total(list2)==expected_return2:
                                          passed +=1
    
      else:
        #test failed
             failed +=1
             print('failed test 1')
        
# openfile=open('507grade.csv', w)
# openfile.write()