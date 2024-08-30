
let tabUsere = JSON.parse(localStorage.getItem("inscpce"))
let etdrdvhe = document.querySelector(".etdrdvhe");
let taer = 0

if (tabUsere) {
    tabUsere.forEach((i) => {
    
        taer+=1
        etdrdvhe.innerHTML = taer
    
    })
}

let red = document.querySelector('#red')
if (red){
    red.style.background = 'red';
}

let blue = document.querySelector('#blue')
if (blue){
    blue.style.background = 'blue';
}
let yellow = document.querySelector('#yellow')
if (yellow){
    yellow.style.background = 'yellow';
}
let green = document.querySelector('#green')
if (green){
    green.style.background = 'green';
}
let orange = document.querySelector('#orange')
if (orange){
    orange.style.background = 'orange';
}


let ecran = document.querySelector('#ecran')
let image0 = document.querySelector('#image0')
let image0Input = document.querySelector('#image0Input').value
let image1 = document.querySelector('#image1')
let image1Input = document.querySelector('#image1Input').value
let image2 = document.querySelector('#image2')
let image2Input = document.querySelector('#image2Input').value
let image3 = document.querySelector('#image3');
let image3Input = document.querySelector('#image3Input').value;


let im1 = document.querySelector('#im1')
let im2 = document.querySelector('#im2')
    

image0.addEventListener('click',()=>{
    ecran.src = `/static/uploads/${image0Input}`

    // ecran.style.background = `url(/static/uploads/${image0Input}) 50% no-repeat `
    // ecran.style.backgroundSize= "cover";
    image1.style.border = "none"
    image3.style.border = "none"
    image2.style.border = "none"
    image0.style.border = "2px solid black"

}

)
image1.addEventListener('click',()=>{
   
    ecran.src = `/static/uploads/${image1Input}`
    image2.style.border = "none"
    image3.style.border = "none"
    image0.style.border = "none"
    image1.style.border = "2px solid black"
}

)
image2.addEventListener('click',()=>{
   
    ecran.src = `/static/uploads/${image2Input}`
    image1.style.border = "none"
    image3.style.border = "none"
    image0.style.border = "none"
    image2.style.border = "2px solid black"

}

)
image3.addEventListener('click',()=>{
   
    ecran.src = `/static/uploads/${image3Input}`
    image1.style.border = "none"
    image2.style.border = "none"
    image0.style.border = "none"
    image3.style.border = "2px solid black"

}

)




const aee = document.querySelector('#hdhdj')
const hdhdj2 = document.querySelector('#hdhdj2')
const menu = document.querySelector('.menu')
const recherche = document.querySelector('.recherche')
const imsdghde1 = document.querySelector('.imsdghde1')
const imsdghde12 = document.querySelector('.imsdghde12')

const bww = document.querySelector('.menuddg')
let dd = document.querySelector('#ecran')


aee.addEventListener('click',()=>{
    bww.classList.add('active');
    aee.classList.add('active');
    hdhdj2.classList.add('active');
   
});
hdhdj2.addEventListener('click',()=>{
    hdhdj2.classList.remove('active');
    bww.classList.remove('active');
    aee.classList.remove('active');
   
});
imsdghde1.addEventListener('click',()=>{
    recherche.classList.add('active');
    imsdghde1.classList.add('active');
    imsdghde12.classList.add('active');
    
   
});
imsdghde12.addEventListener('click',()=>{
    recherche.classList.remove('active');
    imsdghde1.classList.remove('active');
    imsdghde12.classList.remove('active');
    
   
});




