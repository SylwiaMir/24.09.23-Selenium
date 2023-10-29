*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${email}    sylwia@wp.pl
${password}     1@#4G


*** Keywords ***
Open my browser
    Open Browser    https://gotujmy.pl/forum/   chrome
    Maximize Browser Window
    Run Keyword And Ignore Error    Click Button   xpath=//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]
    Sleep    3


*** Test Cases ***
Registration
    Open my browser
    Click Element   xpath=//*[@id="navTop"]/nav/ul[1]/li[2]/a
    Run Keyword And Ignore Error   Click Element    xpath=//*[@id="user_register_form"]/fieldset
    Run Keyword And Ignore Error   Click Element    xpath=/html/body/div[2]/div/div[2]/section/form/fieldset/input[1]
    Input Text      xpath=/html/body/div[2]/div/div[2]/section/form/fieldset/input[1]    ${email}
    Input Text      xpath=/html/body/div[2]/div/div[2]/section/form/fieldset/input[2]    ${email}
    Input Text      xpath=/html/body/div[2]/div/div[2]/section/form/fieldset/input[3]    ${password}
    Input Text      xpath=/html/body/div[2]/div/div[2]/section/form/fieldset/input[4]    ${password}
#   nie zawsze trzeba dawac xpath jak to jest xpath
    Checkbox Should Not Be Selected     //*[@id="newsletter_agree"]
    Select Checkbox     //*[@id="newsletter_agree"]
    Checkbox Should Not Be Selected     //*[@id="user_register_form"]/fieldset/label[2]/input
    Select Checkbox     //*[@id="user_register_form"]/fieldset/label[2]/input
    Checkbox Should Not Be Selected     //*[@id="user_register_form"]/fieldset/label[3]/input
    Select Checkbox        //*[@id="user_register_form"]/fieldset/label[3]/input

    Run Keyword And Ignore Error   Click Element    //*[@id="user_register_form"]/fieldset/footer/button


    Sleep    5