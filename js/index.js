document.getElementById("btn-cadastro").onclick = function(e){
    e.preventDefault()
    window.location = './pages/cadastro.html'
}

const url2 = 'https://jchr8izlq0.execute-api.sa-east-1.amazonaws.com/getusuarios';
var request = new XMLHttpRequest();
request.open("GET", url2, true);


document.getElementById("btn-entrar").onclick = function(e){
    e.preventDefault()
    usuario = document.getElementById("login").value;
    senha = document.getElementById("inputPassword").value;
    validarLogin(usuario, senha)
}

var retorno = null;

request.onload = function() {
    var data = JSON.parse(this.response);
    if(request.status == 200){
        retorno = data;
        document.getElementById("login").value = data['usuarios'][0]['login']
        document.getElementById("inputPassword").value = data['usuarios'][0]['password']
    }
  }
  request.send();

function validarLogin(login, password) {
    
    if (login != retorno['usuarios'][0]['login'] || password != retorno['usuarios'][0]['password'] ){
        alert("Usuário ou senha incorretos")
    } else {
        window.location = './pages/main.html'
    }
    
}