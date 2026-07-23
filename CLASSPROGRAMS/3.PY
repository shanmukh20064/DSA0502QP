import pandas as pd
data = {
    "Employee_ID":[101,101,102,103,103,103],
    "Job_ID":["AC_ACCOUNT","AC_MGR","IT_PROG","SA_REP","SA_MAN","HR_REP"]
}
df = pd.DataFrame(data)
result = df["Employee_ID"].value_counts()
print(result[result>=2])