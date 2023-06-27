# Scms
 Scms is a School Management System written in python using django framework.


## Usage

You can run this project on local machine using this command
```
python manage.py runserver
```
and then view the output in browser at `http://127.0.0.1:8000`

- You can change School Name to your own by changing value of `schoolName` key in `baseData` dictionary in `manager/views.py` file.
- Use `username : admin` and `password : 1234` for staff login portal.
- You can also create more staff users by using this command 
```
python manage.py createsuperuser
```
- If you find error `unable to get timezone with key UTC` then run this command
```
pip install tzdata
```
and run the server again.



## Contributing

Contributions are always welcome!

Clone this repository and start improving this project.Make pull requests when you are done with changes.


## Support

For support, email manjindersingh02708@gmail.com or open an issue on GitHub.

