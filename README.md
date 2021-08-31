# testProject
Small little test for the PyCharm IDE to demonstrate the setup of a project, including GitHub version control and testing.

To open this project inside PyCharm (VCS --> Checkout from Version Control) and enter https://github.com/awicenec/testProject into the URL box (make sure that the path box underneath is empty beforehand).

## Get started
* Create a new project in PyCharm (File --> New Project). Give it a name and let PyCharm generate a virtual environment for you. Open the new project in a new window.
* Enable Git as a version control system (VCS --> Enable Version Control Integration and choose Git)
* Share project on GitHub (this will require an account on GitHub and a configuration of PyCharm to use that). PyCharm will ask you for either a password or a token to login to your GitHub account. It can also directly call the web interface of GitHub to generate a token, if you don't have one, yet.
* Add a new directory: (File --> New --> Directory) and name it test
* Create a new unittest Python file in the test directory: (highlight the test directory in the project tree right click --> New --> Python File --> Python unit test) and name it test_me (or something more useful, but start the name with test_)
* The new test file will automatically be opened and populated with a dummy test, which can be run, by clicking on one of the green arrows on the left of the code. The dummy test will fail, because it tries to assert True to False.
* You can also run the actual code by clicking on the small green arrow next to line 13 in the file main.py or by pressing Ctrl + Shift + F10
* You should also always create a README.md file for your project (like this one), describing what this is all about.

## Version Control
* Now the project has all it needs for a start, and you can commit your changes to the version control system (VCS, in our case we are using Git).
* A Version Control System tracks all your changes to every file in the whole project and allows you to go back, produce branches and tag releases. You can view the history of all changes over time for a single file or the whole project. This is very useful even just for yourself, in addition it is possible to do that in collaboration with multiple people working on the same code.
* Git is a distributed VCS and you can work just by yourself, or together with other people and in addition there is a cloud based repository where you can store and share your projects, which is called GitHub.
* To commit your changes locally you can simply click on the small little green tick, close to the upper right corner of the PyCharm window. The system will ask you for a short commit message, explaining in very short terms what had been done to the code. If you are working just for yourself, that is it. 
* If you are sharing the project with others or on GitHub, you can also Push the changes to the remote repository. That is the small little, upwards pointing green arrow next to the commit tag.
* It is good practice running your tests before pushing the changes, just to make sure that the code is working correctly.

## Testing
* Speaking about tests: It is not just good practice, but almost vital in the longer run to write and maintain tests. 
* Tests are snippets of code, which exercise functions and behaviour of the code in your project. 
* Some people are practicing so-called test-driven development. They are writing tests first and then write the code until the tests are passing. 
* In many cases tests are written alongside the code.
* This example project contains a few tests in the test directory to show how tests are written.
* If you would change the string 'World' in main.py to 'Universe' and run the tests again, the test_something_else test will fail, because you have changed the expected default behaviour of the program.

