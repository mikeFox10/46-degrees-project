### Curl examples 

### GET /settleup W/O Payload
```
curl --request GET \
  --url http://localhost:8000/settleup \
  --header 'accept: application/json'
```
### GET /settleup W/ Payload
```
curl --request GET \
  --url 'http://localhost:8000/settleup?payload=%7B%20%22users%22%3A%20%5B%22q%22%2C%20%22qq%22%5D%7D' \
  --header 'accept: application/json'
  ```

### post /add

```
curl --request POST \
  --url http://localhost:8000/add \
  --header 'Content-Type: application/json' \
  --data '{
"user" : "test_user"
}'
```


### POST /iou
```
curl --request POST \
  --url http://localhost:8000/iou \
  --header 'Content-Type: application/json' \
  --data '{
"lender" : "new",
"borrower" : "q",
"amount": 500,
"expiration" : "1212-12-12 13:45:12"
}'
```


### POST /expired_iou

```
curl --request POST \
  --url http://localhost:8000/expired_iou \
  --header 'accept: application/json'
```