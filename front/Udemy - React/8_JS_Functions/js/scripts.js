// Criando uma função

function minhaFuncao(){
    console.log("Testando");
}

minhaFuncao();

const minhaFuncaoEmVariavel = function(){
    console.log("Função em variável");
};

minhaFuncaoEmVariavel(); //variável constante, logo a função não pode ser sobrescrita;
//Usado para consistência

function funcaoComParametro(txt){
    console.log(`Mostrando em tela: ${txt}`);
}
a = "Frase aleatória de exemplo"
funcaoComParametro(a);
//ou
funcaoComParametro("Frase aleatória de exemplo nova");


//return
const valor = 10;
const valor2 = 20;

function soma(n1, n2){
    return n1 + n2;
}

const resultado = soma(valor, valor2);
console.log(`Resultado = ${resultado}`)
console.log(soma(valor, valor));

//escopo da função
let y = 10;

function testandoEscopo(){
    let y = 20;
    console.log(`Y dentro da função é: ${y}`);
}

testandoEscopo();

console.log(`Y fora da função é: ${y}`);