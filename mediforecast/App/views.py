from django.shortcuts import render

# Create your views here.
from joblib import load
model = load('final_model.sav')


def predictor(request):
    if request.mehtod=='POST':
        preg=request.POST['preg']
        glucose=request.POST['glu']
        BP=request.POST['BP']
        st=request.POST['ST']
        Insulin=request.POST['Insulin']
        Bmi=request.POST['BMI']
        Dpf=request.POST['DPF']
        Age=request.POST['Age']
        prediction=classifier.predict([[preg,glucose,BP,st,Insulin,Bmi,Dpf,Age]])
        if (prediction [0] == 0):
            prediction='The person is not diabetic'
        else:
            prediction='The person is diabetic'
        return render(request, 'main.html', {'result' : prediction})
    return render(request, 'main.html')