const boutonshd = document.querySelector("#boutonshd")
if (boutonshd){
    boutonshd.addEventListener('click',()=>{
        
        // let tabUsere = JSON.parse(localStorage.getItem("inscpce")) || []
        // let image = document.querySelector(".image").value
        // let noumeme = document.querySelector(".noumeme").value
        // let prix = document.querySelector(".prix").value
        // let quantite = document.querySelector("#quantiteplos").value
        // let categorie = document.querySelector("#categorie").value
        // let data = {"image":image,"tailed" : "","produite":noumeme,"prixtottal":prix,"quantiteto":quantite,"xs":"","xsn":"","s":"","sn":"","l":"","ln":"","m":"","mn":"","xl":"","xln":"","xxl":"","xxln":"","tranwite":"","tranwiten":"","tranneuf":"","tranneufn":"","karente":"","karenten":"","tranwiteun":"","tranwiteunn":"","tranwitedeux":"","tranwitedeuxn":"","tranwitrois":"","tranwitroisn":"","tranwitekate":"","tranwitekaten":""}
        
        
        let nom = document.querySelector(".nom").value
        let desccopte = document.querySelector(".desccopte").value
        let image = document.querySelector(".image").value
        let noumeme = document.querySelector(".noumeme").value
        let prix = document.querySelector(".prix").value
        let quantite = document.querySelector("#quantiteplos").value
        let porce = document.querySelector(".porce").value
        let porceprix = document.querySelector(".porceprix").value
        let categorie = document.querySelector(".categorie").value
        let tabUsere = JSON.parse(localStorage.getItem("inscpce")) || []
        // let tabUsere = []
        if (categorie=="Montre") {
            let cometrh = 0
            tabUsere.forEach((user) =>{
                let taillepoe = document.querySelector(".taillepoe").value
                let i = user["data"]
                if (parseInt(i.produite) === parseInt(noumeme) && i.tailed === taillepoe) {
                    cometrh+=1
                    
                    i.quantiteto = parseInt(i.quantiteto || 0) + parseInt(quantite);
                    
                    localStorage.setItem("inscpce", JSON.stringify(tabUsere));
                    console.log("les articles", i);
                    window.location.href = "/monpanier";
                    
                }
            })
            if (cometrh<1) {
                let taillepoe = document.querySelector(".taillepoe").value
                // tabUsere = JSON.parse(localStorage.getItem("inscpce")) || []
                let ideler = 0
                tabUsere.forEach(i => {
                    let user = i["data"]
                    if ( parseInt( user["position"] )>= ideler) {
                        ideler = parseInt(user["position"]) + 1
                    }
                    
                });
                let data = {"desccopte":desccopte,"name":nom,"position":ideler,"image":image,"tailed" : taillepoe,"produite":noumeme,"categorie":categorie,"porce":porce,"porceprix":porceprix,"prixtottal":prix,"quantiteto":quantite,"xs":"","xsn":"","s":"","sn":"","l":"","ln":"","m":"","mn":"","xl":"","xln":"","xxl":"","xxln":"","tranwite":"","tranwiten":"","tranneuf":"","tranneufn":"","karente":"","karenten":"","tranwiteun":"","tranwiteunn":"","tranwitedeux":"","tranwitedeuxn":"","tranwitrois":"","tranwitroisn":"","tranwitekate":"","tranwitekaten":""}  
                let usere = {
                    data : data ,
                }
                tabUsere.push(usere)
                localStorage.setItem('inscpce',JSON.stringify(tabUsere))
                console.log('Data successfullyz sent to Python:', data);
                window.location.href = "http://127.0.0.1:5005/monpanierls"
            }
            
        }

        if (categorie=="VetementFemme"){

            let snume = document.querySelector("#snumq");
            let xsnumq = document.querySelector("#xsnumq")
            let xlnumq = document.querySelector("#xlnumq")
            let xxlnumq = document.querySelector("#xxlnumq")
            let lnumq = document.querySelector("#lnumq")
            let mnumq = document.querySelector("#mnumq")

            if (snume)  {
                let cometrh = 0
                tabUsere.forEach((user) =>{
                    let taillepoe = document.querySelector(".taillepoes").value
                    let i = user["data"]
                    if (parseInt(i.produite) === parseInt(noumeme) && i.tailed === taillepoe) {
                        cometrh+=1
                        
                        i.quantiteto = parseInt(i.quantiteto || 0) + parseInt(quantite);
                        
                        localStorage.setItem("inscpce", JSON.stringify(tabUsere));
                        console.log("les articles", i);
                        window.location.href = "/monpanier";
                        
                    }
                })


                if (cometrh<1) {
                    let snume1 = parseInt(snume.value)
                    if (snume1 > 0){
                        // let tabUsere = []
                        
                        let taillepoe = document.querySelector(".taillepoes").value
                        let ideler = 0

                        tabUsere.forEach(i => {
                            let user = i["data"]
                            if ( parseInt( user["position"] )>= ideler) {
                                ideler = parseInt(user["position"]) + 1
                            }
                            
                        });
                        let data = {"desccopte":desccopte,"name":nom,"position":ideler,"image":image,"tailed" : taillepoe,"produite":noumeme,"categorie":categorie,"porce":porce,"porceprix":porceprix,"prixtottal":prix,"quantiteto":snume1,"xs":"","xsn":"","s":"s","sn":snume1,"l":"","ln":"","m":"","mn":"","xl":"","xln":"","xxl":"","xxln":"","tranwite":"","tranwiten":"","tranneuf":"","tranneufn":"","karente":"","karenten":"","tranwiteun":"","tranwiteunn":"","tranwitedeux":"","tranwitedeuxn":"","tranwitrois":"","tranwitroisn":"","tranwitekate":"","tranwitekaten":""}  
                        let usere = {
                            data : data ,
                        }
                        tabUsere.push(usere)
                        localStorage.setItem('inscpce',JSON.stringify(tabUsere))
                        console.log('Data successfullyz sent to Python:', data);
                        // window.location.href = "http://127.0.0.1:5005/monpanierls"
                    }
                }
            }
            if (xsnumq)  {
                let cometrh = 0
                tabUsere.forEach((user) =>{
                    let taillepoe = document.querySelector(".taillepoexs").value
                    let i = user["data"]
                    if (parseInt(i.produite) === parseInt(noumeme) && i.tailed === taillepoe) {
                        cometrh+=1
                        
                        i.quantiteto = parseInt(i.quantiteto || 0) + parseInt(quantite);
                        
                        localStorage.setItem("inscpce", JSON.stringify(tabUsere));
                        console.log("les articles", i);
                        window.location.href = "/monpanier";
                        
                    }
                })
                if (cometrh<1) {
                let xsnumq1 = parseInt(xsnumq.value)
                if (xsnumq1 > 0){
                    // let tabUsere = []
                    let taillepoe = document.querySelector(".taillepoexs").value
                    let ideler = 0
                    tabUsere.forEach(i => {
                        let user = i["data"]
                        if ( parseInt( user["position"] )>= ideler) {
                            ideler = parseInt(user["position"]) + 1
                        }
                        
                    });
                    let data = {"desccopte":desccopte,"name":nom,"position":ideler,"image":image,"tailed" : taillepoe,"produite":noumeme,"categorie":categorie,"porce":porce,"porceprix":porceprix,"prixtottal":prix,"quantiteto":xsnumq1,"xs":"xs","xsn":xsnumq1,"s":"s","sn":"","l":"","ln":"","m":"","mn":"","xl":"","xln":"","xxl":"","xxln":"","tranwite":"","tranwiten":"","tranneuf":"","tranneufn":"","karente":"","karenten":"","tranwiteun":"","tranwiteunn":"","tranwitedeux":"","tranwitedeuxn":"","tranwitrois":"","tranwitroisn":"","tranwitekate":"","tranwitekaten":""}  
                    let usere = {
                        data : data ,
                    }
                    tabUsere.push(usere)
                    localStorage.setItem('inscpce',JSON.stringify(tabUsere))
                    console.log('Data successfullyz sent to Python:', data);
                    // window.location.href = "http://127.0.0.1:5005/monpanierls"
                }
                }
            }
            if (xlnumq)  {
                let cometrh = 0
                tabUsere.forEach((user) =>{
                    let taillepoe = document.querySelector(".taillepoexl").value
                    let i = user["data"]
                    if (parseInt(i.produite) === parseInt(noumeme) && i.tailed === taillepoe) {
                        cometrh+=1
                        
                        i.quantiteto = parseInt(i.quantiteto || 0) + parseInt(quantite);
                        
                        localStorage.setItem("inscpce", JSON.stringify(tabUsere));
                        console.log("les articles", i);
                        window.location.href = "/monpanier";
                        
                    }
                })
                if (cometrh<1) {
                let xlnumq1 = parseInt(xlnumq.value)
                if (xlnumq1 > 0){
                    // let tabUsere = []
                    let taillepoe = document.querySelector(".taillepoexl").value
                    let ideler = 0
                    tabUsere.forEach(i => {
                        let user = i["data"]
                        if ( parseInt( user["position"] )>= ideler) {
                            ideler = parseInt(user["position"]) + 1
                        }
                        
                    });
                    let data = {"desccopte":desccopte,"name":nom,"position":ideler,"image":image,"tailed" : taillepoe,"produite":noumeme,"categorie":categorie,"porce":porce,"porceprix":porceprix,"prixtottal":prix,"quantiteto":xlnumq1,"xs":"xs","xsn":"","s":"s","sn":"","l":"","ln":"","m":"","mn":"","xl":"xl","xln":xlnumq1,"xxl":"","xxln":"","tranwite":"","tranwiten":"","tranneuf":"","tranneufn":"","karente":"","karenten":"","tranwiteun":"","tranwiteunn":"","tranwitedeux":"","tranwitedeuxn":"","tranwitrois":"","tranwitroisn":"","tranwitekate":"","tranwitekaten":""}  
                    let usere = {
                        data : data ,
                    }
                    tabUsere.push(usere)
                    localStorage.setItem('inscpce',JSON.stringify(tabUsere))
                    console.log('Data successfullyz sent to Python:', data);
                    // window.location.href = "http://127.0.0.1:5005/monpanierls"
                }
                }
            }
            if (xxlnumq)  {
                let cometrh = 0
                tabUsere.forEach((user) =>{
                    let taillepoe = document.querySelector(".taillepoexxl").value
                    let i = user["data"]
                    if (parseInt(i.produite) === parseInt(noumeme) && i.tailed === taillepoe) {
                        cometrh+=1
                        
                        i.quantiteto = parseInt(i.quantiteto || 0) + parseInt(quantite);
                        
                        localStorage.setItem("inscpce", JSON.stringify(tabUsere));
                        console.log("les articles", i);
                        window.location.href = "/monpanier";
                        
                    }
                })
                if (cometrh<1) {
                let xxlnumq1 = parseInt(xxlnumq.value)
                if (xxlnumq1 > 0){
                    // let tabUsere = []
                    let taillepoe = document.querySelector(".taillepoexxl").value
                    let ideler = 0
                    tabUsere.forEach(i => {
                        let user = i["data"]
                        if ( parseInt( user["position"] )>= ideler) {
                            ideler = parseInt(user["position"]) + 1
                        }
                        
                    });
                    let data = {"desccopte":desccopte,"name":nom,"position":ideler,"image":image,"tailed" : taillepoe,"produite":noumeme,"categorie":categorie,"porce":porce,"porceprix":porceprix,"prixtottal":prix,"quantiteto":xxlnumq1,"xs":"xs","xsn":"","s":"s","sn":"","l":"","ln":"","m":"","mn":"","xl":"xl","xln":"","xxl":"xxl","xxln":xxlnumq1,"tranwite":"","tranwiten":"","tranneuf":"","tranneufn":"","karente":"","karenten":"","tranwiteun":"","tranwiteunn":"","tranwitedeux":"","tranwitedeuxn":"","tranwitrois":"","tranwitroisn":"","tranwitekate":"","tranwitekaten":""}  
                    let usere = {
                        data : data ,
                    }
                    tabUsere.push(usere)
                    localStorage.setItem('inscpce',JSON.stringify(tabUsere))
                    console.log('Data successfullyz sent to Python:', data);
                    // window.location.href = "http://127.0.0.1:5005/monpanierls"
                }
                }
            }
            if (lnumq)  {
                let cometrh = 0
                tabUsere.forEach((user) =>{
                    let taillepoe = document.querySelector(".taillepoel").value
                    let i = user["data"]
                    if (parseInt(i.produite) === parseInt(noumeme) && i.tailed === taillepoe) {
                        cometrh+=1
                        
                        i.quantiteto = parseInt(i.quantiteto || 0) + parseInt(quantite);
                        
                        localStorage.setItem("inscpce", JSON.stringify(tabUsere));
                        console.log("les articles", i);
                        window.location.href = "/monpanier";
                        
                    }
                })
                if (cometrh<1) {
                let lnumq1 = parseInt(lnumq.value)
                if (lnumq1 > 0){
                    // let tabUsere = []
                    let taillepoe = document.querySelector(".taillepoel").value
                    let ideler = 0
                    tabUsere.forEach(i => {
                        let user = i["data"]
                        if ( parseInt( user["position"] )>= ideler) {
                            ideler = parseInt(user["position"]) + 1
                        }
                        
                    });
                    let data = {"desccopte":desccopte,"name":nom,"position":ideler,"image":image,"tailed" : taillepoe,"produite":noumeme,"categorie":categorie,"porce":porce,"porceprix":porceprix,"prixtottal":prix,"quantiteto":lnumq1,"xs":"xs","xsn":"","s":"s","sn":"","l":"l","ln":lnumq1,"m":"","mn":"","xl":"xl","xln":"","xxl":"xxl","xxln":"","tranwite":"","tranwiten":"","tranneuf":"","tranneufn":"","karente":"","karenten":"","tranwiteun":"","tranwiteunn":"","tranwitedeux":"","tranwitedeuxn":"","tranwitrois":"","tranwitroisn":"","tranwitekate":"","tranwitekaten":""}  
                    let usere = {
                        data : data ,
                    }
                    tabUsere.push(usere)
                    localStorage.setItem('inscpce',JSON.stringify(tabUsere))
                    console.log('Data successfullyz sent to Python:', data);
                    // window.location.href = "http://127.0.0.1:5005/monpanierls"
                }
                }
            }
        
            if (mnumq)  {
                let cometrh = 0
                tabUsere.forEach((user) =>{
                    let taillepoe = document.querySelector(".taillepoem").value
                    let i = user["data"]
                    if (parseInt(i.produite) === parseInt(noumeme) && i.tailed === taillepoe) {
                        cometrh+=1
                        
                        i.quantiteto = parseInt(i.quantiteto || 0) + parseInt(quantite);
                        
                        localStorage.setItem("inscpce", JSON.stringify(tabUsere));
                        console.log("les articles", i);
                        window.location.href = "/monpanier";
                        
                    }
                })
                if (cometrh<1) {
                let mnumq1 = parseInt(mnumq.value)
                if (mnumq1 > 0){
                    // let tabUsere = []
                    let taillepoe = document.querySelector(".taillepoem").value
                    let ideler = 0
                    tabUsere.forEach(i => {
                        let user = i["data"]
                        if ( parseInt( user["position"] )>= ideler) {
                            ideler = parseInt(user["position"]) + 1
                        }
                        
                    });
                    let data = {"desccopte":desccopte,"name":nom,"position":ideler,"image":image,"tailed" : taillepoe,"produite":noumeme,"categorie":categorie,"porce":porce,"porceprix":porceprix,"prixtottal":prix,"quantiteto":mnumq1,"xs":"xs","xsn":"","s":"s","sn":"","l":"l","ln":"","m":"m","mn":mnumq1,"xl":"xl","xln":"","xxl":"xxl","xxln":"","tranwite":"","tranwiten":"","tranneuf":"","tranneufn":"","karente":"","karenten":"","tranwiteun":"","tranwiteunn":"","tranwitedeux":"","tranwitedeuxn":"","tranwitrois":"","tranwitroisn":"","tranwitekate":"","tranwitekaten":""}  
                    let usere = {
                        data : data ,
                    }
                    tabUsere.push(usere)
                    localStorage.setItem('inscpce',JSON.stringify(tabUsere))
                    console.log('Data successfullyz sent to Python:', data);
                    // window.location.href = "http://127.0.0.1:5005/monpanierls"
                }
                }
            }
            window.location.href = "http://127.0.0.1:5005/monpanierls"
            // console.log(xsnume);
        }
        if (categorie=="chaussure"){
            let tranwitenumq = document.querySelector("#tranwitenumq");
            let tranneufnumq = document.querySelector("#tranneufnumq")
            let karentenumq = document.querySelector("#karentenumq")
            let tranwiteunnumq = document.querySelector("#tranwiteunnumq")
            let tranwitedeuxnumq = document.querySelector("#tranwitedeuxnumq")
            let tranwitroisnumq = document.querySelector("#tranwitroisnumq")
            let tranwitekatenumq = document.querySelector("#tranwitekatenumq")
            if (tranwitenumq)  {

                let cometrh = 0
                tabUsere.forEach((user) =>{
                    let taillepoe = document.querySelector(".taillepoetranwite").value
                    let i = user["data"]
                    if (parseInt(i.produite) === parseInt(noumeme) && i.tailed === taillepoe) {
                        cometrh+=1
                        
                        i.quantiteto = parseInt(i.quantiteto || 0) + parseInt(quantite);
                        
                        localStorage.setItem("inscpce", JSON.stringify(tabUsere));
                        console.log("les articles", i);
                        window.location.href = "/monpanier";
                        
                    }
                })
                if (cometrh<1) {
                let tranwitenumq1 = parseInt(tranwitenumq.value)
                if (tranwitenumq1 > 0){
                    // let tabUsere = []
                    let taillepoe = document.querySelector(".taillepoetranwite").value
                    let ideler = 0
                    tabUsere.forEach(i => {
                        let user = i["data"]
                        if ( parseInt( user["position"] )>= ideler) {
                            ideler = parseInt(user["position"]) + 1
                        }
                        
                    });
                    let data = {"desccopte":desccopte,"name":nom,"position":ideler,"image":image,"tailed" : (taillepoe + " ° "),"produite":noumeme,"categorie":categorie,"porce":porce,"porceprix":porceprix,"prixtottal":prix,"quantiteto":tranwitenumq1,"xs":"","xsn":"","s":"","sn":"","l":"","ln":"","m":"","mn":"","xl":"","xln":"","xxl":"","xxln":"","tranwite":"38 ° ","tranwiten":tranwitenumq1,"tranneuf":"","tranneufn":"","karente":"","karenten":"","tranwiteun":"","tranwiteunn":"","tranwitedeux":"","tranwitedeuxn":"","tranwitrois":"","tranwitroisn":"","tranwitekate":"","tranwitekaten":""}  
                    let usere = {
                        data : data ,
                    }
                    tabUsere.push(usere)
                    localStorage.setItem('inscpce',JSON.stringify(tabUsere))
                    console.log('Data successfullyz sent to Python:', data);
                    // window.location.href = "http://127.0.0.1:5005/monpanierls"
                }
                }
            }
            if (tranneufnumq)  {
                let cometrh = 0
                tabUsere.forEach((user) =>{
                    let taillepoe = document.querySelector(".taillepoetranneuf").value
                    let i = user["data"]
                    if (parseInt(i.produite) === parseInt(noumeme) && i.tailed === taillepoe) {
                        cometrh+=1
                        
                        i.quantiteto = parseInt(i.quantiteto || 0) + parseInt(quantite);
                        
                        localStorage.setItem("inscpce", JSON.stringify(tabUsere));
                        console.log("les articles", i);
                        window.location.href = "/monpanier";
                        
                    }
                })
                if (cometrh<1) {
                let tranneufnumq1 = parseInt(tranneufnumq.value)
                if (tranneufnumq1 > 0){
                    // let tabUsere = []
                    let taillepoe = document.querySelector(".taillepoetranneuf").value
                    let ideler = 0
                    tabUsere.forEach(i => {
                        let user = i["data"]
                        if ( parseInt( user["position"] )>= ideler) {
                            ideler = parseInt(user["position"]) + 1
                        }
                        
                    });
                    let data = {"desccopte":desccopte,"name":nom,"position":ideler,"image":image,"tailed" : (taillepoe + " ° "),"produite":noumeme,"categorie":categorie,"porce":porce,"porceprix":porceprix,"prixtottal":prix,"quantiteto":tranneufnumq1,"xs":"","xsn":"","s":"","sn":"","l":"","ln":"","m":"","mn":"","xl":"","xln":"","xxl":"","xxln":"","tranwite":"","tranwiten":"","tranneuf":"39 ° ","tranneufn":tranneufnumq1,"karente":"","karenten":"","tranwiteun":"","tranwiteunn":"","tranwitedeux":"","tranwitedeuxn":"","tranwitrois":"","tranwitroisn":"","tranwitekate":"","tranwitekaten":""}  
                    let usere = {
                        data : data ,
                    }
                    tabUsere.push(usere)
                    localStorage.setItem('inscpce',JSON.stringify(tabUsere))
                    console.log('Data successfullyz sent to Python:', data);
                    // window.location.href = "http://127.0.0.1:5005/monpanierls"
                }
                }
            }
            if (karentenumq)  {
                let cometrh = 0
                tabUsere.forEach((user) =>{
                    let taillepoe = document.querySelector(".taillepoekarente").value
                    let i = user["data"]
                    if (parseInt(i.produite) === parseInt(noumeme) && i.tailed === taillepoe) {
                        cometrh+=1
                        
                        i.quantiteto = parseInt(i.quantiteto || 0) + parseInt(quantite);
                        
                        localStorage.setItem("inscpce", JSON.stringify(tabUsere));
                        console.log("les articles", i);
                        window.location.href = "/monpanier";
                        
                    }
                })
                if (cometrh<1) {
                let karentenumq1 = parseInt(karentenumq.value)
                if (karentenumq1 > 0){
                    // let tabUsere = []
                    let taillepoe = document.querySelector(".taillepoekarente").value
                    let ideler = 0
                    tabUsere.forEach(i => {
                        let user = i["data"]
                        if ( parseInt( user["position"] )>= ideler) {
                            ideler = parseInt(user["position"]) + 1
                        }
                        
                    });
                    let data = {"desccopte":desccopte,"name":nom,"position":ideler,"image":image,"tailed" : (taillepoe + " ° "),"produite":noumeme,"categorie":categorie,"porce":porce,"porceprix":porceprix,"prixtottal":prix,"quantiteto":karentenumq1,"xs":"","xsn":"","s":"","sn":"","l":"","ln":"","m":"","mn":"","xl":"","xln":"","xxl":"","xxln":"","tranwite":"","tranwiten":"","tranneuf":"","tranneufn":"","karente":"40 ° ","karenten":karentenumq1,"tranwiteun":"","tranwiteunn":"","tranwitedeux":"","tranwitedeuxn":"","tranwitrois":"","tranwitroisn":"","tranwitekate":"","tranwitekaten":""}  
                    let usere = {
                        data : data ,
                    }
                    tabUsere.push(usere)
                    localStorage.setItem('inscpce',JSON.stringify(tabUsere))
                    console.log('Data successfullyz sent to Python:', data);
                    // window.location.href = "http://127.0.0.1:5005/monpanierls"
                }
                }
            }
            if (tranwiteunnumq)  {
                let cometrh = 0
                tabUsere.forEach((user) =>{
                    let taillepoe = document.querySelector(".taillepoetranwiteun").value
                    let i = user["data"]
                    if (parseInt(i.produite) === parseInt(noumeme) && i.tailed === taillepoe) {
                        cometrh+=1
                        
                        i.quantiteto = parseInt(i.quantiteto || 0) + parseInt(quantite);
                        
                        localStorage.setItem("inscpce", JSON.stringify(tabUsere));
                        console.log("les articles", i);
                        window.location.href = "/monpanier";
                        
                    }
                })
                if (cometrh<1) {
                    let tranwiteunnumq1 = parseInt(tranwiteunnumq.value)
                    if (tranwiteunnumq1 > 0){
                        // let tabUsere = []
                        let taillepoe = document.querySelector(".taillepoetranwiteun").value
                        let ideler = 0
                        tabUsere.forEach(i => {
                            let user = i["data"]
                            if ( parseInt( user["position"] )>= ideler) {
                                ideler = parseInt(user["position"]) + 1
                            }
                            
                        });
                    let data = {"desccopte":desccopte,"name":nom,"position":ideler,"image":image,"tailed" : (taillepoe + " ° "),"produite":noumeme,"categorie":categorie,"porce":porce,"porceprix":porceprix,"prixtottal":prix,"quantiteto":tranwiteunnumq1,"xs":"","xsn":"","s":"","sn":"","l":"","ln":"","m":"","mn":"","xl":"","xln":"","xxl":"","xxln":"","tranwite":"","tranwiten":"","tranneuf":"","tranneufn":"","karente":"","karenten":"","tranwiteun":"41 ° ","tranwiteunn":tranwiteunnumq1,"tranwitedeux":"","tranwitedeuxn":"","tranwitrois":"","tranwitroisn":"","tranwitekate":"","tranwitekaten":""}  
                        let usere = {
                            data : data ,
                        }
                        tabUsere.push(usere)
                        localStorage.setItem('inscpce',JSON.stringify(tabUsere))
                        console.log('Data successfullyz sent to Python:', data);
                        // window.location.href = "http://127.0.0.1:5005/monpanierls"
                    }
                }
            }
            if (tranwitedeuxnumq)  {
                let cometrh = 0
                tabUsere.forEach((user) =>{
                    let taillepoe = document.querySelector(".taillepoetranwitedeux").value
                    let i = user["data"]
                    if (parseInt(i.produite) === parseInt(noumeme) && i.tailed === taillepoe) {
                        cometrh+=1
                        
                        i.quantiteto = parseInt(i.quantiteto || 0) + parseInt(quantite);
                        
                        localStorage.setItem("inscpce", JSON.stringify(tabUsere));
                        console.log("les articles", i);
                        window.location.href = "/monpanier";
                        
                    }
                })
                if (cometrh<1) {
                    let tranwitedeuxnumq1 = parseInt(tranwitedeuxnumq.value)
                    if (tranwitedeuxnumq1 > 0){
                        // let tabUsere = []
                        let taillepoe = document.querySelector(".taillepoetranwitedeux").value
                        let ideler = 0
                        tabUsere.forEach(i => {
                            let user = i["data"]
                            if ( parseInt( user["position"] )>= ideler) {
                                ideler = parseInt(user["position"]) + 1
                            }
                            
                        });
                        let data = {"desccopte":desccopte,"name":nom,"position":ideler,"image":image,"tailed" : (taillepoe + " ° "),"produite":noumeme,"categorie":categorie,"porce":porce,"porceprix":porceprix,"prixtottal":prix,"quantiteto":tranwitedeuxnumq1,"xs":"","xsn":"","s":"","sn":"","l":"","ln":"","m":"","mn":"","xl":"","xln":"","xxl":"","xxln":"","tranwite":"","tranwiten":"","tranneuf":"","tranneufn":"","karente":"","karenten":"","tranwiteun":"","tranwiteunn":"","tranwitedeux":"42 ° ","tranwitedeuxn":tranwitedeuxnumq1,"tranwitrois":"","tranwitroisn":"","tranwitekate":"","tranwitekaten":""}  
                        let usere = {
                            data : data ,
                        }
                        tabUsere.push(usere)
                        localStorage.setItem('inscpce',JSON.stringify(tabUsere))
                        console.log('Data successfullyz sent to Python:', data);
                        // window.location.href = "http://127.0.0.1:5005/monpanierls"
                    }
                }
            }
            if (tranwitroisnumq)  {
                let cometrh = 0
                tabUsere.forEach((user) =>{
                    let taillepoe = document.querySelector(".taillepoetranwitrois").value
                    let i = user["data"]
                    if (parseInt(i.produite) === parseInt(noumeme) && i.tailed === taillepoe) {
                        cometrh+=1
                        
                        i.quantiteto = parseInt(i.quantiteto || 0) + parseInt(quantite);
                        
                        localStorage.setItem("inscpce", JSON.stringify(tabUsere));
                        console.log("les articles", i);
                        window.location.href = "/monpanier";
                        
                    }
                })
                if (cometrh<1) {
                    let tranwitroisnumq1 = parseInt(tranwitroisnumq.value)
                    if (tranwitroisnumq1 > 0){
                        // let tabUsere = []
                        let taillepoe = document.querySelector(".taillepoetranwitrois").value
                        let ideler = 0
                        tabUsere.forEach(i => {
                            let user = i["data"]
                            if ( parseInt( user["position"] )>= ideler) {
                                ideler = parseInt(user["position"]) + 1
                            }
                            
                        });
                    let data = {"desccopte":desccopte,"name":nom,"position":ideler,"image":image,"tailed" : (taillepoe + " ° "),"produite":noumeme,"categorie":categorie,"porce":porce,"porceprix":porceprix,"prixtottal":prix,"quantiteto":tranwitroisnumq1,"xs":"","xsn":"","s":"","sn":"","l":"","ln":"","m":"","mn":"","xl":"","xln":"","xxl":"","xxln":"","tranwite":"","tranwiten":"","tranneuf":"","tranneufn":"","karente":"","karenten":"","tranwiteun":"","tranwiteunn":"","tranwitedeux":"","tranwitedeuxn":"","tranwitrois":"43 ° ","tranwitroisn":tranwitroisnumq1,"tranwitekate":"","tranwitekaten":""}  
                        let usere = {
                            data : data ,
                        }
                        tabUsere.push(usere)
                        localStorage.setItem('inscpce',JSON.stringify(tabUsere))
                        console.log('Data successfullyz sent to Python:', data);
                        // window.location.href = "http://127.0.0.1:5005/monpanierls"
                    }
                }
            }
            if (tranwitekatenumq)  {
                let cometrh = 0
                tabUsere.forEach((user) =>{
                    let taillepoe = document.querySelector(".taillepoetranwitekate").value
                    let i = user["data"]
                    if (parseInt(i.produite) === parseInt(noumeme) && i.tailed === taillepoe) {
                        cometrh+=1
                        
                        i.quantiteto = parseInt(i.quantiteto || 0) + parseInt(quantite);
                        
                        localStorage.setItem("inscpce", JSON.stringify(tabUsere));
                        console.log("les articles", i);
                        window.location.href = "/monpanier";
                        
                    }
                })
                if (cometrh<1) {
                    let tranwitekatenumq1 = parseInt(tranwitekatenumq.value)
                    if (tranwitekatenumq1 > 0){
                        // let tabUsere = []
                        let taillepoe = document.querySelector(".taillepoetranwitekate").value
                        let ideler = 0
                        tabUsere.forEach(i => {
                            let user = i["data"]
                            if ( parseInt( user["position"] )>= ideler) {
                                ideler = parseInt(user["position"]) + 1
                            }
                            
                        });
                    let data = {"desccopte":desccopte,"name":nom,"position":ideler,"image":image,"tailed" : (taillepoe + " ° "),"produite":noumeme,"categorie":categorie,"porce":porce,"porceprix":porceprix,"prixtottal":prix,"quantiteto":tranwitekatenumq1,"xs":"","xsn":"","s":"","sn":"","l":"","ln":"","m":"","mn":"","xl":"","xln":"","xxl":"","xxln":"","tranwite":"","tranwiten":"","tranneuf":"","tranneufn":"","karente":"","karenten":"","tranwiteun":"","tranwiteunn":"","tranwitedeux":"","tranwitedeuxn":"","tranwitrois":"","tranwitroisn":"","tranwitekate":"44 ° ","tranwitekaten":tranwitekatenumq1}  
                        let usere = {
                            data : data ,
                        }
                        tabUsere.push(usere)
                        localStorage.setItem('inscpce',JSON.stringify(tabUsere))
                        console.log('Data successfullyz sent to Python:', data);
                        // window.location.href = "http://127.0.0.1:5005/monpanierls"
                    }
                }
            }
            window.location.href = "http://127.0.0.1:5005/monpanierls"
            // console.log(xsnume);
        }
        // if (parseInt(xsnume) > 0 ){
        //     let xse = "xs"
            
            
        //     let data = {"image":image,"tailed" : "","produite":noumeme,"categorie":categorie,"porce":porce,"porceprix":porceprix,"prixtottal":prix,"quantiteto":xsnume,"xs":xse,"xsn":xsnume,"s":"","sn":"","l":"","ln":"","m":"","mn":"","xl":"","xln":"","xxl":"","xxln":"","tranwite":"","tranwiten":"","tranneuf":"","tranneufn":"","karente":"","karenten":"","tranwiteun":"","tranwiteunn":"","tranwitedeux":"","tranwitedeuxn":"","tranwitrois":"","tranwitroisn":"","tranwitekate":"","tranwitekaten":""}  
        //     let usere = {
        //         data : data ,
        //     }
        //     tabUsere.push(usere)
        //     localStorage.setItem('inscpce',JSON.stringify(tabUsere))
        // }
        // const xlnume = document.querySelector("#xlnumq").value
        // if (parseInt(xlnume) > 0 ){
        //     let xle = "xl"
            
            
        //     let data = {"image":image,"tailed" : "","produite":noumeme,"categorie":categorie,"porce":porce,"porceprix":porceprix,"prixtottal":prix,"quantiteto":xlnume,"xs":"","xsn":"","s":"","sn":"","l":"","ln":"","m":"","mn":"","xl":xle,"xln":xlnume,"xxl":"","xxln":"","tranwite":"","tranwiten":"","tranneuf":"","tranneufn":"","karente":"","karenten":"","tranwiteun":"","tranwiteunn":"","tranwitedeux":"","tranwitedeuxn":"","tranwitrois":"","tranwitroisn":"","tranwitekate":"","tranwitekaten":""}  
        //     let usere = {
        //         data : data ,
        //     }
        //     tabUsere.push(usere)
        //     localStorage.setItem('inscpce',JSON.stringify(tabUsere))
        // }
        // const xxlnume = document.querySelector("#xxlnumq").value
        // if (parseInt(xxlnume) > 0 ){
        //     let xxle = "xxl"
            
            
        //     let data = {"image":image,"tailed" : "","produite":noumeme,"categorie":categorie,"porce":porce,"porceprix":porceprix,"prixtottal":prix,"quantiteto":xxlnume,"xs":"","xsn":"","s":"","sn":"","l":"","ln":"","m":"","mn":"","xl":"","xln":"","xxl":xxle,"xxln":xxlnume,"tranwite":"","tranwiten":"","tranneuf":"","tranneufn":"","karente":"","karenten":"","tranwiteun":"","tranwiteunn":"","tranwitedeux":"","tranwitedeuxn":"","tranwitrois":"","tranwitroisn":"","tranwitekate":"","tranwitekaten":""}  
        //     let usere = {
        //         data : data ,
        //     }
        //     tabUsere.push(usere)
        //     localStorage.setItem('inscpce',JSON.stringify(tabUsere))
        // }
        // const lnume = document.querySelector("#lnumq").value
        // if (parseInt(lnume) > 0 ){
        //     let le = "l"
            
            
        //     let data = {"image":image,"tailed" : "","produite":noumeme,"categorie":categorie,"porce":porce,"porceprix":porceprix,"prixtottal":prix,"quantiteto":lnume,"xs":"","xsn":"","s":"","sn":"","l":le,"ln":lnume,"m":"","mn":"","xl":"","xln":"","xxl":"","xxln":"","tranwite":"","tranwiten":"","tranneuf":"","tranneufn":"","karente":"","karenten":"","tranwiteun":"","tranwiteunn":"","tranwitedeux":"","tranwitedeuxn":"","tranwitrois":"","tranwitroisn":"","tranwitekate":"","tranwitekaten":""}  
        //     let usere = {
        //         data : data ,
        //     }
        //     tabUsere.push(usere)
        //     localStorage.setItem('inscpce',JSON.stringify(tabUsere))
        // }
        // const snume = document.querySelector("#snumq").value
        // if (parseInt(snume) > 0 ){
        //     let se = "s"
            
            
        //     let data = {"image":image,"tailed" : "","produite":noumeme,"categorie":categorie,"porce":porce,"porceprix":porceprix,"prixtottal":prix,"quantiteto":snume,"xs":"","xsn":"","s":se,"sn":snume,"l":"","ln":"","m":"","mn":"","xl":"","xln":"","xxl":"","xxln":"","tranwite":"","tranwiten":"","tranneuf":"","tranneufn":"","karente":"","karenten":"","tranwiteun":"","tranwiteunn":"","tranwitedeux":"","tranwitedeuxn":"","tranwitrois":"","tranwitroisn":"","tranwitekate":"","tranwitekaten":""}  
        //     let usere = {
        //         data : data ,
        //     }
        //     tabUsere.push(usere)
        //     localStorage.setItem('inscpce',JSON.stringify(tabUsere))
        // }
        // const mnume = document.querySelector("#mnumq").value
        // if (parseInt(mnume) > 0 ){
        //     let me = "m"
            
            
        //     let data = {"image":image,"tailed" : "","produite":noumeme,"categorie":categorie,"porce":porce,"porceprix":porceprix,"prixtottal":prix,"quantiteto":mnume,"xs":"","xsn":"","s":"","sn":"","l":"","ln":"","m":me,"mn":mnume,"xl":"","xln":"","xxl":"","xxln":"","tranwite":"","tranwiten":"","tranneuf":"","tranneufn":"","karente":"","karenten":"","tranwiteun":"","tranwiteunn":"","tranwitedeux":"","tranwitedeuxn":"","tranwitrois":"","tranwitroisn":"","tranwitekate":"","tranwitekaten":""}  
        //     let usere = {
        //         data : data ,
        //     }
        //     tabUsere.push(usere)
        //     localStorage.setItem('inscpce',JSON.stringify(tabUsere))
        // }
    

        // console.log('Data successfully sent to Python:', data);
        // window.location.href = "http://127.0.0.1:5005/monpanierls"
    })
}
// boutonshd.addEventListener('click',()=>{
//     let tabUsere = JSON.parse(localStorage.getItem("inscpce")) || []
//     // let nameid = document.querySelector("#nome").value;
    
    
    

