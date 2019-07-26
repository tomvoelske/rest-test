import json
import requests


def getdata():

	"""Prints list of users and their associated information via a RESTful get request."""

	requestheaders = {'Content-type': 'application/json', 'Accept': 'application/json'}
	baseurl = 'https://reqres.in/'
	# 999 chosen to brute force to get all members to appear in one data set, since no obvious API documentation
	params = {'per_page': 999}

	r = requests.get(baseurl + 'api/users',
					 params=params,
					 headers=requestheaders)

	if r.status_code == requests.codes.ok:

		# verifies that a response code of 200 is acquired (successful get request)

		rawjson = json.loads(r.text)
		rawdata = rawjson['data']
		print('=' * 10 + ' LIST OF USER INFORMATION ' + '=' * 10 + '\n')
		for data in rawdata:
			id = data['id']
			firstname = data['first_name']
			lastname = data['last_name']
			email = data['email']
			avatar = data['avatar']
			print('ID: {0}\nFIRST NAME: {1}\nLAST NAME: {2}\nEMAIL ADDRESS: {3}\nPROFILE AVATAR URL: {4}\n'.format(id, firstname, lastname, email, avatar))
	else:
		print('Error in connecting!')


if __name__ == '__main__':
	getdata()
