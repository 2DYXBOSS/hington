
function activesd(dedre) {
    let dataz = JSON.parse(localStorage.getItem("inscpce"));
    localStorage.removeItem("inscpce");
    fetch('/redsete', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ data: dataz })
        
    })
    .then(data => {
        
        console.log('Data successfully sent to Python:', data);
        

        window.location.href = `/${dedre}`;
    })
    .catch(error => {
        console.error('Error sending data to Python:', error);
    });
}

let tabUsere = JSON.parse(localStorage.getItem("inscpce"))
let etdrdvhe = document.querySelector(".etdrdvhe");
let taer = 0

tabUsere.forEach((i) => {
    
    taer+=1
    console.log(taer,"dfsjhklds");
    etdrdvhe.innerHTML = taer 
})