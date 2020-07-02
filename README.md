 ```
git clone git@github.com:sumukhah/bank-service.git
cd back-service
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
to get information about the branch, visit 
```
http://localhost:8000/<IFSC_CODE>/ 
eg:- http://localhost:8000/ZSBL0000341/
```

 to get information of all the braches in that city, visit 
```
http://localhost:8000/<BANK_NAME>/<CITY>/  
eg:- http://localhost:8000/ZILA_SAHAKRI_BANK_LIMITED_GHAZIABAD/MODINAGAR/
```
