var secctionTitle = 'Titulo de seccion'
document.title = secctionTitle;

sleep(3000).then(() => {
    secctionTitle = 'Nuevo Titulo de seccion'
    document.title = secctionTitle;
    })

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}


let menu = {'a': 1, 'b': 2, 'c' : 3};

for (const [key, value] of Object.entries(menu)) {
  console.log(key, value);
}