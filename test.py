import os

os.system('git init')
os.system('git remote add origin https://github.expedia.biz/divthakur/testRepo.git')
os.system("git add .")
os.system('git commit -m "{}"'.format("june"))
os.system("git push origin master")