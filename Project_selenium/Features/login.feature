Feature: OrangeHRM Login

Scenario: Login to Orangehrm with valid parameters
  Given launch the chrome browser
  When open  Homepage
  Then Enter username "admin" and password "admin123"
  And click on login button
  Then user must successfully login to the Dashboard
