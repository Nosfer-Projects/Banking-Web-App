# Banking-site
Web application created with:
HTML, CSS, Bootstrap, Python, Flask, Postgresql

When we run the page, we see this:

![1](https://user-images.githubusercontent.com/114942472/202913824-f61474d7-8412-4815-a974-ba47e5e7fadd.jpg)

We have homepage, about and login into site.

Section "About":
There is a few news about company.

![2](https://user-images.githubusercontent.com/114942472/202913898-84709a04-f3a2-4389-a0c6-9a2f9647c8f0.jpg)


Section Log in :

![3](https://user-images.githubusercontent.com/114942472/202913941-890b4d80-2130-492f-80b9-28d4380bfd56.jpg)


I have created two users in the database:
admin and admin2.
Lets go into admin.
As we can see, the data is taken from the previous database on the server for the admin client:

![4](https://user-images.githubusercontent.com/114942472/202913990-e9b34119-4414-44a7-9216-d39f1f55792a.jpg)


This is what a simple database looks like before any change:


![5](https://user-images.githubusercontent.com/114942472/202914243-12f40e64-f5ae-4883-b11b-a12bc3e8973e.jpg)


After pressing the "Fast Transfer" button, a window appears where we can enter the recipient's account and the amount, in this case we entered $ 100


![6](https://user-images.githubusercontent.com/114942472/202914392-632f42bb-1388-483a-a72a-2cd484932837.jpg)



After pressing "Accept", a green note appears at the top that everything went as it should and the amount is deducted from the client's account


![7](https://user-images.githubusercontent.com/114942472/202914456-002b9b32-6ca7-4d16-b6b4-b62471f4159a.jpg)


When we refresh PostgreSQL, the amount for a specific client has also been updated:



![8](https://user-images.githubusercontent.com/114942472/202914505-0fc32507-2f56-4887-8696-14d10f95e089.jpg)



When we log out and log back in, the program will check the database and display the current customer data.


