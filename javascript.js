for (let i = 0; i < 10; i++) {
    console.log(i, Math.pow(2, i))
}

function factorial(num) {
    if (num <= 1) {
        return 1
    } else {
        return num * factorial(num - 1)
    }
}

result = factorial(4)
console.log(result)