//     // let dataz = JSON.parse(localStorage.getItem("inscpce"))
//     fetch('/ssme', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json'
//         },
//         // body: JSON.stringify({ data: dataz })
        
//     })
//     .then(response => response.json())
//     .then(data => {
//         let usere = {
//             data:data,
//         }
    
//         tabUsere.push(usere)
//         localStorage.setItem('inscpce',JSON.stringify(tabUsere))
//         console.log('Data successfully sent to Python:', data);
//         window.location.href = "/monpanierls"
        
//     })
//     .catch(error => {
//         console.error('Error sending data to Python:', error);
//     });

// })


// const bouto = document.querySelector('.bouto');
// const formuhfh = document.querySelector('.formuhfh');
// const formuhfhe = document.querySelector('.ccrrooii');

// bouto.addEventListener('click',()=>{
//     formuhfh.classList.add("active");
// });
// formuhfhe.addEventListener('click',()=>{
//     formuhfh.classList.remove("active");
// })

// ;




const moins = document.querySelectorAll('#moins');
const numeric = document.querySelector('#numeric'); // Sélectionnez l'élément lui-même
const eeecran = document.querySelector('#eeecran'); // Sélectionnez l'élément lui-même
const plus = document.querySelectorAll('#plus');

moins.forEach(moins => {
    
moins.addEventListener('click', () => {
    numeric.value = parseInt(numeric.value) - 1; // Mettre à jour le contenu de l'élément
    eeecran.value = parseInt(eeecran.value) - 1; // Mettre à jour le contenu de l'élément
    console.log(numeric.value);
});
});
plus.forEach(plus => {
plus.addEventListener('click', () => {
    numeric.value = parseInt(numeric.value) + 1; // Mettre à jour le contenu de l'élément
    eeecran.value = parseInt(eeecran.value) + 1; // Mettre à jour le contenu de l'élément
    console.log(numeric.value);
});
});




