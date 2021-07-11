# MSM project 

## setup your virtual environment
1. ``` $ sudo pip install virtualenv ```
2. go to path you want to make your virtual environment
python -m venv myenv
4. ```$ path../> cd myenv/Scripts```
5. ```$ path../myenv/Scripts>/activte.bat ```
6. go to Hospital-msm-master file

## install all requirements
7. ```$ pip install -r requirements.txt``` 

## apply database migration
8. ```$ python manage.py migrate```

## run the server
9. ```$ python manage.py runserver```

