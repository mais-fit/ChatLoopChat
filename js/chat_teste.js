document.getElementById("send").onclick = () => {
    const from = document.getElementById("from").value;
    const to = document.getElementById("to").value;
    const msg = document.getElementById("msg").value;

    fetch(new URL('https://ur8rdiwar9.execute-api.sa-east-1.amazonaws.com/Testes'), {
        method: 'POST',
        headers: new Headers({
            "Accept": "application/json",
            "Content-Type": "application/json"
        }),
        body: JSON.stringify({from, to, msg}),
    }).then(response => {
        if(response.status == 400 || response.status == 404){
            response.json().then(error => alert(error.error))
        }
    }).catch(err => {
        console.log(err)
    })
}