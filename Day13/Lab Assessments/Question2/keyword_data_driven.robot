*** Settings ***
Test Template    Login Validation

*** Test Cases ***
Valid Login        Admin    admin123    pass
Invalid Login      Admin    wrongpass   fail
Unknown User       User     user123     fail

*** Keywords ***
Login Validation
    [Arguments]    ${username}    ${password}    ${expected}
    Log    Username=${username}, Password=${password}, Expected=${expected}
    Run Keyword If    '${expected}' == 'pass'    Log    Login Successful
    Run Keyword If    '${expected}' == 'fail'    Log    Login Failed
