import pandas as pd
df1 = pd.read_csv("juvinileset.csv")
df1["fact1"] = df1["fact1"].map({'Yes':1 ,'No':0})
df1["fact2"] = df1["fact2"].map({'Yes':1 ,'No':0})
df1["fact3"] = df1["fact3"].map({'Yes':1 ,'No':0})
df1["fact4"] = df1["fact4"].map({'Yes':1 ,'No':0})
df1["fact5"] = df1["fact5"].map({'Yes':1 ,'No':0})
#print(df1.sum(axis = 0, skipna = True))....sums of all columns
min_support = 33
print("Associations,exceeding Minimum Support are as follows;")
fact1 = df1['fact1'].sum()
fact2 = df1['fact2'].sum()
fact3 = df1['fact3'].sum()
fact4 = df1['fact4'].sum()
fact5 = df1['fact5'].sum()
if (fact1 > min_support):
  #print('fact1',fact1)
  df1['fact12'] = df1['fact1'] & df1['fact2']
  df1['fact13'] = df1['fact1'] & df1['fact3']
  df1['fact14'] = df1['fact1'] & df1['fact4']
  df1['fact15'] = df1['fact1'] & df1['fact5']
  fact12 = df1['fact12'].sum()
  fact13 = df1['fact13'].sum()
  fact14 = df1['fact14'].sum()
  fact15 = df1['fact15'].sum()
  if (fact12 > min_support):
    print('fact12','Poverty Background','Single Mother',fact12)
    df1['fact123'] = df1['fact12'] & df1['fact3']
    fact123 = df1['fact123'].sum()
    if (fact123 > min_support):
      print('fact123',fact123)
      df1['fact1234'] = df1['fact123'] & df1['fact4']
      fact1234 = df1['fact1234'].sum()
      if (fact1234 > min_support):
        print('fact1234',fact1234)
        df1['fact12345'] = df1['fact1234'] & df1['fact5']
        fact12345 = df1['fact12345'].sum()
        if (fact12345 > min_support):
          print('fact12345',fact12345)        
  if (fact13 > min_support):
    print('fact13','Poverty Background','Single Father',fact13)
    df1['fact134'] = df1['fact13'] & df1['fact4']
    fact134 = df1['fact134'].sum()
    if (fact134 > min_support):
      print('fact134','Poverty Background','Single Father','Orphan',fact134)
      df1['fact1345'] = df1['fact134'] & df1['fact5']
      fact1345 = df1['fact1345'].sum()
      if (fact1345 > min_support):
        print('fact1345',fact1345)
  if (fact14 > min_support):
    print('fact14','Poverty Background','Orphan',fact14)
    df1['fact145'] = df1['fact14'] & df1['fact5']
    fact145 = df1['fact145'].sum()
    if (fact145 > min_support):
      print('fact145',fact145)
  if (fact15 > min_support):
    print('fact15','Poverty Background','Family History',fact15)

   
if (fact2 > min_support):
  #print('fact2',fact2)
  df1['fact23'] = df1['fact2'] & df1['fact3']
  df1['fact24'] = df1['fact2'] & df1['fact4']
  df1['fact25'] = df1['fact2'] & df1['fact5']
  fact23 = df1['fact23'].sum()
  fact24 = df1['fact24'].sum()
  fact25 = df1['fact25'].sum()
  if (fact23 > min_support):
    print('fact23',fact23)
    df1['fact234'] = df1['fact23'] & df1['fact4']
    fact234 = df1['fact234'].sum()
    if (fact234 > min_support):
      print('fact234',fact234)
      df1['fact2345'] = df1['fact234'] & df1['fact5']
      fact2345 = df1['fact2345'].sum()
      if (fact2345 > min_support):
        print('fact2345',fact2345)       
  if (fact24 > min_support):
    print('fact24',fact24)
    df1['fact245'] = df1['fact24'] & df1['fact5']
    fact245 = df1['fact245'].sum()
    if (fact245 > min_support):
      print('fact245',fact245)
  if (fact25 > min_support):
    print('fact25',fact25)

if (fact3 > min_support):
  #print('fact3',fact3)
  df1['fact34'] = df1['fact3'] & df1['fact4']
  fact34 = df1['fact34'].sum()
  if (fact34 > min_support):
    print('fact34','Single Father','Orphan',fact34)
    df1['fact345'] = df1['fact34'] & df1['fact5']
    fact345 = df1['fact345'].sum()
    if (fact345 > min_support):
      print('fact345',fact345) 
  df1['fact35'] = df1['fact3'] & df1['fact5']
  fact35 = df1['fact35'].sum()
  if (fact35 > min_support):
    print('fact35',fact35)
if (fact4 > min_support):
  #print('fact4',fact4)
  df1['fact45'] = df1['fact4'] & df1['fact5']
  fact45 = df1['fact45'].sum()
  if (fact45 > min_support):
    print('fact45',fact45)
#if (fact5 > min_support):
  #print('fact5',fact5)