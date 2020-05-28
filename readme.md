# Gridsingularity Demo
This project is on response of the given task

### Installation
Clone the project form git and follow the following steps

Build docker image:

```
docker build -t demo .
```
Run the test cases.

```
docker run -it demo python /opt/app/src/manage.py test gridsingularity
```
The following project run the project on port 8000

```
docker run --rm -it -p 8000:8000 demo
```

### Api end points

Create a simulation 
Url: http://127.0.0.1:8000/api/v1/simulations/
Method : Post,
On success:
    status: 200,
    response body 
```
    {
    "id": 1,
    "active": "0.10",
    "reactive": "0.05"
}
```
Get a simulation;
Url : http://127.0.0.1:8000/api/v1/simulations/<simulation id>/
Method: Get,
On success
status: 200,
response boday
```
{
    "id": 1,
    "active": "0.10",
    "reactive": "0.05"
}
```
On error:
 status : 404 if not simulation with given id
 
 Read active power 
 Url : http://127.0.0.1:8000/api/v1/simulations/<simulation id>/active/
 
Method: Get,
On success,
status: 200,
response boday
```
{
    "active": "0.10",
}
```
On error:
 status : 404 if not simulation with given id
 
Read reactive power 
 Url : http://127.0.0.1:8000/api/v1/simulations/<simulation id>/reactive/
 
Method: Get,
On success,
status: 200,
response boday
```
{
    "reactive": "0.10",
}
```
On error:
 status : 404 if not simulation with given id
 


