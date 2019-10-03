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

## Questions

### Describe briefly the matching and reconciling method chosen

Database consist from 3 tables:
   - Single - contain single records
   - Contributor - contain contributor records
   - SingleViewContributors - links one to many from singles to contributors
   
Secondary index for single title help to match fast single by title.
Also secondary index for contributor title works simular
Extended primary index in links table helps to link singles and contributors fast.

### We constantly receive metadata from our providers, how would you automatize the process?

It better to know receive channel. For example, for email channel would offer a automatic service that read mailbox and each time added new records

### Imagine that the Single View has 20 million musical works, do you think your solution would have a similar response time?

Set of embedded indexes allows to work fine for millions of record.
We may have delays only after adding a new record.

### If not, what would you do to improve it?

Suggest to use Mongo database. It's a good solution for this kind of data.
Plus, of course, use redis for cache     