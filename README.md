<h1> Desafio utilizando Django</h1> 

<p> Esse desafio foi resolvido utilizando django</p>
<p> Para rodar o servidor adequadamente, é necessário um ambiente com django instalado</p>

<h2> Dependencias </h2> 
<p> Utilize <code> python -m virtualenv venv</code> para a criação de um ambiente virtual</p>

<h2> Depencias Python </h2> 
<p> Instale todas as dependencias python com o comando <code> pip install -r requirements.txt</code></p> 

<h2> Rodando o servidor</h2> 
<p> Antes de colocarmos o servidor para funcionar, precisamos primeiro de alguns comandos</p> 
<p> O primeiro comando a ser usado será o <code> python manage.py makemigrations</code> para ser feito a migração do banco de dados</p>
<p> O proximo comando será o <code> python manage.py migrate </code></p>
<p> Temos também de criar um super usuario para podermos acessar a tela de admin do django, crie com o comando <br/> 
<code> python manage.py createsuperuser</code> e coloque as informações. </p> 
<p> E por fim, podemos rodar o servidor com o comando <code> python manage.py runserver</code> </p> 

<h2> Acessando o django-admin</h2> 
<p> Para acessar o Django-admin entre em <code> localhost:8000/admin</code> e acesse com a conta criada pelo <i> superuser</i>
