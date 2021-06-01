# learndjango
…or create a new repository on the command line
echo "# hellos" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Developer-Felix/hellos.git
git push -u origin main
…or push an existing repository from the command line
git remote add origin https://github.com/Developer-Felix/hellos.git
git branch -M main
git push -u origin main


http post http://127.0.0.1:8000/api-token-auth/ username=ben password=1234
http http://localhost:8081/api/user/ "Authorization: a6e3365a644068b79c52426e14339aeb4d1cd218"
