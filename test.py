import os

os.system('git init')
os.system('git remote set-url origin https://github.com/singhimanshu123456/testrepo.git')
#os.system('git config --global user.name "{}"'.format("hilnu"))
#os.system('git config --global user.email "{}"'.format("t-hilnu@expediagroup.com"))

os.system("git add .")
os.system('git commit -m "{}"'.format("june"))
os.system("git push origin master")