const cliquer = document.querySelector('.te2')
// const cliquerw = document.querySelector('.menue')
const enleve = document.querySelector('.monfix')

// cliquerw.addEventListener('click',()=>{

//     enleve.classList.add('active');
// })
cliquer.addEventListener('click',()=>{

    enleve.classList.add('active');
    monfixder.classList.remove('active');
})


enleve.addEventListener('click',()=>{

    enleve.classList.remove('active');
})










const home = document.querySelector('#home')
const contact = document.querySelector('#contact')
const couleur = document.querySelector('.monfix')

home.addEventListener('click',()=>{

    contact.classList.remove('active');
    home.classList.add('active');
   
})
contact.addEventListener('click',()=>{

    home.classList.remove('active');
    contact.classList.add('active');
})


const cleud = document.querySelector('#cleud')
const monfixder = document.querySelector('.monfixder')

cleud.addEventListener('click',()=>{

    monfixder.classList.add('active');
})

monfixder.addEventListener('click',()=>{

    monfixder.classList.remove('active');
})





















let a = document.querySelectorAll('.coloope')
// let b = document.querySelector('.b')

a.forEach(a => {
    a.addEventListener('click',()=>{
        // wee.style.border = '10px solid red'
        // a.style.border = '10px solid pink';
        a.style.background = 'white';
        // wee.style.background = 'url(/menu.png) 50% no-repeat'
        // wee.backgroundSize= "cover";
        
    }

)
});



