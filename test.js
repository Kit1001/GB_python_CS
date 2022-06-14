// Решил задачу превращая число из массива в соответствующий символ из таблицы Unicode.

// создаем массив а из 200 целых чисел от 0 до 1000
let a = [];
for (let i = 0; i < 200; i++){
  a.push(Math.floor(Math.random()*1000))
}

// функция сериализации превращает числа в знак unicode, соответствующий номеру
function Serialize(arr){
  return arr.map(el => String.fromCharCode(el)).join('')
}

// функция десериализации проделывает обратную операцию
function Deserialize(string){
  return string.split('').map(el => el.charCodeAt())
}

let b = Serialize(a)
let c = Deserialize(b)

// результат - переменная b содержит строку длинной 200 символов, при десериализации все элементы массива а равны элементам массива с
console.log(b.length)
console.log(JSON.stringify(a) === JSON.stringify(c))
