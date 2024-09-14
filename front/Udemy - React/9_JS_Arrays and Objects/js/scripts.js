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

// const a = {
//     name: "Cersei "
// };

// const b = a;

// console.log(a);
// console.log(b);
// console.log(a === b);

// a.age = 32;

// console.log(a); //idade vai para os dois
// console.log(b); 

// delete b.age;

// console.log(a); //apaga nos dois
// console.log(b); 

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
