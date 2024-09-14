let num = parseInt(prompt())
for (let i = 0; i <= num; i++) {
    for(let j = 0; j < num - i; j++) {
        process.stdout.write(" ");
    }
    for(let k = 0; k < i; k++) {
        process.stdout.write("* ");
    }
    console.log("\n");
}
for (let i = num-1; i >= 1; i--) {
    for (let j = num-i-1; j >= 0; j--) {
        process.stdout.write(" ");
    }
    for (let k = i - 1; k >= 0; k--) {
        process.stdout.write("* ");
    }
    console.log("\n");
}