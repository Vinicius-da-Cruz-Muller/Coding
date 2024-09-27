// Métodos
const animal = {
    nome: "Bob",
    latir: function(){
        console.log("Au au")
    }
};

console.log(animal.nome);

animal.latir();

const pessoa = {
    nome: "Vinícius",
    getNome: function(){
        return this.nome
    },
    setNome: function(novoNome){
        this.nome = novoNome;
    }
};

console.log(pessoa.nome)
console.log(pessoa.getNome())
pessoa.setNome("Paul");

console.log(pessoa.getNome())

//Prototypes
//é uma espécie de herança, onde objetos filhos herdam propriedades dos pais
const text = "Lorem ipsum"

console.log(Object.getPrototypeOf(text)) //possível para qualquer tipo de dado


const myObject = {
    a: "b"
};

console.log(Object.getPrototypeOf(myObject));
console.log(Object.getPrototypeOf(myObject) === Object.prototype);

const mySecondObject = Object.create(myObject);
console.log(mySecondObject);
console.log(mySecondObject.a);
console.log(Object.getPrototypeOf(mySecondObject) === myObject);

//Classes básicas
const cachorro = {
    raca: null,
    patas: 4
};

const pastor_alemao = Object.create(cachorro);
pastor_alemao.raca = "Pastor Alemão"

console.log(pastor_alemao);
console.log(pastor_alemao.patas)

//Classes baseadas em funções construtoras
//Utilizando funções como classes, conseguimos iniciar as propriedades com a criação do objeto
//Chamamos esse recurso de função construtora
//O construtor tem como objetivo instanciar um objeto, ou seja, criar um novo objeto

function criarCachorro(nome, raca){
    const cachorro = Object.create({});
    cachorro.nome = nome;
    cachorro.raca = raca;

    return cachorro;
}

const bob = criarCachorro("Bob", "Vira-lata");
const zeus = criarCachorro("Zeus", "Pitbull")

console.log(bob);
console.log(zeus);

//new - instanciar novos objetos
function Cachorro(nome, raca){
    this.nome = nome;
    this.raca = raca;
}
const husky = new Cachorro("Ozzy", "Husky");

console.log(husky);

//Classes de funções com métodos ou métodos na função construtora
 Cachorro.prototype.uivar = function(){
    console.log("Auuuuu!");
 };

 husky.uivar();

 //Classes ES6 - versão mais atual do JS
 class Dog{
    constructor(nome, raca){
        this.nome = nome,
        this.raca = raca
    }
 }

 const jeff = new Dog("Jeff", "Labrador");
 console.log(jeff)

 //Não podemos adicionar propriedades diretamente as classes, isso deve ser feito ao inicia-la ou via prototype
class Caminhao{
    constructor(eixos, cor){
        this.eixos = eixos,
        this.cor = cor
    }
    descreverCaminhao(){
        console.log(`Este caminhão tem ${this.eixos} eixos e é da cor ${this.cor}`);
    }
}

const scania = new Caminhao(6, "Vermelha");
console.log(scania);

scania.descreverCaminhao();

Caminhao.prototype.motor = 4.0 //jeito de incluir uma nova propriedade a classe

console.log(scania.motor)


//Override
class Humano{
    constructor(nome, idade){
        this.nome = nome,
        this.idade = idade
    }
}

const vini = new Humano("Vinicius", 24);

console.log(vini);
console.log(Humano.prototype.idade);
Humano.prototype.idade = "Não definida"
console.log(vini.idade);
console.log(Humano.prototype.idade);


//Symbol - em classes, cria propriedade única e imutável
class Aviao{
    constructor(marca, turbinas){
        this.marca = marca,
        this.turbinas = turbinas
    }
}

const asas = Symbol()
Aviao.prototype[asas] = 2

const boeing = new Aviao("Boeing", 10);
console.log(boeing); 
console.log(boeing[asas]);