// const xl = document.querySelector('#xlp');

// const xlnum = document.querySelector('#xlnum');

// xl.addEventListener('click',()=>{
   
//     xl.style.background = 'yellow';
// })
// ;

// console.log("dedy")


let xl = document.querySelector('#xlp')
let xs = document.querySelector('#xsp')
let xxl = document.querySelector('#xxlp')
let l = document.querySelector('#lp')
let m = document.querySelector('#mp')
let s = document.querySelector('#sp')

let xsnum = document.querySelector('#xsnum')
let xlnum = document.querySelector('#xlnum')
let lnum = document.querySelector('#lnum')
let snum = document.querySelector('#snum')
let mnum = document.querySelector('#mnum')
let xxlnum = document.querySelector('#xxlnum')

// let b = document.querySelector('.b')


xl.addEventListener('click',()=>{
   
    // wee.style.border = '10px solid red'
    // a.style.border = '10px solid pink';
    xl.style.background = 'green';
    // wee.style.background = 'url(/menu.png) 50% no-repeat'
    // wee.backgroundSize= "cover";
    
    xlnum.classList.add("active")
    xlnum.value = 0
})


l.addEventListener('click',()=>{
    // wee.style.border = '10px solid red'
    // a.style.border = '10px solid pink';
    l.style.background = 'green';
    // wee.style.background = 'url(/menu.png) 50% no-repeat'
    // wee.backgroundSize= "cover";
    
    lnum.classList.add("active")
    lnum.value = 0
}

)
s.addEventListener('click',()=>{
    // wee.style.border = '10px solid red'
    // a.style.border = '10px solid pink';
    s.style.background = 'green';
    // wee.style.background = 'url(/menu.png) 50% no-repeat'
    // wee.backgroundSize= "cover";
    
    snum.classList.add("active")
    snum.value = 0
}

)
m.addEventListener('click',()=>{
    // wee.style.border = '10px solid red'
    // a.style.border = '10px solid pink';
    m.style.background = 'green';
    // wee.style.background = 'url(/menu.png) 50% no-repeat'
    // wee.backgroundSize= "cover";
    
    mnum.classList.add("active")
    mnum.value = 0
}

)
xxl.addEventListener('click',()=>{
    // wee.style.border = '10px solid red'
    // a.style.border = '10px solid pink';
    xxl.style.background = 'green';
    // wee.style.background = 'url(/menu.png) 50% no-repeat'
    // wee.backgroundSize= "cover";
    
    xxlnum.classList.add("active")
    xxlnum.value = 0
}

)
xs.addEventListener('click',()=>{
    
    // wee.style.border = '10px solid red'
    // a.style.border = '10px solid pink';
    xs.style.background = 'green';
    // wee.style.background = 'url(/menu.png) 50% no-repeat'
    // wee.backgroundSize= "cover";
    
    xsnum.classList.add("active")
    xsnum.value = 0
}

)




