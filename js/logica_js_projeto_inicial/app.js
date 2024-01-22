alert("Boas vindas ao jogo do número secreto!");
let numeroSecreto = 4;
console.log(numeroSecreto)
let chute;
let tentativas = 1;

while(numeroSecreto != chute){
    chute = prompt("Insira um número entre 1 e 10");
        if(chute == numeroSecreto){
            alert(`Isso aí, você descobriu o número secreto (${numeroSecreto} com ${tentativas})!`);
        }else{
            if(numeroSecreto > chute){
                alert('O número é maior que ' + chute);
            }else{
                alert("O número é menor que " + chute);
            }
            tentativas++;
        }
}