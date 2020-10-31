cd 'path_name'
git init
git add .
git status
git commit
git clone --mirrorhttps://github.com/JC12958/PersonalProjects
git remote add origin 'https://github.com/JC12958/PersonalProjects'

vim filenamegit gi
----------
clear
pwd                         <present working directory
cd "File path"
cd ..
mkdir "File path\FolderName"
rm -r "test"
------------------------
vim test/my.txt
press i to start insert
:w
:q
mv </folder/current file> <folder/catnew target file>
 cat test/MyNew.txt
-------------------------
navigate first to the folder you want to initiate
git init
git config --global --edit
:wq
git commit --amend --edit

git log
git log --oneline
git log --graph
------------------------------
echo "# vwino" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/JC12958/vwino.git
git push -u origin main

-----------existing repo
git remote set-url origin https://github.com/JC12958/vwino.git
git remote https://github.com/JC12958/vwino.git
(authenticae connection in github via browser, will automatically open it)
git remote add origin https://github.com/JC12958/vwino.git
git branch -M main
git push -u origin main

ssh-keygen
then enter password
cat ~/.ssh/id_rsa
