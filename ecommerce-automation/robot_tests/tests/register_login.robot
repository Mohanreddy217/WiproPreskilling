*** Settings ***
Library     SeleniumLibrary
Library     CSVLibrary
Resource    ../resources/keywords.robot

*** Test Cases ***
Full User Journey From CSV
    ${data}=    Read Csv File To List    users.csv
    FOR    ${row}    IN    @{data}[1:]
        Open Application

        Register User
        ...    ${row}[0]
        ...    ${row}[1]
        ...    ${row}[2]
        ...    ${row}[3]
        ...    ${row}[4]
        ...    ${row}[5]
        ...    ${row}[6]
        ...    ${row}[7]
        ...    ${row}[8]
        ...    ${row}[9]

        Login User
        Search And Add To Cart    ${row}[10]
        Open Cart
        Update Quantity           ${row}[11]
        Logout User

        Close Application
    END