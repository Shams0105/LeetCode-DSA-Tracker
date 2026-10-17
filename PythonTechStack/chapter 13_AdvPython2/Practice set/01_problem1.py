'''
1. Create two virtual environments, install few packages in the first one. How do you 
create a similar environment in the second one?

S1] firstly went to the practice set folder
S2] Then shift+right click > Open in terminal
S3] virtualenv env1 (cmd env1 : env name)
S4] virtual env2 (cmd env2 : 2nd env name)
S5] Activate env1 : .\ env1\ Scripts\ activate.ps1
S6] Install depedencies like pip install pandas , pyjokes etc in env1
S7] Now create env1 requirements.txt file use:- pip freeze > requirements.txt  (creates requirements.txt auto)
S8] deactivate env2 : simply use : deactivate
S9] Now activate env2 : use - .\ env2\ Scripts\ activate.ps1
S10] Now install env1 requirements in env2 using : pip install -r requirements.txt

'''