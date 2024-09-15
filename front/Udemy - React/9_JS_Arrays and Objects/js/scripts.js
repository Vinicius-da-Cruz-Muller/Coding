// //Arrays

// const lista = [1, 2, 3, 4, 5];

// console.log(lista);

// console.log(typeof lista);

// const items = ["Tyrion Lannister", true, 2, 4.12, [1, 2, 3]];

// console.log(items);

// //mais sobre arrays

// const array = ["a", "b", "c", "d"]
// console.log(array[0]);
// console.log(array[4]);

// //Propriedades
// // São as informações de um objeto

// const numbers = [2, 3 ,4];

// console.log(numbers.length);
// console.log(numbers["length"]);

// //métodos

// const otherNumbers = [1, 2, 3];

// const allNumbers = numbers.concat(otherNumbers);
// console.log(allNumbers);

// const txt = "testando"
// console.log(txt.toUpperCase());
// console.log("IBGE".toLowerCase());
// console.log(typeof txt.toLowerCase());
// console.log(txt.indexOf("a"));

// Objetos
// const person = {
//     name: "Vinícius",
//     age: 24,
//     job: "Desenvolvedor de Software"
// }

// console.log(person); 
// console.log(person.name);
// console.log(person.name.length);

// // Criando e deletando propriedades
// const car = {
//     engine: 2.0,
//     brand:"VW",
//     model: "Tiguan",
//     km: 20000
// };

// console.log(car);
// car.doors = 4; //adicionando propriedade ao objeto
// console.log(car);
// delete car.doors;
// console.log(car);

// //mais sobre objetos
// const obj = {
//     a:"teste",
//     b: true
// };

// console.log(obj instanceof Object); //obj é uma instância de Object?

// const obj2 = {
//     c: []
// }

// Object.assign(obj2, obj); //atribui as propriedades de obj para obj2
// console.log(obj2);

// //Conhecendo melhor sobre objetos

// console.log(Object.keys(obj));
// console.log(Object.keys(obj2));

//Mutação

const a = {
    name: "Cersei "
};

const b = a;

console.log(a);
console.log(b);
console.log(a === b);

a.age = 32;

console.log(a); //idade vai para os dois
console.log(b); 

delete b.age;

console.log(a); //apaga nos dois
console.log(b); 

//logo const b = a não é um objeto novo, e sim uma referância

//Loops em arrays, pop, push, shift e unshift e indices

const users  = ["Tywin", "Cersei", "Jaime", "Tyrion"];

for(let i = 0; i < users.length; i++){
    console.log(`Listando o usuário: ${users[i]}`);
}

users.push("Gemma"); //adiciona elemento ao fim do array

console.log(users);

users.pop(); //retira o último elemento do array

console.log(users);

users.unshift("Lann") //adiciona elemento ao início do array

console.log(users);

users.shift() //retira elemento do início do array

console.log(users);

users.push("Tywin");

console.log(users.indexOf("Cersei"));
console.log(users.indexOf("Tywin"));
console.log(users.lastIndexOf("Tywin"));
console.log(users.indexOf("Lann")); //retorna -1 porque o elemento não existe no array

const siblings = users.slice(1,4); //ignora o último, elemento posição 4 não aparece
console.log(siblings); //se for passado apenas um número ao slice, ele cortará dali em diante

//Foreach

const nums = [1, 2, 3, 4, 5];

nums.forEach((numero) => {
    console.log(`O número é ${numero}`);
});

const posts = [
    {title: "Primeiro post", category: "Javascript"},
    {title: "Segundo post", category: "Python"},
    {title: "Terceiro post", category: "Java"},
    {title: "Quarto post", category: "SQL"},
];

posts.forEach((post) => {
    console.log(`Exibindo post: ${post.title}, vai falar sobre ${post.category}`);
});

// Include

const houses = ["Targaryen", "Lannister", "Stark", "Baratheon", "Hightower"];

console.log(houses.includes("Targaryen"));

console.log(houses.includes("Greyjoy"));

if(houses.includes("Lannister")){
    console.log("Existem Lannisters no seu registro!");
}

//Includes confere se existe um elemento no vetor

//Reverse

console.log(houses.reverse());

// Trim

// Trim remove caracteres especiais e espaços em branco de um texto

const trimTeste = " testando \n ";

console.log(trimTeste);
console.log(trimTeste.trim());
console.log(trimTeste.length);
console.log(trimTeste.trim().length);

//Padstart

const digit = "1";

const serial = digit.padStart(4, "0"); //adiciona zeros ao começo até o tamanho máximo de 4

console.log(digit);
console.log(serial);

const chaveSerial = serial.padEnd(8, "0") //adiciona zeros ao final até o tamanho máximo de 8

console.log(chaveSerial);

//split - divide uma string em um array, determinado por um separador;

const frase = "O rato roeu a roupa do rei de Roma"

const fraseSeparada = frase.split(" ")
console.log(fraseSeparada) //separa nos espaços em branco
console.log(frase.split("r")) //separa a cada r minúsculo

//Join
const fraseUnida = fraseSeparada.join(" ")

console.log(fraseUnida);

//Repeat - repete um texto n vezes

console.log("Teste ".repeat(5))

//Rest operator - utilizado para receber um número indefinido de parâmetros em uma função

const somaInfinita = (...args) => {
    let total = 0

    for(let i = 0 ; i < args.length; i++){
        total += args[i];
    }
    return total;
};

console.log(somaInfinita(1, 2, 3));
console.log(somaInfinita(1, 2, 3, 4, 5, 6, 7, 8, 9, 10));

// For...of - semelhante ao for, mas mais simples

const somaInfinita2 = (...args) =>{
    let total = 0;
    for(num of args){
        total += num;
    }
    return total;
};

console.log(somaInfinita2(1, 2, 3, 4, 5, 6, 7, 8, 9, 10));

//Destructuring em objetos
const userDetails = {
    firstName: "Vinícius",
    middleName: "da Cruz",
    lastName: "Muller",
    job: "Desenvolvedor de Software"
};

const {firstName, middleName, lastName, job} = userDetails; //separa cada uma das propriedades em uma variável separada

console.log(firstName, middleName, lastName, job);

const {firstName: primeiroNome} = userDetails; //atribui a propriedade a uma nova variável

console.log(primeiroNome);

//Destructuring em arrays

const myDogs = ["Átila", "Zeus", "Lorde", "Tyrion"];

const [maisVelho, maior, maisRapida, menor] = myDogs; //atribui as variáveis na ordem do vetor, e não por propriedade

console.log(`Meu cachorro mais velho é o ${maisVelho}`);

//JSON

const myJSON = '{"name": "Vinícius", "age": 24, "skills": ["PowerBI", "Python", "Javascript"]}';
//estrutura de um json com string, number e array
//geralmente é recebido de algum lugar, como uma API.
//muitas vezes precisamos converter um JSON para objeto JS ouum objeto JS para JSON
console.log(myJSON);

const myObjeto = JSON.parse(myJSON);
console.log(myObjeto);

// const badJson = '{"name": Matheus}';
// const convertBadJson = JSON.parse(badJson);

const myNewJson = JSON.stringify(myObjeto);
console.log(myNewJson);