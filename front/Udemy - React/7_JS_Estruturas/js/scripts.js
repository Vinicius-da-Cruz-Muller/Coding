// // Variáveis
// let nome = "Vinícius";
// console.log(nome);

// nome = "Vinícius da Cruz Muller"
// console.log(nome)

// const idade = 24;
// console.log(idade);

// // Mais sobre variáveis
// let a = 5, b = 6, c = 7; //evitar declarar variáveis assim, pois resume demais
// console.log(a, b, c);

// let _teste = "ok";
// let $teste = "ok";
// console.log(_teste, $teste)

// // Função prompt
// // const age = prompt("Digite a sua idade:")
// // console.log(`Você te ${age} anos.`)

// // Função alert
// // alert("Testando")
// // Prompt e alert não são tão profissionais, por isso evite usá-las!!

// // Math - é um objeto que possui diversasd funções para fins matemáticos
// console.log(Math.max(1, 2, 3, 4, 5));
// console.log(Math.floor(3.14));
// console.log(Math.ceil(3.14));

// // console
// console.error("Erro!")
// console.warn("Aviso!")

// IF, ELSE IF E ELSE

// const m = 5;

// if(m > 5){
//     console.log("M maior que 5");
// }else if(m < 5){
//     console.log("M menor que 5");
// }else{
//     console.log("M é igual a 5")
// }

// // estruturas de repetição
// let p = 0;

// WHILE

// while(p < 5){
//     console.log(`Repetindo ${p}`);
//     p = p + 1;
// }

// DO WHILE
// let o = 10;

// do{
//     console.log(`Valor de o: ${o}`);
//     o--;
// }while(o > 0);

// FOR

// for(let t = 0; t <= 10; t++){
//     console.log(`Repetindo algo...${t}`)
// }

// SWITCH

const job = "Advogado";

switch(job){
    case "Programador":
        console.log("Você é um programador");
        break
    case "Advogado":
        console.log("Você é um advogado");
        break
    default:
        console.log("Você é desempregado kkkkk");

}