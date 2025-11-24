def quiz():
    dict={'what is user name':"hithesh","what is 2+2":"4","where is amrita":"coimbatore","which is capital of TN":"chennai"}
    marks=0
    for q,a in dict.items():
        print(q)
        ans=input("enter the ans for the question")
        an=ans.lower()
        if an==a:
            print("correct")
            marks=marks+1
        else:
            print("wrong")
    print("total marks ",marks)
quiz()