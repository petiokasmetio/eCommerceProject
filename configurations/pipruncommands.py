#pytest -v -s
#pytest -v -s --browser chrome
#pytest -v -s --browser firefox
#pytest -v -s -n=2 --browser chrome
#pytest -v -s -n=2 --browser firefox
#pytest -v -s -n=2
#pytest -v -s --html=Reports/report.html --browser chrome
#pytest -v -s --html=Reports/report.html --browser firefox
#pytest -v -s --html=Reports/report.html
#pytest -v -s -n=2 --html=Reports/report.html --browser chrome
#pytest -v -s -n=2 --html=Reports/report.html --browser firefox
#pytest -v -s -n=2 --html=Reports/report.html
#pytest -v -s --html=Reports/report.html #run all test cases in current folder and create report
#pytest -v -s --html=Reports/report.html TestCases/test_loginPageDDT.py #run selected test case and create report
#pytest -s -v -m "sanity and regression"       #run specific group of test cases
