'''6. Run pip freeze for the system interpreter. Take the contents and create a similar 
virtualenv.
'''

#SOLUTION
'''
S1] We already have requirements.txt , no need to create it again
S2] however if i wanna i would use :-
    shift right click in the folder path followed by open w terminal
    & using cmd : pip freeze > requirements.txt

S3] Now create a new env named p6env using : virtualenv p6env

S4] Activate it using :  .\p6env\Scripts\activate.ps1

S5] Install the requirements using : pip install -r requirements.txt
'''