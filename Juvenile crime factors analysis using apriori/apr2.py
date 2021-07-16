import pandas as pd
df1 = pd.read_csv("juvinileset.csv")
df1["fact1"] = df1["fact1"].map({'Yes':1 ,'No':0})
df1["fact2"] = df1["fact2"].map({'Yes':1 ,'No':0})
df1["fact3"] = df1["fact3"].map({'Yes':1 ,'No':0})
df1["fact4"] = df1["fact4"].map({'Yes':1 ,'No':0})
df1["fact5"] = df1["fact5"].map({'Yes':1 ,'No':0})
trows = len(df1.index)
#print(trows)
min_support = 33
print("Confidence Measures for associations,exceeding Minimum Support are as follows;")
fact1 = df1['fact1'].sum()
fact2 = df1['fact2'].sum()
fact3 = df1['fact3'].sum()
fact4 = df1['fact4'].sum()
fact5 = df1['fact5'].sum()
supfact1 = fact1/trows
supfact2 = fact2/trows
supfact3 = fact3/trows
supfact4 = fact4/trows
supfact5 = fact5/trows
#print('Support for factom1 is:',supfact1)
#print('Support for factom2 is:',supfact2)
#print('Support for factom3 is:',supfact3)
#print('Support for factom4 is:',supfact4)
#print('Support for factom5 is:',supfact5)
if (fact1 > min_support):
  ##print('fact1',fact1)
  df1['fact12'] = df1['fact1'] & df1['fact2']
  df1['fact13'] = df1['fact1'] & df1['fact3']
  df1['fact14'] = df1['fact1'] & df1['fact4']
  df1['fact15'] = df1['fact1'] & df1['fact5']
  fact12 = df1['fact12'].sum()
  fact13 = df1['fact13'].sum()
  fact14 = df1['fact14'].sum()
  fact15 = df1['fact15'].sum()
  if (fact12 > min_support):
    #print('fact12',fact12)
    print('Confidence for fact12(Poverty Background & Single Mother) is:',float(fact12/fact2))
    #print('Lift for fact12(Poverty Background & Single Mother) is:',float((fact12/fact2)/supfact2))
    df1['fact123'] = df1['fact12'] & df1['fact3']
    fact123 = df1['fact123'].sum()
    if (fact123 > min_support):
      #print('fact123',fact123)
      print('Confidence for fact123 is:',float(fact123/fact3))
      #print('Lift for fact123 is:',float((fact123/fact3)/supfact3))
      df1['fact1234'] = df1['fact123'] & df1['fact4']
      fact1234 = df1['fact1234'].sum()
      if (fact1234 > min_support):
        #print('fact1234',fact1234)
        print('Confidence for fact1234 is:',float(fact1234/fact4))
        #print('Lift for fact1234 is:',float((fact1234/fact4)/supfact4))
        df1['fact12345'] = df1['fact1234'] & df1['fact5']
        fact12345 = df1['fact12345'].sum()
        if (fact12345 > min_support):
          #print('fact12345',fact12345)
          print('Confidence for fact12345 is:',float(fact12345/fact5))
          #print('Lift for fact12345 is:',float((fact12345/fact5)/supfact5))          
  if (fact13 > min_support):
    #print('fact13',fact13)
    print('Confidence for fact13(Poverty Background & Single Father) is:',float(fact13/fact3))
    #print('Lift for fact13(Poverty Background & Single Father) is:',float((fact13/fact3)/supfact3))
    df1['fact134'] = df1['fact13'] & df1['fact4']
    fact134 = df1['fact134'].sum()
    if (fact134 > min_support):
      #print('fact134',fact134)
      print('Confidence for fact134(Poverty Background,Single Father & Orphan) is:',float(fact134/fact4))
      #print('Lift for fact134(Poverty Background,Single Father & Orphan) is:',float((fact134/fact4)/supfact4))
      df1['fact1345'] = df1['fact134'] & df1['fact5']
      fact1345 = df1['fact1345'].sum()
      if (fact1345 > min_support):
        #print('fact1345',fact1345)
        print('Confidence for fact1345 is:',float(fact1345/fact5))
        #print('Lift for fact12 is:',float((fact1345/fact5)/supfact5))
  if (fact14 > min_support):
    #print('fact14',fact14)
    print('Confidence for fact14(Poverty Background & Orphan) is:',float(fact14/fact4))
    #print('Lift for fact14(Poverty Background & Orphan) is:',float((fact14/fact4)/supfact4))
    df1['fact145'] = df1['fact14'] & df1['fact5']
    fact145 = df1['fact145'].sum()
    if (fact145 > min_support):
      #print('fact145',fact145)
      print('Confidence for fact145 is:',float(fact145/fact5))
      #print('Lift for fact12 is:',float((fact145/fact5)/supfact5))
  if (fact15 > min_support):
    #print('fact15',fact15)
    print('Confidence for fact15(Poverty Background & Family History) is:',float(fact15/fact5))
    #print('Lift for fact15(Poverty Background & Family History) is:',float((fact15/fact5)/supfact5))

   
