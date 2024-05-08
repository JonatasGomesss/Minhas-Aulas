function calcular(altura) {
    var peso = Number(document.getElementById('peso').value)
    var altura = Number(document.getElementById('altura').value)
    var imfo = document.getElementById('imfo')

    var result = peso /( altura * altura)

    imfo.innerHTML = `seu imc é de${result.toFixed(2)}`
}