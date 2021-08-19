Feature: OrangeHRM Logo

Scenario: Logo Presence on OrangeHRM home Page
  Given launch chrome browser
  When open Orange Hrm Homepage
  Then verify that the logo present on home page
  And close Browser
