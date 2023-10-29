*** Settings ***
Library    SeleniumLibrary


*** Variables ***
${error message}    Podany login lub hasło są nieprawidłowe. Spróbuj jeszcze raz.


*** Keywords ***
Log in Wikipedia
    [Arguments]      ${login}      ${password}
    Open Browser    https://pl.wikipedia.org    chrome
    Maximize Browser Window
    Run Keyword And Ignore Error    Click Element    id:nieistniejace
    Wait Until Element Is Visible    id:pt-login-2    5
    Click Element    id:pt-login-2
    Input Text    id:wpName1    ${login}
    Input Password    id:wpPassword1    ${password}
    Click Button    id:wpLoginAttempt
    Sleep    5

*** Test Cases ***
Successful login
    Log in Wikipedia     RobotTests     RobotFramework
    Input Text    name:search    Teoria Wielkiego Problemu
    Click Button    xpath=/html/body/div[1]/header/div[2]/div/div/div/form/div/button
    Close Browser

Unsuccessful login
    Log in Wikipedia    xxxx    xxxx
    ${my_error_message}      Get Text    xpath=//*[@id="userloginForm"]/form/div[1]/div
    Log     ${my_error_message}
    Log To Console      ${my_error_message}
    Should Be Equal As Strings    ${my_error_message}    ${error message}
    Close Browser

