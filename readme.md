# Music Single View

## Description
Test task providing 2 actions:

- import `csv` file with music meta data records
- API endpoint for getting single view record in `JSON` format by ID (iswc)

## Preparing
 
### database
- run local postgres `pgAdmin`
- create postgres login `user_music_db` with password `musiC.forever`  
- create postgres database `music_db` with owner `user_music_db` 

### software
```
git clone https://gitlab.com/szobin/musicsingleview.git
cd musicsingleview
pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
```

## usage for import `csv` file 

```
python3 manage.py import <filename.csv> [0|1]
```
- filename.csv : input file with music meta data
- [0|1] verbosity 
    - 0 - brief report (default value)
    - 1 - detail report

### ready data to test import
```
python3 manage.py import samples/works_metadata.csv 1
```     

## usage for get single view record
```
python3 manage.py runserver
wget http://localhost:8000/api-get-sv/T0101974597
```

