*** Settings ***
Library    SeleniumLibrary
Library    DataDriver    testdata.xlsx
Test Template    OrangeHRM Login With Excel


*** Variables ***
${URL}       https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${BROWSER}   firefox


*** Keywords ***
OrangeHRM Login With Excel
    [Arguments]    ${username}    ${password}
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Sleep    5s

    Input Text    name=username    ${username}
    Input Text    name=password    ${password}
    Sleep    3s
    Capture Page Screenshot

    Click Button    xpath=//button[@type='submit'}
    Sleep    5s
    Capture Page Screenshot

    Close Browser


*** Test Cases ***
TC006_DDExcel_Login