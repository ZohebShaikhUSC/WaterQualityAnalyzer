import pickle

model= None
def get_predicted_potability(ph,Hardness,Solids,Chloramines,Sulfate,Conductivity,Organic_carbon,Trihalomethanes,Turbidity):
    water_potability= model.predict([[ph,Hardness,Solids,Chloramines,Sulfate,Conductivity,Organic_carbon,Trihalomethanes,Turbidity]])
    if water_potability[0]==0:
        return "Water is not safe to consume."
    else:
        return "Water is safe to consume."

def load_saved_artifacts():
    print("load saved artifacts.")
    global model
    with open("./artifacts/WaterPortabilityModel.pickle","rb") as f:
        model=pickle.load(f)
    print("loaded artifacts succesfully")


if __name__=="__main__":
    load_saved_artifacts()
    print(get_predicted_potability(6.9,200,18000,7.5,200,400,10.5,70.6,1.5))
