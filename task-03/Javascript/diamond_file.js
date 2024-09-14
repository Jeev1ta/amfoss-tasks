const fs = require('fs');
fs.readFile('input.txt', (err, data) => {
    if (err) throw err;
    console.log(data.toString());
    let num = parseInt(data);
    fs.writeFile('output.txt', '', (err) => {
        if (err) throw err;
        let star = " ".repeat(num);
        for (let i = 0; i < num; i++) {
            star = star.slice(1);
            star += " *";
            fs.appendFile('output.txt', star, (err) => {
                if (err) throw err;
            });
        }
        for (let j = 0; j < num; j++) {
            star = star.slice(0, -2);
            star = " " + star;
            fs.appendFile('output.txt', star, (err) => {
                if (err) throw err;
            });
        }

    });
});