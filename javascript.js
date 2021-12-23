//sample 1
for (let i = 0; i < 10; i++) {
    console.log(i, Math.pow(2, i))
}
//sample 2
function factorial(num) {
    if (num <= 1) {
        return 1
    } else {
        return num * factorial(num - 1)
    }
}

result = factorial(4)
console.log(result)

//sample 3

function validate(num) {
    if (num < 1 || num > 9) {
        console.log('Out of range')
    } else if (num != parseInt(num)) {
        console.log('Not an integer')
    } else {
        console.log('Just right')
        return true
    }
    return false
}

console.log(validate(-5))
console.log(validate(15))
console.log(validate(-5.2))
console.log(validate(2))