// let a = document.querySelectorAll('.coloope')
// // let b = document.querySelector('.b')

// a.forEach(a => {
//     a.addEventListener('click',()=>{
//         // wee.style.border = '10px solid red'
//         // a.style.border = '10px solid pink';
//         a.style.background = 'white'
//         // wee.style.background = 'url(/menu.png) 50% no-repeat'
//         // wee.backgroundSize= "cover";

//     }

// )
// });


function moinsp(ecranid) {
    couterw =document.querySelector("#couterw").value
    et = "#" + ecranid + ""
    let ecraid  = document.querySelector(et)
    if (ecraid.value >= 1){
        ecraid.value = parseInt(ecraid.value) - 1; 
        somiu = document.querySelector("#somiu")
    
        somiu.innerHTML = parseInt(somiu.innerHTML)  - 1// Mettre à jour le contenu de l'élément
        quantiteplos = document.querySelector("#quantiteplos")
        quantiteplos.value = somiu.innerHTML
        lepris = document.querySelector("#lepris")
        lepris.innerHTML = lepris.innerHTML - parseInt(couterw)
    }
    
    console.log(et);
    
    return 0
}

function plusp(ecranid,maxip) {
    et = "#" + ecranid + ""
    let ecraid  = document.querySelector(et)
    if (parseInt(maxip) > parseInt(ecraid.value)) {
        
        couterw =document.querySelector("#couterw").value
        
        ecraid.value = parseInt(ecraid.value) + 1; // Mettre à jour le contenu de l'élément
        console.log(et);
        somiu = document.querySelector("#somiu")
        
        
        somiu.innerHTML = parseInt(somiu.innerHTML)  + 1
        quantiteplos = document.querySelector("#quantiteplos")
        quantiteplos.value = somiu.innerHTML
        lepris = document.querySelector("#lepris")
        lepris.innerHTML = somiu.innerHTML * parseInt(couterw)

    }
    return 0
}


