*** Variables ***
${string}   piesek
@{list}    pierwszy    drugi   trzeci  czwarty piaty  
@{list_of_numbers}   1     2     3    4    5
&{dictionary}   slowo=${string}      numer=30       lista=@{list}
@{imiona}   Kamil   Marta   Sylwia  Adam
@{nazwiska}  Kowalski    Malinowski  Nowak   nijaki

*** Test Cases ***
For Loop In Range 10
    FOR    ${i}    IN RANGE  10
        Log    ${i}
        Log To Console    ${i}
         
    END
For Loop In Range 4-10
    FOR    ${i}    IN RANGE    4    10
        Log    ${i}
        Log To Console    ${i}

    END

For Loop In Range 4-20 Step 3
    FOR    ${i}    IN RANGE    4    20    3
        Log    ${i}
        Log To Console    ${i}

    END

For Loop In List
    FOR    ${item}    IN    @{list_of_numbers}
        Log    ${item}
        Log To Console    ${item}

    END

For Loop In List 2
    FOR    ${item}    IN    @{list_of_numbers}
        IF    ${item}==3    Log     ${item}
    END

For Loop In List Dictionary
    Log     ${dictionary}
    FOR     ${keys_and_values}     IN    &{dictionary}
        Log To Console    ${keys_and_values}
    END