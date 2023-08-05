# custom-qase-client
This is an unofficial client [QASE](https://qase.io)

Official client: https://github.com/qase-tms/qase-python

API QASE: https://developers.qase.io/reference/

Guide: https://developers.qase.io/docs

#### How to work
First, get api token from page https://app.qase.io/user/api/token (See guide)

For body and params use dict type, like in [requests](https://requests.readthedocs.io/en/latest/user/quickstart/#more-complicated-post-requests) library

```python
client = QaseClient(api_token='YOUR_API_TOKEN')

code = 'TEST_CODE' #projecet code
# create project
body = {'title': f'Title test project', 'code': code, 'access': 'all'}
client.projects.create(body=body)

# create suite
body = {"title": "test suit"}
client.suites.create(code=code, body=body)

# create case
body = {"title": "test case"}
client.cases.create(code=code, body=body)

# create test run
body = {"title": "test run"}
client.runs.create(code=code, body=body)

# upload attachment
client.attachments.upload(code, "./cat.jpeg")

# finish test run
client.runs.complete(code=code, uuid=1)

```

In work ...
