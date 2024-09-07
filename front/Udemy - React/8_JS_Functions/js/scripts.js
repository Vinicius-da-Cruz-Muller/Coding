// Criando uma função

// function minhaFuncao(){
//     console.log("Testando");
// }

// minhaFuncao();

// const minhaFuncaoEmVariavel = function(){
//     console.log("Função em variável");
// };

// minhaFuncaoEmVariavel(); //variável constante, logo a função não pode ser sobrescrita;
// //Usado para consistência

// function funcaoComParametro(txt){
//     console.log(`Mostrando em tela: ${txt}`);
// }
// a = "Frase aleatória de exemplo"
// funcaoComParametro(a);
// //ou
// funcaoComParametro("Frase aleatória de exemplo nova");


// //return
// const valor = 10;
// const valor2 = 20;

// function soma(n1, n2){
//     return n1 + n2;
// }

// const resultado = soma(valor, valor2);
// console.log(`Resultado = ${resultado}`)
// console.log(soma(valor, valor));

// //escopo da função
// let y = 10;

// function testandoEscopo(){
//     let y = 20;
//     console.log(`Y dentro da função é: ${y}`);
// }

// testandoEscopo();

// console.log(`Y fora da função é: ${y}`);

// //Escopo aninhado - nested scope

// let m = 10;

// function escopoAninhado(){
//     let m = 20;

//     if (true){
//         let m = 30;
//         if(true){
//             let m = 40;

//             console.log(m);
//         }
//         console.log(m);
//     }
//     console.log(m);
// }

// escopoAninhado();
// console.log(m);

//arrow function
//é uma função anônima - deve estar dentro de uma variável

// const testArrow = () =>{
//     console.log("Esta é uma arrow function");
// };

// testArrow();

// const parOuImpar = (n) =>{
//     if(n % 2 === 0){
//         console.log("par");
//         return;
//     }
//     console.log("impar")
// };

// parOuImpar(5);
// parOuImpar(10);

// const raiz = (x) => {
//     return x * x;
// }

// console.log(raiz(4));

// //versão mais resumida de uma arrow function abaixo:

// const raiz2 = (x) => x * x;

// console.log(raiz2(5));

// console.log(raiz2(13));

//Parametros opcionais

// const multiplication = function(m, n){
//     if(n === undefined){
//         return m * 1;
//     }else{
//         return m * n;
//     }
// };

// console.log(multiplication(5));
// console.log(multiplication(3, 4));

// const greeting = (name) =>{
//     if(!name){
//         console.log("Olá!")
//         return;
//     }
//     console.log(`Olá, ${name}!`);
// };

// greeting();
// greeting("Vinícius")

// //argumentos padrão - default

// const customGreeting = (name, greet = "Olá") => { //se nenhum argumento for passado para greet, ele usará o valor Olá
//     return `${greet}, ${name}!`
// };

// console.log(customGreeting("Fulano"));
// console.log(customGreeting("Tywin", "Saudações"))

// const repeatText = (text, repeat = 2) => {
//     for(let i = 0; i < repeat; i++){
//         console.log(text);
//     }
// };

// repeatText("Texto");

// repeatText("Teste", 5);

// //closure

// function someFunction(){
//     let txt = "Alguma coisa";

//     function display(){
//         console.log(txt)
//     }
//     display();
// }

// someFunction();

// //motivos pra usar: subdividir funções

// const multiplicaClosure = (n) => {
//     return(m) => {
//         return n * m;
//     };
// };
  
// const c1 = multiplicaClosure(5);
// const c2 = multiplicaClosure(10);

// console.log(c1);
// console.log(c2);
// console.log(c1(5));
// console.log(c2(10));

//recursão

const untilTen = (n, m) => {
    if(n < 10){
        console.log("A função parou de executar!");
    }else{
        const x = n - m;
        console.log(x);
        untilTen(x, m);
    }
};

untilTen(100, 9);

function fatorial(x){
    if(x === 0){
        return 1;
    }else{
        return x * fatorial(x - 1);
    }
}

console.log(fatorial(5));