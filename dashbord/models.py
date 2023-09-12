from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from sklearn.tree import DecisionTreeClassifier
from joblib import  load

# Create your models here.
GENDER=(
    (0,'Female'),
    (1,"Male")
)
class Data(models.Model):
    name=models.CharField(max_length=100,null=True)
    age=models.PositiveBigIntegerField(null=True,validators=[MinValueValidator(13),MaxValueValidator(19)])
    height=models.PositiveBigIntegerField(null=True)
    sex=models.PositiveBigIntegerField(choices=GENDER,null=True)
    predictions=models.CharField(max_length=100,blank=True)
    date=models.DateTimeField(auto_created=True)
    
    def save(self,*args,**kwargs):
        ml_model=load('ml_model/ml_sport_model.joblib')
        self.predictions=ml_model.predict([[self.age,self.height,self.sex]])
        return super().save(*args,**kwargs)
    
    class Meta:
        ordering=['-date']
        
    def __str__(self) -> str:
        return self.name    