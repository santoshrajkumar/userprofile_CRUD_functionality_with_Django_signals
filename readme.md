# User Profile with CRUD functionality in Django

### Explanation of functionality
- When root directory is accessed, the login page will come up (without login index page can't be viewed). This is the login page. 

![alt text](https://github.com/santoshrajkumar/userprofile_CRUD_functionality_with_Django_signals/blob/master/images/1.png?raw=true)

- If you don't have an account, you can register by clicking 'Sign Up'. This is the sign up page below, here Django signal takes care of the user profile creation with password hashing and other validation checks.
![alt text](https://github.com/santoshrajkumar/userprofile_CRUD_functionality_with_Django_signals/blob/master/images/2.png?raw=true)

- When logged in, one can Read information of all the user profiles (including self) present in the database (index page):
![alt text](https://github.com/santoshrajkumar/userprofile_CRUD_functionality_with_Django_signals/blob/master/images/3.png?raw=true)

- User can view his own profile info and edit his info by clicking in the profile pic present in the nav-bar. THe follwoing is the screenshot. User can edit any field except his username. Also, media functionality is added, so that user can upload his/her profile picture. A default picture of the author is set for all users in the beginning. 
Delete Profile button is also there to delete the own profile of any user.
![alt text](https://github.com/santoshrajkumar/userprofile_CRUD_functionality_with_Django_signals/blob/master/images/4.png?raw=true)

