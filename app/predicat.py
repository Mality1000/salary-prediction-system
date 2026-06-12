import pandas as pd
import joblib

model = joblib.load("model/salary_model.pkl")
columns = joblib.load("model/model_columns.pkl")

def predict_salary(age, experience, gender,
                   education, location, job_title):

    input_data = pd.DataFrame(0, index=[0], columns=columns)

    input_data["Age"] = age
    input_data["Experience"] = experience

    if gender == "Male":
        input_data["Gender_Male"] = 1

    if education == "High School":
        input_data["Education_High School"] = 1
    elif education == "Master":
        input_data["Education_Master"] = 1
    elif education == "PhD":
        input_data["Education_PhD"] = 1

    if location == "Suburban":
        input_data["Location_Suburban"] = 1
    elif location == "Urban":
        input_data["Location_Urban"] = 1

    if job_title == "Director":
        input_data["Job_Title_Director"] = 1
    elif job_title == "Engineer":
        input_data["Job_Title_Engineer"] = 1
    elif job_title == "Manager":
        input_data["Job_Title_Manager"] = 1

    salary = model.predict(input_data)

    return round(salary[0], 2)