function verif(ide,quantep) {
    et = "#" + quantep + ""
    let ecraid  = document.querySelector(et)
    let a = ecraid.innerHTML
    if ( parseInt(a) > 0){
        let lien ="'" + `https://hington-shop.onrender.com/ssm/${ide}` + "'"
        console.log(lien);
        console.log(window.location);
        // window.location.remove = lien
        return window.location = '/ssm/1'
    }
    if (parseInt(a) < 1){
        console.log("000");
        console.log(window.location);
        return 0
    }
        
}



// const moins = document.querySelectorAll('#moins');
// const numeric = document.querySelector('#numeric'); // Sélectionnez l'élément lui-même
// const eeecran = document.querySelector('#eeecran'); // Sélectionnez l'élément lui-même
// const plus = document.querySelectorAll('#plus');

// moins.forEach(moins => {
    
// moins.addEventListener('click', () => {
//     numeric.value = parseInt(numeric.value) - 1; // Mettre à jour le contenu de l'élément
//     eeecran.value = parseInt(eeecran.value) - 1; // Mettre à jour le contenu de l'élément
//     console.log(numeric.value);
// });
// });
// plus.forEach(plus => {
// plus.addEventListener('click', () => {
//     numeric.value = parseInt(numeric.value) + 1; // Mettre à jour le contenu de l'élément
//     eeecran.value = parseInt(eeecran.value) + 1; // Mettre à jour le contenu de l'élément
//     console.log(numeric.value);
// });
// });

