// 1 - Console, tipos e operadores
console.log(typeof(2))
console.log(typeof("teste"))
console.log(5 * (4+12))
console.log(typeof(NaN))
console.log(typeof(Infinity))
console.log(typeof(1==1))
console.log(typeof(false))
console.log(typeof(30 > 10))

// Strings
console.log("Um texto")
console.log('Mais um texto')
console.log(`E mais um texto`)

// Símbolos especiais
console.log("Texto escrito em \nduas linhas")

// Concatenação e interpolação (template strings)
console.log("Texto" + " mais texto")
console.log(`A soma de dois mais dois é: ${2+2}`)

// Comparações
console.log(5<3)
console.log(5>=5)

// Comparações com idênticos
console.log(9 == "9")
console.log(9 + "9")
console.log(9 === "9")
console.log(9 != "9")
console.log(9 !== "9")

// Operadores lógicos
console.log(true && true) //and
console.log(true || false) //or
console.log(!true)//negação

// null e undefined
console.log(typeof null, typeof undefined)
console.log(null === undefined)
console.log(undefined == false)

// Mudança de tipos
console.log(5*null)
console.log("10" + 1)
console.log("10" - 1)