if (fact2 > min_support):
  ###print('fact2',fact2)
  df1['fact23'] = df1['fact2'] & df1['fact3']
  df1['fact24'] = df1['fact2'] & df1['fact4']
  df1['fact25'] = df1['fact2'] & df1['fact5']
  fact23 = df1['fact23'].sum()
  fact24 = df1['fact24'].sum()
  fact25 = df1['fact25'].sum()
  if (fact23 > min_support):
    ##print('fact23',fact23)
    print('Confidence for fact23 is:',float(fact23/fact3))
    #print('Lift for fact23 is:',float((fact23/fact3)/supfact3))
    df1['fact234'] = df1['fact23'] & df1['fact4']
    fact234 = df1['fact234'].sum()
    if (fact234 > min_support):
      ##print('fact234',fact234)
      print('Confidence for fact234 is:',float(fact234/fact4))
      #print('Lift for fact234 is:',float((fact234/fact4)/supfact4))
      df1['fact2345'] = df1['fact234'] & df1['fact5']
      fact2345 = df1['fact2345'].sum()
      if (fact2345 > min_support):
        ##print('fact2345',fact2345)
        print('Confidence for fact2345 is:',float(fact2345/fact5))
        #print('Lift for fact23 is:',float((fact2345/fact5)/supfact5))        
  if (fact24 > min_support):
    ##print('fact24',fact24)
    print('Confidence for fact24 is:',float(fact24/fact4))
    #print('Lift for fact24 is:',float((fact24/fact4)/supfact4))
    df1['fact245'] = df1['fact24'] & df1['fact5']
    fact245 = df1['fact245'].sum()
    if (fact245 > min_support):
      ##print('fact245',fact245)
      print('Confidence for fact245 is:',float(fact245/fact5))
      #print('Lift for fact245 is:',float((fact245/fact5)/supfact5))
  if (fact25 > min_support):
    ##print('fact25',fact25)
    print('Confidence for fact25 is:',float(fact25/fact5))
    #print('Lift for fact25 is:',float((fact25/fact5)/supfact5))

if (fact3 > min_support):
  ##print('fact3',fact3)
  df1['fact34'] = df1['fact3'] & df1['fact4']
  fact34 = df1['fact34'].sum()
  if (fact34 > min_support):
    #print('fact34',fact34)
    print('Confidence for fact34(Single Father & Orphan) is:',float(fact34/fact4))
    #print('Lift for fact34(Single Father & Orphan) is:',float((fact34/fact4)/supfact4))
    df1['fact345'] = df1['fact34'] & df1['fact5']
    fact345 = df1['fact345'].sum()
    if (fact345 > min_support):
      #print('fact345',fact345)
      print('Confidence for fact345 is:',float(fact345/fact5))
      #print('Lift for fact345 is:',float((fact345/fact5)/supfact5))      
  df1['fact35'] = df1['fact3'] & df1['fact5']
  fact35 = df1['fact35'].sum()
  if (fact35 > min_support):
    print('fact35',fact35)
if (fact4 > min_support):
  ##print('fact4',fact4)
  df1['fact45'] = df1['fact4'] & df1['fact5']
  fact45 = df1['fact45'].sum()
  if (fact45 > min_support):
    #print('fact45',fact45)
    print('Confidence for fact45 is:',float(fact45/fact5))
    #print('Lift for fact45 is:',float((fact45/fact5)/supfact5))
#if (fact5 > min_support):
  ##print('fact5',fact5)