# testProject
Small little test for the PyCharm IDE to see how integrations are working

To open this project inside PyCharm (VCS --> Checkout from Version Control) and enter https://github.com/awicenec/testProject into the URL box (make sure that the path box underneath is empty beforehand).

## Get started
* Create new project in PyCharm (File --> New Project). Give it a name and let PyCharm generate a virtual environment for you. Open the new project in a new window.
* Enable Git as a version control system (VCS --> Enable Version Control Integration and choose Git)
* Share project on GitHub (this will require an account on GitHub and a configuration of PyCharm to use that). PyCharm will ask you for either a password or a token to login to your GitHub account. It can also directly call the web interface of GitHub to generate a token, if you don't have one, yet.
* Add a new directory: (File --> New --> Directory) and name it test
* Create a new unittest Python file in the test directory: (highlight the test directory in the project tree right click --> New --> Python File --> Python unit test) and name it test_me (or something more useful, but start the name with test_)
* The new unittest file will automatically be opened and populated with a dummy test, which can be run, by clicking on one of the green arrows on the left of the code. The dummy test will fail, because it tries to assert True to False.
* You can also run the actual code by clicking on the small green arrow next to line 13 in the file main.py or by pressing Ctrl + Shift + F10
* You should also always create a README.md file for your project (like this one), describing what this is all about.
* 