// function dedy() {
//     let tabUsere = JSON.parse(localStorage.getItem("inscpce")) || []
//     // let nameid = document.querySelector("#nome").value;
    
    
    

//     // let dataz = JSON.parse(localStorage.getItem("inscpce"))
//     fetch('/ssme', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json'
//         },
//         // body: JSON.stringify({ data: dataz })
        
//     })
//     .then(response => response.json())
//     .then(data => {
//         let usere = {
//             data:data,
//         }
    
//         tabUsere.push(usere)
//         localStorage.setItem('inscpce',JSON.stringify(tabUsere))
//         console.log('Data successfully sent to Python:', data);
//         window.location.href = "/monpanierls"
        
//     })
//     .catch(error => {
//         console.error('Error sending data to Python:', error);
//     });

// }
// function dedy() {
    

//     function updateTime() {
//         let now = new Date();
//         let hours = now.getHours();
//         let minutes = now.getMinutes();
//         let seconds = now.getSeconds();
//         console.log(seconds,"nom");
//     }

   
//     window.onload = function() {
//         updateTime();
//         let intervalId = setInterval(updateTime, 1000);

       
//         setTimeout(function() {
//             clearInterval(intervalId);
//             let now = new Date();
            
//             let seconds = now.getSeconds();
//             console.log(seconds,"pres")
//             let tabUsere = JSON.parse(localStorage.getItem("inscpce")) || []
//             // let nameid = document.querySelector("#nome").value;
            
            
            

//             // let dataz = JSON.parse(localStorage.getItem("inscpce"))
//             fetch('/ssme', {
//                 method: 'POST',
//                 headers: {
//                     'Content-Type': 'application/json'
//                 },
//                 // body: JSON.stringify({ data: dataz })
                
//             })
//             .then(response => response.json())
//             .then(data => {
//                 let usere = {
//                     data:data,
//                 }
            
//                 tabUsere.push(usere)
//                 localStorage.setItem('inscpce',JSON.stringify(tabUsere))
//                 console.log('Data successfully sent to Python:', data);
//                 window.location.href = "/monpanierls"
                
//             })
//             .catch(error => {
//                 console.error('Error sending data to Python:', error);
//             });
//         }, 0); // 5000 millisecondes = 10 secondes

        
//     };
        
            
        
    
    
// }
// let boutonid = document.querySelector("#bouste");
// boutonid.addEventListener("click",(event)=>{
//     event.preventDefault()
    
   
//     fetch('http://127.0.0.1:5005/song', {
//         method: 'GET',
//         headers: {
//             'Content-Type': 'application/json'
//         },
        
//     })
//     .then(response => response.json())
//     .then(data => {
//         let tabUsere = JSON.parse(localStorage.getItem("inscpce")) || []
//         let nom =data["prenom"];
//         let prenom =data["prenom"];
    
//         let usere = {
//             nom,
//             prenom,
//         }
//         tabUsere.push(usere)

//         localStorage.setItem('inscpce',JSON.stringify(tabUsere))
//         console.log('Data successfully sent to Python:', data);
//     })
//     .catch(error => {
//         console.error('Error sending data to Python:', error);
//     });
// }) 




function zoommer() {
    
}