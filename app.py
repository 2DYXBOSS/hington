from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask import render_template , redirect , request,url_for,flash,Response ,  make_response
from flask import render_template , redirect , request,url_for,flash,session ,Response
from sqlalchemy import ARRAY
from werkzeug.utils import secure_filename
from flask_mail import Mail, Message
import os
import datetime

import io


app = Flask(__name__)

data = datetime.date.today()
dataheure = datetime.datetime.now()
formatted_time = dataheure.strftime('%H')
formatted = dataheure.strftime('%M')
print(data)
print(dataheure)
print(formatted_time)
print(formatted)
print(dataheure)


from flask import Flask, request, render_template, redirect, url_for,send_file
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# import pywhatkit

# Configurations pour le serveur SMTP


app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads/'
app.debug = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['SECRET_KEY'] = 'BONJOUR'


app.config['SECRET_KEY'] = 'sdfgghjklhkj'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = '0streamblay@gmail.com'
app.config['MAIL_PASSWORD'] = 'vgux fpjq qyqr nxem'
app.config['MAIL_DEFAULT_SENDER'] = '0streamblay@gmail.com'



SMTP_SERVER = 'smtp.googlemail.com'  # Remplacez par l'adresse de votre serveur SMTP
SMTP_PORT = 587  # Port SMTP (généralement 587 pour TLS)
SMTP_USERNAME = 'pythonanywhere225@gmail.com'
SMTP_PASSWORD = 'tdqn cklm uvjd aonn'
# Clé secrète pour sécuriser l'application
app.secret_key = os.urandom(24)
mail = Mail(app)
# fin

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


db = SQLAlchemy(app)



debug = True

class Adminit(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    nom = db.Column(db.String(100), unique = False , nullable = False) 
    description = db.Column(db.String(100), unique = False , nullable = False) 
    nom = db.Column(db.String(100), unique = False , nullable = False) 
    derfjj = db.Column(db.String(), unique = False , nullable = False)
    
   
    def __init__(self,nom,numero,tags):
        self.nom = nom
        self.numero = numero
        self.tags = tags
       
       
    def __repr__(self):
        
        return {
            "nom": self.nom,
            "numero": self.numero,
            "tags": self.tags,
        }
    

with app.app_context() :
    try :
        db.create_all()
    except Exception as e:
        print("error de creation de la table")

class Maboutik(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    nom = db.Column(db.String(100), unique = False , nullable = False)
    description = db.Column(db.String(100), unique = True , nullable = False)
    prix = db.Column(db.Integer,nullable = False)
    image = db.Column(db.String(100), unique = True , nullable = False)
    categorie = db.Column(db.String(100), unique = False , nullable = False)
    like = db.Column(db.Integer, unique = False , nullable = False)
   
    def __init__(self,nom,description,prix,image,categorie,like):
        self.nom = nom
        self.description = description
        self.prix = prix
        self.image = image
        self.categorie = categorie
        self.like = like


    # db.init_app(app)
    # with app.app_context() :
    # #     db.create_all()
    # def __str__(self):
    #     # Renvoie une chaîne de caractères représentant l'objet
    #     return f"Person(nom: {self.nom}, description: {self.description}, age: {self.age})"
    def __repr__(self):
        
        return {
            "nom": self.nom,
            "description": self.description,
            "prix": self.prix,
            "image": self.image,
            "categorie": self.categorie,
            "like": self.like
        }
    

with app.app_context() :
    try :
        db.create_all()
    except Exception as e:
        print("error de creation de la table")


class Ajouter(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    nom = db.Column(db.String(500), unique = False , nullable = False)
    description = db.Column(db.String(500), unique = False , nullable = False)
    liens = db.Column(db.String(500), unique = False , nullable = False)
    prix = db.Column(db.String(500), unique = False , nullable = False)
    porce = db.Column(db.String(500), unique = False , nullable = False)
    porceprix = db.Column(db.String(500), unique = False , nullable = False)
    categorie = db.Column(db.String(500), unique = False , nullable = False)
    image = db.Column(db.String(500), unique = True , nullable = False)
    twoimage = db.Column(db.String(500), unique = False , nullable = False)
    threeimage = db.Column(db.String(500), unique = False , nullable = False)
    forimage = db.Column(db.String(500), unique = False , nullable = False)
    xs = db.Column(db.String(500), unique = False , nullable = False)
    s = db.Column(db.String(500), unique = False , nullable = False)
    m = db.Column(db.String(500), unique = False , nullable = False)
    l = db.Column(db.String(500), unique = False , nullable = False)
    xl = db.Column(db.String(500), unique = False , nullable = False)
    xxl = db.Column(db.String(500), unique = False , nullable = False)
    rouge = db.Column(db.String(500), unique = False , nullable = False)
    blanc = db.Column(db.String(500), unique = False , nullable = False)
    noir = db.Column(db.String(500), unique = False , nullable = False)
    jaune = db.Column(db.String(500), unique = False , nullable = False)
    vert = db.Column(db.String(500), unique = False , nullable = False)
    orange = db.Column(db.String(500), unique = False , nullable = False)
    bleu = db.Column(db.String(500), unique = False , nullable = False)
    rose = db.Column(db.String(500), unique = False , nullable = False)
    marron = db.Column(db.String(500), unique = False , nullable = False)
    violet = db.Column(db.String(500), unique = False , nullable = False)
    gris = db.Column(db.String(500), unique = False , nullable = False)
    tranwite = db.Column(db.String(500), unique = False , nullable = False)
    tranneuf = db.Column(db.String(500), unique = False , nullable = False)
    karente = db.Column(db.String(500), unique = False , nullable = False)
    tranwiteun = db.Column(db.String(500), unique = False , nullable = False)
    tranwitedeux = db.Column(db.String(500), unique = False , nullable = False)
    tranwitrois = db.Column(db.String(500), unique = False , nullable = False)
    tranwitekate = db.Column(db.String(500), unique = False , nullable = False)

    xslet = db.Column(db.String(500), unique = False , nullable = False)
    slet = db.Column(db.String(500), unique = False , nullable = False)
    mlet = db.Column(db.String(500), unique = False , nullable = False)
    llet = db.Column(db.String(500), unique = False , nullable = False)
    xllet = db.Column(db.String(500), unique = False , nullable = False)
    xxllet = db.Column(db.String(500), unique = False , nullable = False)
    tranwitelet = db.Column(db.String(500), unique = False , nullable = False)
    tranneuflet = db.Column(db.String(500), unique = False , nullable = False)
    karentelet = db.Column(db.String(500), unique = False , nullable = False)
    tranwiteunlet = db.Column(db.String(500), unique = False , nullable = False)
    tranwitedeuxlet = db.Column(db.String(500), unique = False , nullable = False)
    tranwitroislet = db.Column(db.String(500), unique = False , nullable = False)
    tranwitekatelet = db.Column(db.String(500), unique = False , nullable = False)

    quantit = db.Column(db.String(500), unique = False , nullable = False)
    stat = db.Column(db.String(500), unique = False , nullable = False)
   
   
    def __init__(self,nom,description,prix,porce,porceprix,categorie,image,twoimage,threeimage,forimage,xs,s,m,l,xl,xxl,rouge,blanc,noir,jaune,vert,orange,bleu,rose,marron,violet,gris,tranwite,tranneuf,karente,tranwiteun,tranwitedeux,tranwitrois,tranwitekate,quantit,stat,xslet,slet,mlet,llet,xllet,xxllet,tranwitelet,tranneuflet,karentelet,tranwiteunlet,tranwitedeuxlet,tranwitroislet,tranwitekatelet,liens):
        self.nom = nom
        self.description = description
        self.prix = prix
        self.porce = porce
        self.porceprix = porceprix
        self.categorie = categorie
        self.image = image
        self.twoimage = twoimage
        self.threeimage = threeimage
        self.forimage = forimage
        self.xs = xs
        self.s = s
        self.m = m
        self.l = l
        self.xl = xl
        self.xxl = xxl
        self.rouge = rouge
        self.blanc = blanc
        self.noir = noir
        self.jaune = jaune
        self.vert = vert
        self.orange = orange
        self.bleu = bleu
        self.rose = rose
        self.marron = marron
        self.violet = violet
        self.gris = gris
        self.tranwite = tranwite
        self.tranneuf = tranneuf  
        self.karente = karente
        self.tranwiteun = tranwiteun
        self.tranwitedeux = tranwitedeux
        self.tranwitrois = tranwitrois
        self.tranwitekate = tranwitekate
        self.quantit = quantit
        self.stat = stat
        self.xslet = xslet
        self.slet = slet
        self.mlet = mlet
        self.llet = llet
        self.xllet = xllet
        self.xxllet = xxllet
        self.tranwitelet = tranwitelet
        self.tranneuflet = tranneuflet
        self.karentelet = karentelet
        self.tranwiteunlet = tranwiteunlet
        self.tranwitedeuxlet = tranwitedeuxlet
        self.tranwitroislet = tranwitroislet
        self.tranwitekatelet = tranwitekatelet
        self.liens = liens
      
        


    # db.init_app(app)
    # with app.app_context() :
    # #     db.create_all()
    # def __str__(self):
    #     # Renvoie une chaîne de caractères représentant l'objet
    #     return f"Person(nom: {self.nom}, description: {self.description}, age: {self.age})"
    def __repr__(self):
        
        return {
            "nom": self.nom,
            "description": self.description,
            "prix": self.prix,
            "porceprix": self.porceprix,
            "porce": self.porce,
            "categorie": self.categorie,
            "image": self.image,
            "twoimage": self.twoimage,
            "threeimage": self.threeimage,
            "forimage": self.forimage,
            "xs": self.xs,
            "s": self.s,
            "m": self.m,
            "l": self.l,
            "xl": self.xl,
            "xxl": self.xxl,
            "rouge": self.rouge,
            "blanc": self.blanc,
            "noir": self.noir,
            "jaune": self.jaune,
            "vert": self.vert,
            "orange": self.orange,
            "bleu": self.bleu,
            "rose": self.rose,
            "marron": self.marron,
            "violet": self.violet,
            "gris": self.gris,
            "tranwite" : self.tranwite ,
            "tranneuf" : self.tranneuf,
            "karente" : self.karente,
            "tranwiteun" : self.tranwiteun,
            "tranwitedeux" : self.tranwitedeux,
            "tranwitrois" : self.tranwitrois,
            "tranwitekate" : self.tranwitekate,
            "quantit" : self.quantit,
            "stat" : self.stat,
            "xslet" : self.xslet , 
            "slet" : self.slet , 
            "mlet" : self.mlet , 
            "llet" : self.llet , 
            "xllet" : self.xllet , 
            "xxllet" : self.xxllet , 
            "tranwitelet" : self.tranwitelet , 
            "tranneuflet" : self.tranneuflet , 
            "karentelet" : self.karentelet , 
            "tranwiteunlet" : self.tranwiteunlet , 
            "tranwitedeuxlet" : self.tranwitedeuxlet , 
            "tranwitroislet" : self.tranwitroislet , 
            "tranwitekatelet" : self.tranwitekatelet ,
            "liens" : self.liens ,
            
        }
    

with app.app_context() :
    try :
        db.create_all()
    except Exception as e:
        print("error de creation de la table")

class Mailboite(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    proprio = db.Column(db.String(500), unique = False , nullable = False)
    nom = db.Column(db.String(500), unique = False , nullable = False)
    status = db.Column(db.String(500), unique = False , nullable = False)
    depart = db.Column(db.String(500), unique = False , nullable = False)
    arriver = db.Column(db.String(500), unique = False , nullable = False)
    lieu = db.Column(db.String(500), unique = False , nullable = False)
    serie = db.Column(db.String(500), unique = False , nullable = False)
    image = db.Column(db.String(500), unique = False , nullable = False)
    dateactu = db.Column(db.String(500), unique = False , nullable = False)
    categorie = db.Column(db.String(100), unique = False , nullable = False)

    # achat = db.relationship('Panier',back_populates='prendre')
    def __init__(self,proprio,nom,status,depart,arriver,lieu,serie,image,dateactu,categorie):
        self.proprio = proprio
        self.nom = nom
        self.status = status
        self.depart = depart
        self.arriver = arriver
        self.lieu = lieu
        self.serie = serie
        self.image = image
        self.dateactu = dateactu
        self.categorie = categorie
        

    # db.init_app(app)
    # with app.app_context() :
    #     db.create_all()
    # def __str__(self):
    #     # Renvoie une chaîne de caractères représentant l'objet
    #     return f"Person(first_name: {self.first_name}, last_name: {self.last_name}, age: {self.age})"
    def __repr__(self):
        
        return {
            "proprio": self.proprio,
            "nom": self.nom,
            "status": self.status,
            "depart": self.depart,
            "arriver": self.arriver,
            "lieu": self.lieu,
            "serie": self.serie,
            "image": self.image,
            "dateactu": self.dateactu,
            "categorie": self.categorie,
            
        }
    
with app.app_context() :
    try :
        db.create_all()
    except Exception as e:
        print("error de creation de la table")
class Commande(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    idpro = db.Column(db.String(500), unique = False , nullable = False)
    nom = db.Column(db.String(500), unique = False , nullable = False)
    prenom = db.Column(db.String(500), unique = False , nullable = False)
    mail = db.Column(db.String(500), unique = False , nullable = False)
    residence = db.Column(db.String(500), unique = False , nullable = False)
    produitname = db.Column(db.String(500), unique = False , nullable = False)
    prixunit = db.Column(db.String(500), unique = False , nullable = False)
    pourcent = db.Column(db.String(500), unique = False , nullable = False)
    prixtotal = db.Column(db.String(500), unique = False , nullable = False)
    aller = db.Column(db.String(500), unique = False , nullable = False)
    livrer = db.Column(db.String(500), unique = False , nullable = False)
    numero = db.Column(db.String(500), unique = False , nullable = False)
    lieulivraison = db.Column(db.String(8),nullable = False)
    deslieulivraison = db.Column(db.String(8),nullable = False)
    comnumid = db.Column(db.String(8),nullable = False)
    quantite = db.Column(db.String(500),nullable = False)
    image = db.Column(db.String(500),nullable = False)
    status = db.Column(db.String(500),nullable = False)
    categorie = db.Column(db.String(500),nullable = False)
    client = db.Column(db.String(500),nullable = False)
    taille = db.Column(db.String(8),nullable = False)

    # achat = db.relationship('Panier',back_populates='prendre')
    def __init__(self,nom,prenom,mail,residence,produitname,prixunit,pourcent,prixtotal,aller,livrer,numero,lieulivraison,deslieulivraison,comnumid,quantite,taille,idpro,status,image,categorie,client):
        self.nom = nom
        self.prenom = prenom
        self.mail = mail
        self.residence = residence
        self.taille = taille
        self.quantite = quantite
        self.produitname = produitname
        self.prixunit = prixunit
        self.pourcent = pourcent
        self.prixtotal = prixtotal
        self.aller = aller
        self.livrer = livrer
        self.numero = numero
        self.lieulivraison = lieulivraison
        self.deslieulivraison = deslieulivraison
        self.comnumid = comnumid
        self.idpro = idpro
        self.status = status
        self.image = image
        self.categorie = categorie
        self.client = client

    # db.init_app(app)
    # with app.app_context() :
    #     db.create_all()
    # def __str__(self):
    #     # Renvoie une chaîne de caractères représentant l'objet
    #     return f"Person(first_name: {self.first_name}, last_name: {self.last_name}, age: {self.age})"
    def __repr__(self):
        
        return {
            "nom": self.nom,
            "prenom": self.prenom,
            "mail": self.mail,
            "residence": self.residence,
            "produitname": self.produitname,
            "prixunit": self.prixunit,
            "pourcent": self.pourcent,
            "prixtotal": self.prixtotal,
            "aller": self.aller,
            "livrer": self.livrer,
            "numero": self.numero,
            "lieulivraison": self.lieulivraison,
            "deslieulivraison": self.deslieulivraison,
            "comnumid": self.comnumid,
            "taille": self.taille,
            "quantite": self.quantite,
            "idpro": self.idpro,
            "image": self.image,
            "status": self.status,
            "categorie": self.categorie,
            "client": self.client,
            
            
        }
    
with app.app_context() :
    try :
        db.create_all()
    except Exception as e:
        print("error de creation de la table")
class Profil(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    satuq = db.Column(db.Integer)
    prenom = db.Column(db.String(500), unique = False , nullable = False)
    residence = db.Column(db.String(500), unique = False , nullable = False)
    livraison = db.Column(db.String(500), unique = False , nullable = False)
    numero = db.Column(db.String(500), unique = False , nullable = False)
    deslivraion = db.Column(db.String(500), unique = False , nullable = False)
    infoplus = db.Column(db.String(500), unique = False , nullable = False)

    first_name = db.Column(db.String(500), unique = False , nullable = False)
    last_name = db.Column(db.String(500), unique = True , nullable = False)
    age = db.Column(db.String(8),nullable = False)

    # achat = db.relationship('Panier',back_populates='prendre')
    def __init__(self,first_name,last_name,age,prenom,residence,livraison,numero,deslivraion,infoplus,satuq):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.prenom = prenom
        self.residence = residence
        self.livraison = livraison
        self.numero = numero
        self.deslivraion = deslivraion
        self.infoplus = infoplus
        self.satuq = satuq

    # db.init_app(app)
    # with app.app_context() :
    #     db.create_all()
    # def __str__(self):
    #     # Renvoie une chaîne de caractères représentant l'objet
    #     return f"Person(first_name: {self.first_name}, last_name: {self.last_name}, age: {self.age})"
    def __repr__(self):
        
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "prenom": self.prenom,
            "residence": self.residence,
            "livraison": self.livraison,
            "numero": self.numero,
            "deslivraion": self.deslivraion,
            "infoplus": self.infoplus,
            "satuq": self.satuq
        }
    
with app.app_context() :
    try :
        db.create_all()
    except Exception as e:
        print("error de creation de la table")

class Commantaire(db.Model):
    
    id = db.Column(db.Integer, primary_key = True)
    commentairec = db.Column(db.String(500), unique = False , nullable = False)
    idclient = db.Column(db.String(500), unique = False, nullable = False)
    nomclient = db.Column(db.String(500), unique = False, nullable = False)
    idproduit = db.Column(db.Integer)
    datecomman = db.Column(db.String(500), unique = False, nullable = False)
    couleur = db.Column(db.String(500), unique = False, nullable = False)
   
   
    def __init__(self,commentairec,idclient,nomclient,idproduit,datecomman,couleur):
        self.commentairec = commentairec
        self.idclient = idclient
        self.nomclient = nomclient
        self.idproduit = idproduit
        self.datecomman = datecomman
        self.couleur = couleur
        


    # db.init_app(app)
    # with app.app_context() :
    # #     db.create_all()
    # def __str__(self):
    #     # Renvoie une chaîne de caractères représentant l'objet
    #     return f"Person(nom: {self.nom}, mail: {self.mail}, age: {self.age})"
    def __repr__(self):
        
        return {
            "idclient": self.idclient,
            "commentairec": self.commentairec,
            "nomclient": self.nomclient,
            "idproduit": self.idproduit,
            "datecomman": self.datecomman,
            "couleur": self.couleur,
            
        }
    

with app.app_context() :
    try :
        db.create_all()
    except Exception as e:
        print("error de creation de la table")
class Comment(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    nom = db.Column(db.String(15), unique = False , nullable = False)
    mail = db.Column(db.String(100), unique = False, nullable = False)
    message = db.Column(db.String(50), unique = False, nullable = False)
    heure = db.Column(db.String(50), unique = False, nullable = False)
   
   
    def __init__(self,nom,mail,message,heure):
        self.nom = nom
        self.mail = mail
        self.message = message
        self.heure = heure
        


    # db.init_app(app)
    # with app.app_context() :
    # #     db.create_all()
    # def __str__(self):
    #     # Renvoie une chaîne de caractères représentant l'objet
    #     return f"Person(nom: {self.nom}, mail: {self.mail}, age: {self.age})"
    def __repr__(self):
        
        return {
            "nom": self.nom,
            "mail": self.mail,
            "message": self.message,
            "heure": self.heure,
            
        }
    

with app.app_context() :
    try :
        db.create_all()
    except Exception as e:
        print("error de creation de la table")


class Panieruser(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    identifiant = db.Column(db.String(15), unique = False , nullable = False)
    image = db.Column(db.String(15), unique = False , nullable = False)
    produite = db.Column(db.String(15), unique = False , nullable = False)
    prixtottal = db.Column(db.String(100), unique = False , nullable = False)

    prixdepouce = db.Column(db.String(100), unique = False , nullable = False)
    nomprodui = db.Column(db.String(100), unique = False , nullable = False)
    descrprosui = db.Column(db.String(100), unique = False , nullable = False)
    pourcentage = db.Column(db.String(100), unique = False , nullable = False)
    categorie = db.Column(db.String(100), unique = False , nullable = False)

    dispono = db.Column(db.String(100), unique = False , nullable = False)
    statuse = db.Column(db.String(100), unique = False , nullable = False)


    quantiteto = db.Column(db.String(100), unique = False , nullable = False)
    tailed = db.Column(db.String(100), unique = False , nullable = False)
    xs = db.Column(db.String(100), unique = False , nullable = False)
    xsn = db.Column(db.String(100), unique = False , nullable = False)
    s = db.Column(db.String(100), unique = False , nullable = False)
    sn = db.Column(db.String(100), unique = False , nullable = False)
    m = db.Column(db.String(100), unique = False , nullable = False)
    mn = db.Column(db.String(100), unique = False , nullable = False)
    l = db.Column(db.String(100), unique = False , nullable = False)
    ln = db.Column(db.String(100), unique = False , nullable = False)
    xl = db.Column(db.String(100), unique = False , nullable = False)
    xln = db.Column(db.String(100), unique = False , nullable = False)
    xxl = db.Column(db.String(100), unique = False , nullable = False)
    xxln = db.Column(db.String(100), unique = False , nullable = False)
    tranwite = db.Column(db.String(100), unique = False , nullable = False)
    tranwiten = db.Column(db.String(100), unique = False , nullable = False)
    tranneuf = db.Column(db.String(100), unique = False , nullable = False)
    tranneufn = db.Column(db.String(100), unique = False , nullable = False)
    karente = db.Column(db.String(100), unique = False , nullable = False)
    karenten = db.Column(db.String(100), unique = False , nullable = False)
    tranwiteun = db.Column(db.String(100), unique = False , nullable = False)
    tranwiteunn = db.Column(db.String(100), unique = False , nullable = False)
    tranwitedeux = db.Column(db.String(100), unique = False , nullable = False)
    tranwitedeuxn = db.Column(db.String(100), unique = False , nullable = False)
    tranwitrois = db.Column(db.String(100), unique = False , nullable = False)
    tranwitroisn = db.Column(db.String(100), unique = False , nullable = False)
    tranwitekate = db.Column(db.String(100), unique = False , nullable = False)
    tranwitekaten = db.Column(db.String(100), unique = False , nullable = False)
   
   
   
    def __init__(self,identifiant,tailed,image,produite,prixtottal,quantiteto,xs,xsn,s,sn,m,mn,l,ln,xl,xln,xxl,xxln,tranwite,tranwiten,tranneuf,tranneufn,karente,karenten,tranwiteun,tranwiteunn,tranwitedeux,tranwitedeuxn,tranwitrois,tranwitroisn,tranwitekate,tranwitekaten,prixdepouce,nomprodui,descrprosui,pourcentage,categorie,dispono,statuse):

        self.identifiant = identifiant
        self.image = image
        self.produite = produite
        self.tailed = tailed
        self.prixtottal = prixtottal
        self.quantiteto = quantiteto
        self.xs = xs
        self.xsn = xsn
        self.s = s
        self.sn = sn
        self.m = m
        self.mn = mn
        self.l = l
        self.ln = ln
        self.xl = xl
        self.xln = xln
        self.xxl = xxl
        self.xxln = xxln
        self.tranwite = tranwite
        self.tranwiten = tranwiten
        self.tranneuf = tranneuf
        self.tranneufn = tranneufn
        self.karente = karente
        self.karenten = karenten
        self.tranwiteun = tranwiteun
        self.tranwiteunn = tranwiteunn
        self.tranwitedeux = tranwitedeux
        self.tranwitedeuxn = tranwitedeuxn
        self.tranwitrois = tranwitrois
        self.tranwitroisn = tranwitroisn
        self.tranwitekate = tranwitekate
        self.tranwitekaten = tranwitekaten
        self.prixdepouce = prixdepouce
        self.nomprodui = nomprodui
        self.descrprosui = descrprosui
        self.pourcentage = pourcentage
        self.categorie = categorie
        self.dispono = dispono
        self.statuse = statuse
      
        


    # db.init_app(app)
    # with app.app_context() :
    # #     db.create_all()
    # def __str__(self):
    #     # Renvoie une chaîne de caractères représentant l'objet
    #     return f"Person(nom: {self.nom}, description: {self.description}, age: {self.age})"
    def __repr__(self):
        
        return {
            "identifiant": self.identifiant,
            "image": self.image,
            "produite": self.produite,
            "tailed": self.tailed,
            "prixtottal": self.prixtottal,
            "quantiteto": self.quantiteto,
            "xs": self.xs,
            "xsn": self.xsn,
            "s": self.s,
            "sn": self.sn,
            "m": self.m,
            "mn": self.mn,
            "l": self.l,
            "ln": self.ln,
            "xl": self.xl,
            "xln": self.xln,
            "xxl": self.xxl,
            "xxln": self.xxln,
            "tranwite" : self.tranwite ,
            "tranwiten" : self.tranwiten ,
            "tranneuf" : self.tranneuf,
            "tranneufn" : self.tranneufn,
            "karente" : self.karente,
            "karenten" : self.karenten,
            "tranwiteun" : self.tranwiteun,
            "tranwiteunn" : self.tranwiteunn,
            "tranwitedeux" : self.tranwitedeux,
            "tranwitedeuxn" : self.tranwitedeuxn,
            "tranwitrois" : self.tranwitrois,
            "tranwitroisn" : self.tranwitroisn,
            "tranwitekate" : self.tranwitekate,
            "tranwitekaten" : self.tranwitekaten,
            "prixdepouce" : self.prixdepouce,
            "nomprodui" : self.nomprodui,
            "descrprosui" : self.descrprosui,
            "pourcentage" : self.pourcentage,
            "categorie" : self.categorie,
            "dispono" : self.dispono,
            "statuse" : self.statuse,
            
        }

    

with app.app_context() :
    try :
        db.create_all()
    except Exception as e:
        print("error de creation de la table")











@app.route('/commentaire', methods=['POST'])
def commentaire():
    print(formatted_time)
    print(formatted)
    nom = request.form.get("nom")
    mail = request.form.get("mail")
    message = request.form.get("message")
    heure = f"Le {data} depuis Abidjan,CI à {formatted_time}h{formatted}"

    envoyer = Comment(nom=nom, message=message,mail=mail,heure=heure)

        
    db.session.add(envoyer)
    db.session.commit()
             
    return redirect('/')



@app.route('/mailsamin')
def mailsamin():
    if 'utilisateur_id' in session:
        useru = Profil.query.get(session['utilisateur_id'])
        if useru.satuq == 1 :
            pass
        else:
            return redirect('/')
    else:
        return redirect('/pre/administa')
    return render_template("mailadmin.html")
# AJOUTER IMAGES DES ARTICLES{}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
# @app.route('/add_objet')
# def add_objet():
    
#     return render_template("image.html")

@app.route('/add_objet', methods=['POST'])
def upload_image():
    if 'utilisateur_id' in session:
        useru = Profil.query.get(session['utilisateur_id'])
        if useru.satuq == 1 :
            pass
        else:
            return redirect('/')
    else:
        return redirect('/pre/administa')
    try :
        if 'file' not in request.files:
            # flash('No file part')
            return redirect(request.url)
        # cheki1 = request.form.get("cheki1",'')
        # print(cheki1)
        # cheki2 = request.form.get("cheki2",'')
        # print(cheki2)
        # cheki3 = request.form.get("cheki3",'')
        # print(cheki3)
        # cheki4 = request.form.get("cheki4",'')
        # print(cheki4)
        file = request.files['file']
        file1 = request.files['file1']
        file2 = request.files['file2']
        file3 = request.files['file3']
        print(file.filename)
        if file.filename == '' :
            # flash('Aucune image sélectionnée pour le téléchargement')
            return redirect(request.url)
        if file1.filename == '' :
            # flash('Aucune image sélectionnée pour le téléchargement')
            filename1 = 'vide'
        if file2.filename == '' :
            # flash('Aucune image sélectionnée pour le téléchargement')
            filename2 = 'vide'
        if file3.filename == '' :
            # flash('Aucune image sélectionnée pour le téléchargement')
            filename3 = 'vide'


        if file and allowed_file(file.filename):
            filenamea1 = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filenamea1))
            #print('upload_image filename: ' + filename)
            # flash('Image téléchargée avec succès et affichée ci-dessous')
            filename=file.filename
            # return render_template('boutique.html', filename=filename)
        if file1 and allowed_file(file1.filename):
            filenamea2 = secure_filename(file1.filename)
            file1.save(os.path.join(app.config['UPLOAD_FOLDER'], filenamea2))
            #print('upload_image filename: ' + filename)
            # flash('Image téléchargée avec succès et affichée ci-dessous')
            filename1=file1.filename
            
            # return render_template('boutique.html', filename=filename)
        if file2 and allowed_file(file2.filename):
            filenamea3 = secure_filename(file2.filename)
            file2.save(os.path.join(app.config['UPLOAD_FOLDER'], filenamea3))
            #print('upload_image filename: ' + filename)
            filename2=file2.filename
            # flash('Image téléchargée avec succès et affichée ci-dessous')

            # return render_template('boutique.html', filename=filename)
        if file3 and allowed_file(file3.filename):
            filenamea4 = secure_filename(file3.filename)
            file3.save(os.path.join(app.config['UPLOAD_FOLDER'], filenamea4))
            #print('upload_image filename: ' + filename)
            filename3=file3.filename
            # flash('Image téléchargée avec succès et affichée ci-dessous')
           
        print(f'premier{filename},deux{filename1},trois{filename2},quatre{filename3}')


        cheki1 = request.form.get("seldldss")
        # print(cheki1)
        # cheki2 = request.form.get("cheki2",'')
        # print(cheki2)
        # cheki3 = request.form.get("cheki3",'')
        # print(cheki3)
        # cheki4 = request.form.get("cheki4",'')
        # print(cheki4)
        
        
        if cheki1 == 'Vetementfemmes' :
            return render_template('boutique.html', filename1=filename1 , filename=filename ,filename2=filename2 , filename3=filename3 , cheki1 = cheki1)
        elif cheki1 == 'Chaussures' :
            return render_template('ajchausee.html', filename1=filename1 , filename=filename ,filename2=filename2 , filename3=filename3, cheki1 = cheki1)
        elif cheki1 == 'montres':
            return render_template('ajmontre.html', filename1=filename1 , filename=filename ,filename2=filename2 , filename3=filename3, cheki1 = cheki1)
        # return render_template('boutique.html', filename1=filename1 , filename=filename ,filename2=filename2 , filename3=filename3)
            # return render_template('boutique.html', filename=filename)
        # if not file and not allowed_file(file.filename) :
        #     return render_template('boutique.html', filename=filename , filename1=file1.filename ,filename2=file2.filename , filename3=file3.filename)
        # if not file2 and not allowed_file(file2.filename) :
        #     return render_template('boutique.html', filename2=filename2 , filename1=file1.filename ,filename=file.filename , filename3=file3.filename)
        # if not file3 and not allowed_file(file3.filename) :
        #     return render_template('boutique.html', filename3=filename3 , filename1=file1.filename ,filename2=file2.filename , filename=file.filename)
        # if not file1 and not allowed_file(file1.filename) :
        #     return render_template('boutique.html', filename1=filename1 , filename=file.filename ,filename2=file2.filename , filename3=file3.filename)
    except:
        # flash('Les types dimages autorisés sont - png, jpg, jpeg, gif')
        return redirect(request.url)

        # uploads.image
 
@app.route('/display/<filename>')
def display_image(filename):
    #print('display_image filename: ' + filename)
    return redirect(url_for('static', filename = 'uploads/' + filename), code=301)
# FIN AJOUTER IMAGES DES ARTICLES{}










# AJOUTER DES ARTICLES{}

@app.route('/objet',methods = ["POST"])
def objet(): 
        if 'utilisateur_id' in session:
            useru = Profil.query.get(session['utilisateur_id'])
            if useru.satuq == 1 :
                pass
            else:
                return redirect('/')
        else:
            return redirect('/pre/administa')
    
    
      
        nom = request.form.get("nom")
        description = request.form.get("description")
        prix = request.form.get("prix")
        porce = request.form.get("porce","0")
        porceprix = str(int(int(prix)-(int(prix) * (int(porce)/100))))
        image = request.form.get("image")      
        liens = request.form.get("liens")      
        categorie = request.form.get('categorie')
        quantit = request.form.get('quantit',"rien")
        twoimage = request.form.get('twoimage')
        threeimage = request.form.get('threeimage')
        forimage = request.form.get('forimage')
        xs = request.form.get("xs","rien")
        s = request.form.get("s","rien")
        m = request.form.get("m","rien")
        l = request.form.get("l","rien")
        xl = request.form.get("xl","rien")
        xxl = request.form.get("xxl","rien")
        rouge = request.form.get("rouge","rien")
        blanc = request.form.get("blanc","rien")
        noir = request.form.get("noir","rien")
        jaune = request.form.get("jaune","rien")
        vert = request.form.get("vert","rien")
        orange = request.form.get("orange","rien")
        bleu = request.form.get("bleu","rien")
        rose = request.form.get("rose","rien")
        marron = request.form.get("marron","rien")
        violet = request.form.get("violet","rien")
        gris = request.form.get("gris","rien")
        tranwite = request.form.get("tranwite","rien")
        tranneuf = request.form.get("tranneuf","rien")
        karente = request.form.get("karente","rien")
        tranwiteun = request.form.get("tranwiteun","rien")
        tranwitedeux = request.form.get("tranwitedeux","rien")
        tranwitrois = request.form.get("tranwitrois","rien")
        tranwitekate = request.form.get("tranwitekate","rien")

        tranwitelet = request.form.get("tranwitelet","rien")
        tranneuflet = request.form.get("tranneuflet","rien")
        karentelet = request.form.get("karentelet","rien")
        tranwiteunlet = request.form.get("tranwiteunlet","rien")
        tranwitedeuxlet = request.form.get("tranwitedeuxlet","rien")
        tranwitroislet = request.form.get("tranwitroislet","rien")
        tranwitekatelet = request.form.get("tranwitekatelet","rien")
        xslet = request.form.get("xslet","rien")
        slet = request.form.get("slet","rien")
        mlet = request.form.get("mlet","rien")
        llet = request.form.get("llet","rien")
        xllet = request.form.get("xllet","rien")
        xxllet = request.form.get("xxllet","rien")


        if categorie == "chaussure" :
            tablepmd = [tranwitelet,tranneuflet,karentelet,tranwiteunlet,tranwitedeuxlet,tranwitroislet,tranwitekatelet,xslet,slet,mlet,llet,xllet,xxllet]
            if quantit == "rien" :
                quantit = 0
                
                for i in range(len(tablepmd))  :
                    print("les njdgjhdjkd",i)
                    if tablepmd[i] != 'rien' and tablepmd[i] != "" and tablepmd[i] != " " and (tablepmd[i]).isdigit(): 
                        quantit += int(tablepmd[i])
                    elif tablepmd[i] == 'rien' or tablepmd[i] == "" or tablepmd[i] == " ": 
                        tablepmd[i] = 0
                    else :
                        print('ya rien tchai')

                    print("dfghjk",tablepmd,"fin",tablepmd[i])

            
            pani = Ajouter(nom=nom,description=description,prix=prix,porceprix=porceprix,porce=porce,categorie=categorie,image=image,twoimage=twoimage,threeimage=threeimage,forimage=forimage,xs=xs,s=s,l=l,m=m,xl=xl,xxl=xxl,rouge=rouge,blanc=blanc,noir=noir,jaune=jaune,vert=vert,orange=orange,bleu=bleu,rose=rose,marron=marron,violet=violet,gris=gris,tranwite=tranwite,tranneuf=tranneuf,karente=karente,tranwiteun=tranwiteun,tranwitedeux=tranwitedeux,tranwitrois=tranwitrois,tranwitekate=tranwitekate,quantit=quantit,stat="vrai",xslet=xslet,slet=slet,mlet=mlet,llet=llet,xllet=xllet,xxllet=xxllet,tranwitelet=int(tablepmd[0]),tranneuflet=int(tablepmd[1]),karentelet=int(tablepmd[2]),tranwiteunlet=int(tablepmd[3]),tranwitedeuxlet=int(tablepmd[4]),tranwitroislet=int(tablepmd[5]),tranwitekatelet=int(tablepmd[7]),liens=liens)
            # pani = Panier(nom = nom), description = description ), prix = prix)
            
            db.session.add(pani)
            db.session.commit()
        if categorie == "VetementFemme" :
            tablepmd = [tranwitelet,tranneuflet,karentelet,tranwiteunlet,tranwitedeuxlet,tranwitroislet,tranwitekatelet,xslet,slet,mlet,llet,xllet,xxllet]
            if quantit == "rien" :
                quantit = 0
                
                for i in range(len(tablepmd))  :
                    print("les njdgjhdjkd",i)
                    if tablepmd[i] != 'rien' and tablepmd[i] != "" and tablepmd[i] != " " and (tablepmd[i]).isdigit(): 
                        quantit += int(tablepmd[i])
                    elif tablepmd[i] == 'rien' or tablepmd[i] == "" or tablepmd[i] == " ": 
                        tablepmd[i] = 0
                    else :
                        print('ya rien tchai')

                    print("dfghjk",tablepmd,"fin",tablepmd[i])
            
            print("qsdfghjk",tablepmd)
            
            pani = Ajouter(nom=nom,description=description,prix=prix,porceprix=porceprix,porce=porce,categorie=categorie,image=image,twoimage=twoimage,threeimage=threeimage,forimage=forimage,xs=xs,s=s,l=l,m=m,xl=xl,xxl=xxl,rouge=rouge,blanc=blanc,noir=noir,jaune=jaune,vert=vert,orange=orange,bleu=bleu,rose=rose,marron=marron,violet=violet,gris=gris,tranwite=tranwite,tranneuf=tranneuf,karente=karente,tranwiteun=tranwiteun,tranwitedeux=tranwitedeux,tranwitrois=tranwitrois,tranwitekate=tranwitekate,quantit=quantit,stat="vrai",xslet=int(tablepmd[7]),slet=int(tablepmd[8]),mlet=int(tablepmd[9]),llet=int(tablepmd[10]),xllet=int(tablepmd[11]),xxllet=int(tablepmd[12]) , tranwitelet=tranwitelet,tranneuflet=tranneuflet,karentelet=karentelet,tranwiteunlet=tranwiteunlet,tranwitedeuxlet=tranwitedeuxlet,tranwitroislet=tranwitroislet,tranwitekatelet=tranwitekatelet,liens=liens)
            # pani = Panier(nom = nom), description = description ), prix = prix)
            
            db.session.add(pani)
            db.session.commit()

        if categorie == "Montre" :
          
            
            
            pani = Ajouter(nom=nom,description=description,prix=prix,porceprix=porceprix,porce=porce,categorie=categorie,image=image,twoimage=twoimage,threeimage=threeimage,forimage=forimage,xs=xs,s=s,l=l,m=m,xl=xl,xxl=xxl,rouge=rouge,blanc=blanc,noir=noir,jaune=jaune,vert=vert,orange=orange,bleu=bleu,rose=rose,marron=marron,violet=violet,gris=gris,tranwite=tranwite,tranneuf=tranneuf,karente=karente,tranwiteun=tranwiteun,tranwitedeux=tranwitedeux,tranwitrois=tranwitrois,tranwitekate=tranwitekate,quantit=int(quantit),stat="vrai",xslet=xslet,slet=slet,mlet=mlet,llet=llet,xllet=xllet,xxllet=xxllet,tranwitelet=tranwitelet,tranneuflet=tranneuflet,karentelet=karentelet,tranwiteunlet=tranwiteunlet,tranwitedeuxlet=tranwitedeuxlet,tranwitroislet=tranwitroislet,tranwitekatelet=tranwitekatelet,liens=liens)
            # pani = Panier(nom = nom), description = description ), prix = prix)
            
            db.session.add(pani)
            db.session.commit()
             
        # self,nom,description,prix,porce,porceprix,categorie,image,twoimage,threeimage,forimage,xs,s,m,l,xl,xxl,rouge,blanc,noir,jaune,vert,orange,bleu,rose,marron,violet,gris,tranwite,tranneuf,karente,tranwiteun,tranwitedeux,tranwitrois,tranwitekate,quantit,stat,xslet,slet,mlet,llet,xllet,xxllet,tranwitelet,tranneuflet,karentelet,tranwiteunlet,tranwitedeuxlet,tranwitroislet,tranwitekatelet
        return redirect("/")
    
    
    # except :
    #     print(nom,'1',description,'2',image,'3',categorie,'4',twoimage,
    #     '5',threeimage
    #     ,'6',forimage
    #     ,'7',xs
    #     ,'8',s
    #     ,'9',m
    #     ,'10',l
    #     ,'11',xl
    #     ,'12',xxl
    #     ,'13',rouge
    #     ,'14',blanc
    #     ,'15',noir
    #     ,'16',jaune
    #     ,'17',vert
    #     ,'18',orange
    #     ,'19',bleu
    #     ,'20',rose
    #     ,'21',marron
    #     ,'22',violet
    #     ,'23',gris
    #     ,'24',tranwite
    #     ,'25',tranneuf
    #     ,'26',karente
    #     ,'27',tranwiteun
    #     ,'28',tranwitedeux
    #     ,'29',tranwitrois
    #     ,'30',tranwitekate
    #     ,"31" ,xslet
    #     ,"32" ,slet
    #     ,"33" ,mlet
    #     ,"34" ,llet
    #     ,"35" ,xllet
    #     ,"36" ,xxllet
    #     ,"37" ,tranwitelet
    #     ,"38" ,tranneuflet
    #     ,"39" ,karentelet
    #     ,"40" ,tranwiteunlet
    #     ,"41" ,tranwitedeuxlet
    #     ,"42" ,tranwitroislet
    #     ,"43" ,tranwitekatelet)
        # return render_template("boutique.html")
@app.route('/sacs/<int:id>')
def sacs(id):
    if 'utilisateur_id' in session:
        useru = Profil.query.get(session['utilisateur_id'])
    else:
        return redirect(f'/chasuss/{id}')
    useruo = Profil.query.get(useru.id)
    tableaus = Panieruser.query.all()
    tableauserz = Commantaire.query.all()
     
    conueww = 0    
    gdhsuud = []
    
    for i in tableaus : 
        
        if int(i.identifiant) == useruo.id :
            if i.statuse == "dispobine" :
                conueww += int(i.quantiteto)
            print('prevdg', i.identifiant , 'prevdg' , useruo.id)
            hdhdud = Ajouter.query.get(i.produite)
           

            gdhsuud.append({"element":i.produite,"prix":i.prixdepouce,"image":i.image,"quantite":i.quantiteto,"taille":i.tailed,"nom":i.nomprodui,"description":i.descrprosui,"pource":i.prixtottal,"porce":i.pourcentage ,"tailed":i.tailed,"categorie":i.categorie})

            # prixdepouce,nomprodui,descrprosui,pourcentage,categorie

    # conueww = len(gdhsuud) 
  
    
    commenta = []
    recupe = Ajouter.query.all()
    
    for i in recupe:
        if i.categorie ==  "Montre":
            commenta.append(i)

    if len(commenta)>10 :
        commenta = commenta[:10]

    commenta1 = []
    recupe = Ajouter.query.all()
    
    for i in recupe:
        if i.categorie == "chaussure" :
            commenta1.append(i)

    if len(commenta1)>10 :
        commenta1 = commenta1[:10]

    commenta2 = []
    recupe = Ajouter.query.all()
    
    for i in recupe:
        if i.categorie == "VetementFemme" :
            commenta2.append(i)

    if len(commenta2)>10 :
        commenta2 = commenta2[:10]


    
    user = Ajouter.query.filter_by(id=id).first()
    if user :
        data = [user.image,user.twoimage,user.threeimage,user.forimage]
        # a = Ajouter.query.all()
        # for i in a:
        #     if i.categorie == 'VetementFemme':
        #         data.append(i)
          
        for i in tableauserz:
            print("trouvé",i.idproduit,type(i.idproduit) ,"==", user.id,type(user.id))
            if i.idproduit == user.id :
                print("j'ai trouvé un",i.idproduit ,"=", user.id)
        return render_template('sacinfo.html',user = user,data=data,commenta=commenta,commenta1=commenta1,commenta2=commenta2,useru=useru,conueww=conueww,tableauserz=tableauserz)
    print("MO")

    return redirect("/sac")
    
@app.route("/sac")
def sac():
    if 'utilisateur_id' in session:
        useru = Profil.query.get(session['utilisateur_id'])
    else:
        return redirect('/chaussureslog')
    data = []
    a = Ajouter.query.all()
    for i in a:
        if i.categorie == 'chaussure':
            data.append(i)
    

    useruo = Profil.query.get(useru.id)
    tableaus = Panieruser.query.all()
    gdhsuud = []
    conueww = 0    
    
    for i in tableaus : 
        
        if int(i.identifiant) == useruo.id :
            print('prevdg', i.identifiant , 'prevdg' , useruo.id)
            hdhdud = Ajouter.query.get(i.produite)
        

            gdhsuud.append({"element":i.produite,"prix":i.prixdepouce,"image":i.image,"quantite":i.quantiteto,"taille":i.tailed,"nom":i.nomprodui,"description":i.descrprosui,"pource":i.prixtottal,"porce":i.pourcentage ,"tailed":i.tailed,"categorie":i.categorie, "statuse":i.statuse})

            # prixdepouce,nomprodui,descrprosui,pourcentage,categorie

    # conueww = len(gdhsuud)    
    somme = 0     
    for i in gdhsuud :
 
        if i["statuse"] == "dispobine" :
            
            conueww += int(i["quantite"])
            somme += int(i["pource"])  
    return render_template("sac.html", data = data ,conueww=conueww,somme=somme)
@app.route('/homme/<int:id>')
def homme(id):
    
    commenta = []
    recupe = Ajouter.query.all()
    
    for i in recupe:
        if i.categorie == "VetementHomme" :
            commenta.append(i)

    if len(commenta)>10 :
        commenta = commenta[:10]
 


    
    
    user = Ajouter.query.filter_by(id=id).first()
    if user :
        data = [user.image,user.twoimage,user.threeimage,user.forimage]
        # a = Ajouter.query.all()
        # for i in a:
        #     if i.categorie == 'VetementFemme':
        #         data.append(i)
        return render_template('hommeinfo.html',user = user,data=data,commenta=commenta)
    print("MO")

    return redirect("/hommes")
    
   
@app.route("/hommes")
def hommes():

    data = []
    a = Ajouter.query.all()
    for i in a:
        if i.categorie == 'VetementHomme':
            data.append(i)
    
    return render_template("/homme.html", data = data)
@app.route("/vente")
def acc():
    if 'utilisateur_id' in session:
        useru = Profil.query.get(session['utilisateur_id'])
    else:
        return redirect('/vetefemlog')
    data = []
    a = Ajouter.query.all()
    for i in a:
        if i.categorie == 'VetementFemme':
            data.append(i)

    
    
    useruo = Profil.query.get(useru.id)
    tableaus = Panieruser.query.all()
    gdhsuud = []
    conueww = 0  
    
    for i in tableaus : 
        
        if int(i.identifiant) == useruo.id :
            print('prevdg', i.identifiant , 'prevdg' , useruo.id)
            hdhdud = Ajouter.query.get(i.produite)
        

            gdhsuud.append({"element":i.produite,"prix":i.prixdepouce,"image":i.image,"quantite":i.quantiteto,"taille":i.tailed,"nom":i.nomprodui,"description":i.descrprosui,"pource":i.prixtottal,"porce":i.pourcentage ,"tailed":i.tailed,"categorie":i.categorie,"statuse":i.statuse})

            # prixdepouce,nomprodui,descrprosui,pourcentage,categorie

    # conueww = len(gdhsuud)    
    somme = 0     
    for i in gdhsuud :
      
        if i["statuse"] == "dispobine" :
            conueww += int(i["quantite"])
            somme += int(i["pource"])  
    return render_template("vente.html", data = data , conueww=conueww,somme=somme)
@app.route("/montre")
def montre():
    if 'utilisateur_id' in session:
        useru = Profil.query.get(session['utilisateur_id'])
    else:
        return redirect('/montrels')
    data = []
    a = Ajouter.query.all()
    for i in a:
        if i.categorie == 'Montre':
            data.append(i)
    

    
    
    useruo = Profil.query.get(useru.id)
    tableaus = Panieruser.query.all()
    gdhsuud = []
    conueww = 0    
    
    for i in tableaus : 
        
        if int(i.identifiant) == useruo.id :
            print('prevdg', i.identifiant , 'prevdg' , useruo.id)
            hdhdud = Ajouter.query.get(i.produite)
            

            gdhsuud.append({"element":i.produite,"prix":i.prixdepouce,"image":i.image,"quantite":i.quantiteto,"taille":i.tailed,"nom":i.nomprodui,"description":i.descrprosui,"pource":i.prixtottal,"porce":i.pourcentage ,"tailed":i.tailed,"categorie":i.categorie,"statuse":i.statuse})

            # prixdepouce,nomprodui,descrprosui,pourcentage,categorie

    # conueww = len(gdhsuud)  
    somme = 0     
    for i in gdhsuud :
        
        if i["statuse"] == "dispobine" :
            conueww += int(i["quantite"])
            somme += int(i["pource"])  
    return render_template("montre.html", data = data,conueww=conueww,somme=somme)
@app.route("/montrels")
def montrels():
    data = []
    a = Ajouter.query.all()
    for i in a:
        if i.categorie == 'Montre':
            data.append(i)
    

    return render_template("montrels.html", data = data)
@app.route("/chaussureslog")
def chaussureslog():
    data = []
    a = Ajouter.query.all()
    for i in a:
        if i.categorie == 'chaussure':
            data.append(i)
    

    return render_template("sacls.html", data = data)
@app.route("/vetefemlog")
def vetefemlog():
    data = []
    a = Ajouter.query.all()
    for i in a:
        if i.categorie == 'VetementFemme':
            data.append(i)
    

    return render_template("habifemmelog.html", data = data)
   

@app.route('/mesrechercheszq',methods = ["POST"])
def mesrechercheszq():
    
    if 'utilisateur_id' in session:
        useru = Profil.query.get(session['utilisateur_id'])
    else :
        useru = SMTP_USERNAME
        return redirect("/pre/monpanier")
    
 
    mail = Mail(app)
    msg = Message("Préoccupation ou une suggestion depuis la plateforme",
                sender=useru.last_name,
                recipients=[SMTP_USERNAME])
    recher = request.form.get('recher', '').lower()
    # Envoyer l'e-mail
    msg.body = recher
    mail.send(msg)
    

    return redirect('/')
@app.route('/mesrecherches',methods = ["POST"])
def rechepo():
    recherches = {
        'montres': '/montre',
        'montre': '/montre',
        'robes': '/vente',
        'robe': '/vente',
        'habit femme': '/vente',
        'femmes': '/vente',
        'femme': '/vente',
        'chaussures': '/sac',
        'chaussure': '/sac',
        'chaussures femmes': '/sac',
        'chaussure femmes': '/sac',
        'chaussures femme': '/sac',
        'chaussure femme': '/sac'
    }

    recher = request.form.get('recher', '').lower()
    redirection = recherches.get(recher)

    if redirection:
        return redirect(redirection)
    else:
        return redirect('/indisponible')

    # recher = request.form.get('recher')
    # if recher.lower() == 'montres' or recher.lower() == 'montre' :
    #     return redirect('/montre')
    # if recher.lower() == 'robe' or recher.lower() == 'robes' or recher.lower() == 'habit femme' or recher.lower() == 'femmes' or recher.lower() == 'femme':
    #     return redirect('/vente')
    # if recher.lower() == 'chaussures' or recher.lower() == 'chaussure' or recher.lower() == 'chaussures femmes' or recher.lower() == 'chaussure femmes' or recher.lower() == 'chaussures femme' or recher.lower() == 'chaussure femme':
    #     return redirect('/sac')
    # return redirect('/indisponible')
# FIN AJOUTER IMAGES DES ARTICLES{}
    

# @app.route("/")
# def acc():
#     return render_template("/vente.html", data = data)

# @app.route("/")
# def acc():
#     return render_template("/acceuil.html")

@app.route("/ajou")
def ajou():
   
    eude = Ajouter.query.all()
    return render_template("ajoufini.html")
import json
@app.route('/monprofil')
def monprofil():
    
    if 'utilisateur_id' in session:
        useru = Profil.query.get(session['utilisateur_id'])
    else:
        return redirect(f'/pre/acceuilconnect')
  



    commenta = []
    recupe = Ajouter.query.all()
    
    for i in recupe:
        if i.categorie ==  "Montre":
            commenta.append(i)

    if len(commenta)>10 :
        commenta = commenta[:10]

    commenta1 = []
    recupe = Ajouter.query.all()
    
    for i in recupe:
        if i.categorie == "chaussure" :
            commenta1.append(i)

    if len(commenta1)>10 :
        commenta1 = commenta1[:10]

    commenta2 = []
    recupe = Ajouter.query.all()
    
    for i in recupe:
        if i.categorie == "VetementFemme" :
            commenta2.append(i)

    if len(commenta2)>10 :
        commenta2 = commenta2[:10]



   
    inform = Profil.query.get(useru.id)

    
    
   
    
    
    
    
   
    tabefdl = {"id":inform.id ,"infoplus":inform.infoplus ,"last_name":inform.last_name ,"first_name":inform.first_name ,"prenom": inform.prenom ,"livraison":inform.livraison ,"residence":inform.residence,"numero":inform.numero ,"deslivraion":inform.deslivraion }


    return render_template('profildeuser.html',commenta=commenta,commenta1=commenta1,commenta2=commenta2,useru=useru,tabefdl=tabefdl)
@app.route('/boiteamail')
def boiteamail():
    
    if 'utilisateur_id' in session:
        useru = Profil.query.get(session['utilisateur_id'])
    else:
        return redirect(f'/pre/boiteamail')
  

   

    comens = Mailboite.query.all()
    pmse = []
    
    for i in comens :
        if int(i.proprio) == int(useru.id):
            pmse.append(i)

    lenhsfd = len(pmse)


    commenta = []
    recupe = Ajouter.query.all()
    
    for i in recupe:
        if i.categorie ==  "Montre":
            commenta.append(i)

    if len(commenta)>10 :
        commenta = commenta[:10]

    commenta1 = []
    recupe = Ajouter.query.all()
    
    for i in recupe:
        if i.categorie == "chaussure" :
            commenta1.append(i)

    if len(commenta1)>10 :
        commenta1 = commenta1[:10]

    commenta2 = []
    recupe = Ajouter.query.all()
    
    for i in recupe:
        if i.categorie == "VetementFemme" :
            commenta2.append(i)

    if len(commenta2)>10 :
        commenta2 = commenta2[:10]



    return render_template('boiteamail.html',commenta=commenta,commenta1=commenta1,commenta2=commenta2,useru=useru,lenhsfd=lenhsfd,pmse=pmse)
@app.route('/mescommandes')
def mescommandes():
    
    if 'utilisateur_id' in session:
        useru = Profil.query.get(session['utilisateur_id'])
    else:
        return redirect(f'/pre/mescommandes')
  



    commenta = []
    recupe = Ajouter.query.all()
    comens = Commande.query.all()
    pmse = []
    
    for i in comens :
        if int(i.client) == int(useru.id):
            pmse.append(i)

    lenhsfd = len(pmse)

    for i in recupe:
        if i.categorie ==  "Montre":
            commenta.append(i)

    if len(commenta)>10 :
        commenta = commenta[:10]

    commenta1 = []
    recupe = Ajouter.query.all()
    
    for i in recupe:
        if i.categorie == "chaussure" :
            commenta1.append(i)

    if len(commenta1)>10 :
        commenta1 = commenta1[:10]

    commenta2 = []
    recupe = Ajouter.query.all()
    
    for i in recupe:
        if i.categorie == "VetementFemme" :
            commenta2.append(i)

    if len(commenta2)>10 :
        commenta2 = commenta2[:10]



    return render_template('mescommandes.html',commenta=commenta,commenta1=commenta1,commenta2=commenta2,useru=useru,pmse=pmse,lenhsfd=lenhsfd)
  
  
@app.route('/montres/<int:id>')
def montres(id):
    
    if 'utilisateur_id' in session:
        useru = Profil.query.get(session['utilisateur_id'])
    else:
        return redirect(f'/habidetls/{id}')
    useruo = Profil.query.get(useru.id)
    tableaus = Panieruser.query.all()
    tableauserz = Commantaire.query.all()
    gdhsuud = []
    conueww = 0  
  
    for i in tableaus : 
        
        if int(i.identifiant) == useruo.id :
            if i.statuse == "dispobine" :
                conueww += int(i.quantiteto)
            print('prevdg', i.identifiant , 'prevdg' , useruo.id)
            hdhdud = Ajouter.query.get(i.produite)
            gdhsuud.append({"element":i.produite,"prix":i.prixdepouce,"image":i.image,"quantite":i.quantiteto,"taille":i.tailed,"nom":i.nomprodui,"description":i.descrprosui,"pource":i.prixtottal,"porce":i.pourcentage ,"tailed":i.tailed,"categorie":i.categorie})

            # prixdepouce,nomprodui,descrprosui,pourcentage,categorie
    # conueww = len(gdhsuud)   



    commenta = []
    recupe = Ajouter.query.all()
    
    for i in recupe:
        if i.categorie ==  "Montre":
            commenta.append(i)

    if len(commenta)>10 :
        commenta = commenta[:10]

    commenta1 = []
    recupe = Ajouter.query.all()
    
    for i in recupe:
        if i.categorie == "chaussure" :
            commenta1.append(i)

    if len(commenta1)>10 :
        commenta1 = commenta1[:10]

    commenta2 = []
    recupe = Ajouter.query.all()
    
    for i in recupe:
        if i.categorie == "VetementFemme" :
            commenta2.append(i)

    if len(commenta2)>10 :
        commenta2 = commenta2[:10]



    
    user = Ajouter.query.filter_by(id=id).first()
    if user :
        data = [user.image,user.twoimage,user.threeimage,user.forimage]
        # a = Ajouter.query.all()
        # for i in a:
        #     if i.categorie == 'VetementFemme':
        #         data.append(i)
        return render_template('montrederail.html',user = user,data=data,commenta=commenta,commenta1=commenta1,commenta2=commenta2,useru=useru,conueww=conueww,tableauserz=tableauserz)
    print("MO")

    return redirect("/montre")
  
    


@app.route('/chasuss/<int:id>')
def chasuss(id):
    
    # useruo = Profil.query.get(useru.id)
    # tableaus = Panieruser.query.all()
    # gdhsuud = []
    
    # for i in tableaus : 
        
    #     if int(i.identifiant) == useruo.id :
    #         print('prevdg', i.identifiant , 'prevdg' , useruo.id)
    #         hdhdud = Ajouter.query.get(i.produite)
    #         gdhsuud.append({"element":i.produite,"prix":hdhdud.prix,"image":i.image,"quantite":i.quantiteto,"taille":i.tailed,"nom":hdhdud.nom,"description":hdhdud.description,"pource":hdhdud.porceprix,"porce":hdhdud.porce ,"tailed":i.tailed,"categorie":hdhdud.categorie})

    # conueww = len(gdhsuud)   



    
  
    commenta = []
    recupe = Ajouter.query.all()
    
    for i in recupe:
        if i.categorie ==  "Montre":
            commenta.append(i)

    if len(commenta)>10 :
        commenta = commenta[:10]

    commenta1 = []
    recupe = Ajouter.query.all()
    
    for i in recupe:
        if i.categorie == "chaussure" :
            commenta1.append(i)

    if len(commenta1)>10 :
        commenta1 = commenta1[:10]

    commenta2 = []
    recupe = Ajouter.query.all()
    
    for i in recupe:
        if i.categorie == "VetementFemme" :
            commenta2.append(i)

    if len(commenta2)>10 :
        commenta2 = commenta2[:10]
 



    
    user = Ajouter.query.filter_by(id=id).first()
    if user :
        data = [user.image,user.twoimage,user.threeimage,user.forimage]
        # a = Ajouter.query.all()
        # for i in a:
        #     if i.categorie == 'VetementFemme':
        #         data.append(i)
        return render_template('sacinfols.html',user = user,data=data,commenta=commenta,commenta1=commenta1,commenta2=commenta2)
    print("MO")

    return redirect("/chaussureslog")
@app.route('/habidetls/<int:id>')
def habidetls(id):
    
    # useruo = Profil.query.get(useru.id)
    # tableaus = Panieruser.query.all()
    # gdhsuud = []
    
    # for i in tableaus : 
        
    #     if int(i.identifiant) == useruo.id :
    #         print('prevdg', i.identifiant , 'prevdg' , useruo.id)
    #         hdhdud = Ajouter.query.get(i.produite)
    #         gdhsuud.append({"element":i.produite,"prix":hdhdud.prix,"image":i.image,"quantite":i.quantiteto,"taille":i.tailed,"nom":hdhdud.nom,"description":hdhdud.description,"pource":hdhdud.porceprix,"porce":hdhdud.porce ,"tailed":i.tailed,"categorie":hdhdud.categorie})

    # conueww = len(gdhsuud)   



    
  
    commenta = []
    recupe = Ajouter.query.all()
    
    for i in recupe:
        if i.categorie ==  "Montre":
            commenta.append(i)

    if len(commenta)>10 :
        commenta = commenta[:10]

    commenta1 = []
    recupe = Ajouter.query.all()
    
    for i in recupe:
        if i.categorie == "chaussure" :
            commenta1.append(i)

    if len(commenta1)>10 :
        commenta1 = commenta1[:10]

    commenta2 = []
    recupe = Ajouter.query.all()
    
    for i in recupe:
        if i.categorie == "VetementFemme" :
            commenta2.append(i)

    if len(commenta2)>10 :
        commenta2 = commenta2[:10]
 



    
    user = Ajouter.query.filter_by(id=id).first()
    if user :
        data = [user.image,user.twoimage,user.threeimage,user.forimage]
        # a = Ajouter.query.all()
        # for i in a:
        #     if i.categorie == 'VetementFemme':
        #         data.append(i)
        return render_template('habiingolog.html',user = user,data=data,commenta=commenta,commenta1=commenta1,commenta2=commenta2)
    print("MO")

    return redirect("/vetefemlog")
@app.route('/montredetls/<int:id>')
def montredetls(id):
    
    # useruo = Profil.query.get(useru.id)
    # tableaus = Panieruser.query.all()
    # gdhsuud = []
    
    # for i in tableaus : 
        
    #     if int(i.identifiant) == useruo.id :
    #         print('prevdg', i.identifiant , 'prevdg' , useruo.id)
    #         hdhdud = Ajouter.query.get(i.produite)
    #         gdhsuud.append({"element":i.produite,"prix":hdhdud.prix,"image":i.image,"quantite":i.quantiteto,"taille":i.tailed,"nom":hdhdud.nom,"description":hdhdud.description,"pource":hdhdud.porceprix,"porce":hdhdud.porce ,"tailed":i.tailed,"categorie":hdhdud.categorie})

    # conueww = len(gdhsuud)   



    
  
    commenta = []
    recupe = Ajouter.query.all()
    
    for i in recupe:
        if i.categorie ==  "Montre":
            commenta.append(i)

    if len(commenta)>10 :
        commenta = commenta[:10]

    commenta1 = []
    recupe = Ajouter.query.all()
    
    for i in recupe:
        if i.categorie == "chaussure" :
            commenta1.append(i)

    if len(commenta1)>10 :
        commenta1 = commenta1[:10]

    commenta2 = []
    recupe = Ajouter.query.all()
    
    for i in recupe:
        if i.categorie == "VetementFemme" :
            commenta2.append(i)

    if len(commenta2)>10 :
        commenta2 = commenta2[:10]
 



    
    user = Ajouter.query.filter_by(id=id).first()
    if user :
        data = [user.image,user.twoimage,user.threeimage,user.forimage]
        # a = Ajouter.query.all()
        # for i in a:
        #     if i.categorie == 'VetementFemme':
        #         data.append(i)
        return render_template('montredetls.html',user = user,data=data,commenta=commenta,commenta1=commenta1,commenta2=commenta2)
    print("MO")

    return redirect("/montrels")

    
@app.route('/info/<int:id>')
def info(id):
    if 'utilisateur_id' in session:
        useru = Profil.query.get(session['utilisateur_id'])
    else:
        
        return redirect(f'/habidetls/{id}')
    useruo = Profil.query.get(useru.id)
    tableaus = Panieruser.query.all()
    tableauserz = Commantaire.query.all()
    gdhsuud = []
    conueww = 0   
    
    for i in tableaus : 
        
        if int(i.identifiant) == useruo.id :
            if i.statuse == "dispobine" :
                conueww += int(i.quantiteto)
            print('prevdg', i.identifiant , 'prevdg' , useruo.id)
            hdhdud = Ajouter.query.get(i.produite)
            gdhsuud.append({"element":i.produite,"prix":i.prixdepouce,"image":i.image,"quantite":i.quantiteto,"taille":i.tailed,"nom":i.nomprodui,"description":i.descrprosui,"pource":i.prixtottal,"porce":i.pourcentage ,"tailed":i.tailed,"categorie":i.categorie})



            

    
    

  
    commenta = []
    recupe = Ajouter.query.all()
    
    for i in recupe:
        if i.categorie ==  "Montre":
            commenta.append(i)

    if len(commenta)>10 :
        commenta = commenta[:10]

    commenta1 = []
    recupe = Ajouter.query.all()
    
    for i in recupe:
        if i.categorie == "chaussure" :
            commenta1.append(i)

    if len(commenta1)>10 :
        commenta1 = commenta1[:10]

    commenta2 = []
    recupe = Ajouter.query.all()
    
    for i in recupe:
        if i.categorie == "VetementFemme" :
            commenta2.append(i)

    if len(commenta2)>10 :
        commenta2 = commenta2[:10]



    
    user = Ajouter.query.filter_by(id=id).first()
    if user :
        data = [user.image,user.twoimage,user.threeimage,user.forimage]
        # a = Ajouter.query.all()
        # for i in a:
        #     if i.categorie == 'VetementFemme':
        #         data.append(i)
        return render_template('info.html',user = user,data=data,commenta=commenta,commenta1=commenta1,commenta2=commenta2,useru=useru,conueww=conueww,tableauserz=tableauserz)
    print("MO")

    return redirect("/vente")

# @app.route('/zet/<int:id>')
# def zet(id):
    
#     user = Maboutik.query.filter_by(id=id).first()
#     return render_template('info.html',user = user)

# @app.route('/info/<int:id>',methods=["POST"])
# def info(id):
#     if request.method == "POST" :
#         user = Maboutik.query.filter_by(id=id).first()
#         return render_template('info.html',user = user)
#     print("MO")
#     return redirect("/vente")


import random
@app.route('/finishcommand', methods=["POST"])
def finishcommand():
    if 'utilisateur_id' in session:
        useru = Profil.query.get(session['utilisateur_id'])
    else:
        return redirect('/pre/validecommande')
    data = datetime.date.today()
    dataheure = datetime.datetime.now()
    formatted_time = dataheure.strftime('%H')
    formatted = dataheure.strftime('%M')
    print(data)
    print(dataheure)
    print(formatted_time)
    print(formatted)
    print(dataheure)
    jsuef = f"Reçu le {data} à {formatted_time}h{formatted}"
    tableaus = Panieruser.query.all()
    nom = request.form.get("nom")
    prenom = request.form.get("prenom")
    mail = request.form.get("mail")
   
    numero = request.form.get("numero")
   
    aller = request.form.get("aller")
    livrer = request.form.get("livrer")
    residence = request.form.get("residence")
    lieulivraison = request.form.get("lieulivraison")
    deslieulivraison = request.form.get("deslieulivraison")

    commande = Commande.query.all()
    compterut = 0
    veridie =0
    total =0
    quantitezr =0
    pmse = []
    
    
    
    for i in commande:
        de = i.comnumid
        if int(de[-1]) >= int(compterut) :
            compterut = int(de[-1])
            
    for i in tableaus : 
        couleurz = ["ZHRE-pJPO-808-HP-02","MLUE-SKKO-467-AZ-09","NDJB-XGDU-849-SQ-02","HSBS-IWBV-9348-TE-09","VSGD-LSOS-9348-TE-08","ZRRE-IEBV-9348-TE-09","FDGH-IUES-9348-TE-09","NSIZ-IEZV-7352-TS-09","FDGH-LSBD-9348-TE-07","FAGH-ZRAZ-9148-TE-02","PQMD-IEBV-1348-SQ-03","ZAKS-IEBV-9348-ZE-09","IJDS-ISBV-9348-XC-09","ZIZS-IEBV-9328-EZ-01","FDGH-NSIZ-9342-TE-02"]
    
        aleaez = random.randint(0,(len(couleurz)-1))
        print("aleatoore",aleaez)
        if int(i.identifiant) == useru.id and i.statuse == "dispobine" :
            
            hdhdud = Ajouter.query.get(i.produite)
            compterut = int(compterut) + 1
            compterute =  couleurz[aleaez] + str(compterut)
             
            
            quantitezr += int(i.quantiteto)
            total += int(i.quantiteto) * int(hdhdud.porceprix)
            pmse.append({"idpro":i.produite,"nom":nom,"prenom":prenom,"mail":mail,"residence":residence,"produitname":hdhdud.nom,"prixunit":hdhdud.porceprix,"pourcent":hdhdud.porce,"prixtotal":(int(i.quantiteto) * int(hdhdud.porceprix)),"aller":aller,"livrer":livrer,"numero":numero,"lieulivraison":lieulivraison,"deslieulivraison":deslieulivraison,"comnumid":compterute,"taille":i.tailed,"quantite":i.quantiteto,"status":"En cours","image":i.image,"categorie":hdhdud.categorie,"client":useru.id})
            pani = Commande(idpro=i.produite,nom=nom,prenom=prenom,mail=mail,residence=residence,produitname=hdhdud.nom,prixunit=hdhdud.porceprix,pourcent=hdhdud.porce,prixtotal=(int(i.quantiteto) * int(hdhdud.porceprix)),aller=aller,livrer=livrer,numero=numero,lieulivraison=lieulivraison,deslieulivraison=deslieulivraison,comnumid=compterute,taille=i.tailed,quantite=i.quantiteto,status="En cours",image=i.image,categorie=hdhdud.categorie,client=useru.id)
                    
            db.session.add(pani)
            db.session.commit()
            veridie+=1

        if int(i.identifiant) == useru.id and i.statuse == "dispobine" :
            pani = Mailboite(dateactu=jsuef,image=i.image,status="En cours",depart=aller,arriver=livrer,proprio=useru.id,serie=compterute,lieu=lieulivraison,nom=hdhdud.nom,categorie=hdhdud.categorie)
                    
            db.session.add(pani)
            db.session.commit()
    

    if veridie > 0:
        tableods = ""
        for i in tableaus : 
            if int(i.identifiant) == useru.id and i.statuse == "dispobine" :
                
                hdhdud = Ajouter.query.get(i.produite)
                compterut +=1
                phrase = f" \n Categorie {hdhdud.categorie} , Nom {hdhdud.nom} , Prix unitaire {hdhdud.porceprix} , Qtite {i.quantiteto} , Prix total{(int(i.quantiteto) * int(hdhdud.porceprix))} "
                tableods += phrase



        # msg = MIMEMultipart()
        # msg['From'] = SMTP_USERNAME
        # msg['To'] = useru.last_name
        # msg['Subject'] = "Commande éffectuée chez HINGTON SHOP"
        # masz = f"{nom} {prenom} \n {numero} \n {lieulivraison} {deslieulivraison} \n {tableods}"
        # message_texte = MIMEText(masz)
        # msg.attach(message_texte)
        
        # Connexion au serveur SMTP et envoi du courrier électronique
        # try:
        #     server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        #     server.starttls()
        #     server.login(SMTP_USERNAME, SMTP_PASSWORD)
        #     server.sendmail(SMTP_USERNAME, useru.last_name, msg.as_string())
        #     server.quit()
        #     return redirect('/mescommandes')
        # except Exception as e:
        #     return "Erreur lors de l'envoi de l'e-mail : " + str(e)

        monpanue = Panieruser.query.all()
        for i in monpanue :
            print("avan",int(i.identifiant) ,"==", int(useru.id))
            if int(i.identifiant) == int(useru.id) :
                print("apret",int(i.identifiant) ,"==", int(useru.id))
                lpmsezs = int(i.id)
                adm= Panieruser.query.get(lpmsezs)
                db.session.delete(adm)
                db.session.commit()
    

        comens = Commande.query.all()

        
        for i in comens :
            
            if i.mail == useru.last_name:
                datez = i.livrer
                commen = i.comnumid
                prenom = i.prenom
                nom =i.nom

        lenhsfd = len(pmse)

        
        mail = Mail(app)
        msg = Message("Commande éffectuée chez HINGTON SHOP",
                    sender=SMTP_USERNAME,
                    recipients=[useru.last_name])
        with app.open_resource("static/IMAGE/hinglogo.png") as img:
                msg.attach("hinglogo.png", "image/jpeg", img.read(), headers={'Content-ID': f'<myimage>'})

        with app.open_resource("static/IMAGE/fgshs.png") as img:
                msg.attach("fgshs.png", "image/jpeg", img.read(), headers={'Content-ID': f'<facebook>'})
        with app.open_resource("static/IMAGE/tikti.png") as img:
                msg.attach("tikti.png", "image/jpeg", img.read(), headers={'Content-ID': f'<titko>'})
        with app.open_resource("static/IMAGE/awp.png") as img:
                msg.attach("awp.png", "image/jpeg", img.read(), headers={'Content-ID': f'<whats>'})
        for i in pmse :
            lesfg = i["image"]
            with app.open_resource(f"static/uploads/{lesfg}") as img:
                msg.attach(f"{lesfg}", "image/jpeg", img.read(), headers={'Content-ID': f'<{lesfg}>'})
        # Rendre le template HTML
        msg.html = render_template("designmail.html",lenhsfd=lenhsfd,pmse=pmse,prenom=prenom,commen=commen,nom=nom,datez=datez,livraison=lieulivraison,emballage=data,quantitezr=quantitezr,total=total)
        
        # Envoyer l'e-mail
        mail.send(msg)



        
        

        for empa in pmse :

            
                
            print(empa["categorie"])
            if empa["categorie"] == "VetementFemme" :

                print(empa["categorie"])
                taille = empa["taille"]
                
                adm = Ajouter.query.get(int(empa["idpro"]))

                if taille == "m" :
                    if int(adm.mlet) > 0 :
                        print("int(adm.mlet)", int(adm.mlet) , ">" , 0)

                        if int(adm.quantit) == int(empa["quantite"]) :

                            adm.stat = "faux"
                            adm.mlet = int(adm.mlet) - int(empa["quantite"])
                            adm.quantit = int(adm.quantit) - int(empa["quantite"])
                            db.session.commit()

                            monkzu = Panieruser.query.all()
                            print("on a recu")
                            for imo in monkzu :
                                if int(imo.produite) == int(empa["idpro"]) :
                                    sfymp = int(imo.dispono) - int(empa["quantite"])
                                    if sfymp >= int(imo.quantiteto)   :
                                        imo.dispono = int(imo.dispono) - int(empa["quantite"])
                                        imo.statuse = "dispobine"
                                        print(sfymp , ">=" , int(imo.quantiteto))
                                        print("terlin")
                                    else : 
                                        print(sfymp , "<" , int(imo.quantiteto))
                                        imo.dispono = int(imo.dispono) - int(empa["quantite"])
                                        imo.statuse = "nondisp"
                                        print("pas terlin")
                                    db.session.commit()
                            continue


                        if int(adm.quantit) == 0 :
                            adm.stat = "faux"
                            
                            db.session.commit()
                            continue

                        adm.mlet = int(adm.mlet) - int(empa["quantite"])
                        adm.quantit = int(adm.quantit) - int(empa["quantite"])
                        db.session.commit()




                        monkzu = Panieruser.query.all()
                        for imo in monkzu :
                            if int(imo.produite) == int(empa["idpro"]) :
                                sfymp = int(imo.dispono) - int(empa["quantite"])
                                if sfymp >= int(imo.quantiteto)   :
                                    imo.dispono = int(imo.dispono) - int(empa["quantite"])
                                    imo.statuse = "dispobine"
                                    print(sfymp , ">=" , int(imo.quantiteto))
                                else : 
                                    print(sfymp , "<" , int(imo.quantiteto))
                                    imo.dispono = int(imo.dispono) - int(empa["quantite"])
                                    imo.statuse = "nondisp"
                                db.session.commit()
                        
                        continue

                    if int(adm.mlet) == 0 :
                        continue



                if taille == "xs" :
                    if int(adm.xslet) > 0 :
                        print("int(adm.xslet)", int(adm.xslet) , ">" , 0)

                        if int(adm.quantit) == int(empa["quantite"]) :

                            adm.stat = "faux"
                            adm.xslet = int(adm.xslet) - int(empa["quantite"])
                            adm.quantit = int(adm.quantit) - int(empa["quantite"])
                            db.session.commit()

                            monkzu = Panieruser.query.all()
                            print("on a recu")
                            for imo in monkzu :
                                if int(imo.produite) == int(empa["idpro"]) :
                                    sfymp = int(imo.dispono) - int(empa["quantite"])
                                    if sfymp >= int(imo.quantiteto)   :
                                        imo.dispono = int(imo.dispono) - int(empa["quantite"])
                                        imo.statuse = "dispobine"
                                        print(sfymp , ">=" , int(imo.quantiteto))
                                        print("terlin")
                                    else : 
                                        print(sfymp , "<" , int(imo.quantiteto))
                                        imo.dispono = int(imo.dispono) - int(empa["quantite"])
                                        imo.statuse = "nondisp"
                                        print("pas terlin")
                                    db.session.commit()
                            continue


                        if int(adm.quantit) == 0 :
                            adm.stat = "faux"
                            
                            db.session.commit()
                            continue

                        adm.xslet = int(adm.xslet) - int(empa["quantite"])
                        adm.quantit = int(adm.quantit) - int(empa["quantite"])
                        db.session.commit()




                        monkzu = Panieruser.query.all()
                        for imo in monkzu :
                            if int(imo.produite) == int(empa["idpro"]) :
                                sfymp = int(imo.dispono) - int(empa["quantite"])
                                if sfymp >= int(imo.quantiteto)   :
                                    imo.dispono = int(imo.dispono) - int(empa["quantite"])
                                    imo.statuse = "dispobine"
                                    print(sfymp , ">=" , int(imo.quantiteto))
                                else : 
                                    print(sfymp , "<" , int(imo.quantiteto))
                                    imo.dispono = int(imo.dispono) - int(empa["quantite"])
                                    imo.statuse = "nondisp"
                                db.session.commit()
                        
                        continue

                    if int(adm.xslet) == 0 :
                        continue


                if taille == "xl" :
                    if int(adm.xllet) > 0 :
                        print("int(adm.xllet)", int(adm.xllet) , ">" , 0)

                        if int(adm.quantit) == int(empa["quantite"]) :

                            adm.stat = "faux"
                            adm.xllet = int(adm.xllet) - int(empa["quantite"])
                            adm.quantit = int(adm.quantit) - int(empa["quantite"])
                            db.session.commit()

                            monkzu = Panieruser.query.all()
                            print("on a recu")
                            for imo in monkzu :
                                if int(imo.produite) == int(empa["idpro"]) :
                                    sfymp = int(imo.dispono) - int(empa["quantite"])
                                    if sfymp >= int(imo.quantiteto)   :
                                        imo.dispono = int(imo.dispono) - int(empa["quantite"])
                                        imo.statuse = "dispobine"
                                        print(sfymp , ">=" , int(imo.quantiteto))
                                        print("terlin")
                                    else : 
                                        print(sfymp , "<" , int(imo.quantiteto))
                                        imo.dispono = int(imo.dispono) - int(empa["quantite"])
                                        imo.statuse = "nondisp"
                                        print("pas terlin")
                                    db.session.commit()
                            continue


                        if int(adm.quantit) == 0 :
                            adm.stat = "faux"
                            
                            db.session.commit()
                            continue

                        adm.xllet = int(adm.xllet) - int(empa["quantite"])
                        adm.quantit = int(adm.quantit) - int(empa["quantite"])
                        db.session.commit()




                        monkzu = Panieruser.query.all()
                        for imo in monkzu :
                            if int(imo.produite) == int(empa["idpro"]) :
                                sfymp = int(imo.dispono) - int(empa["quantite"])
                                if sfymp >= int(imo.quantiteto)   :
                                    imo.dispono = int(imo.dispono) - int(empa["quantite"])
                                    imo.statuse = "dispobine"
                                    print(sfymp , ">=" , int(imo.quantiteto))
                                else : 
                                    print(sfymp , "<" , int(imo.quantiteto))
                                    imo.dispono = int(imo.dispono) - int(empa["quantite"])
                                    imo.statuse = "nondisp"
                                db.session.commit()
                        
                        continue

                    if int(adm.xllet) == 0 :
                        continue

                if taille == "xxl" :
                    if int(adm.xxllet) > 0 :
                        print("int(adm.xxllet)", int(adm.xxllet) , ">" , 0)

                        if int(adm.quantit) == int(empa["quantite"]) :

                            adm.stat = "faux"
                            adm.xxllet = int(adm.xxllet) - int(empa["quantite"])
                            adm.quantit = int(adm.quantit) - int(empa["quantite"])
                            db.session.commit()

                            monkzu = Panieruser.query.all()
                            print("on a recu")
                            for imo in monkzu :
                                if int(imo.produite) == int(empa["idpro"]) :
                                    sfymp = int(imo.dispono) - int(empa["quantite"])
                                    if sfymp >= int(imo.quantiteto)   :
                                        imo.dispono = int(imo.dispono) - int(empa["quantite"])
                                        imo.statuse = "dispobine"
                                        print(sfymp , ">=" , int(imo.quantiteto))
                                        print("terlin")
                                    else : 
                                        print(sfymp , "<" , int(imo.quantiteto))
                                        imo.dispono = int(imo.dispono) - int(empa["quantite"])
                                        imo.statuse = "nondisp"
                                        print("pas terlin")
                                    db.session.commit()
                            continue


                        if int(adm.quantit) == 0 :
                            adm.stat = "faux"
                            
                            db.session.commit()
                            continue

                        adm.xxllet = int(adm.xxllet) - int(empa["quantite"])
                        adm.quantit = int(adm.quantit) - int(empa["quantite"])
                        db.session.commit()




                        monkzu = Panieruser.query.all()
                        for imo in monkzu :
                            if int(imo.produite) == int(empa["idpro"]) :
                                sfymp = int(imo.dispono) - int(empa["quantite"])
                                if sfymp >= int(imo.quantiteto)   :
                                    imo.dispono = int(imo.dispono) - int(empa["quantite"])
                                    imo.statuse = "dispobine"
                                    print(sfymp , ">=" , int(imo.quantiteto))
                                else : 
                                    print(sfymp , "<" , int(imo.quantiteto))
                                    imo.dispono = int(imo.dispono) - int(empa["quantite"])
                                    imo.statuse = "nondisp"
                                db.session.commit()
                        
                        continue

                    if int(adm.xxllet) == 0 :
                        continue

                

                if taille == "s" :
                    if int(adm.slet) > 0 :
                        print("int(adm.slet)", int(adm.slet) , ">" , 0)

                        if int(adm.quantit) == int(empa["quantite"]) :

                            adm.stat = "faux"
                            adm.slet = int(adm.slet) - int(empa["quantite"])
                            adm.quantit = int(adm.quantit) - int(empa["quantite"])
                            db.session.commit()

                            monkzu = Panieruser.query.all()
                            print("on a recu")
                            for imo in monkzu :
                                if int(imo.produite) == int(empa["idpro"]) :
                                    sfymp = int(imo.dispono) - int(empa["quantite"])
                                    if sfymp >= int(imo.quantiteto)   :
                                        imo.dispono = int(imo.dispono) - int(empa["quantite"])
                                        imo.statuse = "dispobine"
                                        print(sfymp , ">=" , int(imo.quantiteto))
                                        print("terlin")
                                    else : 
                                        print(sfymp , "<" , int(imo.quantiteto))
                                        imo.dispono = int(imo.dispono) - int(empa["quantite"])
                                        imo.statuse = "nondisp"
                                        print("pas terlin")
                                    db.session.commit()
                            continue


                        if int(adm.quantit) == 0 :
                            adm.stat = "faux"
                            
                            db.session.commit()
                            continue

                        adm.slet = int(adm.slet) - int(empa["quantite"])
                        adm.quantit = int(adm.quantit) - int(empa["quantite"])
                        db.session.commit()




                        monkzu = Panieruser.query.all()
                        for imo in monkzu :
                            if int(imo.produite) == int(empa["idpro"]) :
                                sfymp = int(imo.dispono) - int(empa["quantite"])
                                if sfymp >= int(imo.quantiteto)   :
                                    imo.dispono = int(imo.dispono) - int(empa["quantite"])
                                    imo.statuse = "dispobine"
                                    print(sfymp , ">=" , int(imo.quantiteto))
                                else : 
                                    print(sfymp , "<" , int(imo.quantiteto))
                                    imo.dispono = int(imo.dispono) - int(empa["quantite"])
                                    imo.statuse = "nondisp"
                                db.session.commit()
                        
                        continue

                    if int(adm.slet) == 0 :
                        continue

                if taille == "l" :
                    if int(adm.llet) > 0 :
                        print("int(adm.llet)", int(adm.llet) , ">" , 0)

                        if int(adm.quantit) == int(empa["quantite"]) :

                            adm.stat = "faux"
                            adm.llet = int(adm.llet) - int(empa["quantite"])
                            adm.quantit = int(adm.quantit) - int(empa["quantite"])
                            db.session.commit()

                            monkzu = Panieruser.query.all()
                            print("on a recu")
                            for imo in monkzu :
                                if int(imo.produite) == int(empa["idpro"]) :
                                    sfymp = int(imo.dispono) - int(empa["quantite"])
                                    if sfymp >= int(imo.quantiteto)   :
                                        imo.dispono = int(imo.dispono) - int(empa["quantite"])
                                        imo.statuse = "dispobine"
                                        print(sfymp , ">=" , int(imo.quantiteto))
                                        print("terlin")
                                    else : 
                                        print(sfymp , "<" , int(imo.quantiteto))
                                        imo.dispono = int(imo.dispono) - int(empa["quantite"])
                                        imo.statuse = "nondisp"
                                        print("pas terlin")
                                    db.session.commit()
                            continue


                        if int(adm.quantit) == 0 :
                            adm.stat = "faux"
                            
                            db.session.commit()
                            continue

                        adm.llet = int(adm.llet) - int(empa["quantite"])
                        adm.quantit = int(adm.quantit) - int(empa["quantite"])
                        db.session.commit()




                        monkzu = Panieruser.query.all()
                        for imo in monkzu :
                            if int(imo.produite) == int(empa["idpro"]) :
                                sfymp = int(imo.dispono) - int(empa["quantite"])
                                if sfymp >= int(imo.quantiteto)   :
                                    imo.dispono = int(imo.dispono) - int(empa["quantite"])
                                    imo.statuse = "dispobine"
                                    print(sfymp , ">=" , int(imo.quantiteto))
                                else : 
                                    print(sfymp , "<" , int(imo.quantiteto))
                                    imo.dispono = int(imo.dispono) - int(empa["quantite"])
                                    imo.statuse = "nondisp"
                                db.session.commit()
                        
                        continue

                    if int(adm.llet) == 0 :
                        continue


            if empa["categorie"] == "chaussure" :
                print(empa["categorie"])
                taille = empa["taille"]
                
                adm = Ajouter.query.get(int(empa["idpro"]))


                if taille == "38 ° " :
                    if int(adm.tranwitelet) > 0 :
                        print("int(adm.tranwitelet)", int(adm.tranwitelet) , ">" , 0)

                        if int(adm.quantit) == int(empa["quantite"]) :

                            adm.stat = "faux"
                            adm.tranwitelet = int(adm.tranwitelet) - int(empa["quantite"])
                            adm.quantit = int(adm.quantit) - int(empa["quantite"])
                            db.session.commit()

                            monkzu = Panieruser.query.all()
                            print("on a recu")
                            for imo in monkzu :
                                if int(imo.produite) == int(empa["idpro"]) :
                                    sfymp = int(imo.dispono) - int(empa["quantite"])
                                    if sfymp >= int(imo.quantiteto)   :
                                        imo.dispono = int(imo.dispono) - int(empa["quantite"])
                                        imo.statuse = "dispobine"
                                        print(sfymp , ">=" , int(imo.quantiteto))
                                        print("terlin")
                                    else : 
                                        print(sfymp , "<" , int(imo.quantiteto))
                                        imo.dispono = int(imo.dispono) - int(empa["quantite"])
                                        imo.statuse = "nondisp"
                                        print("pas terlin")
                                    db.session.commit()
                            continue


                        if int(adm.quantit) == 0 :
                            adm.stat = "faux"
                            
                            db.session.commit()
                            continue

                        adm.tranwitelet = int(adm.tranwitelet) - int(empa["quantite"])
                        adm.quantit = int(adm.quantit) - int(empa["quantite"])
                        db.session.commit()




                        monkzu = Panieruser.query.all()
                        for imo in monkzu :
                            if int(imo.produite) == int(empa["idpro"]) :
                                sfymp = int(imo.dispono) - int(empa["quantite"])
                                if sfymp >= int(imo.quantiteto)   :
                                    imo.dispono = int(imo.dispono) - int(empa["quantite"])
                                    imo.statuse = "dispobine"
                                    print(sfymp , ">=" , int(imo.quantiteto))
                                else : 
                                    print(sfymp , "<" , int(imo.quantiteto))
                                    imo.dispono = int(imo.dispono) - int(empa["quantite"])
                                    imo.statuse = "nondisp"
                                db.session.commit()
                        
                        continue

                    if int(adm.tranwitelet) == 0 :
                        continue

              

                if taille == "39 ° " :
                    if int(adm.tranneuflet) > 0 :

                        print("int(adm.tranneuflet)", int(adm.tranneuflet) , ">" , 0)

                        if int(adm.quantit) == int(empa["quantite"]) :

                            adm.stat = "faux"
                            adm.tranneuflet = int(adm.tranneuflet) - int(empa["quantite"])
                            adm.quantit = int(adm.quantit) - int(empa["quantite"])
                            db.session.commit()

                            monkzu = Panieruser.query.all()
                            print("on a recu")
                            for imo in monkzu :
                                if int(imo.produite) == int(empa["idpro"]) :
                                    sfymp = int(imo.dispono) - int(empa["quantite"])
                                    if sfymp >= int(imo.quantiteto)   :
                                        imo.dispono = int(imo.dispono) - int(empa["quantite"])
                                        imo.statuse = "dispobine"
                                        print(sfymp , ">=" , int(imo.quantiteto))
                                        print("terlin")
                                    else : 
                                        print(sfymp , "<" , int(imo.quantiteto))
                                        imo.dispono = int(imo.dispono) - int(empa["quantite"])
                                        imo.statuse = "nondisp"
                                        print("pas terlin")
                                    db.session.commit()
                            continue


                        if int(adm.quantit) == 0 :
                            adm.stat = "faux"
                            
                            db.session.commit()
                            continue

                        adm.tranneuflet = int(adm.tranneuflet) - int(empa["quantite"])
                        adm.quantit = int(adm.quantit) - int(empa["quantite"])
                        db.session.commit()






                        monkzu = Panieruser.query.all()
                        for imo in monkzu :
                            if int(imo.produite) == int(empa["idpro"]) :
                                sfymp = int(imo.dispono) - int(empa["quantite"])
                                if sfymp >= int(imo.quantiteto)   :
                                    imo.dispono = int(imo.dispono) - int(empa["quantite"])
                                    imo.statuse = "dispobine"
                                    print(sfymp , ">=" , int(imo.quantiteto))
                                else : 
                                    print(sfymp , "<" , int(imo.quantiteto))
                                    imo.dispono = int(imo.dispono) - int(empa["quantite"])
                                    imo.statuse = "nondisp"
                                db.session.commit()
                        
                        continue

                    if int(adm.tranneuflet) == 0 :
                        continue

              

                if taille == "40 ° " :
                    if int(adm.karentelet) > 0 :
                        print("int(adm.karentelet)", int(adm.karentelet) , ">" , 0)

                        if int(adm.quantit) == int(empa["quantite"]) :

                            adm.stat = "faux"
                            adm.karentelet = int(adm.karentelet) - int(empa["quantite"])
                            adm.quantit = int(adm.quantit) - int(empa["quantite"])
                            db.session.commit()

                            monkzu = Panieruser.query.all()
                            print("on a recu")
                            for imo in monkzu :
                                if int(imo.produite) == int(empa["idpro"]) :
                                    sfymp = int(imo.dispono) - int(empa["quantite"])
                                    if sfymp >= int(imo.quantiteto)   :
                                        imo.dispono = int(imo.dispono) - int(empa["quantite"])
                                        imo.statuse = "dispobine"
                                        print(sfymp , ">=" , int(imo.quantiteto))
                                        print("terlin")
                                    else : 
                                        print(sfymp , "<" , int(imo.quantiteto))
                                        imo.dispono = int(imo.dispono) - int(empa["quantite"])
                                        imo.statuse = "nondisp"
                                        print("pas terlin")
                                    db.session.commit()
                            continue


                        if int(adm.quantit) == 0 :
                            adm.stat = "faux"
                            
                            db.session.commit()
                            continue

                        adm.karentelet = int(adm.karentelet) - int(empa["quantite"])
                        adm.quantit = int(adm.quantit) - int(empa["quantite"])
                        db.session.commit()




                        monkzu = Panieruser.query.all()
                        for imo in monkzu :
                            if int(imo.produite) == int(empa["idpro"]) :
                                sfymp = int(imo.dispono) - int(empa["quantite"])
                                if sfymp >= int(imo.quantiteto)   :
                                    imo.dispono = int(imo.dispono) - int(empa["quantite"])
                                    imo.statuse = "dispobine"
                                    print(sfymp , ">=" , int(imo.quantiteto))
                                else : 
                                    print(sfymp , "<" , int(imo.quantiteto))
                                    imo.dispono = int(imo.dispono) - int(empa["quantite"])
                                    imo.statuse = "nondisp"
                                db.session.commit()
                        
                        continue

                    if int(adm.karentelet) == 0 :
                        continue

              

                if taille == "41 ° " :
                    if int(adm.tranwiteunlet) > 0 :
                        print("int(adm.tranwiteunlet)", int(adm.tranwiteunlet) , ">" , 0)

                        if int(adm.quantit) == int(empa["quantite"]) :

                            adm.stat = "faux"
                            adm.tranwiteunlet = int(adm.tranwiteunlet) - int(empa["quantite"])
                            adm.quantit = int(adm.quantit) - int(empa["quantite"])
                            db.session.commit()

                            monkzu = Panieruser.query.all()
                            print("on a recu")
                            for imo in monkzu :
                                if int(imo.produite) == int(empa["idpro"]) :
                                    sfymp = int(imo.dispono) - int(empa["quantite"])
                                    if sfymp >= int(imo.quantiteto)   :
                                        imo.dispono = int(imo.dispono) - int(empa["quantite"])
                                        imo.statuse = "dispobine"
                                        print(sfymp , ">=" , int(imo.quantiteto))
                                        print("terlin")
                                    else : 
                                        print(sfymp , "<" , int(imo.quantiteto))
                                        imo.dispono = int(imo.dispono) - int(empa["quantite"])
                                        imo.statuse = "nondisp"
                                        print("pas terlin")
                                    db.session.commit()
                            continue


                        if int(adm.quantit) == 0 :
                            adm.stat = "faux"
                            
                            db.session.commit()
                            continue

                        adm.tranwiteunlet = int(adm.tranwiteunlet) - int(empa["quantite"])
                        adm.quantit = int(adm.quantit) - int(empa["quantite"])
                        db.session.commit()




                        monkzu = Panieruser.query.all()
                        for imo in monkzu :
                            if int(imo.produite) == int(empa["idpro"]) :
                                sfymp = int(imo.dispono) - int(empa["quantite"])
                                if sfymp >= int(imo.quantiteto)   :
                                    imo.dispono = int(imo.dispono) - int(empa["quantite"])
                                    imo.statuse = "dispobine"
                                    print(sfymp , ">=" , int(imo.quantiteto))
                                else : 
                                    print(sfymp , "<" , int(imo.quantiteto))
                                    imo.dispono = int(imo.dispono) - int(empa["quantite"])
                                    imo.statuse = "nondisp"
                                db.session.commit()
                        
                        continue

                    if int(adm.tranwiteunlet) == 0 :
                        continue

              

                if taille == "42 ° " :
                    if int(adm.tranwitedeuxlet) > 0 :
                        print("int(adm.tranwitedeuxlet)", int(adm.tranwitedeuxlet) , ">" , 0)

                        if int(adm.quantit) == int(empa["quantite"]) :

                            adm.stat = "faux"
                            adm.tranwitedeuxlet = int(adm.tranwitedeuxlet) - int(empa["quantite"])
                            adm.quantit = int(adm.quantit) - int(empa["quantite"])
                            db.session.commit()

                            monkzu = Panieruser.query.all()
                            print("on a recu")
                            for imo in monkzu :
                                if int(imo.produite) == int(empa["idpro"]) :
                                    sfymp = int(imo.dispono) - int(empa["quantite"])
                                    if sfymp >= int(imo.quantiteto)   :
                                        imo.dispono = int(imo.dispono) - int(empa["quantite"])
                                        imo.statuse = "dispobine"
                                        print(sfymp , ">=" , int(imo.quantiteto))
                                        print("terlin")
                                    else : 
                                        print(sfymp , "<" , int(imo.quantiteto))
                                        imo.dispono = int(imo.dispono) - int(empa["quantite"])
                                        imo.statuse = "nondisp"
                                        print("pas terlin")
                                    db.session.commit()
                            continue


                        if int(adm.quantit) == 0 :
                            adm.stat = "faux"
                            
                            db.session.commit()
                            continue

                        adm.tranwitedeuxlet = int(adm.tranwitedeuxlet) - int(empa["quantite"])
                        adm.quantit = int(adm.quantit) - int(empa["quantite"])
                        db.session.commit()




                        monkzu = Panieruser.query.all()
                        for imo in monkzu :
                            if int(imo.produite) == int(empa["idpro"]) :
                                sfymp = int(imo.dispono) - int(empa["quantite"])
                                if sfymp >= int(imo.quantiteto)   :
                                    imo.dispono = int(imo.dispono) - int(empa["quantite"])
                                    imo.statuse = "dispobine"
                                    print(sfymp , ">=" , int(imo.quantiteto))
                                else : 
                                    print(sfymp , "<" , int(imo.quantiteto))
                                    imo.dispono = int(imo.dispono) - int(empa["quantite"])
                                    imo.statuse = "nondisp"
                                db.session.commit()
                        
                        continue

                    if int(adm.tranwitedeuxlet) == 0 :
                        continue

              

                if taille == "43 ° " :
                    if int(adm.tranwitroislet) > 0 :
                        print("int(adm.tranwitroislet)", int(adm.tranwitroislet) , ">" , 0)

                        if int(adm.quantit) == int(empa["quantite"]) :

                            adm.stat = "faux"
                            adm.tranwitroislet = int(adm.tranwitroislet) - int(empa["quantite"])
                            adm.quantit = int(adm.quantit) - int(empa["quantite"])
                            db.session.commit()

                            monkzu = Panieruser.query.all()
                            print("on a recu")
                            for imo in monkzu :
                                if int(imo.produite) == int(empa["idpro"]) :
                                    sfymp = int(imo.dispono) - int(empa["quantite"])
                                    if sfymp >= int(imo.quantiteto)   :
                                        imo.dispono = int(imo.dispono) - int(empa["quantite"])
                                        imo.statuse = "dispobine"
                                        print(sfymp , ">=" , int(imo.quantiteto))
                                        print("terlin")
                                    else : 
                                        print(sfymp , "<" , int(imo.quantiteto))
                                        imo.dispono = int(imo.dispono) - int(empa["quantite"])
                                        imo.statuse = "nondisp"
                                        print("pas terlin")
                                    db.session.commit()
                            continue


                        if int(adm.quantit) == 0 :
                            adm.stat = "faux"
                            
                            db.session.commit()
                            continue

                        adm.tranwitroislet = int(adm.tranwitroislet) - int(empa["quantite"])
                        adm.quantit = int(adm.quantit) - int(empa["quantite"])
                        db.session.commit()




                        monkzu = Panieruser.query.all()
                        for imo in monkzu :
                            if int(imo.produite) == int(empa["idpro"]) :
                                sfymp = int(imo.dispono) - int(empa["quantite"])
                                if sfymp >= int(imo.quantiteto)   :
                                    imo.dispono = int(imo.dispono) - int(empa["quantite"])
                                    imo.statuse = "dispobine"
                                    print(sfymp , ">=" , int(imo.quantiteto))
                                else : 
                                    print(sfymp , "<" , int(imo.quantiteto))
                                    imo.dispono = int(imo.dispono) - int(empa["quantite"])
                                    imo.statuse = "nondisp"
                                db.session.commit()
                        
                        continue

                    if int(adm.tranwitroislet) == 0 :
                        continue

              

                if taille == "44 ° " :
                    if int(adm.tranwitekatelet) > 0 :
                        print("int(adm.tranwitekatelet)", int(adm.tranwitekatelet) , ">" , 0)

                        if int(adm.quantit) == int(empa["quantite"]) :

                            adm.stat = "faux"
                            adm.tranwitekatelet = int(adm.tranwitekatelet) - int(empa["quantite"])
                            adm.quantit = int(adm.quantit) - int(empa["quantite"])
                            db.session.commit()

                            monkzu = Panieruser.query.all()
                            print("on a recu")
                            for imo in monkzu :
                                if int(imo.produite) == int(empa["idpro"]) :
                                    sfymp = int(imo.dispono) - int(empa["quantite"])
                                    if sfymp >= int(imo.quantiteto)   :
                                        imo.dispono = int(imo.dispono) - int(empa["quantite"])
                                        imo.statuse = "dispobine"
                                        print(sfymp , ">=" , int(imo.quantiteto))
                                        print("terlin")
                                    else : 
                                        print(sfymp , "<" , int(imo.quantiteto))
                                        imo.dispono = int(imo.dispono) - int(empa["quantite"])
                                        imo.statuse = "nondisp"
                                        print("pas terlin")
                                    db.session.commit()
                            continue


                        if int(adm.quantit) == 0 :
                            adm.stat = "faux"
                            
                            db.session.commit()
                            continue

                        adm.tranwitekatelet = int(adm.tranwitekatelet) - int(empa["quantite"])
                        adm.quantit = int(adm.quantit) - int(empa["quantite"])
                        db.session.commit()




                        monkzu = Panieruser.query.all()
                        for imo in monkzu :
                            if int(imo.produite) == int(empa["idpro"]) :
                                sfymp = int(imo.dispono) - int(empa["quantite"])
                                if sfymp >= int(imo.quantiteto)   :
                                    imo.dispono = int(imo.dispono) - int(empa["quantite"])
                                    imo.statuse = "dispobine"
                                    print(sfymp , ">=" , int(imo.quantiteto))
                                else : 
                                    print(sfymp , "<" , int(imo.quantiteto))
                                    imo.dispono = int(imo.dispono) - int(empa["quantite"])
                                    imo.statuse = "nondisp"
                                db.session.commit()
                        
                        continue

                    if int(adm.tranwitekatelet) == 0 :
                        continue

              
                   
                   

            else :
                
                if empa["categorie"] == "Montre" :
                    taille = empa["taille"] 
                
                    adm = Ajouter.query.get(int(empa["idpro"]))
                    if int(adm.quantit) > 0 :
                        print("int(adm.quantit)", int(adm.quantit) , ">" , 0)

                        if int(adm.quantit) == int(empa["quantite"]) :

                            adm.stat = "faux"
                            
                            adm.quantit = int(adm.quantit) - int(empa["quantite"])
                            db.session.commit()

                            monkzu = Panieruser.query.all()
                            print("on a recu")
                            for imo in monkzu :
                                if int(imo.produite) == int(empa["idpro"]) :
                                    sfymp = int(imo.dispono) - int(empa["quantite"])
                                    if sfymp >= int(imo.quantiteto)   :
                                        imo.dispono = int(imo.dispono) - int(empa["quantite"])
                                        imo.statuse = "dispobine"
                                        print(sfymp , ">=" , int(imo.quantiteto))
                                        print("terlin")
                                    else : 
                                        print(sfymp , "<" , int(imo.quantiteto))
                                        imo.dispono = int(imo.dispono) - int(empa["quantite"])
                                        imo.statuse = "nondisp"
                                        print("pas terlin")
                                    db.session.commit()
                            continue


                        if int(adm.quantit) == 0 :
                            adm.stat = "faux"
                            
                            db.session.commit()
                            continue

                        
                        adm.quantit = int(adm.quantit) - int(empa["quantite"])
                        db.session.commit()




                        monkzu = Panieruser.query.all()
                        for imo in monkzu :
                            if int(imo.produite) == int(empa["idpro"]) :
                                sfymp = int(imo.dispono) - int(empa["quantite"])
                                if sfymp >= int(imo.quantiteto)   :
                                    imo.dispono = int(imo.dispono) - int(empa["quantite"])
                                    imo.statuse = "dispobine"
                                    print(sfymp , ">=" , int(imo.quantiteto))
                                else : 
                                    print(sfymp , "<" , int(imo.quantiteto))
                                    imo.dispono = int(imo.dispono) - int(empa["quantite"])
                                    imo.statuse = "nondisp"
                                db.session.commit()
                        
                        continue

                    if int(adm.quantit) == 0 :
                        continue
                            
                        
            
            

      
            
            
        
        return redirect('/mescommandes')

    return redirect('/mescommandes')


@app.route('/commandeznow', methods=["POST"])
def commandeznow():
    if 'utilisateur_id' in session:
        useru = Profil.query.get(session['utilisateur_id'])
    else:
        return redirect('/pre/monpanier')
    
    
    
    useruo = Profil.query.get(useru.id)
    tableaus = Panieruser.query.all()
    gdhsuud = []
    macommande = []
    
    for i in tableaus : 
        
        if int(i.identifiant) == useruo.id :
            print('prevdg', i.identifiant , 'prevdg' , useruo.id)
            hdhdud = Ajouter.query.get(i.produite)
            if hdhdud.categorie == 'VetementFemme' :
                macommande.append({"lien":f"Le lien : https://hington-shop.onrender.com/info/{i.produite} ","Categorie":hdhdud.categorie,"Nom":hdhdud.nom,"Reduction":hdhdud.porce,"Prixbarré":hdhdud.prix,"Prix final":hdhdud.porceprix,"Quantité":i.quantiteto,"taille":i.tailed})
            if hdhdud.categorie == 'Montre' :
                macommande.append({"lien":f"Le lien : https://hington-shop.onrender.com/montres/{i.produite} ","Categorie":hdhdud.categorie,"Nom":hdhdud.nom,"Reduction":hdhdud.porce,"Prixbarré":hdhdud.prix,"Prix final":hdhdud.porceprix,"Quantité":i.quantiteto})
            if hdhdud.categorie == 'chaussure' :
                macommande.append({"lien":f"Le lien : https://hington-shop.onrender.com/sacs/{i.produite} ","Categorie":hdhdud.categorie,"Nom":hdhdud.nom,"Reduction":hdhdud.porce,"Prixbarré":hdhdud.prix,"Prix final":hdhdud.porceprix,"Quantité":i.quantiteto,"taille":i.tailed})

    somme = 0
    
    for i in macommande :
        print(int(i["Prix final"]))
        print(i["Prix final"])
        somme += int(i["Prix final"])
    
    macommande.append({"Somme totale" : somme})


    ms = macommande
    tableauser = Adminit.query.all()
    pani = Panieruser(nom="nom",numero = "numero",tags=ms)
            
    db.session.add(tableauser)
    db.session.commit()
    
    return redirect(f"https://api.whatsapp.com/send/?phone=2250101678809&text={ms}&type=phone_number&app_absent=0")
  
[{'lien': 'Le lien : https://hington-shop.onrender.com/info/9 ', 'Categorie': 'VetementFemme', 'Nom': 'robe simple', 'Reduction': '48', 'Prixbarré': '2500', 'Prix final': '1300', 'Quantité': '2', 'taille': 's'}, {'lien': 'Le lien : https://hington-shop.onrender.com/info/9 ', 'Categorie': 'VetementFemme', 'Nom': 'robe simple', 'Reduction': '48', 'Prixbarré': '2500', 'Prix final': '1300', 'Quantité': '2', 'taille': 'xxl'}, {'Somme totale': 2600}]




@app.route('/Supprimer/<int:id>')
def Supprimer(id):
    if 'utilisateur_id' in session:
        useru = Profil.query.get(session['utilisateur_id'])
    # else:
    #     return redirect(f'/pre/Supprimer/{id}')
    
    useruo = Profil.query.get(useru.id)
    tableaus = Panieruser.query.all()
    
    ior =0
    for i in tableaus : 
        ior+=1
        print('produit,',ior)
        if int(i.identifiant) == useruo.id :
            user = Panieruser.query.filter_by(produite = id, identifiant = useruo.id).first()
            zerre = Panieruser.query.get(id)
            db.session.delete(zerre)
            db.session.commit()
            return redirect('/monpanier')
            print('produit supprimer')

    print('NON supprimer')  
    return redirect('/monpanier')


from urllib.parse import quote
@app.route('/ssm', methods=["POST"])
def ssm():
    if 'utilisateur_id' in session:
        useru = Profil.query.get(session['utilisateur_id'])
    # else :
    #     return redirect('/pre/')
    nom = request.form.get("nom")
    livraison = request.form.get("livraison")
    image = request.form.get("image")
    noumeme = request.form.get("noumeme")
    prix = request.form.get("prix")
    quantite = request.form.get("quantiteplos")
    hfshggf = Ajouter.query.get(int(noumeme))
    print("le voivi gegeghhdhjhdjhdjh",noumeme)
    
  

        
    

        

    # eudeyyt = Profil.query.all()
    if hfshggf.categorie == "Montre":
        print("les identifiants articles ",image,noumeme,prix,quantite)
        print("les identifiants  ",noumeme,useru.id)
        
        # derst = Panieruser.query.filter_by(identifiant=useru.id,produite=int(noumeme))
        derst = Panieruser.query.all()
        for i in derst :
            
            if int(i.produite) == int(noumeme) and int(i.identifiant)==int(useru.id) :
                print("les articles ",i.produite,i.identifiant)
                dhher = Panieruser.query.get(i.id)

                if (int(dhher.quantiteto) + int(quantite) ) <= int(hfshggf.quantit) :
                    dhher.quantiteto = int(dhher.quantiteto) + int(quantite)
                    db.session.commit()
                    
                return redirect("/monpanier")

        pani = Panieruser(image=image,tailed = "",identifiant=useru.id,produite=noumeme,prixtottal=prix,quantiteto=quantite,xs="",xsn="",s="",sn="",l="",ln="",m="",mn="",xl="",xln="",xxl="",xxln="",tranwite="",tranwiten="",tranneuf="",tranneufn="",karente="",karenten="",tranwiteun="",tranwiteunn="",tranwitedeux="",tranwitedeuxn="",tranwitrois="",tranwitroisn="",tranwitekate="",tranwitekaten="", prixdepouce = hfshggf.prix ,nomprodui = hfshggf.nom,descrprosui = hfshggf.description,pourcentage = hfshggf.porce,categorie = hfshggf.categorie ,dispono=int(hfshggf.quantit),statuse="dispobine")
            
        db.session.add(pani)
        db.session.commit()
        return redirect("/monpanier")


    xs = request.form.get("xs","")
    xsnum = request.form.get("xsnum","0")
    if int(xsnum) > 0 :
        xs = "xs"
        cpo=0
        derst = Panieruser.query.all()
        for i in derst :
             
            if int(i.produite) == int(noumeme) and int(i.identifiant)==int(useru.id) and str(xs) == str(i.tailed):
                print("les articles ",i.produite,i.identifiant)
                cpo+=1
                dhher = Panieruser.query.get(i.id)

                if (int(dhher.quantiteto) + int(quantite) ) <=int(hfshggf.xslet) :
                    dhher.quantiteto = int(dhher.quantiteto) + int(quantite)
                    db.session.commit()
        if cpo == 0 :
            xs = "xs"
            
            pani = Panieruser(image=image,tailed =xs,identifiant=useru.id,produite=noumeme,prixtottal=prix,quantiteto=xsnum,xs=xs,xsn=xsnum,s="",sn="",l="",ln="",m="",mn="",xl="",xln="",xxl="",xxln="",tranwite="",tranwiten="",tranneuf="",tranneufn="",karente="",karenten="",tranwiteun="",tranwiteunn="",tranwitedeux="",tranwitedeuxn="",tranwitrois="",tranwitroisn="",tranwitekate="",tranwitekaten="",prixdepouce = hfshggf.prix ,nomprodui = hfshggf.nom,descrprosui = hfshggf.description,pourcentage = hfshggf.porce,categorie = hfshggf.categorie,dispono=int(hfshggf.xslet),statuse="dispobine")
            
            db.session.add(pani)
            db.session.commit()


        
    if int(xsnum) == 0 :
        xs = ""
        xsnum = ""


    s = request.form.get("s","")
    snum = request.form.get("snum","0")
    if int(snum) > 0 :
        s = "s"
        cpo=0
        derst = Panieruser.query.all()
        for i in derst :
            
            if int(i.produite) == int(noumeme) and int(i.identifiant)==int(useru.id) and  str(s) ==  str(i.tailed):
                print("les articles ",i.produite,i.identifiant)
                cpo+=1
                dhher = Panieruser.query.get(i.id)

                if (int(dhher.quantiteto) + int(quantite) ) <= int(hfshggf.slet) :
                    dhher.quantiteto = int(dhher.quantiteto) + int(quantite)
                    db.session.commit()

        
        if cpo == 0 :
            s = "s"
            
            pani = Panieruser(image=image,tailed =s,identifiant=useru.id,produite=noumeme,prixtottal=prix,quantiteto=snum,xs="",xsn="",s=s,sn=snum,l="",ln="",m="",mn="",xl="",xln="",xxl="",xxln="",tranwite="",tranwiten="",tranneuf="",tranneufn="",karente="",karenten="",tranwiteun="",tranwiteunn="",tranwitedeux="",tranwitedeuxn="",tranwitrois="",tranwitroisn="",tranwitekate="",tranwitekaten="",prixdepouce = hfshggf.prix ,nomprodui = hfshggf.nom,descrprosui = hfshggf.description,pourcentage = hfshggf.porce,categorie = hfshggf.categorie,dispono=int(hfshggf.slet),statuse="dispobine")
            
            db.session.add(pani)
            db.session.commit()
    if int(snum) == 0 :
        s = ""
        snum = ""
    m = request.form.get("m","")
    mnum = request.form.get("mnum","0")
    if int(mnum) > 0 :
        m = "m"
        cpo=0
        derst = Panieruser.query.all()
        for i in derst :
            
            if int(i.produite) == int(noumeme) and int(i.identifiant)==int(useru.id) and str(m) ==  str(i.tailed):
                print("les articles ",i.produite,i.identifiant)
                cpo+=1
                dhher = Panieruser.query.get(i.id)

                if (int(dhher.quantiteto) + int(quantite) ) <=int(hfshggf.mlet) :
                    dhher.quantiteto = int(dhher.quantiteto) + int(quantite)
                    db.session.commit()
        if cpo == 0 :
            m = "m"
            
            pani = Panieruser(image=image,tailed =m,identifiant=useru.id,produite=noumeme,prixtottal=prix,quantiteto=mnum,xs="",xsn="",s="",sn="",l="",ln="",m=m,mn=mnum,xl="",xln="",xxl="",xxln="",tranwite="",tranwiten="",tranneuf="",tranneufn="",karente="",karenten="",tranwiteun="",tranwiteunn="",tranwitedeux="",tranwitedeuxn="",tranwitrois="",tranwitroisn="",tranwitekate="",tranwitekaten="",prixdepouce = hfshggf.prix ,nomprodui = hfshggf.nom,descrprosui = hfshggf.description,pourcentage = hfshggf.porce,categorie = hfshggf.categorie,dispono=int(hfshggf.mlet),statuse="dispobine")
            
            db.session.add(pani)
            db.session.commit()
    if int(mnum) == 0 :
        m = ""
        mnum = ""
    l = request.form.get("l","")
    lnum = request.form.get("lnum","0")
    if int(lnum) > 0 :
        l = "l"
        cpo=0
        derst = Panieruser.query.all()
        for i in derst :
            
            if int(i.produite) == int(noumeme) and int(i.identifiant)==int(useru.id) and str(l) ==  str(i.tailed):
                print("les articles ",i.produite,i.identifiant)
                cpo+=1
                dhher = Panieruser.query.get(i.id)

                if (int(dhher.quantiteto) + int(quantite) ) <=int(hfshggf.llet) :
                    dhher.quantiteto = int(dhher.quantiteto) + int(quantite)
                    db.session.commit()
        if cpo == 0 :
            l = "l"
            
            pani = Panieruser(image=image,tailed =l,identifiant=useru.id,produite=noumeme,prixtottal=prix,quantiteto=lnum,xs="",xsn="",s="",sn="",l=l,ln=lnum,m="",mn="",xl="",xln="",xxl="",xxln="",tranwite="",tranwiten="",tranneuf="",tranneufn="",karente="",karenten="",tranwiteun="",tranwiteunn="",tranwitedeux="",tranwitedeuxn="",tranwitrois="",tranwitroisn="",tranwitekate="",tranwitekaten="",prixdepouce = hfshggf.prix ,nomprodui = hfshggf.nom,descrprosui = hfshggf.description,pourcentage = hfshggf.porce,categorie = hfshggf.categorie,dispono=int(hfshggf.llet),statuse="dispobine")
            
            db.session.add(pani)
            db.session.commit()
    if int(lnum) == 0 :
        l = ""
        lnum = ""
    xl = request.form.get("xl","")
    xlnum = request.form.get("xlnum","0")
    if int(xlnum) > 0 :
        cpo=0
        xl = "xl"
        derst = Panieruser.query.all()
        for i in derst :
            
            if int(i.produite) == int(noumeme) and int(i.identifiant)==int(useru.id) and str(xl) ==  str(i.tailed):
                print("les articles ",i.produite,i.identifiant)
                cpo+=1
                dhher = Panieruser.query.get(i.id)

                if (int(dhher.quantiteto) + int(quantite) ) <=int(hfshggf.xllet) :
                    dhher.quantiteto = int(dhher.quantiteto) + int(quantite)
                    db.session.commit()
        if cpo == 0 :
            xl = "xl"
            
            pani = Panieruser(image=image, tailed = xl,identifiant=useru.id,produite=noumeme,prixtottal=prix,quantiteto=xlnum,xs="",xsn="",s="",sn="",l="",ln="",m="",mn="",xl=xl,xln=xlnum,xxl="",xxln="",tranwite="",tranwiten="",tranneuf="",tranneufn="",karente="",karenten="",tranwiteun="",tranwiteunn="",tranwitedeux="",tranwitedeuxn="",tranwitrois="",tranwitroisn="",tranwitekate="",tranwitekaten="",prixdepouce = hfshggf.prix ,nomprodui = hfshggf.nom,descrprosui = hfshggf.description,pourcentage = hfshggf.porce,categorie = hfshggf.categorie,dispono=int(hfshggf.xllet),statuse="dispobine")
            
            db.session.add(pani)
            db.session.commit()
    if int(xlnum) == 0 :
        xl = ""
        xlnum = ""
    xxlnum = request.form.get("xxlnum","0")
    xxl = request.form.get("xxl","")
    if int(xxlnum) > 0 :
        xxl = "xxl"
        cpo=0
        derst = Panieruser.query.all()
        for i in derst :
            print(int(i.produite) ,"==", int(noumeme) , int(i.identifiant) ,"==",int(useru.id) , str(xxl)  ,"==",  str(i.tailed))
            if int(i.produite) == int(noumeme) and int(i.identifiant)==int(useru.id) and str(xxl) ==  str(i.tailed):
                print("les articles ",i.produite,i.identifiant)
                cpo+=1
                dhher = Panieruser.query.get(i.id)

                if (int(dhher.quantiteto) + int(quantite) ) <=int(hfshggf.xxllet) :
                    dhher.quantiteto = int(dhher.quantiteto) + int(quantite)
                    db.session.commit()
        if cpo == 0 :
            xxl = "xxl"
            
            pani = Panieruser(image=image, tailed = xxl,identifiant=useru.id,produite=noumeme,prixtottal=prix,quantiteto=xxlnum,xs="",xsn="",s="",sn="",l="",ln="",m="",mn="",xl="",xln="",xxl=xxl,xxln=xxlnum,tranwite="",tranwiten="",tranneuf="",tranneufn="",karente="",karenten="",tranwiteun="",tranwiteunn="",tranwitedeux="",tranwitedeuxn="",tranwitrois="",tranwitroisn="",tranwitekate="",tranwitekaten="",prixdepouce = hfshggf.prix ,nomprodui = hfshggf.nom,descrprosui = hfshggf.description,pourcentage = hfshggf.porce,categorie = hfshggf.categorie,dispono=int(hfshggf.xxllet),statuse="dispobine")
            
            db.session.add(pani)
            db.session.commit()
    if int(xxlnum) == 0 :
        xxl = ""
        xxlnum = ""

    
    # rouge = request.form.get("rouge","")
    # blanc = request.form.get("blanc","")
    # noir = request.form.get("noir","")
    # jaune = request.form.get("jaune","")
    # vert = request.form.get("vert","")
    # orange = request.form.get("orange","")
    # bleu = request.form.get("bleu","")
    # rose = request.form.get("rose","")
    # marron = request.form.get("marron","")
    # violet = request.form.get("violet","")
    # gris = request.form.get("gris","")
    tranwite = request.form.get("tranwite","")
    tranwitenum = request.form.get("tranwitenum","0")
    if int(tranwitenum) > 0 :
        tranwite = "38 ° "
        cpo=0
        derst = Panieruser.query.all()
        for i in derst :
            print(int(i.produite) ,"==", int(noumeme) , int(i.identifiant) ,"==",int(useru.id) , str(tranwite)  ,"==",  str(i.tailed))
            if int(i.produite) == int(noumeme) and int(i.identifiant)==int(useru.id) and str(tranwite) ==  str(i.tailed):
                print("les articles ",i.produite,i.identifiant)
                cpo+=1
                dhher = Panieruser.query.get(i.id)

                if (int(dhher.quantiteto) + int(quantite) ) <=int(hfshggf.tranwitelet) :
                    dhher.quantiteto = int(dhher.quantiteto) + int(quantite)
                    db.session.commit()
        if cpo == 0 :
            tranwite = "38 ° "
            tranwitenum = tranwitenum
            
            pani = Panieruser(image=image,tailed = tranwite,identifiant=useru.id,produite=noumeme,prixtottal=prix,quantiteto=tranwitenum,xs="",xsn="",s="",sn="",l="",ln="",m="",mn="",xl="",xln="",xxl="",xxln="",tranwite=tranwite,tranwiten=tranwitenum,tranneuf="",tranneufn="",karente="",karenten="",tranwiteun="",tranwiteunn="",tranwitedeux="",tranwitedeuxn="",tranwitrois="",tranwitroisn="",tranwitekate="",tranwitekaten="",prixdepouce = hfshggf.prix ,nomprodui = hfshggf.nom,descrprosui = hfshggf.description,pourcentage = hfshggf.porce,categorie = hfshggf.categorie,dispono=int(hfshggf.tranwitelet),statuse="dispobine")
            
            db.session.add(pani)
            db.session.commit()
    if int(tranwitenum) == 0 :
        tranwite = ""
        tranwitenum = ""
    
    tranneuf = request.form.get("tranneuf","")
    tranneufnum = request.form.get("tranneufnum","0")
    if int(tranneufnum) > 0 :
        tranneuf = "39 ° "
        cpo=0
        derst = Panieruser.query.all()
        for i in derst :
            print(int(i.produite) ,"==", int(noumeme) , int(i.identifiant) ,"==",int(useru.id) , str(tranneuf)  ,"==",  str(i.tailed))
            if int(i.produite) == int(noumeme) and int(i.identifiant)==int(useru.id) and str(tranneuf) ==  str(i.tailed):
                print("les articles ",i.produite,i.identifiant)
                cpo+=1
                dhher = Panieruser.query.get(i.id)

                if (int(dhher.quantiteto) + int(quantite) ) <=int(hfshggf.tranneuflet) :
                    dhher.quantiteto = int(dhher.quantiteto) + int(quantite)
                    db.session.commit()
        if cpo == 0 :
            tranneuf = "39 ° "
            tranneufnum = tranneufnum
            
            pani = Panieruser(image=image,tailed = tranneuf,identifiant=useru.id,produite=noumeme,prixtottal=prix,quantiteto=tranneufnum,xs="",xsn="",s="",sn="",l="",ln="",m="",mn="",xl="",xln="",xxl="",xxln="",tranwite="",tranwiten="",tranneuf=tranneuf,tranneufn=tranneufnum,karente="",karenten="",tranwiteun="",tranwiteunn="",tranwitedeux="",tranwitedeuxn="",tranwitrois="",tranwitroisn="",tranwitekate="",tranwitekaten="",prixdepouce = hfshggf.prix ,nomprodui = hfshggf.nom,descrprosui = hfshggf.description,pourcentage = hfshggf.porce,categorie = hfshggf.categorie,dispono=int(hfshggf.tranneuflet),statuse="dispobine")
            
            db.session.add(pani)
            db.session.commit()
    if int(tranneufnum) == 0 :
        tranneuf = ""
        tranneufnum = ""
    karente = request.form.get("karente","")
    karentenum = request.form.get("karentenum","0")
    if int(karentenum) > 0 :
        karente = "40 ° "
        cpo=0
        derst = Panieruser.query.all()
        for i in derst :
            print(int(i.produite) ,"==", int(noumeme) , int(i.identifiant) ,"==",int(useru.id) , str(karente)  ,"==",  str(i.tailed))
            if int(i.produite) == int(noumeme) and int(i.identifiant)==int(useru.id) and str(karente) ==  str(i.tailed):
                print("les articles ",i.produite,i.identifiant)
                cpo+=1
                dhher = Panieruser.query.get(i.id)

                if (int(dhher.quantiteto) + int(quantite) ) <=int(hfshggf.karentelet) :
                    
                    dhher.quantiteto = int(dhher.quantiteto) + int(quantite)
                    db.session.commit()
        if cpo == 0 :
            karente = "40 ° "
            karentenum = karentenum
            
            pani = Panieruser(image=image,tailed = karente,identifiant=useru.id,produite=noumeme,prixtottal=prix,quantiteto=karentenum,xs="",xsn="",s="",sn="",l="",ln="",m="",mn="",xl="",xln="",xxl="",xxln="",tranwite="",tranwiten="",tranneuf="",tranneufn="",karente=karente,karenten=karentenum,tranwiteun="",tranwiteunn="",tranwitedeux="",tranwitedeuxn="",tranwitrois="",tranwitroisn="",tranwitekate="",tranwitekaten="",prixdepouce = hfshggf.prix ,nomprodui = hfshggf.nom,descrprosui = hfshggf.description,pourcentage = hfshggf.porce,categorie = hfshggf.categorie,dispono=int(hfshggf.karentelet),statuse="dispobine")
            
            db.session.add(pani)
            db.session.commit()
    if int(karentenum) == 0 :
        karente = ""
        karentenum = ""
    tranwiteun = request.form.get("tranwiteun","")
    tranwiteunnum = request.form.get("tranwiteunnum","0")
    if int(tranwiteunnum) > 0 :
        tranwiteun = "41 ° "
        cpo=0
        derst = Panieruser.query.all()
        for i in derst :
            print(int(i.produite) ,"==", int(noumeme) , int(i.identifiant) ,"==",int(useru.id) , str(tranwiteun)  ,"==",  str(i.tailed))
            if int(i.produite) == int(noumeme) and int(i.identifiant)==int(useru.id) and str(tranwiteun) ==  str(i.tailed):
                print("les articles ",i.produite,i.identifiant)
                cpo+=1
                dhher = Panieruser.query.get(i.id)

                if (int(dhher.quantiteto) + int(quantite) ) <=int(hfshggf.tranwiteunlet) :
                    dhher.quantiteto = int(dhher.quantiteto) + int(quantite)
                    db.session.commit()
        if cpo == 0 :
            tranwiteun = "41 ° "
            tranwiteunnum = tranwiteunnum
            
            pani = Panieruser(image=image,tailed =tranwiteun ,identifiant=useru.id,produite=noumeme,prixtottal=prix,quantiteto=tranwiteunnum,xs="",xsn="",s="",sn="",l="",ln="",m="",mn="",xl="",xln="",xxl="",xxln="",tranwite="",tranwiten="",tranneuf="",tranneufn="",karente="",karenten="",tranwiteun=tranwiteun,tranwiteunn=tranwiteunnum,tranwitedeux="",tranwitedeuxn="",tranwitrois="",tranwitroisn="",tranwitekate="",tranwitekaten="",prixdepouce = hfshggf.prix ,nomprodui = hfshggf.nom,descrprosui = hfshggf.description,pourcentage = hfshggf.porce,categorie = hfshggf.categorie,dispono=int(hfshggf.tranwiteunlet),statuse="dispobine")
            
            db.session.add(pani)
            db.session.commit()
    if int(tranwiteunnum) == 0 :
        tranwiteun = ""
        tranwiteunnum = ""
    tranwitedeux = request.form.get("tranwitedeux","")
    tranwitedeuxnum = request.form.get("tranwitedeuxnum","0")
    if int(tranwitedeuxnum) > 0 :
        tranwitedeux = "42 ° "
        cpo=0
        derst = Panieruser.query.all()
        for i in derst :
            print(int(i.produite) ,"==", int(noumeme) , int(i.identifiant) ,"==",int(useru.id) , str(tranwitedeux)  ,"==",  str(i.tailed))
            if int(i.produite) == int(noumeme) and int(i.identifiant)==int(useru.id) and str(tranwitedeux) ==  str(i.tailed):
                print("les articles ",i.produite,i.identifiant)
                cpo+=1
                dhher = Panieruser.query.get(i.id)

                if (int(dhher.quantiteto) + int(quantite) ) <=int(hfshggf.tranwitedeuxlet) :
                    dhher.quantiteto = int(dhher.quantiteto) + int(quantite)
                    db.session.commit()
        if cpo == 0 :
            tranwitedeux = "42 ° "
            tranwitedeuxnum = tranwitedeuxnum
            
            pani = Panieruser(image=image,tailed = tranwitedeux ,identifiant=useru.id,produite=noumeme,prixtottal=prix,quantiteto=tranwitedeuxnum,xs="",xsn="",s="",sn="",l="",ln="",m="",mn="",xl="",xln="",xxl="",xxln="",tranwite="",tranwiten="",tranneuf="",tranneufn="",karente="",karenten="",tranwiteun="",tranwiteunn="",tranwitedeux=tranwitedeux,tranwitedeuxn=tranwitedeuxnum,tranwitrois="",tranwitroisn="",tranwitekate="",tranwitekaten="",prixdepouce = hfshggf.prix ,nomprodui = hfshggf.nom,descrprosui = hfshggf.description,pourcentage = hfshggf.porce,categorie = hfshggf.categorie,dispono=int(hfshggf.tranwitedeuxlet),statuse="dispobine")
            
            db.session.add(pani)
            db.session.commit()
    if int(tranwitedeuxnum) == 0 :
        tranwitedeux = ""
        tranwitedeuxnum = ""
    tranwitrois = request.form.get("tranwitrois","")
    tranwitroisnum = request.form.get("tranwitroisnum","0")
    if int(tranwitroisnum) > 0 :
        tranwitrois = "43 ° "
        cpo=0
        derst = Panieruser.query.all()
        for i in derst :
            print(int(i.produite) ,"==", int(noumeme) , int(i.identifiant) ,"==",int(useru.id) , str(tranwitrois)  ,"==",  str(i.tailed))
            if int(i.produite) == int(noumeme) and int(i.identifiant)==int(useru.id) and str(tranwitrois) ==  str(i.tailed):
                print("les articles ",i.produite,i.identifiant)
                cpo+=1
                dhher = Panieruser.query.get(i.id)

                if (int(dhher.quantiteto) + int(quantite) ) <=int(hfshggf.tranwitroislet) :
                    dhher.quantiteto = int(dhher.quantiteto) + int(quantite)
                    db.session.commit()
        if cpo == 0 :
            tranwitrois = "43 ° "
            tranwitroisnum = tranwitroisnum
            
            pani = Panieruser(image=image,tailed = tranwitrois,identifiant=useru.id,produite=noumeme,prixtottal=prix,quantiteto=tranwitroisnum,xs="",xsn="",s="",sn="",l="",ln="",m="",mn="",xl="",xln="",xxl="",xxln="",tranwite="",tranwiten="",tranneuf="",tranneufn="",karente="",karenten="",tranwiteun="",tranwiteunn="",tranwitedeux="",tranwitedeuxn="",tranwitrois=tranwitrois,tranwitroisn=tranwitroisnum,tranwitekate="",tranwitekaten="",prixdepouce = hfshggf.prix ,nomprodui = hfshggf.nom,descrprosui = hfshggf.description,pourcentage = hfshggf.porce,categorie = hfshggf.categorie,dispono=int(hfshggf.tranwitroislet),statuse="dispobine")
            
            db.session.add(pani)
            db.session.commit()
    if int(tranwitroisnum) == 0 :
        tranwitrois = ""
        tranwitroisnum = ""
    tranwitekate = request.form.get("tranwitekate","")
    tranwitekatenum = request.form.get("tranwitekatenum","0")
    if int(tranwitekatenum) > 0 :
        tranwitekate = "44 ° "
        cpo=0
        derst = Panieruser.query.all()
        for i in derst :
            print(int(i.produite) ,"==", int(noumeme) , int(i.identifiant) ,"==",int(useru.id) , str(tranwitekate)  ,"==",  str(i.tailed))
            if int(i.produite) == int(noumeme) and int(i.identifiant)==int(useru.id) and str(tranwitekate) ==  str(i.tailed):
                print("les articles ",i.produite,i.identifiant)
                cpo+=1
                dhher = Panieruser.query.get(i.id)

                if (int(dhher.quantiteto) + int(quantite) ) <=int(hfshggf.tranwitekatelet) :
                    dhher.quantiteto = int(dhher.quantiteto) + int(quantite)
                    db.session.commit()
        if cpo == 0 :
            tranwitekate = "44 ° "
            tranwitekatenum = tranwitekatenum
            
            pani = Panieruser(image=image,tailed = tranwitekate,identifiant=useru.id,produite=noumeme,prixtottal=prix,quantiteto=tranwitekatenum,xs="",xsn="",s="",sn="",l="",ln="",m="",mn="",xl="",xln="",xxl="",xxln="",tranwite="",tranwiten="",tranneuf="",tranneufn="",karente="",karenten="",tranwiteun="",tranwiteunn="",tranwitedeux="",tranwitedeuxn="",tranwitrois="",tranwitroisn="",tranwitekate=tranwitekate,tranwitekaten=tranwitekatenum,prixdepouce = hfshggf.prix ,nomprodui = hfshggf.nom,descrprosui = hfshggf.description,pourcentage = hfshggf.porce,categorie = hfshggf.categorie,dispono=int(hfshggf.tranwitekatelet),statuse="dispobine")
            
            db.session.add(pani)
            db.session.commit()
    if int(tranwitekatenum) == 0 :
        tranwitekate = ""
        tranwitekatenum = ""
    
    
    

    # pani = Panieruser(image=image,identifiant=useru.id,produite=noumeme,prixtottal=prix,quantiteto=quantite,xs=xs,xsn=xsnum,s=s,sn=snum,l=l,ln=lnum,m=m,mn=mnum,xl=xl,xln=xlnum,xxl=xxl,xxln=xxlnum,tranwite=tranwite,tranwiten=tranwitenum,tranneuf=tranneuf,tranneufn=tranneufnum,karente=karente,karenten=karentenum,tranwiteun=tranwiteun,tranwiteunn=tranwiteunnum,tranwitedeux=tranwitedeux,tranwitedeuxn=tranwitedeuxnum,tranwitrois=tranwitrois,tranwitroisn=tranwitroisnum,tranwitekate=tranwitekate,tranwitekaten=tranwitekatenum)
        
    # db.session.add(pani)
    # db.session.commit()

    # tou = Ajouter.query.get(id)
    # import urllib.parse
    
    # if tou.categorie == 'VetementFemme' :
    #     quantite = quantite
    #     if int(quantite) < 1 :
    #         flash("Veuillez choisir la taille de l'article avant de commander svp ! ")
    #         return redirect(f'/info/{id}#formuhfh1')
    
    #     ms = f"Le lien : https://hington-shop.onrender.com/info/{a} , Quantite = {quantite} , Prix = {int(quantite)*int(prix)} , Nom = {nom} , Livraison = {livraison} , Numero = {numero} , Taille = {xs}{xsnum} {s}{snum} {l}{lnum} {m}{mnum} {xxl}{xxlnum} {xl}{xlnum} "
        
    #     return redirect(f"https://api.whatsapp.com/send/?phone=2250101678809&text={ms}&type=phone_number&app_absent=0")

    # if tou.categorie == 'chaussure' :
    #     quantite = quantite
    #     if int(quantite) < 1 :
    #         flash("Veuillez choisir la taille de l'article avant de commander svp ! ")
    #         return redirect(f'/sacs/{id}#formuhfh1')
    #     ms = f"Le lien : https://hington-shop.onrender.com/sacs/{a} , Quantite = {quantite} , Prix = {int(quantite)*int(prix)} , Nom = {nom} , Livraison = {livraison} , Numero = {numero} , Taille = {tranwite}{tranwitenum} {tranneuf}{tranneufnum} {karente}{karentenum} {tranwiteun}{tranwiteunnum} {tranwitedeux}{tranwitedeuxnum} {tranwitrois}{tranwitroisnum} {tranwitekate}{tranwitekatenum} "

    #     return redirect(f"https://api.whatsapp.com/send/?phone=2250101678809&text={ms}&type=phone_number&app_absent=0")
    
    # if tou.categorie == 'Montre' :
    #     quantite = quantite
    #     if int(quantite) < 1 :
    #         flash("Veuillez choisir la taille de l'article avant de commander svp ! ")
    #         return redirect(f'/montres/{id}#formuhfh1')
    #     ms = f"Le lien : https://hington-shop.onrender.com/montres/{a} , Quantite = {quantite} ,Prix = {int(quantite)*int(prix)} , Nom = {nom} , Livraison = {livraison} , Numero = {numero}  "
        

    #     return redirect(f"https://api.whatsapp.com/send/?phone=2250101678809&text={ms}&type=phone_number&app_absent=0")

    # ms_encoded = urllib.parse.quote(ms)
    # print(ms)
    # print(ms_encoded)

    # Encode the message string before passing it to the quote function
    # encoded_message = ms.encode('utf-8')
    # pywhatkit.sendwhats_image("+2250787022061", "bonjou", formatted_time, 45)
    # pywhatkit.sendwhats_image("+2250787022061", "https://web.whatsapp.com/send?phone=+22578587708&text={ms}", formatted_time, formatted)
    # return redirect(f"https://web.whatsapp.com/send?phone=+22578587708&text={ms}")
    # return redirect("/vente")
    

    # 
    return redirect("/monpanier")
@app.route('/passsm', methods=["POST"])
def passsm():
    if 'utilisateur_id' in session:
        useru = Profil.query.get(session['utilisateur_id'])
    # else :
    #     return redirect('/pre/')
    nom = request.form.get("nom")
    livraison = request.form.get("livraison")
    image = request.form.get("image")
    noumeme = request.form.get("noumeme")
    print("le voivi gegeghhdhjhdjhdjh",noumeme)
    prix = request.form.get("prix")
    quantite = request.form.get("quantiteplos")
    # hfshggf = Ajouter.query.get(int(noumeme))
    # jue = int(noumeme)
    nlogd = Panieruser.query.filter_by(produite = noumeme).first()

    print("fdghjkl",nlogd.id, "dfghjk")

    hfshggf = Panieruser.query.get(nlogd.id)


    # eudeyyt = Profil.query.all()
    if hfshggf.categorie == "Montre":
        if 'utilisateur_id' in session:
            useru = Profil.query.get(session['utilisateur_id'])
        print("les identifiants articles ",image,noumeme,prix,quantite)
        print("les identifiants  ",noumeme,useru.id)
        
        # derst = Panieruser.query.filter_by(identifiant=useru.id,produite=int(noumeme))
        derst = Panieruser.query.all()
        for i in derst :
            
            if int(i.produite) == int(noumeme) and int(i.identifiant)==int(useru.id):
                print("les articles ",i.produite,i.identifiant)
                dhher = Panieruser.query.get(i.id)
                zhher = Ajouter.query.get(int(i.produite))
                if zhher :
                    if (int(dhher.quantiteto) + int(quantite) ) <= int(zhher.quantit) :
                        dhher.quantiteto = int(dhher.quantiteto) + int(quantite)
                        db.session.commit()

             
                return redirect("/monpanier")
        return redirect("/monpanier")


    xs = request.form.get("xs","")
    xsnum = request.form.get("xsnum","0")
    if int(xsnum) > 0 :
        xs = "xs"
        derst = Panieruser.query.all()
        for i in derst :
             
            if int(i.produite) == int(noumeme) and int(i.identifiant)==int(useru.id) and str(xs) == str(i.tailed):
                print("les articles ",i.produite,i.identifiant)
                
                dhher = Panieruser.query.get(i.id)

                zhher = Ajouter.query.get(int(i.produite))
                if zhher :
                    if (int(dhher.quantiteto) + int(quantite) ) <= int(zhher.xslet) :
                        dhher.quantiteto = int(dhher.quantiteto) + int(quantite)
                        db.session.commit()

        
    if int(xsnum) == 0 :
        xs = ""
        xsnum = ""


    s = request.form.get("s","")
    snum = request.form.get("snum","0")
    if int(snum) > 0 :
        s = "s"
        derst = Panieruser.query.all()
        for i in derst :
            
            if int(i.produite) == int(noumeme) and int(i.identifiant)==int(useru.id) and  str(s) ==  str(i.tailed):
                print("les articles s",i.produite,i.identifiant)
                
                dhher = Panieruser.query.get(i.id)
                zhher = Ajouter.query.get(int(i.produite))
                if zhher :
                    if (int(dhher.quantiteto) + int(quantite) ) <= int(zhher.slet) :
                        dhher.quantiteto = int(dhher.quantiteto) + int(quantite)
                        db.session.commit()

    if int(snum) == 0 :
        s = ""
        snum = ""
    m = request.form.get("m","")
    mnum = request.form.get("mnum","0")
    if int(mnum) > 0 :
        m = "m"
        derst = Panieruser.query.all()
        for i in derst :
            
            if int(i.produite) == int(noumeme) and int(i.identifiant)==int(useru.id) and str(m) ==  str(i.tailed):
                print("les articles ",i.produite,i.identifiant)
                
                dhher = Panieruser.query.get(i.id)

                zhher = Ajouter.query.get(int(i.produite))
                if zhher :
                    if (int(dhher.quantiteto) + int(quantite) ) <= int(zhher.mlet) :
                        dhher.quantiteto = int(dhher.quantiteto) + int(quantite)
                        db.session.commit()


    if int(mnum) == 0 :
        m = ""
        mnum = ""
    l = request.form.get("l","")
    lnum = request.form.get("lnum","0")
    if int(lnum) > 0 :
        l = "l"
        derst = Panieruser.query.all()
        for i in derst :
            
            if int(i.produite) == int(noumeme) and int(i.identifiant)==int(useru.id) and str(l) ==  str(i.tailed):
                print("les articles ",i.produite,i.identifiant)
                
                dhher = Panieruser.query.get(i.id)

                zhher = Ajouter.query.get(int(i.produite))
                if zhher :
                    if (int(dhher.quantiteto) + int(quantite) ) <= int(zhher.llet) :
                        dhher.quantiteto = int(dhher.quantiteto) + int(quantite)
                        db.session.commit()
    if int(lnum) == 0 :
        l = ""
        lnum = ""
    xl = request.form.get("xl","")
    xlnum = request.form.get("xlnum","0")
    if int(xlnum) > 0 :
        xl = "xl"
        derst = Panieruser.query.all()
        for i in derst :
            
            if int(i.produite) == int(noumeme) and int(i.identifiant)==int(useru.id) and str(xl) ==  str(i.tailed):
                print("les articles ",i.produite,i.identifiant)
                
                dhher = Panieruser.query.get(i.id)

                zhher = Ajouter.query.get(int(i.produite))
                if zhher :
                    if (int(dhher.quantiteto) + int(quantite) ) <= int(zhher.xllet) :
                        dhher.quantiteto = int(dhher.quantiteto) + int(quantite)
                        db.session.commit()
    if int(xlnum) == 0 :
        xl = ""
        xlnum = ""
    xxlnum = request.form.get("xxlnum","0")
    xxl = request.form.get("xxl","")
    if int(xxlnum) > 0 :
        xxl = "xxl"
        derst = Panieruser.query.all()
        for i in derst :
            print(int(i.produite) ,"==", int(noumeme) , int(i.identifiant) ,"==",int(useru.id) , str(xxl)  ,"==",  str(i.tailed))
            if int(i.produite) == int(noumeme) and int(i.identifiant)==int(useru.id) and str(xxl) ==  str(i.tailed):
                print("les articles ",i.produite,i.identifiant)
                
                dhher = Panieruser.query.get(i.id)

                zhher = Ajouter.query.get(int(i.produite))
                if zhher :
                    if (int(dhher.quantiteto) + int(quantite) ) <= int(zhher.xxllet) :
                        dhher.quantiteto = int(dhher.quantiteto) + int(quantite)
                        db.session.commit()
    if int(xxlnum) == 0 :
        xxl = ""
        xxlnum = ""
    tranwite = request.form.get("tranwite","")
    tranwitenum = request.form.get("tranwitenum","0")
    if int(tranwitenum) > 0 :
        tranwite = "38 ° "
        derst = Panieruser.query.all()
        for i in derst :
            print(int(i.produite) ,"==", int(noumeme) , int(i.identifiant) ,"==",int(useru.id) , str(tranwite)  ,"==",  str(i.tailed))
            if int(i.produite) == int(noumeme) and int(i.identifiant)==int(useru.id) and str(tranwite) ==  str(i.tailed):
                print("les articles k",i.produite,i.identifiant)
                
                dhher = Panieruser.query.get(i.id)

                zhher = Ajouter.query.get(int(i.produite))
                if zhher :
                    if (int(dhher.quantiteto) + int(quantite) ) <= int(zhher.tranwitelet) :
                        dhher.quantiteto = int(dhher.quantiteto) + int(quantite)
                        db.session.commit()
    if int(tranwitenum) == 0 :
        tranwite = ""
        tranwitenum = ""
    
    tranneuf = request.form.get("tranneuf","")
    tranneufnum = request.form.get("tranneufnum","0")
    if int(tranneufnum) > 0 :
        tranneuf = "39 ° "
        derst = Panieruser.query.all()
        for i in derst :
            print(int(i.produite) ,"==", int(noumeme) , int(i.identifiant) ,"==",int(useru.id) , str(tranneuf)  ,"==",  str(i.tailed))
            if int(i.produite) == int(noumeme) and int(i.identifiant)==int(useru.id) and str(tranneuf) ==  str(i.tailed):
                print("les articles ",i.produite,i.identifiant)
                
                dhher = Panieruser.query.get(i.id)

                zhher = Ajouter.query.get(int(i.produite))
                if zhher :
                    if (int(dhher.quantiteto) + int(quantite) ) <= int(zhher.tranneuflet) :
                        dhher.quantiteto = int(dhher.quantiteto) + int(quantite)
                        db.session.commit()
    if int(tranneufnum) == 0 :
        tranneuf = ""
        tranneufnum = ""
    karente = request.form.get("karente","")
    karentenum = request.form.get("karentenum","0")
    if int(karentenum) > 0 :
        karente = "40 ° "
        derst = Panieruser.query.all()
        for i in derst :
            print(int(i.produite) ,"==", int(noumeme) , int(i.identifiant) ,"==",int(useru.id) , str(karente)  ,"==",  str(i.tailed))
            if int(i.produite) == int(noumeme) and int(i.identifiant)==int(useru.id) and str(karente) ==  str(i.tailed):
                print("les articles ",i.produite,i.identifiant)
                
                dhher = Panieruser.query.get(i.id)


                zhher = Ajouter.query.get(int(i.produite))
                if zhher :
                    if (int(dhher.quantiteto) + int(quantite) ) <= int(zhher.karentelet) :
                        dhher.quantiteto = int(dhher.quantiteto) + int(quantite)
                        db.session.commit()
    if int(karentenum) == 0 :
        karente = ""
        karentenum = ""
    tranwiteun = request.form.get("tranwiteun","")
    tranwiteunnum = request.form.get("tranwiteunnum","0")
    if int(tranwiteunnum) > 0 :
        tranwiteun = "41 ° "
        derst = Panieruser.query.all()
        for i in derst :
            print(int(i.produite) ,"==", int(noumeme) , int(i.identifiant) ,"==",int(useru.id) , str(tranwiteun)  ,"==",  str(i.tailed))
            if int(i.produite) == int(noumeme) and int(i.identifiant)==int(useru.id) and str(tranwiteun) ==  str(i.tailed):
                print("les articles ",i.produite,i.identifiant)
                
                dhher = Panieruser.query.get(i.id)


                zhher = Ajouter.query.get(int(i.produite))
                if zhher :
                    if (int(dhher.quantiteto) + int(quantite) ) <= int(zhher.tranwiteunlet) :
                        dhher.quantiteto = int(dhher.quantiteto) + int(quantite)
                        db.session.commit()
    if int(tranwiteunnum) == 0 :
        tranwiteun = ""
        tranwiteunnum = ""
    tranwitedeux = request.form.get("tranwitedeux","")
    tranwitedeuxnum = request.form.get("tranwitedeuxnum","0")
    if int(tranwitedeuxnum) > 0 :
        tranwitedeux = "42 ° "
        derst = Panieruser.query.all()
        for i in derst :
            print(int(i.produite) ,"==", int(noumeme) , int(i.identifiant) ,"==",int(useru.id) , str(tranwitedeux)  ,"==",  str(i.tailed))
            if int(i.produite) == int(noumeme) and int(i.identifiant)==int(useru.id) and str(tranwitedeux) ==  str(i.tailed):
                print("les articles ",i.produite,i.identifiant)
                
                dhher = Panieruser.query.get(i.id)

                zhher = Ajouter.query.get(int(i.produite))
                if zhher :
                    if (int(dhher.quantiteto) + int(quantite) ) <= int(zhher.tranwitedeuxlet) :
                        dhher.quantiteto = int(dhher.quantiteto) + int(quantite)
                        db.session.commit()
    if int(tranwitedeuxnum) == 0 :
        tranwitedeux = ""
        tranwitedeuxnum = ""
    tranwitrois = request.form.get("tranwitrois","")
    tranwitroisnum = request.form.get("tranwitroisnum","0")
    if int(tranwitroisnum) > 0 :
        tranwitrois = "43 ° "
        derst = Panieruser.query.all()
        for i in derst :
            print(int(i.produite) ,"==", int(noumeme) , int(i.identifiant) ,"==",int(useru.id) , str(tranwitrois)  ,"==",  str(i.tailed))
            if int(i.produite) == int(noumeme) and int(i.identifiant)==int(useru.id) and str(tranwitrois) ==  str(i.tailed):
                print("les articles ",i.produite,i.identifiant)
                
                dhher = Panieruser.query.get(i.id)

                
                zhher = Ajouter.query.get(int(i.produite))
                if zhher :
                    if (int(dhher.quantiteto) + int(quantite) ) <= int(zhher.tranwitroislet) :
                        dhher.quantiteto = int(dhher.quantiteto) + int(quantite)
                        db.session.commit()
    if int(tranwitroisnum) == 0 :
        tranwitrois = ""
        tranwitroisnum = ""
    tranwitekate = request.form.get("tranwitekate","")
    tranwitekatenum = request.form.get("tranwitekatenum","0")
    if int(tranwitekatenum) > 0 :
        tranwitekate = "44 ° "
        derst = Panieruser.query.all()
        for i in derst :
            print(int(i.produite) ,"==", int(noumeme) , int(i.identifiant) ,"==",int(useru.id) , str(tranwitekate)  ,"==",  str(i.tailed))
            if int(i.produite) == int(noumeme) and int(i.identifiant)==int(useru.id) and str(tranwitekate) ==  str(i.tailed):
                print("les articles ",i.produite,i.identifiant)
                
                dhher = Panieruser.query.get(i.id)


                zhher = Ajouter.query.get(int(i.produite))
                if zhher :
                    if (int(dhher.quantiteto) + int(quantite) ) <= int(zhher.tranwitekatelet) :
                        dhher.quantiteto = int(dhher.quantiteto) + int(quantite)
                        db.session.commit()
    if int(tranwitekatenum) == 0 :
        tranwitekate = ""
        tranwitekatenum = ""
    
   
    return redirect("/monpanier")
@app.route('/moinsssm', methods=["POST"])
def moinsssm():
    if 'utilisateur_id' in session:
        useru = Profil.query.get(session['utilisateur_id'])
    # else :
    #     return redirect('/pre/')
    nom = request.form.get("nom")
    livraison = request.form.get("livraison")
    image = request.form.get("image")
    noumeme = request.form.get("noumeme")
    print("le voivi gegeghhdhjhdjhdjh",noumeme)
    prix = request.form.get("prix")
    quantite = request.form.get("quantiteplosp")
    # hfshggf = Ajouter.query.get(int(noumeme))
    
    nlogd = Panieruser.query.filter_by(produite = noumeme).first()

    print("fdghjkl",nlogd.id, "dfghjk")

    hfshggf = Panieruser.query.get(nlogd.id)
    
  

    # eudeyyt = Profil.query.all()
    if hfshggf.categorie == "Montre" :
        if 'utilisateur_id' in session:
            useru = Profil.query.get(session['utilisateur_id'])
        print("les moins articles ",image,noumeme,prix,quantite)
        print("les moins  ",noumeme,useru.id)
        
        # derst = Panieruser.query.filter_by(identifiant=useru.id,produite=int(noumeme))
        derst = Panieruser.query.all()
        for i in derst :
            
            if int(i.produite) == int(noumeme) and int(i.identifiant)==int(useru.id):
                print("les articles ",i.produite,i.identifiant)
                dhher = Panieruser.query.get(i.id)
                if int(dhher.quantiteto) > 1 :
                    dhher.quantiteto = int(dhher.quantiteto) - 1


                    if int(dhher.quantiteto) <= int(dhher.dispono):
                        i.statuse = "dispobine"
                    db.session.commit()
                return redirect("/monpanier")
        return redirect("/monpanier")


    xs = request.form.get("xs","")
    xsnum = request.form.get("xsnum","0")
    if int(xsnum) >1 :
        xs = "xs"
        derst = Panieruser.query.all()
        for i in derst :
             
            if int(i.produite) == int(noumeme) and int(i.identifiant)==int(useru.id) and str(xs) == str(i.tailed):
                print("les articles ",i.produite,i.identifiant)
                
                dhher = Panieruser.query.get(i.id)


                dhher.quantiteto = int(dhher.quantiteto) - 1
                if int(dhher.quantiteto) <= int(dhher.dispono):
                    i.statuse = "dispobine"
                db.session.commit()

        
    if int(xsnum) == 0 :
        xs = ""
        xsnum = ""


    s = request.form.get("s","")
    snum = request.form.get("snum","0")
    if int(snum) >1 :
        s = "s"
        derst = Panieruser.query.all()
        for i in derst :
            
            if int(i.produite) == int(noumeme) and int(i.identifiant)==int(useru.id) and  str(s) ==  str(i.tailed):
                print("les articles s",i.produite,i.identifiant)
                
                dhher = Panieruser.query.get(i.id)
                dhher.quantiteto = int(dhher.quantiteto) - 1
                if int(dhher.quantiteto) <= int(dhher.dispono):
                    i.statuse = "dispobine"
                db.session.commit()

    if int(snum) == 0 :
        s = ""
        snum = ""
    m = request.form.get("m","")
    mnum = request.form.get("mnum","0")
    if int(mnum) >1 :
        m = "m"
        derst = Panieruser.query.all()
        for i in derst :
            
            if int(i.produite) == int(noumeme) and int(i.identifiant)==int(useru.id) and str(m) ==  str(i.tailed):
                print("les articles ",i.produite,i.identifiant)
                
                dhher = Panieruser.query.get(i.id)


                dhher.quantiteto = int(dhher.quantiteto) - 1


                 
                    
                if int(dhher.quantiteto) <= int(dhher.dispono):
                    
                    i.statuse = "dispobine"
             
              
                db.session.commit()




    if int(mnum) == 0 :
        m = ""
        mnum = ""
    l = request.form.get("l","")
    lnum = request.form.get("lnum","0")
    if int(lnum) >1 :
        l = "l"
        derst = Panieruser.query.all()
        for i in derst :
            
            if int(i.produite) == int(noumeme) and int(i.identifiant)==int(useru.id) and str(l) ==  str(i.tailed):
                print("les articles ",i.produite,i.identifiant)
                
                dhher = Panieruser.query.get(i.id)


                dhher.quantiteto = int(dhher.quantiteto) - 1
                if int(dhher.quantiteto) <= int(dhher.dispono):
                    i.statuse = "dispobine"
                db.session.commit()
    if int(lnum) == 0 :
        l = ""
        lnum = ""
    xl = request.form.get("xl","")
    xlnum = request.form.get("xlnum","0")
    if int(xlnum) >1 :
        xl = "xl"
        derst = Panieruser.query.all()
        for i in derst :
            
            if int(i.produite) == int(noumeme) and int(i.identifiant)==int(useru.id) and str(xl) ==  str(i.tailed):
                print("les articles ",i.produite,i.identifiant)
                
                dhher = Panieruser.query.get(i.id)


                dhher.quantiteto = int(dhher.quantiteto) - 1
                if int(dhher.quantiteto) <= int(dhher.dispono):
                    i.statuse = "dispobine"
                db.session.commit()
    if int(xlnum) == 0 :
        xl = ""
        xlnum = ""
    xxlnum = request.form.get("xxlnum","0")
    xxl = request.form.get("xxl","")
    if int(xxlnum) >1 :
        xxl = "xxl"
        derst = Panieruser.query.all()
        for i in derst :
            print(int(i.produite) ,"==", int(noumeme) , int(i.identifiant) ,"==",int(useru.id) , str(xxl)  ,"==",  str(i.tailed))
            if int(i.produite) == int(noumeme) and int(i.identifiant)==int(useru.id) and str(xxl) ==  str(i.tailed):
                print("les articles ",i.produite,i.identifiant)
                
                dhher = Panieruser.query.get(i.id)


                dhher.quantiteto = int(dhher.quantiteto) - 1
                if int(dhher.quantiteto) <= int(dhher.dispono):
                    i.statuse = "dispobine"
                db.session.commit()
    if int(xxlnum) == 0 :
        xxl = ""
        xxlnum = ""
    tranwite = request.form.get("tranwite","")
    tranwitenum = request.form.get("tranwitenum","0")
    if int(tranwitenum) >1 :
        tranwite = "38 ° "
        derst = Panieruser.query.all()
        for i in derst :
            print(int(i.produite) ,"==", int(noumeme) , int(i.identifiant) ,"==",int(useru.id) , str(tranwite)  ,"==",  str(i.tailed))
            if int(i.produite) == int(noumeme) and int(i.identifiant)==int(useru.id) and str(tranwite) ==  str(i.tailed):
                print("les articles k",i.produite,i.identifiant)
                
                dhher = Panieruser.query.get(i.id)


                dhher.quantiteto = int(dhher.quantiteto) - 1
                if int(dhher.quantiteto) <= int(dhher.dispono):
                    i.statuse = "dispobine"
                db.session.commit()
    if int(tranwitenum) == 0 :
        tranwite = ""
        tranwitenum = ""
    
    tranneuf = request.form.get("tranneuf","")
    tranneufnum = request.form.get("tranneufnum","0")
    if int(tranneufnum) >1 :
        tranneuf = "39 ° "
        derst = Panieruser.query.all()
        for i in derst :
            print(int(i.produite) ,"==", int(noumeme) , int(i.identifiant) ,"==",int(useru.id) , str(tranneuf)  ,"==",  str(i.tailed))
            if int(i.produite) == int(noumeme) and int(i.identifiant)==int(useru.id) and str(tranneuf) ==  str(i.tailed):
                print("les articles ",i.produite,i.identifiant)
                
                dhher = Panieruser.query.get(i.id)


                dhher.quantiteto = int(dhher.quantiteto) - 1
                if int(dhher.quantiteto) <= int(dhher.dispono):
                    i.statuse = "dispobine"
                db.session.commit()
    if int(tranneufnum) == 0 :
        tranneuf = ""
        tranneufnum = ""
    karente = request.form.get("karente","")
    karentenum = request.form.get("karentenum","0")
    if int(karentenum) >1 :
        karente = "40 ° "
        derst = Panieruser.query.all()
        for i in derst :
            print(int(i.produite) ,"==", int(noumeme) , int(i.identifiant) ,"==",int(useru.id) , str(karente)  ,"==",  str(i.tailed))
            if int(i.produite) == int(noumeme) and int(i.identifiant)==int(useru.id) and str(karente) ==  str(i.tailed):
                print("les articles ",i.produite,i.identifiant)
                
                dhher = Panieruser.query.get(i.id)


                dhher.quantiteto = int(dhher.quantiteto) - 1
                if int(dhher.quantiteto) <= int(dhher.dispono):
                    i.statuse = "dispobine"
                db.session.commit()
    if int(karentenum) == 0 :
        karente = ""
        karentenum = ""
    tranwiteun = request.form.get("tranwiteun","")
    tranwiteunnum = request.form.get("tranwiteunnum","0")
    if int(tranwiteunnum) >1 :
        tranwiteun = "41 ° "
        derst = Panieruser.query.all()
        for i in derst :
            print(int(i.produite) ,"==", int(noumeme) , int(i.identifiant) ,"==",int(useru.id) , str(tranwiteun)  ,"==",  str(i.tailed))
            if int(i.produite) == int(noumeme) and int(i.identifiant)==int(useru.id) and str(tranwiteun) ==  str(i.tailed):
                print("les articles ",i.produite,i.identifiant)
                
                dhher = Panieruser.query.get(i.id)


                dhher.quantiteto = int(dhher.quantiteto) - 1
                if int(dhher.quantiteto) <= int(dhher.dispono):
                    i.statuse = "dispobine"
                db.session.commit()
    if int(tranwiteunnum) == 0 :
        tranwiteun = ""
        tranwiteunnum = ""
    tranwitedeux = request.form.get("tranwitedeux","")
    tranwitedeuxnum = request.form.get("tranwitedeuxnum","0")
    if int(tranwitedeuxnum) >1 :
        tranwitedeux = "42 ° "
        derst = Panieruser.query.all()
        for i in derst :
            print(int(i.produite) ,"==", int(noumeme) , int(i.identifiant) ,"==",int(useru.id) , str(tranwitedeux)  ,"==",  str(i.tailed))
            if int(i.produite) == int(noumeme) and int(i.identifiant)==int(useru.id) and str(tranwitedeux) ==  str(i.tailed):
                print("les articles ",i.produite,i.identifiant)
                
                dhher = Panieruser.query.get(i.id)


                dhher.quantiteto = int(dhher.quantiteto) - 1
                if int(dhher.quantiteto) <= int(dhher.dispono):
                    i.statuse = "dispobine"
                db.session.commit()
    if int(tranwitedeuxnum) == 0 :
        tranwitedeux = ""
        tranwitedeuxnum = ""
    tranwitrois = request.form.get("tranwitrois","")
    tranwitroisnum = request.form.get("tranwitroisnum","0")
    if int(tranwitroisnum) >1 :
        tranwitrois = "43 ° "
        derst = Panieruser.query.all()
        for i in derst :
            print(int(i.produite) ,"==", int(noumeme) , int(i.identifiant) ,"==",int(useru.id) , str(tranwitrois)  ,"==",  str(i.tailed))
            if int(i.produite) == int(noumeme) and int(i.identifiant)==int(useru.id) and str(tranwitrois) ==  str(i.tailed):
                print("les articles ",i.produite,i.identifiant)
                
                dhher = Panieruser.query.get(i.id)


                dhher.quantiteto = int(dhher.quantiteto) - 1
                if int(dhher.quantiteto) <= int(dhher.dispono):
                    i.statuse = "dispobine"
                db.session.commit()
    if int(tranwitroisnum) == 0 :
        tranwitrois = ""
        tranwitroisnum = ""
    tranwitekate = request.form.get("tranwitekate","")
    tranwitekatenum = request.form.get("tranwitekatenum","0")
    if int(tranwitekatenum) >1 :
        tranwitekate = "44 ° "
        derst = Panieruser.query.all()
        for i in derst :
            print(int(i.produite) ,"==", int(noumeme) , int(i.identifiant) ,"==",int(useru.id) , str(tranwitekate)  ,"==",  str(i.tailed))
            if int(i.produite) == int(noumeme) and int(i.identifiant)==int(useru.id) and str(tranwitekate) ==  str(i.tailed):
                print("les articles ",i.produite,i.identifiant)
                
                dhher = Panieruser.query.get(i.id)


                dhher.quantiteto = int(dhher.quantiteto) - 1
                if int(dhher.quantiteto) <= int(dhher.dispono):
                    i.statuse = "dispobine"
                db.session.commit()
    if int(tranwitekatenum) == 0 :
        tranwitekate = ""
        tranwitekatenum = ""
    
   
    return redirect("/monpanier")

        
    

    

# @app.route('/dataze', methods=["POST"])
# def dataze():
#     data = {"image":"image","tailed" : "","produite":"noumeme","prixtottal":"prix","quantiteto":"quantite","xs":"","xsn":"","s":"","sn":"","l":"","ln":"","m":"","mn":"","xl":"","xln":"","xxl":"","xxln":"","tranwite":"","tranwiten":"","tranneuf":"","tranneufn":"","karente":"","karenten":"","tranwiteun":"","tranwiteunn":"","tranwitedeux":"","tranwitedeuxn":"","tranwitrois":"","tranwitroisn":"","tranwitekate":"","tranwitekaten":""}
#     des = {"image":"image","tailed" : "","dee":"fggh"}    
#     print(data)
#     return des
@app.route('/ssme', methods=["POST"])
def ssme():
    
    nom = request.form.get("nom")
    livraison = request.form.get("livraison")
    image = request.form.get("image")
    noumeme = request.form.get("noumeme")
    prix = request.form.get("prix")
    quantite = request.form.get("quantiteplos")

        # eudeyyt = Profil.query.all()
    if 1==1:
        
        print("les identifiants articles non connecter",image,noumeme,prix,quantite)
    
        data = {"image":image,"tailed" : "","produite":noumeme,"prixtottal":prix,"quantiteto":quantite,"xs":"","xsn":"","s":"","sn":"","l":"","ln":"","m":"","mn":"","xl":"","xln":"","xxl":"","xxln":"","tranwite":"","tranwiten":"","tranneuf":"","tranneufn":"","karente":"","karenten":"","tranwiteun":"","tranwiteunn":"","tranwitedeux":"","tranwitedeuxn":"","tranwitrois":"","tranwitroisn":"","tranwitekate":"","tranwitekaten":""}
            
        print(data)
        detr = {
            "image": "pho1.jpg",
            "karente": "",
            "karenten": "",
            "l": "",
            "ln": "",
            "m": "",
            "mn": "",
            "prixtottal": "4800",
            "produite": "1",
            "quantiteto": "3",
            "s": "",
            "sn": "",
            "tailed": "",
            "tranneuf": "",
            "tranneufn": "",
            "tranwite": "",
            "tranwitedeux": "",
            "tranwitedeuxn": "",
            "tranwitekate": "",
            "tranwitekaten": "",
            "tranwiten": "",
            "tranwiteun": "",
            "tranwiteunn": "",
            "tranwitrois": "",
            "tranwitroisn": "",
            "xl": "",
            "xln": "",
            "xs": "",
            "xsn": "",
            "xxl": "",
            "xxln": ""
            }
        return data


    xs = request.form.get("xs","")
    xsnum = request.form.get("xsnum","0")
    if int(xsnum) > 0 :
        xs = "xs"
        
        data = {"image":image,"tailed" :xs,"produite":noumeme,"prixtottal":prix,"quantiteto":xsnum,"xs":xs,"xsn":xsnum,"s":"","sn":snum,"l":"","ln":"","m":"","mn":"","xl":"","xln":"","xxl":"","xxln":"","tranwite":"","tranwiten":"","tranneuf":"","tranneufn":"","karente":"","karenten":"","tranwiteun":"","tranwiteunn":"","tranwitedeux":"","tranwitedeuxn":"","tranwitrois":"","tranwitroisn":"","tranwitekate":"","tranwitekaten":""}
        print(data)
        return data
        
    if int(xsnum) == 0 :
        xs = ""
        xsnum = ""


    s = request.form.get("s","")
    snum = request.form.get("snum","0")
    if int(snum) > 0 :
        s = "s"
        
        data = {"image":image,"tailed" :s,"produite":noumeme,"prixtottal":prix,"quantiteto":snum,"xs":"","xsn":"","s":s,"sn":snum,"l":"","ln":"","m":"","mn":"","xl":"","xln":"","xxl":"","xxln":"","tranwite":"","tranwiten":"","tranneuf":"","tranneufn":"","karente":"","karenten":"","tranwiteun":"","tranwiteunn":"","tranwitedeux":"","tranwitedeuxn":"","tranwitrois":"","tranwitroisn":"","tranwitekate":"","tranwitekaten":""}
        print(data)
        return data
        
    if int(snum) == 0 :
        s = ""
        snum = ""
    m = request.form.get("m","")
    mnum = request.form.get("mnum","0")
    if int(mnum) > 0 :
        m = "m"
        
        data = {"image":image,"tailed" :m,"produite":noumeme,"prixtottal":prix,"quantiteto":mnum,"xs":"","xsn":"","s":"","sn":"","l":"","ln":"","m":m,"mn":mnum,"xl":"","xln":"","xxl":"","xxln":"","tranwite":"","tranwiten":"","tranneuf":"","tranneufn":"","karente":"","karenten":"","tranwiteun":"","tranwiteunn":"","tranwitedeux":"","tranwitedeuxn":"","tranwitrois":"","tranwitroisn":"","tranwitekate":"","tranwitekaten":""}
        print(data)
        return data
        
    if int(mnum) == 0 :
        m = ""
        mnum = ""
    l = request.form.get("l","")
    lnum = request.form.get("lnum","0")
    if int(lnum) > 0 :
        l = "l"
        
        data = {"image":image,"tailed" :l,"produite":noumeme,"prixtottal":prix,"quantiteto":lnum,"xs":"","xsn":"","s":"","sn":"","l":l,"ln":lnum,"m":"","mn":"","xl":"","xln":"","xxl":"","xxln":"","tranwite":"","tranwiten":"","tranneuf":"","tranneufn":"","karente":"","karenten":"","tranwiteun":"","tranwiteunn":"","tranwitedeux":"","tranwitedeuxn":"","tranwitrois":"","tranwitroisn":"","tranwitekate":"","tranwitekaten":""}
        print(data)
        return data
        
    if int(lnum) == 0 :
        l = ""
        lnum = ""
    xl = request.form.get("xl","")
    xlnum = request.form.get("xlnum","0")
    if int(xlnum) > 0 :
        xl = "xl"
        
        data = {"image":image, "tailed" : xl,"produite":noumeme,"prixtottal":prix,"quantiteto":xlnum,"xs":"","xsn":"","s":"","sn":"","l":"","ln":"","m":"","mn":"","xl":xl,"xln":xlnum,"xxl":"","xxln":"","tranwite":"","tranwiten":"","tranneuf":"","tranneufn":"","karente":"","karenten":"","tranwiteun":"","tranwiteunn":"","tranwitedeux":"","tranwitedeuxn":"","tranwitrois":"","tranwitroisn":"","tranwitekate":"","tranwitekaten":""}
        print(data)
        return data
        
    if int(xlnum) == 0 :
        xl = ""
        xlnum = ""
    xxlnum = request.form.get("xxlnum","0")
    xxl = request.form.get("xxl","")
    if int(xxlnum) > 0 :
        xxl = "xxl"
        
        data = {"image":image, "tailed" : xxl,"produite":noumeme,"prixtottal":prix,"quantiteto":xxlnum,"xs":"","xsn":"","s":"","sn":"","l":"","ln":"","m":"","mn":"","xl":"","xln":"","xxl":xxl,"xxln":xxlnum,"tranwite":"","tranwiten":"","tranneuf":"","tranneufn":"","karente":"","karenten":"","tranwiteun":"","tranwiteunn":"","tranwitedeux":"","tranwitedeuxn":"","tranwitrois":"","tranwitroisn":"","tranwitekate":"","tranwitekaten":""}
        print(data)
        return data
        
    if int(xxlnum) == 0 :
        xxl = ""
        xxlnum = ""

    tranwite = request.form.get("tranwite","")
    tranwitenum = request.form.get("tranwitenum","0")
    if int(tranwitenum) > 0 :
        tranwite = "38 ° "
        tranwitenum = tranwitenum
        
        data = {"image":image,"tailed" : tranwite,"produite":noumeme,"prixtottal":prix,"quantiteto":tranwitenum,"xs":"","xsn":"","s":"","sn":"","l":"","ln":"","m":"","mn":"","xl":"","xln":"","xxl":"","xxln":"","tranwite":tranwite,"tranwiten":tranwitenum,"tranneuf":"","tranneufn":"","karente":"","karenten":"","tranwiteun":"","tranwiteunn":"","tranwitedeux":"","tranwitedeuxn":"","tranwitrois":"","tranwitroisn":"","tranwitekate":"","tranwitekaten":""}
        print(data)
        return data
        
    if int(tranwitenum) == 0 :
        tranwite = ""
        tranwitenum = ""
    
    tranneuf = request.form.get("tranneuf","")
    tranneufnum = request.form.get("tranneufnum","0")
    if int(tranneufnum) > 0 :
        tranneuf = "39 ° "
        tranneufnum = tranneufnum
        
        data = {"image":image,"tailed" : tranneuf,"produite":noumeme,"prixtottal":prix,"quantiteto":tranneufnum,"xs":"","xsn":"","s":"","sn":"","l":"","ln":"","m":"","mn":"","xl":"","xln":"","xxl":"","xxln":"","tranwite":"","tranwiten":"","tranneuf":tranneuf,"tranneufn":tranneufnum,"karente":"","karenten":"","tranwiteun":"","tranwiteunn":"","tranwitedeux":"","tranwitedeuxn":"","tranwitrois":"","tranwitroisn":"","tranwitekate":"","tranwitekaten":""}
        print(data)
        return data
        
    if int(tranneufnum) == 0 :
        tranneuf = ""
        tranneufnum = ""
    karente = request.form.get("karente","")
    karentenum = request.form.get("karentenum","0")
    if int(karentenum) > 0 :
        karente = "40 ° "
        karentenum = karentenum
        
        data = {"image":image,"tailed" : karente,"produite":noumeme,"prixtottal":prix,"quantiteto":karentenum,"xs":"","xsn":"","s":"","sn":"","l":"","ln":"","m":"","mn":"","xl":"","xln":"","xxl":"","xxln":"","tranwite":"","tranwiten":"","tranneuf":"","tranneufn":"","karente":karente,"karenten":karentenum,"tranwiteun":"","tranwiteunn":"","tranwitedeux":"","tranwitedeuxn":"","tranwitrois":"","tranwitroisn":"","tranwitekate":"","tranwitekaten":""}
        print(data)
        return data
        
    if int(karentenum) == 0 :
        karente = ""
        karentenum = ""
    tranwiteun = request.form.get("tranwiteun","")
    tranwiteunnum = request.form.get("tranwiteunnum","0")
    if int(tranwiteunnum) > 0 :
        tranwiteun = "41 ° "
        tranwiteunnum = tranwiteunnum
        
        data = {"image":image,"tailed" :tranwiteun ,"produite":noumeme,"prixtottal":prix,"quantiteto":tranwiteunnum,"xs":"","xsn":"","s":"","sn":"","l":"","ln":"","m":"","mn":"","xl":"","xln":"","xxl":"","xxln":"","tranwite":"","tranwiten":"","tranneuf":"","tranneufn":"","karente":"","karenten":"","tranwiteun":tranwiteun,"tranwiteunn":tranwiteunnum,"tranwitedeux":"","tranwitedeuxn":"","tranwitrois":"","tranwitroisn":"","tranwitekate":"","tranwitekaten":""}
        print(data)
        return data
        
    if int(tranwiteunnum) == 0 :
        tranwiteun = ""
        tranwiteunnum = ""
    tranwitedeux = request.form.get("tranwitedeux","")
    tranwitedeuxnum = request.form.get("tranwitedeuxnum","0")
    if int(tranwitedeuxnum) > 0 :
        tranwitedeux = "42 ° "
        tranwitedeuxnum = tranwitedeuxnum
        
        data = {"image":image,"tailed" : tranwitedeux ,"produite":noumeme,"prixtottal":prix,"quantiteto":tranwitedeuxnum,"xs":"","xsn":"","s":"","sn":"","l":"","ln":"","m":"","mn":"","xl":"","xln":"","xxl":"","xxln":"","tranwite":"","tranwiten":"","tranneuf":"","tranneufn":"","karente":"","karenten":"","tranwiteun":"","tranwiteunn":"","tranwitedeux":tranwitedeux,"tranwitedeuxn":tranwitedeuxnum,"tranwitrois":"","tranwitroisn":"","tranwitekate":"","tranwitekaten":""}
        print(data)
        return data
        
    if int(tranwitedeuxnum) == 0 :
        tranwitedeux = ""
        tranwitedeuxnum = ""
    tranwitrois = request.form.get("tranwitrois","")
    tranwitroisnum = request.form.get("tranwitroisnum","0")
    if int(tranwitroisnum) > 0 :
        tranwitrois = "43 ° "
        tranwitroisnum = tranwitroisnum
        
        data = {"image":image,"tailed" : tranwitrois,"produite":noumeme,"prixtottal":prix,"quantiteto":tranwitroisnum,"xs":"","xsn":"","s":"","sn":"","l":"","ln":"","m":"","mn":"","xl":"","xln":"","xxl":"","xxln":"","tranwite":"","tranwiten":"","tranneuf":"","tranneufn":"","karente":"","karenten":"","tranwiteun":"","tranwiteunn":"","tranwitedeux":"","tranwitedeuxn":"","tranwitrois":tranwitrois,"tranwitroisn":tranwitroisnum,"tranwitekate":"","tranwitekaten":""}
        print(data)
        return data
        
    if int(tranwitroisnum) == 0 :
        tranwitrois = ""
        tranwitroisnum = ""
    tranwitekate = request.form.get("tranwitekate","")
    tranwitekatenum = request.form.get("tranwitekatenum","0")
    if int(tranwitekatenum) > 0 :
        tranwitekate = "44 ° "
        tranwitekatenum = tranwitekatenum
        
        data = {"image":image,"tailed" : tranwitekate,"produite":noumeme,"prixtottal":prix,"quantiteto":tranwitekatenum,"xs":"","xsn":"","s":"","sn":"","l":"","ln":"","m":"","mn":"","xl":"","xln":"","xxl":"","xxln":"","tranwite":"","tranwiten":"","tranneuf":"","tranneufn":"","karente":"","karenten":"","tranwiteun":"","tranwiteunn":"","tranwitedeux":"","tranwitedeuxn":"","tranwitrois":"","tranwitroisn":"","tranwitekate":tranwitekate,"tranwitekaten":tranwitekatenum}
        print(data)
        return data
        
    if int(tranwitekatenum) == 0 :
        tranwitekate = ""
        tranwitekatenum = ""
    
    # sizes = ["xs", "s", "m", "l", "xl", "xxl", "tranwite", "tranneuf", "karente", "tranwiteun", "tranwitedeux", "tranwitrois", "tranwitekate"]
    # size_suffixes = {"tranwite": "38 ° ", "tranneuf": "39 ° ", "karente": "40 ° ", "tranwiteun": "41 ° ", "tranwitedeux": "42 ° ", "tranwitrois": "43 ° ", "tranwitekate": "44 ° "}
    
    # image = request.form.get("image", "")
    # noumeme = request.form.get("noumeme", "")
    # prix = request.form.get("prix", "")
    
    # for size in sizes:
    #     num_key = f"{size}num"
    #     size_value = request.form.get(size, "")
    #     num_value = request.form.get(num_key, "0")
        
    #     if int(num_value) > 0:
    #         tailed = size_suffixes.get(size, size)
    #         data = {
    #             "image": image,
    #             "tailed": tailed,
    #             "produite": noumeme,
    #             "prixtottal": prix,
    #             "quantiteto": num_value,
    #             "xs": "",
    #             "xsn": "",
    #             "s": "",
    #             "sn": "",
    #             "l": "",
    #             "ln": "",
    #             "m": "",
    #             "mn": "",
    #             "xl": "",
    #             "xln": "",
    #             "xxl": "",
    #             "xxln": "",
    #             "tranwite": "",
    #             "tranwiten": "",
    #             "tranneuf": "",
    #             "tranneufn": "",
    #             "karente": "",
    #             "karenten": "",
    #             "tranwiteun": "",
    #             "tranwiteunn": "",
    #             "tranwitedeux": "",
    #             "tranwitedeuxn": "",
    #             "tranwitrois": "",
    #             "tranwitroisn": "",
    #             "tranwitekate": "",
    #             "tranwitekaten": ""
    #         }
    #         data[size] = tailed
    #         data[num_key] = num_value
    #         print(data)
    #         return data
    
    return redirect("/monpanierls")

    


@app.route("/commadeadmin")
def commadeadmin():
    if 'utilisateur_id' in session:
        useru = Profil.query.get(session['utilisateur_id'])
        if useru.satuq == 1 :
            pass
        else:
            return redirect('/')
    else:
        return redirect('/pre/administa')
    try :
        administa = Ajouter.query.all()
        pofil = Profil.query.all()
        compt=0
        compzt=0
        compt1=0
        nombdre1=0
        nombdre=0
        compt2=0
        bommande = Commande.query.all()
        bommande0 = []
        bommande00 = []
        bommande1 = []
        bommande2 = []
        for i in bommande:
            if i.status == "En cours":
                compt += int(i.prixtotal)
                bommande0.append(i)
                compzt += 1
                nombdre = compzt

               
                bommande00.append(i.mail)
               
               
                    
                
            if i.status == "Déja livré":
                compt1 += int(i.prixtotal)
                bommande1.append(i)
            if i.status == "Annulé":
                compt2 += int(i.prixtotal)
                bommande2.append(i)
                nombdre1 = len(bommande2)

        bommande00 = list(set(bommande00))
        VetementHomme = []
        a = Ajouter.query.all()
        for i in a:
            if i.categorie == 'VetementHomme':
                VetementHomme.append(i)
        VetementFemme = []
        a = Ajouter.query.all()
        for i in a:
            if i.categorie == 'VetementFemme':
                VetementFemme.append(i)
        Montre = []
        a = Ajouter.query.all()
        for i in a:
            if i.categorie == 'Montre':
                Montre.append(i)
        sac = []
        a = Ajouter.query.all()
        for i in a:
            if i.categorie == 'chaussure':
                sac.append(i)




        
        return render_template("listecommandeadmin.html",administa=administa,VetementHomme=VetementHomme,VetementFemme=VetementFemme,Montre=Montre,sac=sac,pofil=pofil,bommande=bommande,nombdre=nombdre,nombdre1=nombdre1,compt=compt,compt1=compt1,bommande0=bommande0,bommande1=bommande1,bommande2=bommande2,bommande00=bommande00)

    except :
        return render_template("listecommandeadmin.html",administa=administa,VetementHomme=VetementHomme,VetementFemme=VetementFemme,Montre=Montre,sac=sac,nombdre=nombdre,compt=compt)
    

@app.route("/filtrecommande",methods = ["POST"])
def filtrecommande():
    if 'utilisateur_id' in session:
        useru = Profil.query.get(session['utilisateur_id'])
        if useru.satuq == 1 :
            pass
        else:
            return redirect('/')
    else:
        return redirect('/pre/administa')



    seldldss = request.form.get("seldldss")


    try :
        administa = Ajouter.query.all()
        pofil = Profil.query.all()
        compt=0
        compzt=0
        compt1=0
        nombdre1=0
        nombdre=0
        compt2=0
        bommande = Commande.query.all()
        bommande0 = []
        bommande00 = []
        bommande1 = []
        bommande2 = []
        for i in bommande:
            if i.status == "En cours":
                compt += int(i.prixtotal)
               
                if i not in bommande00:
                   bommande00.append(i.mail)
                compzt += 1
                nombdre = compzt

            if i.status == "En cours" and i.mail == seldldss:
               
                bommande0.append(i)
           
                
            if i.status == "Déja livré":
                compt1 += int(i.prixtotal)
                bommande1.append(i)
            if i.status == "Annulé":
                compt2 += int(i.prixtotal)
                bommande2.append(i)
                nombdre1 = len(bommande2)

        bommande00 = list(set(bommande00))
        VetementHomme = []
        a = Ajouter.query.all()
        for i in a:
            if i.categorie == 'VetementHomme':
                VetementHomme.append(i)
        VetementFemme = []
        a = Ajouter.query.all()
        for i in a:
            if i.categorie == 'VetementFemme':
                VetementFemme.append(i)
        Montre = []
        a = Ajouter.query.all()
        for i in a:
            if i.categorie == 'Montre':
                Montre.append(i)
        sac = []
        a = Ajouter.query.all()
        for i in a:
            if i.categorie == 'chaussure':
                sac.append(i)


        return render_template("listecommandeadmin.html",administa=administa,VetementHomme=VetementHomme,VetementFemme=VetementFemme,Montre=Montre,sac=sac,pofil=pofil,bommande=bommande,nombdre=nombdre,nombdre1=nombdre1,compt=compt,compt1=compt1,bommande0=bommande0,bommande1=bommande1,bommande2=bommande2,bommande00=bommande00)

    except :
        return render_template("listecommandeadmin.html",administa=administa,VetementHomme=VetementHomme,VetementFemme=VetementFemme,Montre=Montre,sac=sac,nombdre=nombdre,compt=compt)
    


@app.route("/userasmin")
def userasmin():
    if 'utilisateur_id' in session:
        useru = Profil.query.get(session['utilisateur_id'])
        if useru.satuq == 1 :
            pass
        else:
            return redirect('/')
    else:
        return redirect('/pre/administa')
    try :
        pofil = Profil.query.all()
        compt=0
        nombdre1=0
        nombdre=0
        compt1=0
        compt2=0
        bommande = Commande.query.all()
        bommande0 = []
        bommande1 = []
        bommande2 = []
        for i in bommande:
            if i.status == "En cours":
                compt += int(i.prixtotal)
                bommande0.append(i)
                nombdre = len(bommande0)
            if i.status == "Déja livré":
                compt1 += int(i.prixtotal)
                bommande1.append(i)
            if i.status == "Annulé":
                compt2 += int(i.prixtotal)
                bommande2.append(i)
                nombdre1 = len(bommande2)

        
        VetementHomme = []
        a = Ajouter.query.all()
        for i in a:
            if i.categorie == 'VetementHomme':
                VetementHomme.append(i)
        VetementFemme = []
        a = Ajouter.query.all()
        for i in a:
            if i.categorie == 'VetementFemme':
                VetementFemme.append(i)
        Montre = []
        a = Ajouter.query.all()
        for i in a:
            if i.categorie == 'Montre':
                Montre.append(i)
        sac = []
        a = Ajouter.query.all()
        for i in a:
            if i.categorie == 'chaussure':
                sac.append(i)




        return render_template("listeuseradmin.html",administa=administa,VetementHomme=VetementHomme,VetementFemme=VetementFemme,Montre=Montre,sac=sac,pofil=pofil,bommande=bommande,nombdre=nombdre,nombdre1=nombdre1,compt=compt,compt1=compt1,bommande0=bommande0,bommande1=bommande1,bommande2=bommande2)

    except :
        return render_template("listeuseradmin.html",administa=administa,VetementHomme=VetementHomme,VetementFemme=VetementFemme,Montre=Montre,sac=sac,nombdre=nombdre,compt=compt)
    
@app.route("/listederobe")
def userlistederobe():
    if 'utilisateur_id' in session:
        useru = Profil.query.get(session['utilisateur_id'])
        if useru.satuq == 1 :
            pass
        else:
            return redirect('/')
    else:
        return redirect('/pre/administa')
    try :
        pofil = Profil.query.all()
        compt=0
        nombdre1=0
        nombdre=0
        compt1=0
        compt2=0
        bommande = Commande.query.all()
        bommande0 = []
        bommande1 = []
        bommande2 = []
        sacze = []
        for i in bommande:
            if i.status == "En cours":
                compt += int(i.prixtotal)
                bommande0.append(i)
                nombdre = len(bommande0)
            if i.status == "Déja livré":
                compt1 += int(i.prixtotal)
                bommande1.append(i)
            if i.status == "Annulé":
                compt2 += int(i.prixtotal)
                bommande2.append(i)
                nombdre1 = len(bommande2)

        
        VetementHomme = []
        a = Ajouter.query.all()
        for i in a:
            if i.categorie == 'VetementHomme':
                VetementHomme.append(i)
        VetementFemme = []
        a = Ajouter.query.all()
        for i in a:
            if i.categorie == 'VetementFemme':
                VetementFemme.append(i)
        Montre = []
        a = Ajouter.query.all()
        for i in a:
            if i.categorie == 'Montre':
                Montre.append(i)
        sac = []
        a = Ajouter.query.all()
        for i in a:
            if i.categorie == 'chaussure':
                sac.append(i)



        if len(VetementFemme) > 0 :
            for i in VetementFemme :
                if i.xs == 'xs' :
                    mpezslsm = {"nom":i.nom,"id":i.id,"description":i.description,"prix":i.prix,"porceprix":i.porceprix,"porce":i.porce,"categorie":i.categorie,"image":i.image,"twoimage":i.twoimage,"threeimage":i.threeimage,"forimage":i.forimage,"rouge":i.rouge,"blanc":i.blanc,"noir":i.noir,"jaune":i.jaune,"vert":i.vert,"orange":i.orange,"bleu":i.bleu,"rose":i.rose,"marron":i.marron,"violet":i.violet,"gris":i.gris,"quantit":i.xslet,"stat":i.stat,"taille":i.xs}
                    sacze.append(mpezslsm)
                
                if i.xl == 'xl' :
                    mpezslsm = {"nom":i.nom,"id":i.id,"description":i.description,"prix":i.prix,"porceprix":i.porceprix,"porce":i.porce,"categorie":i.categorie,"image":i.image,"twoimage":i.twoimage,"threeimage":i.threeimage,"forimage":i.forimage,"rouge":i.rouge,"blanc":i.blanc,"noir":i.noir,"jaune":i.jaune,"vert":i.vert,"orange":i.orange,"bleu":i.bleu,"rose":i.rose,"marron":i.marron,"violet":i.violet,"gris":i.gris,"quantit":i.xllet,"stat":i.stat,"taille":i.xl}
                    sacze.append(mpezslsm)
                
                if i.xxl == 'xxl' :
                    mpezslsm = {"nom":i.nom,"id":i.id,"description":i.description,"prix":i.prix,"porceprix":i.porceprix,"porce":i.porce,"categorie":i.categorie,"image":i.image,"twoimage":i.twoimage,"threeimage":i.threeimage,"forimage":i.forimage,"rouge":i.rouge,"blanc":i.blanc,"noir":i.noir,"jaune":i.jaune,"vert":i.vert,"orange":i.orange,"bleu":i.bleu,"rose":i.rose,"marron":i.marron,"violet":i.violet,"gris":i.gris,"quantit":i.xxllet,"stat":i.stat,"taille":i.xxl}
                    sacze.append(mpezslsm)
                
                if i.s == 's' :
                    mpezslsm = {"nom":i.nom,"id":i.id,"description":i.description,"prix":i.prix,"porceprix":i.porceprix,"porce":i.porce,"categorie":i.categorie,"image":i.image,"twoimage":i.twoimage,"threeimage":i.threeimage,"forimage":i.forimage,"rouge":i.rouge,"blanc":i.blanc,"noir":i.noir,"jaune":i.jaune,"vert":i.vert,"orange":i.orange,"bleu":i.bleu,"rose":i.rose,"marron":i.marron,"violet":i.violet,"gris":i.gris,"quantit":i.slet,"stat":i.stat,"taille":i.s}
                    sacze.append(mpezslsm)
                
                if i.m == 'm' :
                    mpezslsm = {"nom":i.nom,"id":i.id,"description":i.description,"prix":i.prix,"porceprix":i.porceprix,"porce":i.porce,"categorie":i.categorie,"image":i.image,"twoimage":i.twoimage,"threeimage":i.threeimage,"forimage":i.forimage,"rouge":i.rouge,"blanc":i.blanc,"noir":i.noir,"jaune":i.jaune,"vert":i.vert,"orange":i.orange,"bleu":i.bleu,"rose":i.rose,"marron":i.marron,"violet":i.violet,"gris":i.gris,"quantit":i.mlet,"stat":i.stat,"taille":i.m}
                    sacze.append(mpezslsm)
                

                if i.l == 'l' :
                    mpezslsm = {"nom":i.nom,"id":i.id,"description":i.description,"prix":i.prix,"porceprix":i.porceprix,"porce":i.porce,"categorie":i.categorie,"image":i.image,"twoimage":i.twoimage,"threeimage":i.threeimage,"forimage":i.forimage,"rouge":i.rouge,"blanc":i.blanc,"noir":i.noir,"jaune":i.jaune,"vert":i.vert,"orange":i.orange,"bleu":i.bleu,"rose":i.rose,"marron":i.marron,"violet":i.violet,"gris":i.gris,"quantit":i.llet,"stat":i.stat,"taille":i.l}
                    sacze.append(mpezslsm)
                

        return render_template("listederobe.html",administa=administa,VetementHomme=VetementHomme,VetementFemme=sacze,Montre=Montre,sac=sac,pofil=pofil,bommande=bommande,nombdre=nombdre,nombdre1=nombdre1,compt=compt,compt1=compt1,bommande0=bommande0,bommande1=bommande1,bommande2=bommande2)

    except :
        return render_template("listederobe.html",administa=administa,VetementHomme=VetementHomme,VetementFemme=VetementFemme,Montre=Montre,sac=sac,nombdre=nombdre,compt=compt)
    
@app.route("/montreadosn")
def montreadosn():
    if 'utilisateur_id' in session:
        useru = Profil.query.get(session['utilisateur_id'])
        if useru.satuq == 1 :
            pass
        else:
            return redirect('/')
    else:
        return redirect('/pre/administa')
    try :
        pofil = Profil.query.all()
        compt=0
        nombdre1=0
        nombdre=0
        compt1=0
        compt2=0
        bommande = Commande.query.all()
        bommande0 = []
        bommande1 = []
        bommande2 = []
        for i in bommande:
            if i.status == "En cours":
                compt += int(i.prixtotal)
                bommande0.append(i)
                nombdre = len(bommande0)
            if i.status == "Déja livré":
                compt1 += int(i.prixtotal)
                bommande1.append(i)
            if i.status == "Annulé":
                compt2 += int(i.prixtotal)
                bommande2.append(i)
                nombdre1 = len(bommande2)

        
        VetementHomme = []
        a = Ajouter.query.all()
        for i in a:
            if i.categorie == 'VetementHomme':
                VetementHomme.append(i)
        VetementFemme = []
        a = Ajouter.query.all()
        for i in a:
            if i.categorie == 'VetementFemme':
                VetementFemme.append(i)
        Montre = []
        a = Ajouter.query.all()
        for i in a:
            if i.categorie == 'Montre':
                Montre.append(i)
        sac = []
        a = Ajouter.query.all()
        for i in a:
            if i.categorie == 'chaussure':
                sac.append(i)




        # fig = px.line(x=[1, 2, 3, 4], y=[1, 8, 2, 3], title="Graphique nombre de commannde / Jours")
        # graph_html = fig.to_html(full_html=False)
    
        
        return render_template("montreadosn.html",administa=administa,VetementHomme=VetementHomme,VetementFemme=VetementFemme,Montre=Montre,sac=sac,pofil=pofil,bommande=bommande,nombdre=nombdre,nombdre1=nombdre1,compt=compt,compt1=compt1,bommande0=bommande0,bommande1=bommande1,bommande2=bommande2)

    except :
        return render_template("montreadosn.html",administa=administa,VetementHomme=VetementHomme,VetementFemme=VetementFemme,Montre=Montre,sac=sac,nombdre=nombdre,compt=compt)
    
@app.route("/cahuseadmin")
def cahuseadmin():
    if 'utilisateur_id' in session:
        useru = Profil.query.get(session['utilisateur_id'])
        if useru.satuq == 1 :
            pass
        else:
            return redirect('/')
    else:
        return redirect('/pre/administa')
    try :
        
        compt=0
        nombdre1=0
        nombdre=0
        compt1=0
        compt2=0
        bommande = Commande.query.all()
        bommande0 = []
        bommande1 = []
        bommande2 = []
        for i in bommande:
            if i.status == "En cours":
                compt += int(i.prixtotal)
                bommande0.append(i)
                nombdre = len(bommande0)
            if i.status == "Déja livré":
                compt1 += int(i.prixtotal)
                bommande1.append(i)
            if i.status == "Annulé":
                compt2 += int(i.prixtotal)
                bommande2.append(i)
                nombdre1 = len(bommande2)

        
        VetementHomme = []
        a = Ajouter.query.all()
        for i in a:
            if i.categorie == 'VetementHomme':
                VetementHomme.append(i)
        VetementFemme = []
        a = Ajouter.query.all()
        for i in a:
            if i.categorie == 'VetementFemme':
                VetementFemme.append(i)
        Montre = []
        a = Ajouter.query.all()
        for i in a:
            if i.categorie == 'Montre':
                Montre.append(i)
        sac = []
        sacze = []
        a = Ajouter.query.all()
        for i in a:
            if i.categorie == 'chaussure':
                sac.append(i)

        
        for i in sac :
            if i.tranwite == '38' :
                mpezslsm = {"nom":i.nom,"id":i.id,"description":i.description,"prix":i.prix,"porceprix":i.porceprix,"porce":i.porce,"categorie":i.categorie,"image":i.image,"twoimage":i.twoimage,"threeimage":i.threeimage,"forimage":i.forimage,"rouge":i.rouge,"blanc":i.blanc,"noir":i.noir,"jaune":i.jaune,"vert":i.vert,"orange":i.orange,"bleu":i.bleu,"rose":i.rose,"marron":i.marron,"violet":i.violet,"gris":i.gris,"quantit":i.tranwitelet,"stat":i.stat,"taille":i.tranwite}
                sacze.append(mpezslsm)
            
            if i.tranneuf == '39' :
                mpezslsm = {"nom":i.nom,"id":i.id,"description":i.description,"prix":i.prix,"porceprix":i.porceprix,"porce":i.porce,"categorie":i.categorie,"image":i.image,"twoimage":i.twoimage,"threeimage":i.threeimage,"forimage":i.forimage,"rouge":i.rouge,"blanc":i.blanc,"noir":i.noir,"jaune":i.jaune,"vert":i.vert,"orange":i.orange,"bleu":i.bleu,"rose":i.rose,"marron":i.marron,"violet":i.violet,"gris":i.gris,"quantit":i.tranneuflet,"stat":i.stat,"taille":i.tranneuf}
                sacze.append(mpezslsm)
            
            if i.karente == '40' :
                mpezslsm = {"nom":i.nom,"id":i.id,"description":i.description,"prix":i.prix,"porceprix":i.porceprix,"porce":i.porce,"categorie":i.categorie,"image":i.image,"twoimage":i.twoimage,"threeimage":i.threeimage,"forimage":i.forimage,"rouge":i.rouge,"blanc":i.blanc,"noir":i.noir,"jaune":i.jaune,"vert":i.vert,"orange":i.orange,"bleu":i.bleu,"rose":i.rose,"marron":i.marron,"violet":i.violet,"gris":i.gris,"quantit":i.karentelet,"stat":i.stat,"taille":i.karente}
                sacze.append(mpezslsm)
            
            if i.tranwiteun == '41' :
                mpezslsm = {"nom":i.nom,"id":i.id,"description":i.description,"prix":i.prix,"porceprix":i.porceprix,"porce":i.porce,"categorie":i.categorie,"image":i.image,"twoimage":i.twoimage,"threeimage":i.threeimage,"forimage":i.forimage,"rouge":i.rouge,"blanc":i.blanc,"noir":i.noir,"jaune":i.jaune,"vert":i.vert,"orange":i.orange,"bleu":i.bleu,"rose":i.rose,"marron":i.marron,"violet":i.violet,"gris":i.gris,"quantit":i.tranwiteunlet,"stat":i.stat,"taille":i.tranwiteun}
                sacze.append(mpezslsm)
            
            if i.tranwitedeux == '42' :
                mpezslsm = {"nom":i.nom,"id":i.id,"description":i.description,"prix":i.prix,"porceprix":i.porceprix,"porce":i.porce,"categorie":i.categorie,"image":i.image,"twoimage":i.twoimage,"threeimage":i.threeimage,"forimage":i.forimage,"rouge":i.rouge,"blanc":i.blanc,"noir":i.noir,"jaune":i.jaune,"vert":i.vert,"orange":i.orange,"bleu":i.bleu,"rose":i.rose,"marron":i.marron,"violet":i.violet,"gris":i.gris,"quantit":i.tranwitedeuxlet,"stat":i.stat,"taille":i.tranwitedeux}
                sacze.append(mpezslsm)
            

            if i.tranwitrois == '43' :
                mpezslsm = {"nom":i.nom,"id":i.id,"description":i.description,"prix":i.prix,"porceprix":i.porceprix,"porce":i.porce,"categorie":i.categorie,"image":i.image,"twoimage":i.twoimage,"threeimage":i.threeimage,"forimage":i.forimage,"rouge":i.rouge,"blanc":i.blanc,"noir":i.noir,"jaune":i.jaune,"vert":i.vert,"orange":i.orange,"bleu":i.bleu,"rose":i.rose,"marron":i.marron,"violet":i.violet,"gris":i.gris,"quantit":i.tranwitroislet,"stat":i.stat,"taille":i.tranwitrois}
                sacze.append(mpezslsm)
            
            if i.tranwitekate == '44' :
                mpezslsm = {"nom":i.nom,"id":i.id,"description":i.description,"prix":i.prix,"porceprix":i.porceprix,"porce":i.porce,"categorie":i.categorie,"image":i.image,"twoimage":i.twoimage,"threeimage":i.threeimage,"forimage":i.forimage,"rouge":i.rouge,"blanc":i.blanc,"noir":i.noir,"jaune":i.jaune,"vert":i.vert,"orange":i.orange,"bleu":i.bleu,"rose":i.rose,"marron":i.marron,"violet":i.violet,"gris":i.gris,"quantit":i.tranwitekatelet,"stat":i.stat,"taille":i.tranwitekate}
                sacze.append(mpezslsm)
                
        print("gjhkl",sacze)


        
        
        return render_template("cahuseadmin.html",nombdre=nombdre,nombdre1=nombdre1,compt=compt,compt1=compt1,sacze=sacze)


    except Exception as e:
        # Gestion des erreurs et retour d'un message d'erreur
        return f"Une erreur s'est produite : {e}", 500
    




@app.route("/administa")
def administa():

    if 'utilisateur_id' in session:
        useru = Profil.query.get(session['utilisateur_id'])
        if useru.satuq == 1 :
            pass
        else:
            return redirect('/')
    else:
        return redirect('/pre/administa')
    try :
        pofil = Profil.query.all()
        compt=0
        compt1=0
        nombdre1=0
        nombdre=0
        compt2=0
        bommande = Commande.query.all()
        bommande0 = []
        bommande1 = []
        bommande2 = []
        for i in bommande:
            if i.status == "En cours":
                compt += int(i.prixtotal)
                bommande0.append(i)
                nombdre = len(bommande0)
            if i.status == "Déja livré":
                compt1 += int(i.prixtotal)
                bommande1.append(i)
            if i.status == "Annulé":
                compt2 += int(i.prixtotal)
                bommande2.append(i)
                nombdre1 = len(bommande2)

        
        VetementHomme = []
        a = Ajouter.query.all()
        for i in a:
            if i.categorie == 'VetementHomme':
                VetementHomme.append(i)
        VetementFemme = []
        a = Ajouter.query.all()
        for i in a:
            if i.categorie == 'VetementFemme':
                VetementFemme.append(i)
        Montre = []
        a = Ajouter.query.all()
        for i in a:
            if i.categorie == 'Montre':
                Montre.append(i)
        sac = []
        a = Ajouter.query.all()
        for i in a:
            if i.categorie == 'chaussure':
                sac.append(i)




        # fig = px.line(x=[1, 2, 3, 4], y=[1, 8, 2, 3], title="Graphique nombre de commannde / Jours")
        # graph_html = fig.to_html(full_html=False)
    
        
        return render_template("administa.html",administa=administa,VetementHomme=VetementHomme,VetementFemme=VetementFemme,Montre=Montre,sac=sac,pofil=pofil,bommande=bommande,nombdre=nombdre,nombdre1=nombdre1,compt=compt,compt1=compt1,bommande0=bommande0,bommande1=bommande1,bommande2=bommande2)

    except :
        return render_template("administa.html",administa=administa,VetementHomme=VetementHomme,VetementFemme=VetementFemme,Montre=Montre,sac=sac,nombdre=nombdre,compt=compt)

@app.route("/indisponible")
def indisponible():

    return render_template("indiso.html")


# @app.route("/pacceuil",methods=["POST","GET"])
# def pacceuil():
#     if 'utilisateur_id' in session:
#         useru = Profil.query.get(session['utilisateur_id'])
#         data = request.get_json()
#         print(data)
#         pani = Panieruser(image=data.image,tailed =data.tailed,identifiant=useru.id,produite=data.produite,prixtottal=data.prixtottal,quantiteto=data.quantiteto,xs=data.xs,xsn=data.xsn,s=data.s,sn=data.sn,l=data.l,ln=data.ln,m=data.m,mn=data.mn,xl=data.xl,xln=data.xln,xxl=data.xxl,xxln=data.xxln,tranwite=data.tranwite,tranwiten=data.tranwiten,tranneuf=data.tranneuf,tranneufn=data.tranneufn,karente=data.karente,karenten=data.karenten,tranwiteun=data.tranwiteun,tranwiteunn=data.tranwiteunn,tranwitedeux=data.tranwitedeux,tranwitedeuxn=data.tranwitedeuxn,tranwitrois=data.tranwitrois,tranwitroisn=data.tranwitroisn,tranwitekate=data.tranwitekate,tranwitekaten=data.tranwitekaten)
            
#         db.session.add(pani)
#         db.session.commit()

        
#         return redirect("/")
#     return redirect("/pre")



# CONNEXION {}
@app.route('/pre/<routeure>')
def pree(routeure):
    catefemme = []
    montre = []
    chaussure = []
    tout = Ajouter.query.all()
    commenta = []
    recupe = Comment.query.all()
    
    for i in recupe:
        commenta.append(i)

    for i in tout:
        if i.categorie == "VetementFemme" :
            catefemme.append(i)

        if i.categorie == "Montre" :
            montre.append(i)

        if i.categorie == "chaussure" :
            chaussure.append(i)
    if len(catefemme)>10 :
        catefemme = catefemme[:10]
    if len(montre) >10 :
        montre = montre[:10]
    if len(chaussure) >10 :
        chaussure = chaussure[:10]


    # print(commenta[0].mail)
    
    return render_template("connexion.html",commenta=commenta,catefemme=catefemme,montre=montre,chaussure=chaussure,routeure=routeure)

    # return render_template('connexion.html')







@app.route('/sprome/<routeure>', methods=["GET", "POST"])
def sprome(routeure):
    last_name = request.form.get("last_name")
    age = request.form.get("age")

    recupetou = Profil.query.all()
    for i in recupetou:
        print("lorjf",bcrypt.checkpw(age.encode('utf-8'), i.age))
        print("gfgshd",last_name ,"==", i.last_name)
        if bcrypt.checkpw(age.encode('utf-8'), i.age) and last_name == i.last_name :
        


            if i.satuq == 0 :
        
      
        
                print(f"vous etes connecter{i.first_name}{i.id}")
                

                session['utilisateur_id'] = i.id
            
                return redirect(f"/rediriger/{routeure}")
            elif i.satuq == 1 :


                print(f"vous etes connecter{i.first_name}{i.id}")
                

                session['utilisateur_id'] = i.id
                
                return redirect(f"/administa")
            elif i.satuq == 2 :

                flash("Compte suspendu")
                return redirect(f"/pre/{routeure}")
            else :

                flash("Email ou Mot de passe invalide")
                return redirect(f"/pre/{routeure}")

    return redirect(f"/pre/{routeure}")



    # user = Profil.query.filter_by(last_name = request.form.get("last_name"),age = request.form.get("age"),satuq=0).first()
    # admos = Profil.query.filter_by(last_name = request.form.get("last_name"),age = request.form.get("age"),satuq=1).first()
    # suspen = Profil.query.filter_by(last_name = request.form.get("last_name"),age = request.form.get("age"),satuq=2).first()

    # if user :
        
      
        
    #     print(f"vous etes connecter{user.first_name}{user.id}")
        

    #     session['utilisateur_id'] = user.id
    
    #     return redirect(f"/rediriger/{routeure}")
    # elif admos :


    #     print(f"vous etes connecter{admos.first_name}{admos.id}")
        

    #     session['utilisateur_id'] = admos.id
        
    #     return redirect(f"/administa")
    # elif suspen :

    #     flash("Compte suspendu")
    #     return redirect(f"/pre/{routeure}")
    # else :

    #     flash("Email ou Mot de passe invalide")
    #     return redirect(f"/pre/{routeure}")
    



    
    
@app.route('/dedyiez',methods = ["GET","POST"])
def dedyiez() :
    routeure = request.form.get("routeure")
    return redirect(f"/{routeure}")
    
    


# @app.route('/song',methods = ["GET","POST"])
# def song() :
   
#     return {"nom": "cabri","prenom":"mamoud"}


# FIN CONNEXION {}


@app.route("/deconn")
def deconn():
    if 'utilisateur_id' in session:
       
        session.pop('utilisateur_id', None)
        return redirect("/pre/deconn")
    return redirect("/")

@app.route("/rediriger/<routeure>")
def rediriger(routeure):
 
    return render_template("rediriger.html",routeure=routeure)
@app.route("/redsete", methods=["POST"])
def redsete():
    data = request.get_json()['data']
    print("voivi les ",data)
    
    if 'utilisateur_id' in session:
        useru = Profil.query.get(session['utilisateur_id'])
        print("je suis llllllll")
        for i in data:
            
            b = i["data"]
            mskd = Ajouter.query.get(int(b['produite']))
            if mskd :
                if b['categorie'] == "Montre" :
                    mskd = Ajouter.query.get(int(b['produite']))
                    
                    mskde = int(mskd.quantit)
                    print("dfghjk", mskde ,">=" ,int(b['quantiteto']))
                    if mskde >= int(b['quantiteto']) :
                        pani = Panieruser(
                                image=b['image'],
                                tailed="",
                                identifiant=useru.id,
                                produite= int(b['produite']),
                                prixtottal= int(b['porceprix']),
                                quantiteto= int(b['quantiteto']),
                                xs=b['xs'],
                                xsn=b['xsn'],
                                s=b['s'],
                                sn=b['sn'],
                                l=b['l'],
                                ln=b['ln'],
                                m=b['m'],
                                mn=b['mn'],
                                xl=b['xl'],
                                xln=b['xln'],
                                xxl=b['xxl'],
                                xxln=b['xxln'],
                                tranwite=b['tranwite'],
                                tranwiten=b['tranwiten'],
                                tranneuf=b['tranneuf'],
                                tranneufn=b['tranneufn'],
                                karente=b['karente'],
                                karenten=b['karenten'],
                                tranwiteun=b['tranwiteun'],
                                tranwiteunn=b['tranwiteunn'],
                                tranwitedeux=b['tranwitedeux'],
                                tranwitedeuxn=b['tranwitedeuxn'],
                                tranwitrois=b['tranwitrois'],
                                tranwitroisn=b['tranwitroisn'],
                                tranwitekate=b['tranwitekate'],
                                tranwitekaten=b['tranwitekaten'],


                                prixdepouce = int(b['prixtottal']),
                                nomprodui = b['name'],
                                descrprosui = b['desccopte'],
                                pourcentage = b['porce'],
                                categorie = b['categorie'],
                                dispono = mskde,
                                statuse = "dispobine",


                            
                            )
                    else :

                        pani = Panieruser(
                        image=b['image'],
                        tailed="",
                        identifiant=useru.id,
                        produite= int(b['produite']),
                        prixtottal= int(b['porceprix']),
                        quantiteto= int(b['quantiteto']),
                        xs=b['xs'],
                        xsn=b['xsn'],
                        s=b['s'],
                        sn=b['sn'],
                        l=b['l'],
                        ln=b['ln'],
                        m=b['m'],
                        mn=b['mn'],
                        xl=b['xl'],
                        xln=b['xln'],
                        xxl=b['xxl'],
                        xxln=b['xxln'],
                        tranwite=b['tranwite'],
                        tranwiten=b['tranwiten'],
                        tranneuf=b['tranneuf'],
                        tranneufn=b['tranneufn'],
                        karente=b['karente'],
                        karenten=b['karenten'],
                        tranwiteun=b['tranwiteun'],
                        tranwiteunn=b['tranwiteunn'],
                        tranwitedeux=b['tranwitedeux'],
                        tranwitedeuxn=b['tranwitedeuxn'],
                        tranwitrois=b['tranwitrois'],
                        tranwitroisn=b['tranwitroisn'],
                        tranwitekate=b['tranwitekate'],
                        tranwitekaten=b['tranwitekaten'],


                        prixdepouce = int(b['prixtottal']),
                        nomprodui = b['name'],
                        descrprosui = b['desccopte'],
                        pourcentage = b['porce'],
                        categorie = b['categorie'],
                        dispono = mskde,
                        statuse = "nondisp",


                        
                        )

                else :
                    mskd = Ajouter.query.get(int(b['produite']))
                

                    if b['tailed'] == "m" :
                        mskde = int(mskd.mlet)
                        print("m ->",mskde)

                    elif b['tailed'] == "s" :
                        mskde = int(mskd.slet)

                        print("s ->",mskde)

                    elif b['tailed'] == "l" :
                        mskde = int(mskd.llet)

                        print("l ->",mskde)

                    elif b['tailed'] == "xl" :
                        mskde = int(mskd.xllet)

                        print("xl ->",mskde)

                    elif b['tailed'] == "xxl" :
                        mskde = int(mskd.xxllet)

                        print("xxl ->",mskde)

                    elif b['tailed'] == "xs" :
                        mskde = int(mskd.xslet)

                        print("xs ->",mskde)

                    elif b['tailed'] == "38 ° " :
                        mskde = int(mskd.tranwitelet)
                        print("38 ->",mskde)
                    elif b['tailed'] == "39 ° " :
                        mskde = int(mskd.tranneuflet)
                        print("39 ->",mskde)
                    elif b['tailed'] == "40 ° " :
                        mskde = int(mskd.karentelet)
                        print("40 ->",mskde)
                    elif b['tailed'] == "41 ° " :
                        mskde = int(mskd.tranwiteunlet)
                        print("41 ->",mskde)
                    elif b['tailed'] == "42 ° " :
                        mskde = int(mskd.tranwitedeuxlet)
                        print("42 ->",mskde)
                    elif b['tailed'] == "43 ° " :
                        mskde = int(mskd.tranwitroislet)
                        print("43 ->",mskde)
                    elif b['tailed'] == "44 ° " :
                        mskde = int(mskd.tranwitekatelet)
                        print("44 ->",mskde)

                    else :
                        print("fin")


                
                    if mskde >= int(b['quantiteto']) :
                        pani = Panieruser(
                            image=b['image'],
                            tailed=b['tailed'],
                            identifiant=useru.id,
                            produite=b['produite'],
                            prixtottal=b['porceprix'],
                            quantiteto=b['quantiteto'],
                            xs=b['xs'],
                            xsn=b['xsn'],
                            s=b['s'],
                            sn=b['sn'],
                            l=b['l'],
                            ln=b['ln'],
                            m=b['m'],
                            mn=b['mn'],
                            xl=b['xl'],
                            xln=b['xln'],
                            xxl=b['xxl'],
                            xxln=b['xxln'],
                            tranwite=b['tranwite'],
                            tranwiten=b['tranwiten'],
                            tranneuf=b['tranneuf'],
                            tranneufn=b['tranneufn'],
                            karente=b['karente'],
                            karenten=b['karenten'],
                            tranwiteun=b['tranwiteun'],
                            tranwiteunn=b['tranwiteunn'],
                            tranwitedeux=b['tranwitedeux'],
                            tranwitedeuxn=b['tranwitedeuxn'],
                            tranwitrois=b['tranwitrois'],
                            tranwitroisn=b['tranwitroisn'],
                            tranwitekate=b['tranwitekate'],
                            tranwitekaten=b['tranwitekaten'],


                            prixdepouce = b['prixtottal'],
                            nomprodui = b['name'],
                            descrprosui = b['desccopte'],
                            pourcentage = b['porce'],
                            categorie = b['categorie'],
                            dispono = mskde,
                            statuse = "dispobine",


                        
                        )
                    else :
                        pani = Panieruser(
                            image=b['image'],
                            tailed=b['tailed'],
                            identifiant=useru.id,
                            produite=b['produite'],
                            prixtottal=b['porceprix'],
                            quantiteto=b['quantiteto'],
                            xs=b['xs'],
                            xsn=b['xsn'],
                            s=b['s'],
                            sn=b['sn'],
                            l=b['l'],
                            ln=b['ln'],
                            m=b['m'],
                            mn=b['mn'],
                            xl=b['xl'],
                            xln=b['xln'],
                            xxl=b['xxl'],
                            xxln=b['xxln'],
                            tranwite=b['tranwite'],
                            tranwiten=b['tranwiten'],
                            tranneuf=b['tranneuf'],
                            tranneufn=b['tranneufn'],
                            karente=b['karente'],
                            karenten=b['karenten'],
                            tranwiteun=b['tranwiteun'],
                            tranwiteunn=b['tranwiteunn'],
                            tranwitedeux=b['tranwitedeux'],
                            tranwitedeuxn=b['tranwitedeuxn'],
                            tranwitrois=b['tranwitrois'],
                            tranwitroisn=b['tranwitroisn'],
                            tranwitekate=b['tranwitekate'],
                            tranwitekaten=b['tranwitekaten'],


                            prixdepouce = b['prixtottal'],
                            nomprodui = b['name'],
                            descrprosui = b['desccopte'],
                            pourcentage = b['porce'],
                            categorie = b['categorie'],
                            dispono = mskde,
                            statuse = "nondisp",


                        
                        )



                derst = Panieruser.query.all()
                crte = 0
                for p in derst :
                
                    if int(p.produite) == int(b['produite']) and int(p.identifiant)==int(useru.id) and p.tailed == b['tailed'] and b['categorie'] != "Montre":

                        print("fghger",int(p.produite),"==",int(b['produite']))
                        print("hger",int(p.identifiant),"==",int(int(useru.id)))

                        crte +=1
                        dhher = Panieruser.query.get(int(p.id))

                        if (int(dhher.quantiteto) + int(b['quantiteto']) )<= int(p.dispono):
                            dhher.quantiteto = int(dhher.quantiteto) + int(b['quantiteto'])
                            db.session.commit()
                        continue

                    if b['categorie'] == "Montre" :

                        print("Montre",int(p.produite),"==",int(b['produite']))
                        print("hger",int(p.identifiant),"==",int(int(useru.id)))

                       
                        

                        if int(p.identifiant) == int(useru.id) and int(p.produite) == int(b['produite']):
                            print("cvbn,;:")
                            crte +=1
                            mpsxd = int(p.id)
                            dhher = Panieruser.query.get(mpsxd)
                            if (int(dhher.quantiteto) + int(b['quantiteto']) ) <= int(dhher.dispono):
                                print("mpskjdkd")
                                
                                dhher.quantiteto = int(dhher.quantiteto) + int(b['quantiteto'])
                                db.session.commit()

                            


                if crte == 0 :
                    print("on passe")
                    
                    db.session.add(pani)
                    db.session.commit()
                    continue
            
    return {"message":"enregistrement reussi"}





@app.route("/pacceuil", methods=["POST"])
def pacceuil():
    print("je suis la 2")
    if 'utilisateur_id' in session:
        useru = Profil.query.get(session['utilisateur_id'])
        print("je suis la 1")
        # if request.method == 'POST':
        #     data = request.get_json()['data']
        #     for i in data:
        #         pani = Panieruser(
        #             image=data['image'],
        #             tailed=data['tailed'],
        #             identifiant=useru.id,
        #             produite=data['produite'],
        #             prixtottal=data['prixtottal'],
        #             quantiteto=data['quantiteto'],
        #             xs=data['xs'],
        #             xsn=data['xsn'],
        #             s=data['s'],
        #             sn=data['sn'],
        #             l=data['l'],
        #             ln=data['ln'],
        #             m=data['m'],
        #             mn=data['mn'],
        #             xl=data['xl'],
        #             xln=data['xln'],
        #             xxl=data['xxl'],
        #             xxln=data['xxln'],
        #             tranwite=data['tranwite'],
        #             tranwiten=data['tranwiten'],
        #             tranneuf=data['tranneuf'],
        #             tranneufn=data['tranneufn'],
        #             karente=data['karente'],
        #             karenten=data['karenten'],
        #             tranwiteun=data['tranwiteun'],
        #             tranwiteunn=data['tranwiteunn'],
        #             tranwitedeux=data['tranwitedeux'],
        #             tranwitedeuxn=data['tranwitedeuxn'],
        #             tranwitrois=data['tranwitrois'],
        #             tranwitroisn=data['tranwitroisn'],
        #             tranwitekate=data['tranwitekate'],
        #             tranwitekaten=data['tranwitekaten']
        #         )
        #         db.session.add(pani)
        #         db.session.commit()
        #     return jsonify({'status': 'success'}), 200
            
        return redirect("/")
    return redirect("/pre/acceuilconnect")

@app.route("/")
def acceuil():
    
   
    
    catefemme = []
    montre = []
    chaussure = []
    tout = Ajouter.query.all()
    commenta = []
    recupe = Comment.query.all()
    
    for i in recupe:
        commenta.append(i)

    for i in tout:
        if i.categorie == "VetementFemme" :
            catefemme.append(i)

        if i.categorie == "Montre" :
            montre.append(i)

        if i.categorie == "chaussure" :
            chaussure.append(i)
    if len(catefemme)>10 :
        catefemme = catefemme[:10]
    if len(montre) >10 :
        montre = montre[:10]
    if len(chaussure) >10 :
        chaussure = chaussure[:10]

    if len(commenta) > 1:
        print(commenta[0].mail)
    
    return render_template("acceuil.html",commenta=commenta,catefemme=catefemme,montre=montre,chaussure=chaussure)
@app.route("/acceuilconnect")
def acceuilconnect():
    
   
    
    catefemme = []
    montre = []
    chaussure = []
    tout = Ajouter.query.all()
    commenta = []
    recupe = Comment.query.all()
    
    for i in recupe:
        commenta.append(i)

    for i in tout:
        if i.categorie == "VetementFemme" :
            catefemme.append(i)

        if i.categorie == "Montre" :
            montre.append(i)

        if i.categorie == "chaussure" :
            chaussure.append(i)
    if len(catefemme)>10 :
        catefemme = catefemme[:10]
    if len(montre) >10 :
        montre = montre[:10]
    if len(chaussure) >10 :
        chaussure = chaussure[:10]


    if len(commenta) > 1:
        print(commenta[0].mail)
    
    return render_template("acceuil.html",commenta=commenta,catefemme=catefemme,montre=montre,chaussure=chaussure)


@app.route("/completplus/<int:id>", methods = ["GET","POST"])
def completplus(id):
    
    catego = request.form.get("catego","montre")

    if catego == "chaussure" :
        pontut = {"38":"adm.tranwitelet","39":"adm.tranneuflet","40":"adm.karentelet","41":"adm.tranwiteunlet","42":"adm.tranwitedeuxlet","43":"adm.tranwitroislet","44":"adm.tranwitekatelet"}
        taille = request.form.get("taille")
        losjjs = request.form.get("losjjs")

        
        if taille == "38" :
            adm = Ajouter.query.get(id)
            adm.tranwitelet = int(adm.tranwitelet) + 1
            adm.quantit = int(adm.quantit) + 1
            adm.stat = "vrai"
            db.session.commit()


            monkzu = Panieruser.query.all()
            for imo in monkzu :
                if int(imo.produite) == id :
                    sfymp = int(imo.dispono) + 1
                    if sfymp < int(imo.quantiteto)   :
                        imo.dispono = int(imo.dispono) + 1
                        imo.statuse = "nondisp"
                        print(sfymp , ">=" , int(imo.quantiteto))

                    else : 
                        print(sfymp , "<" , int(imo.quantiteto))
                        imo.dispono = int(imo.dispono) + 1
                        imo.statuse = "dispobine"
                    db.session.commit()

        if taille == "39" :
            adm = Ajouter.query.get(id)
            adm.tranneuflet = int(adm.tranneuflet) + 1
            adm.quantit = int(adm.quantit) + 1
            adm.stat = "vrai"
            db.session.commit()


            monkzu = Panieruser.query.all()
            for imo in monkzu :
                if int(imo.produite) == id :
                    sfymp = int(imo.dispono) + 1
                    if sfymp < int(imo.quantiteto)   :
                        imo.dispono = int(imo.dispono) + 1
                        imo.statuse = "nondisp"
                        print(sfymp , ">=" , int(imo.quantiteto))

                    else : 
                        print(sfymp , "<" , int(imo.quantiteto))
                        imo.dispono = int(imo.dispono) + 1
                        imo.statuse = "dispobine"
                    db.session.commit()

        if taille == "40" :
            adm = Ajouter.query.get(id)
            adm.karentelet = int(adm.karentelet) + 1
            adm.quantit = int(adm.quantit) + 1
            adm.stat = "vrai"
            db.session.commit()


            monkzu = Panieruser.query.all()
            for imo in monkzu :
                if int(imo.produite) == id :
                    sfymp = int(imo.dispono) + 1
                    if sfymp < int(imo.quantiteto)   :
                        imo.dispono = int(imo.dispono) + 1
                        imo.statuse = "nondisp"
                        print(sfymp , ">=" , int(imo.quantiteto))

                    else : 
                        print(sfymp , "<" , int(imo.quantiteto))
                        imo.dispono = int(imo.dispono) + 1
                        imo.statuse = "dispobine"
                    db.session.commit()

        if taille == "41" :
            adm = Ajouter.query.get(id)
            adm.tranwiteunlet = int(adm.tranwiteunlet) + 1
            adm.quantit = int(adm.quantit) + 1
            adm.stat = "vrai"
            db.session.commit()


            monkzu = Panieruser.query.all()
            for imo in monkzu :
                if int(imo.produite) == id :
                    sfymp = int(imo.dispono) + 1
                    if sfymp < int(imo.quantiteto)   :
                        imo.dispono = int(imo.dispono) + 1
                        imo.statuse = "nondisp"
                        print(sfymp , ">=" , int(imo.quantiteto))

                    else : 
                        print(sfymp , "<" , int(imo.quantiteto))
                        imo.dispono = int(imo.dispono) + 1
                        imo.statuse = "dispobine"
                    db.session.commit()

        if taille == "42" :
            adm = Ajouter.query.get(id)
            adm.tranwitedeuxlet = int(adm.tranwitedeuxlet) + 1
            adm.quantit = int(adm.quantit) + 1
            adm.stat = "vrai"
            db.session.commit()


            monkzu = Panieruser.query.all()
            for imo in monkzu :
                if int(imo.produite) == id :
                    sfymp = int(imo.dispono) + 1
                    if sfymp < int(imo.quantiteto)   :
                        imo.dispono = int(imo.dispono) + 1
                        imo.statuse = "nondisp"
                        print(sfymp , ">=" , int(imo.quantiteto))

                    else : 
                        print(sfymp , "<" , int(imo.quantiteto))
                        imo.dispono = int(imo.dispono) + 1
                        imo.statuse = "dispobine"
                    db.session.commit()

        if taille == "43" :
            adm = Ajouter.query.get(id)
            adm.tranwitroislet = int(adm.tranwitroislet) + 1
            adm.quantit = int(adm.quantit) + 1
            adm.stat = "vrai"
            db.session.commit()


            monkzu = Panieruser.query.all()
            for imo in monkzu :
                if int(imo.produite) == id :
                    sfymp = int(imo.dispono) + 1
                    if sfymp < int(imo.quantiteto)   :
                        imo.dispono = int(imo.dispono) + 1
                        imo.statuse = "nondisp"
                        print(sfymp , ">=" , int(imo.quantiteto))

                    else : 
                        print(sfymp , "<" , int(imo.quantiteto))
                        imo.dispono = int(imo.dispono) + 1
                        imo.statuse = "dispobine"
                    db.session.commit()

        if taille == "44" :
            adm = Ajouter.query.get(id)
            adm.tranwitekatelet = int(adm.tranwitekatelet) + 1
            adm.quantit = int(adm.quantit) + 1
            adm.stat = "vrai"
            db.session.commit()


            monkzu = Panieruser.query.all()
            for imo in monkzu :
                if int(imo.produite) == id :
                    sfymp = int(imo.dispono) + 1
                    if sfymp < int(imo.quantiteto)   :
                        imo.dispono = int(imo.dispono) + 1
                        imo.statuse = "nondisp"
                        print(sfymp , ">=" , int(imo.quantiteto))

                    else : 
                        print(sfymp , "<" , int(imo.quantiteto))
                        imo.dispono = int(imo.dispono) + 1
                        imo.statuse = "dispobine"
                    db.session.commit()


      

        

        return redirect(f'/{losjjs}')
    


    if catego == "VetementFemme" :
        pontut = {"38":"adm.tranwitelet","39":"adm.tranneuflet","40":"adm.karentelet","41":"adm.tranwiteunlet","42":"adm.tranwitedeuxlet","43":"adm.tranwitroislet","44":"adm.tranwitekatelet"}
        taille = request.form.get("taille")
        losjjs = request.form.get("losjjs")

        
        if taille == "xs" :
            adm = Ajouter.query.get(id)
            adm.xslet = int(adm.xslet) + 1
            adm.quantit = int(adm.quantit) + 1
            adm.stat = "vrai"
            db.session.commit()

            monkzu = Panieruser.query.all()
            for imo in monkzu :
                if int(imo.produite) == id :
                    sfymp = int(imo.dispono) + 1
                    if sfymp < int(imo.quantiteto)   :
                        imo.dispono = int(imo.dispono) + 1
                        imo.statuse = "nondisp"
                        print(sfymp , ">=" , int(imo.quantiteto))

                    else : 
                        print(sfymp , "<" , int(imo.quantiteto))
                        imo.dispono = int(imo.dispono) + 1
                        imo.statuse = "dispobine"
                    db.session.commit()

        if taille == "xl" :
            adm = Ajouter.query.get(id)
            adm.xllet = int(adm.xllet) + 1
            adm.quantit = int(adm.quantit) + 1
            adm.stat = "vrai"
            db.session.commit()

            monkzu = Panieruser.query.all()
            for imo in monkzu :
                if int(imo.produite) == id :
                    sfymp = int(imo.dispono) + 1
                    if sfymp < int(imo.quantiteto)   :
                        imo.dispono = int(imo.dispono) + 1
                        imo.statuse = "nondisp"
                        print(sfymp , ">=" , int(imo.quantiteto))

                    else : 
                        print(sfymp , "<" , int(imo.quantiteto))
                        imo.dispono = int(imo.dispono) + 1
                        imo.statuse = "dispobine"
                    db.session.commit()

        if taille == "xxl" :
            adm = Ajouter.query.get(id)
            adm.xxllet = int(adm.xxllet) + 1
            adm.quantit = int(adm.quantit) + 1
            adm.stat = "vrai"
            db.session.commit()

            monkzu = Panieruser.query.all()
            for imo in monkzu :
                if int(imo.produite) == id :
                    sfymp = int(imo.dispono) + 1
                    if sfymp < int(imo.quantiteto)   :
                        imo.dispono = int(imo.dispono) + 1
                        imo.statuse = "nondisp"
                        print(sfymp , ">=" , int(imo.quantiteto))

                    else : 
                        print(sfymp , "<" , int(imo.quantiteto))
                        imo.dispono = int(imo.dispono) + 1
                        imo.statuse = "dispobine"
                    db.session.commit()

        if taille == "m" :
            adm = Ajouter.query.get(id)
            adm.mlet = int(adm.mlet) + 1
            adm.quantit = int(adm.quantit) + 1
            adm.stat = "vrai"
            db.session.commit()



            monkzu = Panieruser.query.all()
            for imo in monkzu :
                if int(imo.produite) == id :
                    sfymp = int(imo.dispono) + 1
                    if sfymp < int(imo.quantiteto)   :
                        imo.dispono = int(imo.dispono) + 1
                        imo.statuse = "nondisp"
                        print(sfymp , ">=" , int(imo.quantiteto))

                    else : 
                        print(sfymp , "<" , int(imo.quantiteto))
                        imo.dispono = int(imo.dispono) + 1
                        imo.statuse = "dispobine"
                    db.session.commit()

        if taille == "s" :
            adm = Ajouter.query.get(id)
            adm.slet = int(adm.slet) + 1
            adm.quantit = int(adm.quantit) + 1
            adm.stat = "vrai"
            db.session.commit()

            monkzu = Panieruser.query.all()
            for imo in monkzu :
                if int(imo.produite) == id :
                    sfymp = int(imo.dispono) + 1
                    if sfymp < int(imo.quantiteto)   :
                        imo.dispono = int(imo.dispono) + 1
                        imo.statuse = "nondisp"
                        print(sfymp , ">=" , int(imo.quantiteto))

                    else : 
                        print(sfymp , "<" , int(imo.quantiteto))
                        imo.dispono = int(imo.dispono) + 1
                        imo.statuse = "dispobine"
                    db.session.commit()

        if taille == "l" :
            adm = Ajouter.query.get(id)
            adm.llet = int(adm.llet) + 1
            adm.quantit = int(adm.quantit) + 1
            adm.stat = "vrai"
            db.session.commit()

            monkzu = Panieruser.query.all()
            for imo in monkzu :
                if int(imo.produite) == id :
                    sfymp = int(imo.dispono) + 1
                    if sfymp < int(imo.quantiteto)   :
                        imo.dispono = int(imo.dispono) + 1
                        imo.statuse = "nondisp"
                        print(sfymp , ">=" , int(imo.quantiteto))

                    else : 
                        print(sfymp , "<" , int(imo.quantiteto))
                        imo.dispono = int(imo.dispono) + 1
                        imo.statuse = "dispobine"
                    db.session.commit()




        return redirect(f'/{losjjs}')
    # if catego == "VetementFemme" :
    #     pontut = {"xs":"adm.xslet","s":"adm.slet","m":"adm.mlet","l":"adm.llet","xl":"adm.xllet","xxl":"adm.xxllet"}
    #     catego = request.form.get("catego")
        
        
    #     adm = Ajouter.query.get(id)
    #     adm.quantit = int(adm.quantit) + 1
    #     adm.stat = "vrai"
    #     db.session.commit()
    if catego == "montre" :
        losjjs = request.form.get("losjjs")
        adm = Ajouter.query.get(id)
        adm.quantit = int(adm.quantit) + 1
        adm.stat = "vrai"
        db.session.commit()
        
    

        monkzu = Panieruser.query.all()
        for imo in monkzu :
            if int(imo.produite) == id :
                sfymp = int(imo.dispono) + 1
                if sfymp < int(imo.quantiteto)   :
                    imo.dispono = int(imo.dispono) + 1
                    imo.statuse = "nondisp"
                    print(sfymp , ">=" , int(imo.quantiteto))

                else : 
                    print(sfymp , "<" , int(imo.quantiteto))
                    imo.dispono = int(imo.dispono) + 1
                    imo.statuse = "dispobine"
                db.session.commit()

        return redirect(f'/{losjjs}')

    
    # stat
    return redirect("/commadeadmin")
    
  
@app.route("/fairemoins/<int:id>", methods = ["GET","POST"])
def fairemoins(id):
    try :
        catego = request.form.get("categom")
        print("la catego ", catego , "==" , "VetementFemme")

        if catego == "chaussure" :
            taille = request.form.get("taillem")
            losjjs = request.form.get("losjjsm")
            adm = Ajouter.query.get(id)
            if taille == "38" :
                print("la taille ", taille , "==" , "xs")
                if int(adm.tranwitelet) > 0 :
                    print("int(adm.tranwitelet)", int(adm.tranwitelet) , ">" , 0)
                    if int(adm.quantit) == 1 :

                        adm.stat = "faux"
                        adm.tranwitelet = int(adm.tranwitelet) - 1
                        adm.quantit = int(adm.quantit) - 1
                        db.session.commit()
                        monkzu = Panieruser.query.all()
                        print("on a recu")
                        for imo in monkzu :
                            if int(imo.produite) == id :
                                sfymp = int(imo.dispono) - 1
                                if sfymp >= int(imo.quantiteto)   :
                                    imo.dispono = int(imo.dispono) - 1
                                    imo.statuse = "dispobine"
                                    print(sfymp , ">=" , int(imo.quantiteto))
                                    print("terlin")
                                else : 
                                    print(sfymp , "<" , int(imo.quantiteto))
                                    imo.dispono = int(imo.dispono) - 1
                                    imo.statuse = "nondisp"
                                    print("pas terlin")
                                db.session.commit()
                        return redirect(f'/{losjjs}')
                    if int(adm.quantit) == 0 :
                        adm.stat = "faux"
                        
                        db.session.commit()
                        return redirect(f'/{losjjs}')

                    adm.tranwitelet = int(adm.tranwitelet) - 1
                    adm.quantit = int(adm.quantit) - 1
                    db.session.commit()



                    monkzu = Panieruser.query.all()
                    for imo in monkzu :
                        if int(imo.produite) == id :
                            sfymp = int(imo.dispono) - 1
                            if sfymp >= int(imo.quantiteto)   :
                                imo.dispono = int(imo.dispono) - 1
                                print(sfymp , ">=" , int(imo.quantiteto))
                                imo.statuse = "dispobine"
                            else : 
                                print(sfymp , "<" , int(imo.quantiteto))
                                imo.dispono = int(imo.dispono) - 1
                                imo.statuse = "nondisp"
                            db.session.commit()
                            


                            

                if int(adm.tranwitelet) == 0 :
                    pass

            if taille == "39" :
                if int(adm.tranneuflet) > 0 :
                    print("int(adm.tranneuflet)", int(adm.tranneuflet) , ">" , 0)
                    if int(adm.quantit) == 1 :

                        adm.stat = "faux"
                        adm.tranneuflet = int(adm.tranneuflet) - 1
                        adm.quantit = int(adm.quantit) - 1
                        db.session.commit()
                        monkzu = Panieruser.query.all()
                        print("on a recu")
                        for imo in monkzu :
                            if int(imo.produite) == id :
                                sfymp = int(imo.dispono) - 1
                                if sfymp >= int(imo.quantiteto)   :
                                    imo.dispono = int(imo.dispono) - 1
                                    imo.statuse = "dispobine"
                                    print(sfymp , ">=" , int(imo.quantiteto))
                                    print("terlin")
                                else : 
                                    print(sfymp , "<" , int(imo.quantiteto))
                                    imo.dispono = int(imo.dispono) - 1
                                    imo.statuse = "nondisp"
                                    print("pas terlin")
                                db.session.commit()
                        return redirect(f'/{losjjs}')
                    if int(adm.quantit) == 0 :
                        adm.stat = "faux"
                        
                        db.session.commit()
                        return redirect(f'/{losjjs}')

                    adm.tranneuflet = int(adm.tranneuflet) - 1
                    adm.quantit = int(adm.quantit) - 1
                    db.session.commit()

                    monkzu = Panieruser.query.all()
                    for imo in monkzu :
                        if int(imo.produite) == id :
                            sfymp = int(imo.dispono) - 1
                            if sfymp >= int(imo.quantiteto)   :
                                imo.dispono = int(imo.dispono) - 1
                                imo.statuse = "dispobine"
                                print(sfymp , ">=" , int(imo.quantiteto))
                            else : 
                                print(sfymp , "<" , int(imo.quantiteto))
                                imo.dispono = int(imo.dispono) - 1
                                imo.statuse = "nondisp"
                            db.session.commit()
                            

                if int(adm.tranneuflet) == 0 :
                    pass

            if taille == "40" :
                if int(adm.karentelet) > 0 :
                    print("int(adm.karentelet)", int(adm.karentelet) , ">" , 0)
                    if int(adm.quantit) == 1 :

                        adm.stat = "faux"
                        adm.karentelet = int(adm.karentelet) - 1
                        adm.quantit = int(adm.quantit) - 1
                        db.session.commit()
                        monkzu = Panieruser.query.all()
                        print("on a recu")
                        for imo in monkzu :
                            if int(imo.produite) == id :
                                sfymp = int(imo.dispono) - 1
                                if sfymp >= int(imo.quantiteto)   :
                                    imo.dispono = int(imo.dispono) - 1
                                    imo.statuse = "dispobine"
                                    print(sfymp , ">=" , int(imo.quantiteto))
                                    print("terlin")
                                else : 
                                    print(sfymp , "<" , int(imo.quantiteto))
                                    imo.dispono = int(imo.dispono) - 1
                                    imo.statuse = "nondisp"
                                    print("pas terlin")
                                db.session.commit()
                        return redirect(f'/{losjjs}')
                    if int(adm.quantit) == 0 :
                        adm.stat = "faux"
                        
                        db.session.commit()
                        return redirect(f'/{losjjs}')

                    adm.karentelet = int(adm.karentelet) - 1
                    adm.quantit = int(adm.quantit) - 1
                    db.session.commit()



                    monkzu = Panieruser.query.all()
                    for imo in monkzu :
                        if int(imo.produite) == id :
                            sfymp = int(imo.dispono) - 1
                            if sfymp >= int(imo.quantiteto)   :
                                imo.dispono = int(imo.dispono) - 1
                                imo.statuse = "dispobine"
                                print(sfymp , ">=" , int(imo.quantiteto))

                            else : 
                                print(sfymp , "<" , int(imo.quantiteto))
                                imo.dispono = int(imo.dispono) - 1
                                imo.statuse = "nondisp"
                            db.session.commit()
                            

                if int(adm.karentelet) == 0 :
                    pass

            if taille == "41" :
                if int(adm.tranwiteunlet) > 0 :
                    print("int(adm.tranwiteunlet)", int(adm.tranwiteunlet) , ">" , 0)
                    if int(adm.quantit) == 1 :

                        adm.stat = "faux"
                        adm.tranwiteunlet = int(adm.tranwiteunlet) - 1
                        adm.quantit = int(adm.quantit) - 1
                        db.session.commit()
                        monkzu = Panieruser.query.all()
                        print("on a recu")
                        for imo in monkzu :
                            if int(imo.produite) == id :
                                sfymp = int(imo.dispono) - 1
                                if sfymp >= int(imo.quantiteto)   :
                                    imo.dispono = int(imo.dispono) - 1
                                    imo.statuse = "dispobine"
                                    print(sfymp , ">=" , int(imo.quantiteto))
                                    print("terlin")
                                else : 
                                    print(sfymp , "<" , int(imo.quantiteto))
                                    imo.dispono = int(imo.dispono) - 1
                                    imo.statuse = "nondisp"
                                    print("pas terlin")
                                db.session.commit()
                        return redirect(f'/{losjjs}')
                    if int(adm.quantit) == 0 :
                        adm.stat = "faux"
                        
                        db.session.commit()
                        return redirect(f'/{losjjs}')

                    adm.tranwiteunlet = int(adm.tranwiteunlet) - 1
                    adm.quantit = int(adm.quantit) - 1
                    db.session.commit()



                    monkzu = Panieruser.query.all()
                    for imo in monkzu :
                        if int(imo.produite) == id :
                            sfymp = int(imo.dispono) - 1
                            if sfymp >= int(imo.quantiteto)   :
                                imo.dispono = int(imo.dispono) - 1
                                imo.statuse = "dispobine"
                                print(sfymp , ">=" , int(imo.quantiteto))
                            else : 
                                print(sfymp , "<" , int(imo.quantiteto))
                                imo.dispono = int(imo.dispono) - 1
                                imo.statuse = "nondisp"
                            db.session.commit()
                            

                if int(adm.tranwiteunlet) == 0 :
                    pass

            if taille == "42" :
                if int(adm.tranwitedeuxlet) > 0 :
                    print("int(adm.tranwitedeuxlet)", int(adm.tranwitedeuxlet) , ">" , 0)
                    if int(adm.quantit) == 1 :

                        adm.stat = "faux"
                        adm.tranwitedeuxlet = int(adm.tranwitedeuxlet) - 1
                        adm.quantit = int(adm.quantit) - 1
                        db.session.commit()
                        monkzu = Panieruser.query.all()
                        print("on a recu")
                        for imo in monkzu :
                            if int(imo.produite) == id :
                                sfymp = int(imo.dispono) - 1
                                if sfymp >= int(imo.quantiteto)   :
                                    imo.dispono = int(imo.dispono) - 1
                                    imo.statuse = "dispobine"
                                    print(sfymp , ">=" , int(imo.quantiteto))
                                    print("terlin")
                                else : 
                                    print(sfymp , "<" , int(imo.quantiteto))
                                    imo.dispono = int(imo.dispono) - 1
                                    imo.statuse = "nondisp"
                                    print("pas terlin")
                                db.session.commit()
                        return redirect(f'/{losjjs}')
                    if int(adm.quantit) == 0 :
                        adm.stat = "faux"
                        
                        db.session.commit()
                        return redirect(f'/{losjjs}')

                    adm.tranwitedeuxlet = int(adm.tranwitedeuxlet) - 1
                    adm.quantit = int(adm.quantit) - 1
                    db.session.commit()




                    monkzu = Panieruser.query.all()
                    for imo in monkzu :
                        if int(imo.produite) == id :
                            sfymp = int(imo.dispono) - 1
                            if sfymp >= int(imo.quantiteto)   :
                                imo.dispono = int(imo.dispono) - 1
                                imo.statuse = "dispobine"
                                print(sfymp , ">=" , int(imo.quantiteto))
                            else : 
                                print(sfymp , "<" , int(imo.quantiteto))
                                imo.dispono = int(imo.dispono) - 1
                                imo.statuse = "nondisp"
                            db.session.commit()
                            

                if int(adm.tranwitedeuxlet) == 0 :
                    pass

            if taille == "43" :
                if int(adm.tranwitroislet) > 0 :
                    print("int(adm.tranwitroislet)", int(adm.tranwitroislet) , ">" , 0)
                    if int(adm.quantit) == 1 :

                        adm.stat = "faux"
                        adm.tranwitroislet = int(adm.tranwitroislet) - 1
                        adm.quantit = int(adm.quantit) - 1
                        db.session.commit()
                        monkzu = Panieruser.query.all()
                        print("on a recu")
                        for imo in monkzu :
                            if int(imo.produite) == id :
                                sfymp = int(imo.dispono) - 1
                                if sfymp >= int(imo.quantiteto)   :
                                    imo.dispono = int(imo.dispono) - 1
                                    imo.statuse = "dispobine"
                                    print(sfymp , ">=" , int(imo.quantiteto))
                                    print("terlin")
                                else : 
                                    print(sfymp , "<" , int(imo.quantiteto))
                                    imo.dispono = int(imo.dispono) - 1
                                    imo.statuse = "nondisp"
                                    print("pas terlin")
                                db.session.commit()
                        return redirect(f'/{losjjs}')
                    if int(adm.quantit) == 0 :
                        adm.stat = "faux"
                        
                        db.session.commit()
                        return redirect(f'/{losjjs}')

                    adm.tranwitroislet = int(adm.tranwitroislet) - 1
                    adm.quantit = int(adm.quantit) - 1
                    db.session.commit()




                    monkzu = Panieruser.query.all()
                    for imo in monkzu :
                        if int(imo.produite) == id :
                            sfymp = int(imo.dispono) - 1
                            if sfymp >= int(imo.quantiteto)   :
                                imo.dispono = int(imo.dispono) - 1
                                imo.statuse = "dispobine"
                                print(sfymp , ">=" , int(imo.quantiteto))
                            else : 
                                print(sfymp , "<" , int(imo.quantiteto))
                                imo.dispono = int(imo.dispono) - 1
                                imo.statuse = "nondisp"
                            db.session.commit()
                            

                if int(adm.tranwitroislet) == 0 :
                    pass


            if taille == "44" :
                if int(adm.tranwitekatelet) > 0 :
                    print("int(adm.tranwitekatelet)", int(adm.tranwitekatelet) , ">" , 0)
                    if int(adm.quantit) == 1 :

                        adm.stat = "faux"
                        adm.tranwitekatelet = int(adm.tranwitekatelet) - 1
                        adm.quantit = int(adm.quantit) - 1
                        db.session.commit()
                        monkzu = Panieruser.query.all()
                        print("on a recu")
                        for imo in monkzu :
                            if int(imo.produite) == id :
                                sfymp = int(imo.dispono) - 1
                                if sfymp >= int(imo.quantiteto)   :
                                    imo.dispono = int(imo.dispono) - 1
                                    imo.statuse = "dispobine"
                                    print(sfymp , ">=" , int(imo.quantiteto))
                                    print("terlin")
                                else : 
                                    print(sfymp , "<" , int(imo.quantiteto))
                                    imo.dispono = int(imo.dispono) - 1
                                    imo.statuse = "nondisp"
                                    print("pas terlin")
                                db.session.commit()
                        return redirect(f'/{losjjs}')
                    if int(adm.quantit) == 0 :
                        adm.stat = "faux"
                        
                        db.session.commit()
                        return redirect(f'/{losjjs}')

                    adm.tranwitekatelet = int(adm.tranwitekatelet) - 1
                    adm.quantit = int(adm.quantit) - 1
                    db.session.commit()



                    monkzu = Panieruser.query.all()
                    for imo in monkzu :
                        if int(imo.produite) == id :
                            sfymp = int(imo.dispono) - 1
                            if sfymp >= int(imo.quantiteto)   :
                                imo.dispono = int(imo.dispono) - 1
                                imo.statuse = "dispobine"
                                print(sfymp , ">=" , int(imo.quantiteto))
                            else : 
                                print(sfymp , "<" , int(imo.quantiteto))
                                imo.dispono = int(imo.dispono) - 1
                                imo.statuse = "nondisp"
                            db.session.commit()
                            

                if int(adm.tranwitekatelet) == 0 :
                    pass

            

        elif catego == "VetementFemme" :
            taille = request.form.get("taillem")
            losjjs = request.form.get("losjjsm")
            adm = Ajouter.query.get(id)
            if taille == "xs" :
                print("la taille ", taille , "==" , "xs")
                if int(adm.xslet) > 0 :
                    print("int(adm.xslet)", int(adm.xslet) , ">" , 0)
                    if int(adm.quantit) == 1 :

                        adm.stat = "faux"
                        adm.xslet = int(adm.xslet) - 1
                        adm.quantit = int(adm.quantit) - 1
                        db.session.commit()
                        return redirect(f'/{losjjs}')
                    if int(adm.quantit) == 0 :
                        adm.stat = "faux"
                        
                        db.session.commit()
                        return redirect(f'/{losjjs}')

                    adm.xslet = int(adm.xslet) - 1
                    adm.quantit = int(adm.quantit) - 1
                    db.session.commit()



                    monkzu = Panieruser.query.all()
                    for imo in monkzu :
                        if int(imo.produite) == id :
                            sfymp = int(imo.dispono) - 1
                            if sfymp >= int(imo.quantiteto)   :
                                imo.dispono = int(imo.dispono) - 1
                                imo.statuse = "dispobine"
                                print(sfymp , ">=" , int(imo.quantiteto))
                            else : 
                                print(sfymp , "<" , int(imo.quantiteto))
                                imo.dispono = int(imo.dispono) - 1
                                imo.statuse = "nondisp"
                            db.session.commit()
                            

                if int(adm.xslet) == 0 :
                    pass


            if taille == "xl" :
                if int(adm.xllet) > 0 :
                    print("int(adm.xllet)", int(adm.xllet) , ">" , 0)
                    if int(adm.quantit) == 1 :

                        adm.stat = "faux"
                        adm.xllet = int(adm.xllet) - 1
                        adm.quantit = int(adm.quantit) - 1
                        db.session.commit()
                        return redirect(f'/{losjjs}')
                    if int(adm.quantit) == 0 :
                        adm.stat = "faux"
                        
                        db.session.commit()
                        return redirect(f'/{losjjs}')

                    adm.xllet = int(adm.xllet) - 1
                    adm.quantit = int(adm.quantit) - 1
                    db.session.commit()




                    monkzu = Panieruser.query.all()
                    for imo in monkzu :
                        if int(imo.produite) == id :
                            sfymp = int(imo.dispono) - 1
                            if sfymp >= int(imo.quantiteto)   :
                                imo.dispono = int(imo.dispono) - 1
                                imo.statuse = "dispobine"
                                print(sfymp , ">=" , int(imo.quantiteto))
                            else : 
                                print(sfymp , "<" , int(imo.quantiteto))
                                imo.dispono = int(imo.dispono) - 1
                                imo.statuse = "nondisp"
                            db.session.commit()
                            

                if int(adm.xllet) == 0 :
                    pass

            if taille == "xxl" :
                if int(adm.xxllet) > 0 :
                    print("int(adm.xxllet)", int(adm.xxllet) , ">" , 0)
                    if int(adm.quantit) == 1 :

                        adm.stat = "faux"
                        adm.xxllet = int(adm.xxllet) - 1
                        adm.quantit = int(adm.quantit) - 1
                        db.session.commit()
                        return redirect(f'/{losjjs}')
                    if int(adm.quantit) == 0 :
                        adm.stat = "faux"
                        
                        db.session.commit()
                        return redirect(f'/{losjjs}')

                    adm.xxllet = int(adm.xxllet) - 1
                    adm.quantit = int(adm.quantit) - 1
                    db.session.commit()

                if int(adm.xxllet) == 0 :
                    pass

            if taille == "m" :
                if int(adm.mlet) > 0 :
                    print("int(adm.mlet)", int(adm.mlet) , ">" , 0)
                    if int(adm.quantit) == 1 :

                        adm.stat = "faux"
                        adm.mlet = int(adm.mlet) - 1
                        adm.quantit = int(adm.quantit) - 1
                        db.session.commit()

                        monkzu = Panieruser.query.all()
                        print("on a recu")
                        for imo in monkzu :
                            if int(imo.produite) == id :
                                sfymp = int(imo.dispono) - 1
                                if sfymp >= int(imo.quantiteto)   :
                                    imo.dispono = int(imo.dispono) - 1
                                    imo.statuse = "dispobine"
                                    print(sfymp , ">=" , int(imo.quantiteto))
                                    print("terlin")
                                else : 
                                    print(sfymp , "<" , int(imo.quantiteto))
                                    imo.dispono = int(imo.dispono) - 1
                                    imo.statuse = "nondisp"
                                    print("pas terlin")
                                db.session.commit()
                        return redirect(f'/{losjjs}')
                    if int(adm.quantit) == 0 :
                        adm.stat = "faux"
                        
                        db.session.commit()
                        return redirect(f'/{losjjs}')

                    adm.mlet = int(adm.mlet) - 1
                    adm.quantit = int(adm.quantit) - 1
                    db.session.commit()




                    monkzu = Panieruser.query.all()
                    for imo in monkzu :
                        if int(imo.produite) == id :
                            sfymp = int(imo.dispono) - 1
                            if sfymp >= int(imo.quantiteto)   :
                                imo.dispono = int(imo.dispono) - 1
                                imo.statuse = "dispobine"
                                print(sfymp , ">=" , int(imo.quantiteto))
                            else : 
                                print(sfymp , "<" , int(imo.quantiteto))
                                imo.dispono = int(imo.dispono) - 1
                                imo.statuse = "nondisp"
                            db.session.commit()
                            

                if int(adm.mlet) == 0 :
                    pass

            if taille == "s" :
                if int(adm.slet) > 0 :
                    print("int(adm.slet)", int(adm.slet) , ">" , 0)
                    if int(adm.quantit) == 1 :

                        adm.stat = "faux"
                        adm.slet = int(adm.slet) - 1
                        adm.quantit = int(adm.quantit) - 1
                        db.session.commit()
                        monkzu = Panieruser.query.all()
                        print("on a recu")
                        for imo in monkzu :
                            if int(imo.produite) == id :
                                sfymp = int(imo.dispono) - 1
                                if sfymp >= int(imo.quantiteto)   :
                                    imo.dispono = int(imo.dispono) - 1
                                    imo.statuse = "dispobine"
                                    print(sfymp , ">=" , int(imo.quantiteto))
                                    print("terlin")
                                else : 
                                    print(sfymp , "<" , int(imo.quantiteto))
                                    imo.dispono = int(imo.dispono) - 1
                                    imo.statuse = "nondisp"
                                    print("pas terlin")
                                db.session.commit()
                        return redirect(f'/{losjjs}')
                    if int(adm.quantit) == 0 :
                        adm.stat = "faux"
                        
                        db.session.commit()
                        return redirect(f'/{losjjs}')

                    adm.slet = int(adm.slet) - 1
                    adm.quantit = int(adm.quantit) - 1
                    db.session.commit()



                    monkzu = Panieruser.query.all()
                    for imo in monkzu :
                        if int(imo.produite) == id :
                            sfymp = int(imo.dispono) - 1
                            if sfymp >= int(imo.quantiteto)   :
                                imo.dispono = int(imo.dispono) - 1
                                imo.statuse = "dispobine"
                                print(sfymp , ">=" , int(imo.quantiteto))
                            else : 
                                print(sfymp , "<" , int(imo.quantiteto))
                                imo.dispono = int(imo.dispono) - 1
                                imo.statuse = "nondisp"
                            db.session.commit()
                            

                if int(adm.slet) == 0 :
                    pass

            if taille == "l" :
                if int(adm.llet) > 0 :
                    print("int(adm.llet)", int(adm.llet) , ">" , 0)
                    if int(adm.quantit) == 1 :

                        adm.stat = "faux"
                        adm.llet = int(adm.llet) - 1
                        adm.quantit = int(adm.quantit) - 1
                        db.session.commit()
                        monkzu = Panieruser.query.all()
                        print("on a recu")
                        for imo in monkzu :
                            if int(imo.produite) == id :
                                sfymp = int(imo.dispono) - 1
                                if sfymp >= int(imo.quantiteto)   :
                                    imo.dispono = int(imo.dispono) - 1
                                    imo.statuse = "dispobine"
                                    print(sfymp , ">=" , int(imo.quantiteto))
                                    print("terlin")
                                else : 
                                    print(sfymp , "<" , int(imo.quantiteto))
                                    imo.dispono = int(imo.dispono) - 1
                                    imo.statuse = "nondisp"
                                    print("pas terlin")
                                db.session.commit()
                        return redirect(f'/{losjjs}')
                    if int(adm.quantit) == 0 :
                        adm.stat = "faux"
                        
                        db.session.commit()
                        return redirect(f'/{losjjs}')

                    adm.llet = int(adm.llet) - 1
                    adm.quantit = int(adm.quantit) - 1
                    db.session.commit()




                    monkzu = Panieruser.query.all()
                    for imo in monkzu :
                        if int(imo.produite) == id :
                            sfymp = int(imo.dispono) - 1
                            if sfymp >= int(imo.quantiteto)   :
                                imo.dispono = int(imo.dispono) - 1
                                imo.statuse = "dispobine"
                                print(sfymp , ">=" , int(imo.quantiteto))
                            else : 
                                print(sfymp , "<" , int(imo.quantiteto))
                                imo.dispono = int(imo.dispono) - 1
                                imo.statuse = "nondisp"
                            db.session.commit()
                            

                if int(adm.llet) == 0 :
                    pass

        else :
            if catego == "montre" :
                taille = request.form.get("taille")
                losjjs = request.form.get("losjjs")
                adm = Ajouter.query.get(id)
                if int(adm.quantit) == 1 :
                    adm.stat = "faux"
                    adm.quantit = int(adm.quantit) - 1
                    db.session.commit()
                    monkzu = Panieruser.query.all()
                    print("on a recu")
                    for imo in monkzu :
                        if int(imo.produite) == id :
                            sfymp = int(imo.dispono) - 1
                            if sfymp >= int(imo.quantiteto)   :
                                imo.dispono = int(imo.dispono) - 1
                                imo.statuse = "dispobine"
                                print(sfymp , ">=" , int(imo.quantiteto))
                                print("terlin")
                            else : 
                                print(sfymp , "<" , int(imo.quantiteto))
                                imo.dispono = int(imo.dispono) - 1
                                imo.statuse = "nondisp"
                                print("pas terlin")
                            db.session.commit()
                    return redirect(f'/{losjjs}')
                if int(adm.quantit) == 0 :
                    adm.stat = "faux"
                    
                    db.session.commit()
                    return redirect("/commadeadmin")
                
                adm.quantit = int(adm.quantit) - 1
                db.session.commit()




                monkzu = Panieruser.query.all()
                for imo in monkzu :
                    if int(imo.produite) == id :
                        sfymp = int(imo.dispono) - 1
                        if sfymp >= int(imo.quantiteto)   :
                            imo.dispono = int(imo.dispono) - 1
                            imo.statuse = "dispobine"
                            print(sfymp , ">=" , int(imo.quantiteto))
                        else : 
                            print(sfymp , "<" , int(imo.quantiteto))
                            imo.dispono = int(imo.dispono) - 1
                            imo.statuse = "nondisp"
                        db.session.commit()
                        


    
    
    

    
        losjjs = request.form.get("losjjsm")
        return redirect(f'/{losjjs}')
    except Exception as e :
        return e
   
    

@app.route("/onsupprime/<int:id>")
def onsupprime(id):
 
    adm = Commande.query.get(id)
    adm.status = "Annulé"
    adm.livrer = data
    db.session.commit()



    commande = Commande.query.all()
    compterut = 0
    pmse = []
    
    
    
    for i in commande:
        de = i.comnumid
        if int(de[-1]) >= int(compterut) :
            compterut = int(de[-1])

    couleurz = ["ZHRE-pJPO-808-HP-02","MLUE-SKKO-467-AZ-09","NDJB-XGDU-849-SQ-02","HSBS-IWBV-9348-TE-09","VSGD-LSOS-9348-TE-08","ZRRE-IEBV-9348-TE-09","FDGH-IUES-9348-TE-09","NSIZ-IEZV-7352-TS-09","FDGH-LSBD-9348-TE-07","FAGH-ZRAZ-9148-TE-02","PQMD-IEBV-1348-SQ-03","ZAKS-IEBV-9348-ZE-09","IJDS-ISBV-9348-XC-09","ZIZS-IEBV-9328-EZ-01","FDGH-NSIZ-9342-TE-02"]

    aleaez = random.randint(0,(len(couleurz)-1))
    print("aleatoore",aleaez)
    
    compterut = int(compterut) + 1
    compterute =  couleurz[aleaez] + str(compterut)


    aercfer = f"Reçu le {data} à {formatted_time}h{formatted}"
    # Reçu le 2024-08-25 à 17h54
    pani = Mailboite(dateactu=aercfer,image=adm.image,status="Annulé",depart=adm.aller,arriver=data,proprio=adm.client,serie=compterute,lieu=adm.lieulivraison,nom=adm.produitname,categorie=adm.categorie)
            
    db.session.add(pani)
    db.session.commit()


    adm = Commande.query.get(id)
    pmse = [adm]
    # comens = Commande.query.all()

    
        
    datez = adm.livrer
    commen = adm.comnumid
    prenom = adm.prenom
    nom =adm.nom

    lenhsfd = adm.quantite
    lsjhd = adm.mail
    
    mail = Mail(app)
    msg = Message("Commande éffectuée chez HINGTON SHOP",
                sender=SMTP_USERNAME,
                recipients=[lsjhd])
    with app.open_resource("static/IMAGE/hinglogo.png") as img:
            msg.attach("hinglogo.png", "image/jpeg", img.read(), headers={'Content-ID': f'<myimage>'})

    with app.open_resource("static/IMAGE/fgshs.png") as img:
            msg.attach("fgshs.png", "image/jpeg", img.read(), headers={'Content-ID': f'<facebook>'})
    with app.open_resource("static/IMAGE/tikti.png") as img:
            msg.attach("tikti.png", "image/jpeg", img.read(), headers={'Content-ID': f'<titko>'})
    with app.open_resource("static/IMAGE/awp.png") as img:
            msg.attach("awp.png", "image/jpeg", img.read(), headers={'Content-ID': f'<whats>'})
    
    with app.open_resource(f"static/uploads/{adm.image}") as img:
        msg.attach(f"{adm.image}", "image/jpeg", img.read(), headers={'Content-ID': f'<{adm.image}>'})
    # Rendre le template HTML
    msg.html = render_template("anulesignmail.html",lenhsfd=lenhsfd,pmse=pmse,prenom=prenom,commen=commen,nom=nom,datez=datez,livraison=adm.lieulivraison,emballage=data,quantitezr=lenhsfd,total=adm.prixtotal,adm=adm)
    
    # Envoyer l'e-mail
    mail.send(msg)

    return redirect("/commadeadmin")
  
@app.route("/onvalide/<int:id>")
def onvalide(id):
    
        adm = Commande.query.get(id)
        adm.status = "Déja livré"
        adm.livrer = data
        
        db.session.commit()


        commande = Commande.query.all()
        compterut = 0
        pmse = []
        
        
        
        for i in commande:
            de = i.comnumid
            if int(de[-1]) >= int(compterut) :
                compterut = int(de[-1])

        couleurz = ["ZHRE-pJPO-808-HP-02","MLUE-SKKO-467-AZ-09","NDJB-XGDU-849-SQ-02","HSBS-IWBV-9348-TE-09","VSGD-LSOS-9348-TE-08","ZRRE-IEBV-9348-TE-09","FDGH-IUES-9348-TE-09","NSIZ-IEZV-7352-TS-09","FDGH-LSBD-9348-TE-07","FAGH-ZRAZ-9148-TE-02","PQMD-IEBV-1348-SQ-03","ZAKS-IEBV-9348-ZE-09","IJDS-ISBV-9348-XC-09","ZIZS-IEBV-9328-EZ-01","FDGH-NSIZ-9342-TE-02"]
    
        aleaez = random.randint(0,(len(couleurz)-1))
        print("aleatoore",aleaez)
       
        compterut = int(compterut) + 1
        compterute =  couleurz[aleaez] + str(compterut)


        aercfer = f"Reçu le {data} à {formatted_time}h{formatted}"
        # Reçu le 2024-08-25 à 17h54
        pani = Mailboite(dateactu=aercfer,image=adm.image,status="Déja livré",depart=adm.aller,arriver=data,proprio=adm.client,serie=compterute,lieu=adm.lieulivraison,nom=adm.produitname,categorie=adm.categorie)
                
        db.session.add(pani)
        db.session.commit()
    
        
        adm = Commande.query.get(id)
        pmse = [adm]
        # comens = Commande.query.all()

        
            
        datez = adm.livrer
        commen = adm.comnumid
        prenom = adm.prenom
        nom =adm.nom

        lenhsfd = adm.quantite
        lsjhd = adm.mail
        
        mail = Mail(app)
        msg = Message("Commande éffectuée chez HINGTON SHOP",
                    sender=SMTP_USERNAME,
                    recipients=[lsjhd])
        with app.open_resource("static/IMAGE/hinglogo.png") as img:
                msg.attach("hinglogo.png", "image/jpeg", img.read(), headers={'Content-ID': f'<myimage>'})

        with app.open_resource("static/IMAGE/fgshs.png") as img:
                msg.attach("fgshs.png", "image/jpeg", img.read(), headers={'Content-ID': f'<facebook>'})
        with app.open_resource("static/IMAGE/tikti.png") as img:
                msg.attach("tikti.png", "image/jpeg", img.read(), headers={'Content-ID': f'<titko>'})
        with app.open_resource("static/IMAGE/awp.png") as img:
                msg.attach("awp.png", "image/jpeg", img.read(), headers={'Content-ID': f'<whats>'})
        
        with app.open_resource(f"static/uploads/{adm.image}") as img:
            msg.attach(f"{adm.image}", "image/jpeg", img.read(), headers={'Content-ID': f'<{adm.image}>'})
        # Rendre le template HTML
        msg.html = render_template("validedesignmail.html",lenhsfd=lenhsfd,pmse=pmse,prenom=prenom,commen=commen,nom=nom,datez=datez,livraison=adm.lieulivraison,emballage=data,quantitezr=lenhsfd,total=adm.prixtotal,adm=adm)
        
        # Envoyer l'e-mail
        mail.send(msg)
            
    
        return redirect("/commadeadmin")
    
    
@app.route("/attendre/<int:id>" , methods=['POST'])
def attendre(id):
    redirhd1 = request.form.get("redirhd1")
    try :
        adm= Profil.query.get(id)
        if adm.satuq == 2 : 
            adm.satuq = 0
            db.session.commit()
        elif adm.satuq == 0 : 
            adm.satuq = 2
            db.session.commit()
        else :
            pass
       

        return redirect(f"/{redirhd1}")
    
    except :

        return redirect(f"/{redirhd1}")
@app.route("/Suppesss/<int:id>" , methods=['POST'])
def Suppesss(id):
    redirhd1 = request.form.get("redirhd1")
    try :
        adm= Profil.query.get(id)
        db.session.delete(adm)
        db.session.commit()

        return redirect(f"/{redirhd1}")
    
    except :

        return redirect(f"/{redirhd1}")
@app.route("/Suppesz/<int:id>" , methods=['POST'])
def Suppesz(id):
    redirhd1 = request.form.get("redirhd1")
    try :
        recy = Panieruser.query.all()
        for i in recy :
            if int(i.produite) == id :
                i.statuse = "nondisp"
                i.dispono = 0
                db.session.commit()

        recye = Commande.query.all()
        for i in recye :
            if int(i.idpro) == id :
                i.status = "Annulé"
                db.session.commit()
        
        
        adm= Ajouter.query.get(id)
        db.session.delete(adm)
        db.session.commit()
        
        wer1 = adm.image
        wer2 = adm.twoimage
        wer3 = adm.threeimage
        wer4 = adm.forimage
        chemin_image1 = os.path.join(app.config['UPLOAD_FOLDER'], wer1)
        chemin_image2 = os.path.join(app.config['UPLOAD_FOLDER'], wer2)
        chemin_image3 = os.path.join(app.config['UPLOAD_FOLDER'], wer3)
        chemin_image4 = os.path.join(app.config['UPLOAD_FOLDER'], wer4)

        # filename = secure_filename(file.filename)
        # file.save(os.path.join(, filename))
        os.remove(chemin_image1)
        os.remove(chemin_image2)
        os.remove(chemin_image3)
        os.remove(chemin_image4)





        adm= Ajouter.query.get(id)
        db.session.delete(adm)



       

       
        return redirect(f"/{redirhd1}")
    
    except :

        return redirect(f"/{redirhd1}")


@app.route("/informsa")
def informsa():

    # return redirect(f"image/{id}") dans le html
    return render_template("informate.html")

@app.route("/image/<int:id>")
def image(id):

    return render_template("selectimage.html")
# AJOUTER IMAGES DES ARTICLES{}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/add_objetwere', methods=['POST'])
def add_objetwere():
    try :
        if 'file' not in request.files:
            # flash('No file part')
            print('No file part')
            return redirect(request.url)
        file = request.files['file']
        print(file.filename)
        if file.filename == '':
            # flash('Aucune image sélectionnée pour le téléchargement')
            print('Aucune image sélectionnée pour le téléchargement')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #print('upload_image filename: ' + filename)
            # flash('Image téléchargée avec succès et affichée ci-dessous')
            print('Image téléchargée avec succès et affichée ci-dessous')
            return render_template('selectimage.html', filename=file.filename)
            # return render_template('boutique.html', filename=filename)
    except:
        # flash('Les types dimages autorisés sont - png, jpg, jpeg, gif')
        print('eerrr')
        return redirect(request.url)

        # uploads.image
 
# @app.route('/display/<filename>')
# def display_image(filename):
#     #print('display_image filename: ' + filename)
#     return redirect(url_for('static', filename = 'uploads/' + filename), code=301)
# FIN AJOUTER IMAGES DES ARTICLES{}

@app.route('/monpanier')
def panierus():
    if 'utilisateur_id' in session:
        useru = Profil.query.get(session['utilisateur_id'])
        
    else:
        return redirect('/pre/monpanier')
    
    useruo = Profil.query.get(useru.id)
    eudeyyt = Profil.query.all()
    tableaus = Panieruser.query.all()
    catefemme = []
    montre = []
    gdhsuud = []
    chaussure = []
    tout = Ajouter.query.all()
    commenta = []
    articeldd = []
    recupe = Comment.query.all()
    
    for i in recupe:
        commenta.append(i)

    for i in eudeyyt:
        articeldd.append(i)

    
    for i in tableaus : 
        
        if int(i.identifiant) == useruo.id :
            print('prevdg', i.identifiant , 'prevdg' , useruo.id)
            hdhdud = Ajouter.query.get(i.produite)
            if hdhdud :
                lien = hdhdud.liens


                gdhsuud.append({"id":i.id,"element":i.produite,"prix":i.prixdepouce,"image":i.image,"quantite":i.quantiteto,"taille":i.tailed,"nom":i.nomprodui,"description":i.descrprosui,"pource":i.prixtottal,"porce":i.pourcentage ,"tailed":i.tailed,"categorie":i.categorie,"statuse": i.statuse,"liens":lien})
            else :
                lien = "y'a pas lien"
                i.statuse = "nondisp"
                i.quantite = 0
                db.session.commit()
                gdhsuud.append({"id":i.id,"element":i.produite,"prix":i.prixdepouce,"image":i.image,"quantite":i.quantiteto,"taille":i.tailed,"nom":i.nomprodui,"description":i.descrprosui,"pource":i.prixtottal,"porce":i.pourcentage ,"tailed":i.tailed,"categorie":i.categorie,"statuse": i.statuse ,"liens":lien})
            
        # prixdepouce,nomprodui,descrprosui,pourcentage,categorie

    conueww = 0    
    somme = 0     
    for i in gdhsuud :
        if i["statuse"] == "dispobine" :
            
            somme += int(i["pource"])*int(i["quantite"])
            conueww += int(i["quantite"])
    for i in tout:
        if i.categorie == "VetementFemme" :
            catefemme.append(i)

        if i.categorie == "Montre" :
            montre.append(i)
        if i.categorie == "chaussure" :
            chaussure.append(i)
    if len(catefemme)>10 :
        catefemme = catefemme[:10]
    if len(montre) >10 :
        montre = montre[:10]
    if len(chaussure) >10 :
        chaussure = chaussure[:10]


    if len(commenta) > 1:
        print(commenta[0].mail)
    
    return render_template("panierus.html",gdhsuud=gdhsuud,commenta=commenta,catefemme=catefemme,montre=montre,id=useru.id,chaussure=chaussure,somme=somme,conueww=conueww,useruo=useruo.id,pmpl=useruo)

@app.route('/validecommande', methods=['POST'])
def validecommande():
    
    if 'utilisateur_id' in session:
        useru = Profil.query.get(session['utilisateur_id'])
        
    else:
        return redirect('/pre/monpanier')
    
    
    data = datetime.date.today()
    apres_demain = data + datetime.timedelta(days=2)
    dataheure = datetime.datetime.now()
    
    formatted_time = dataheure.strftime('%H')
    formatted = dataheure.strftime('%M')
    print(data)
    print(dataheure)
    print(formatted_time)
    print(formatted)
    print(dataheure)


    useruo = Profil.query.get(useru.id)
    eudeyyt = Profil.query.all()
    tableaus = Panieruser.query.all()
    gdhsuud = []
    commenta = []
    articeldd = []
    recupe = Comment.query.all()
    
    for i in recupe:
        commenta.append(i)

    for i in eudeyyt:
        articeldd.append(i)

    
    for i in tableaus : 
        
        if int(i.identifiant) == useruo.id and i.statuse == "dispobine":
            print('prevdg', i.identifiant , 'prevdg' , useruo.id)
            hdhdud = Ajouter.query.get(int(i.produite))
            if hdhdud :
                gdhsuud.append({"id":i.id,"element":i.produite,"prix":i.prixdepouce,"image":i.image,"quantite":int(i.quantiteto),"taille":i.tailed,"nom":i.nomprodui,"description":i.descrprosui,"pource":int(i.prixtottal),"porce":i.pourcentage ,"tailed":i.tailed,"categorie":i.categorie,"statuse":i.statuse})

    # prixdepouce,nomprodui,descrprosui,pourcentage,categorie,prixtottal

    conueww = 0       
    somme = 0     
    for i in gdhsuud :
       
        if i["statuse"] == "dispobine" :
            somme += int(i["pource"])*int(i["quantite"])
            conueww += int(i["quantite"])
    
    # conueww = 0    
    # conueww += int(i["quantite"])

    if len(commenta) > 1:
        print(commenta[0].mail)
    livraison = request.form.get("livraison",useruo.livraison)
    description = request.form.get("description",useruo.deslivraion)
    numero = request.form.get("numero",useruo.numero)

    if len(gdhsuud) != 0 :
        return render_template("validecommande.html",gdhsuud=gdhsuud,commenta=commenta,id=id,somme=somme,conueww=conueww,clientr = useruo,apres_demain=apres_demain,livraison=livraison,description=description,numero=numero,dataer=data)
    else :
        return redirect("/monpanier")
@app.route('/monpanierls')
def monpanierls():
    
    # data = request.get_json()
   
    # if not data:
    #     return jsonify({"error": "No data received"}), 400
    # print(data)  
    # return jsonify({"message": "Data received successfully", "data": data}), 200
    gdhsuud = "data"
    conueww = len(gdhsuud)  
    eudeyyt = Profil.query.all()
    
    catefemme = []
    montre = []
 
    chaussure = []
    tout = Ajouter.query.all()
    commenta = []
    articeldd = []
    recupe = Comment.query.all()
    
    for i in recupe:
        commenta.append(i)

    for i in eudeyyt:
        articeldd.append(i)

  
    for i in tout:
        if i.categorie == "VetementFemme" :
            catefemme.append(i)

        if i.categorie == "Montre" :
            montre.append(i)
        if i.categorie == "chaussure" :
            chaussure.append(i)
    if len(catefemme)>10 :
        catefemme = catefemme[:10]
    if len(montre) >10 :
        montre = montre[:10]
    if len(chaussure) >10 :
        chaussure = chaussure[:10]


    if len(commenta) > 1:
        print(commenta[0].mail)
    
    return render_template("panierls.html",commenta=commenta,conueww=conueww,gdhsuud=gdhsuud,catefemme=catefemme,montre=montre,chaussure=chaussure)

  
@app.route('/mofiedd/<int:id>' , methods = ["POST","GET"])
def mofiedd(id):
    ajouet = Ajouter.query.get(id) 

    categorie = request.form.get("categorie")
    return render_template("modifier.html",id=id,categorie=categorie,ajouet=ajouet)
@app.route('/mofie/<int:id>',methods = ["POST"])
def mofie(id):

    reu = Ajouter.query.get(id) 

    nom = request.form.get("nom")
    description = request.form.get("description")
    prix = request.form.get("prix")
    porce = request.form.get("porce","0")
    porceprix = str(int(int(prix)-(int(prix) * (int(porce)/100))))     
    categorie = request.form.get('categorie')
    quantit = request.form.get('quantit',"rien")
    xs = request.form.get("xs","rien")
    s = request.form.get("s","rien")
    m = request.form.get("m","rien")
    l = request.form.get("l","rien")
    xl = request.form.get("xl","rien")
    xxl = request.form.get("xxl","rien")
    tranwite = request.form.get("tranwite","rien")
    tranneuf = request.form.get("tranneuf","rien")
    karente = request.form.get("karente","rien")
    tranwiteun = request.form.get("tranwiteun","rien")
    tranwitedeux = request.form.get("tranwitedeux","rien")
    tranwitrois = request.form.get("tranwitrois","rien")
    tranwitekate = request.form.get("tranwitekate","rien")

    tranwitelet = request.form.get("tranwitelet","rien")
    tranneuflet = request.form.get("tranneuflet","rien")
    karentelet = request.form.get("karentelet","rien")
    tranwiteunlet = request.form.get("tranwiteunlet","rien")
    tranwitedeuxlet = request.form.get("tranwitedeuxlet","rien")
    tranwitroislet = request.form.get("tranwitroislet","rien")
    tranwitekatelet = request.form.get("tranwitekatelet","rien")
    xslet = request.form.get("xslet","rien")
    slet = request.form.get("slet","rien")
    mlet = request.form.get("mlet","rien")
    llet = request.form.get("llet","rien")
    xllet = request.form.get("xllet","rien")
    xxllet = request.form.get("xxllet","rien")


    if categorie == "chaussure" :
        tablepmd = [tranwitelet,tranneuflet,karentelet,tranwiteunlet,tranwitedeuxlet,tranwitroislet,tranwitekatelet,xslet,slet,mlet,llet,xllet,xxllet]
        if quantit == "rien" :
            quantit = 0
            
            for i in range(len(tablepmd))  :
                print("les njdgjhdjkd",i)
                if tablepmd[i] != 'rien' and tablepmd[i] != "" and tablepmd[i] != " " and (tablepmd[i]).isdigit(): 
                    quantit += int(tablepmd[i])
                elif tablepmd[i] == 'rien' or tablepmd[i] == "" or tablepmd[i] == " ": 
                    tablepmd[i] = 0
                else :
                    print('ya rien tchai')

                print("dfghjk",tablepmd,"fin",tablepmd[i])



        "je mets a jour le nombres des articles modifier dans le panier "
        monkzu = Panieruser.query.all()
        for imo in monkzu :
            if imo.categorie == "chaussure" :
                
                if imo.tailed == "38 ° " :
                    imo.dispono = int(tablepmd[0]) 
                    db.session.commit()
                    if int(imo.dispono) < int(imo.quantiteto)   :
                       
                        imo.statuse = "nondisp"
                        db.session.commit()
                      

                    else : 
                     
                        imo.statuse = "dispobine" 
                        db.session.commit()
                elif imo.tailed == "39 ° " :
                    imo.dispono = int(tablepmd[1]) 
                    db.session.commit()
                    if int(imo.dispono) < int(imo.quantiteto)   :
                       
                        imo.statuse = "nondisp"
                        db.session.commit()
                      

                    else : 
                     
                        imo.statuse = "dispobine" 
                        db.session.commit()
                elif imo.tailed == "40 ° " :
                    imo.dispono = int(tablepmd[2]) 
                    db.session.commit()
                    if int(imo.dispono) < int(imo.quantiteto)   :
                       
                        imo.statuse = "nondisp"
                        db.session.commit()
                      

                    else : 
                     
                        imo.statuse = "dispobine" 
                        db.session.commit()
                elif imo.tailed == "41 ° " :
                    imo.dispono = int(tablepmd[3]) 
                    db.session.commit()
                    if int(imo.dispono) < int(imo.quantiteto)   :
                       
                        imo.statuse = "nondisp"
                        db.session.commit()
                      

                    else : 
                     
                        imo.statuse = "dispobine" 
                        db.session.commit()
                elif imo.tailed == "42 ° " :
                    imo.dispono = int(tablepmd[4]) 
                    db.session.commit()
                    if int(imo.dispono) < int(imo.quantiteto)   :
                       
                        imo.statuse = "nondisp"
                        db.session.commit()
                      

                    else : 
                     
                        imo.statuse = "dispobine" 
                        db.session.commit()
                elif imo.tailed == "43 ° " :
                    imo.dispono = int(tablepmd[5]) 
                    db.session.commit()
                    if int(imo.dispono) < int(imo.quantiteto)   :
                       
                        imo.statuse = "nondisp"
                        db.session.commit()
                      

                    else : 
                     
                        imo.statuse = "dispobine" 
                        db.session.commit()
                elif imo.tailed == "44 ° " :
                    imo.dispono = int(tablepmd[6]) 
                    db.session.commit()
                    if int(imo.dispono) < int(imo.quantiteto)   :
                       
                        imo.statuse = "nondisp"
                        db.session.commit()
                      

                    else : 
                     
                        imo.statuse = "dispobine" 
                        db.session.commit()

                else :

                    db.session.commit()
           


        reu.nom = nom
        reu.description = description
        reu.prix = prix
        reu.porce = porce
        reu.porceprix = porceprix
        reu.quantit = int(quantit)
        reu.xs = xs
        reu.s = s
        reu.m = m
        reu.l = l
        reu.xl = xl
        reu.xxl = xxl
        reu.tranwite = tranwite
        reu.tranneuf = tranneuf
        reu.karente = karente
        reu.tranwiteun = tranwiteun
        reu.tranwitedeux = tranwitedeux
        reu.tranwitrois = tranwitrois
        reu.tranwitekate = tranwitekate

        reu.tranwitelet =int(tablepmd[0])
        reu.tranneuflet =int(tablepmd[1])
        reu.karentelet = int(tablepmd[2])
        reu.tranwiteunlet = int(tablepmd[3])
        reu.tranwitedeuxlet = int(tablepmd[4])
        reu.tranwitroislet = int(tablepmd[5])
        reu.tranwitekatelet = int(tablepmd[6])
        reu.xslet = xslet
        reu.slet = slet
        reu.mlet = mlet
        reu.llet = llet
        reu.xllet = xllet
        reu.xxllet = xxllet





        db.session.commit()
        return redirect("/cahuseadmin")






    if categorie == "VetementFemme" :
       
        tablepmd = [tranwitelet,tranneuflet,karentelet,tranwiteunlet,tranwitedeuxlet,tranwitroislet,tranwitekatelet,xslet,slet,mlet,llet,xllet,xxllet]
        if quantit == "rien" :
            quantit = 0
            
            for i in range(len(tablepmd))  :
                print("les njdgjhdjkd",i)
                if tablepmd[i] != 'rien' and tablepmd[i] != "" and tablepmd[i] != " " and (tablepmd[i]).isdigit(): 
                    quantit += int(tablepmd[i])
                elif tablepmd[i] == 'rien' or tablepmd[i] == "" or tablepmd[i] == " ": 
                    tablepmd[i] = 0
                else :
                    print('ya rien tchai')

                print("dfghjk",tablepmd,"fin",tablepmd[i])



        "je mets a jour le nombres des articles modifier dans le panier "
        monkzu = Panieruser.query.all()
        for imo in monkzu :
          
   
            if imo.categorie == "VetementFemme" :
                
                if imo.tailed == "m" :
                    imo.dispono = int(tablepmd[9]) 
                    db.session.commit()
                    if int(imo.dispono) < int(imo.quantiteto)   :
                       
                        imo.statuse = "nondisp"
                        db.session.commit()
                      

                    else : 
                     
                        imo.statuse = "dispobine" 
                        db.session.commit()
                elif imo.tailed == "xxl" :
                    imo.dispono = int(tablepmd[12]) 
                    db.session.commit()
                    if int(imo.dispono) < int(imo.quantiteto)   :
                       
                        imo.statuse = "nondisp"
                        db.session.commit()
                      

                    else : 
                     
                        imo.statuse = "dispobine" 
                        db.session.commit()
                elif imo.tailed == "xs" :
                    imo.dispono = int(tablepmd[7]) 
                    db.session.commit()
                    if int(imo.dispono) < int(imo.quantiteto)   :
                       
                        imo.statuse = "nondisp"
                        db.session.commit()
                      

                    else : 
                     
                        imo.statuse = "dispobine" 
                        db.session.commit()
                elif imo.tailed == "l" :
                    imo.dispono = int(tablepmd[10]) 
                    db.session.commit()
                    if int(imo.dispono) < int(imo.quantiteto)   :
                       
                        imo.statuse = "nondisp"
                        db.session.commit()
                      

                    else : 
                     
                        imo.statuse = "dispobine" 
                        db.session.commit()
                elif imo.tailed == "xl" :
                    imo.dispono = int(tablepmd[11]) 
                    db.session.commit()
                    if int(imo.dispono) < int(imo.quantiteto)   :
                       
                        imo.statuse = "nondisp"
                        db.session.commit()
                      

                    else : 
                     
                        imo.statuse = "dispobine" 
                        db.session.commit()
                elif imo.tailed == "s" :
                    imo.dispono = int(tablepmd[8]) 
                    db.session.commit()
                    if int(imo.dispono) < int(imo.quantiteto)   :
                       
                        imo.statuse = "nondisp"
                        db.session.commit()
                      

                    else : 
                     
                        imo.statuse = "dispobine" 
                        db.session.commit()
                

                else :

                    db.session.commit()
           


        

        reu.nom = nom
        reu.description = description
        reu.prix = prix
        reu.porce = porce
        reu.porceprix = porceprix
        reu.quantit = int(quantit)
        reu.xs = xs
        reu.s = s
        reu.m = m
        reu.l = l
        reu.xl = xl
        reu.xxl = xxl
        reu.tranwite = tranwite
        reu.tranneuf = tranneuf
        reu.karente = karente
        reu.tranwiteun = tranwiteun
        reu.tranwitedeux = tranwitedeux
        reu.tranwitrois = tranwitrois
        reu.tranwitekate = tranwitekate

        reu.tranwitelet = tranwitelet
        reu.tranneuflet = tranneuflet
        reu.karentelet = karentelet
        reu.tranwiteunlet = tranwiteunlet
        reu.tranwitedeuxlet = tranwitedeuxlet
        reu.tranwitroislet = tranwitroislet
        reu.tranwitekatelet = tranwitekatelet
        reu.xslet = int(tablepmd[7])
        reu.slet = int(tablepmd[8])
        reu.mlet = int(tablepmd[9])
        reu.llet = int(tablepmd[10])
        reu.xllet = int(tablepmd[11])
        reu.xxllet = int(tablepmd[12])

        db.session.commit()
        return redirect("/listederobe")

    if categorie == "Montre" :

        "je mets a jour le nombres des articles modifier dans le panier "
        monkzu = Panieruser.query.all()
        for imo in monkzu :
          
   
            if imo.categorie == "Montre" :
                
               
                imo.dispono = int(quantit)
                db.session.commit()
                if int(imo.dispono) < int(imo.quantiteto)   :
                    
                    imo.statuse = "nondisp"
                    db.session.commit()
                    

                else : 
                    
                    imo.statuse = "dispobine" 
                    db.session.commit()
               

           

      
        reu.nom = nom
        reu.description = description
        reu.prix = prix
        reu.porce = porce
        reu.porceprix = porceprix
        reu.quantit = int(quantit)
        reu.xs = xs
        reu.s = s
        reu.m = m
        reu.l = l
        reu.xl = xl
        reu.xxl = xxl
        reu.tranwite = tranwite
        reu.tranneuf = tranneuf
        reu.karente = karente
        reu.tranwiteun = tranwiteun
        reu.tranwitedeux = tranwitedeux
        reu.tranwitrois = tranwitrois
        reu.tranwitekate = tranwitekate

        reu.tranwitelet = tranwitelet
        reu.tranneuflet = tranneuflet
        reu.karentelet = karentelet
        reu.tranwiteunlet = tranwiteunlet
        reu.tranwitedeuxlet = tranwitedeuxlet
        reu.tranwitroislet = tranwitroislet
        reu.tranwitekatelet = tranwitekatelet
        reu.xslet = xslet
        reu.slet = slet
        reu.mlet = mlet
        reu.llet = llet
        reu.xllet = xllet
        reu.xxllet = xxllet

        db.session.commit()

        return redirect("/montreadosn")
    return redirect("/")
    # reu.xs = request.form.get("xs",'')
    # reu.porce = request.form.get("porce",'')
    # reu.prix = reu.prix
    # reu.porceprix = str(int(int(reu.prix)-(int(reu.prix) * (int(reu.porce)/100))))
    # reu.s = request.form.get("s",'')
    # reu.m = request.form.get("m",'')
    # reu.l = request.form.get("l",'')
    # reu.xl = request.form.get("xl",'')
    # reu.xxl = request.form.get("xxl",'')
    # reu.rouge = request.form.get("rouge",'')
    # reu.blanc = request.form.get("blanc",'')
    # reu.noir = request.form.get("noir",'')
    # reu.jaune = request.form.get("jaune",'')
    # reu.vert = request.form.get("vert",'')
    # reu.orange = request.form.get("orange",'')
    # reu.bleu = request.form.get("bleu",'')
    # reu.rose = request.form.get("rose",'')
    # reu.marron = request.form.get("marron",'')
    # reu.violet = request.form.get("violet",'')
    # reu.gris = request.form.get("gris",'')
    # reu.tranwite = request.form.get("tranwite",'')
    # reu.tranneuf = request.form.get("tranneuf",'')
    # reu.karente = request.form.get("karente",'')
    # reu.tranwiteun = request.form.get("tranwiteun",'')
    # reu.tranwitedeux = request.form.get("tranwitedeux",'')
    # reu.tranwitrois = request.form.get("tranwitrois",'')
    # reu.tranwitekate = request.form.get("tranwitekate",'')
    


    # if reu.categorie == "chaussure" :
    #     tablepmd = [reu.tranwitelet,reu.tranneuflet,reu.karentelet,reu.tranwiteunlet,reu.tranwitedeuxlet,reu.tranwitroislet,reu.tranwitekatelet,reu.xslet,reu.slet,reu.mlet,reu.llet,reu.xllet,reu.xxllet]
    #     if quantit == "rien" :
    #         quantit = 0
            
    #         for i in range(len(tablepmd))  :
    #             print("les njdgjhdjkd",i)
    #             if tablepmd[i] != 'rien' and tablepmd[i] != "" and tablepmd[i] != " " and (tablepmd[i]).isdigit(): 
    #                 quantit += int(tablepmd[i])
    #             elif tablepmd[i] == 'rien' or tablepmd[i] == "" or tablepmd[i] == " ": 
    #                 tablepmd[i] = 0
    #             else :
    #                 print('ya rien tchai')

    #             print("dfghjk",tablepmd,"fin",tablepmd[i])



    # reu.tranwitelet = request.form.get("tranwitelet","0")
    # reu.tranneuflet = request.form.get("tranneuflet","0")
    # reu.karentelet = request.form.get("karentelet","0")
    # reu.tranwiteunlet = request.form.get("tranwiteunlet","0")
    # reu.tranwitedeuxlet = request.form.get("tranwitedeuxlet","0")
    # reu.tranwitroislet = request.form.get("tranwitroislet","0")
    # reu.tranwitekatelet = request.form.get("tranwitekatelet","0")
    # reu.xslet = request.form.get("xslet","0")
    # reu.slet = request.form.get("slet","0")
    # reu.mlet = request.form.get("mlet","0")
    # reu.llet = request.form.get("llet","0")
    # reu.xllet = request.form.get("xllet","0")
    # reu.xxllet = request.form.get("xxllet","0")
    # db.session.commit()
    # return redirect('/administa')



@app.route('/add_data')
def add_data():
    catefemme = []
    montre = []
    chaussure = []
    tout = Ajouter.query.all()
    commenta = []
    recupe = Comment.query.all()
    
    for i in recupe:
        commenta.append(i)

    for i in tout:
        if i.categorie == "VetementFemme" :
            catefemme.append(i)

        if i.categorie == "Montre" :
            montre.append(i)

        if i.categorie == "chaussure" :
            chaussure.append(i)
    if len(catefemme)>10 :
        catefemme = catefemme[:10]
    if len(montre) >10 :
        montre = montre[:10]
    if len(chaussure) >10 :
        chaussure = chaussure[:10]


    if len(commenta) > 1:
        print(commenta[0].mail)
    
    return render_template("add_profile.html",commenta=commenta,catefemme=catefemme,montre=montre,chaussure=chaussure)

   



import bcrypt




@app.route('/add',methods = ["POST"])
def profile() :
    
    
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    hashed_password = request.form.get("age")
    confe = request.form.get("conf")
    
    salt = bcrypt.gensalt()
    # Hasher le mot de passe avec le sel
    age = bcrypt.hashpw(hashed_password.encode('utf-8'), salt)
   
  

    if confe != hashed_password :
        flash("Email ou Mot de passe invalide")
        return redirect("/add_data")
    
    for i in range (len(last_name)) :
        if last_name[i] == "@" :

            if "moc.liamg" == last_name[:i:-1]:

                pass
            else :
                flash("Email ou Mot de passe invalide")
                return redirect("/add_data")
            



    user = Profil.query.filter_by(last_name = request.form.get("last_name")).first()
    if user :
        flash("Impossible de crée un compte") 
        return redirect(url_for("add_data"))
    else :
        if first_name != " " and last_name != " " and hashed_password is not None and len(hashed_password)== 8 :
            p = Profil(first_name = first_name, last_name = last_name , age = age , prenom="",residence="",livraison="",numero="",deslivraion="",infoplus="",satuq=0)

            db.session.add(p)
            db.session.commit()
            return redirect("/pre/acceuilconnect")
        else :
            return redirect("/add_data")
        
# FIN AJOUTER DES USER{} 


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    
    if request.method == 'POST':
        user = Profil.query.get(id)
        eude = Profil.query.all()

        user.infoplus = request.form['infoplus']
        user.last_name = request.form['last_name']
        user.first_name = request.form['first_name']
        user.prenom = request.form['prenom']
        user.livraison = request.form['livraison']
        user.residence = request.form['residence']
        user.numero = request.form['numero']
        user.deslivraion = request.form['deslivraion']
        user.age = user.age

        print("1",user.infoplus,"2", user.last_name,"3",user.first_name,"4",user.prenom,"5",user.livraison,"6",user.residence,"7",user.numero,"8",user.deslivraion,"9", user.age )
        db.session.commit()
        # for i in eude :
        #     if i == user :
        #         continue
        #     if i.last_name == user.last_name :
        #         flash("Email ou Mot de passe invalide")
        #         return redirect(url_for('update', id=id))
        #     else :
            
        #         for i in range (len(user.last_name)) :

        #             if user.last_name[i] == "@" :
                        
        #                 if "moc.liamg" == user.last_name[:i:-1] :

        #                     db.session.commit()
        #                     return redirect(url_for('monprofil'))
                        
        #                 else :

        #                     flash("Email ou Mot de passe invalide")
        #                     return redirect(url_for('update', id=id))
                   
                        
 
            
           
    flash("Email ou Mot de passe invalide")
    return redirect(url_for('monprofil'))
@app.route('/commantairear', methods=['POST'])
def commantairear():
    if 'utilisateur_id' in session:
        useru = Profil.query.get(session['utilisateur_id'])
        
    else:
        return redirect('/pre/monpanier')
    
    data = datetime.date.today()
    dataheure = datetime.datetime.now()
    formatted_time = dataheure.strftime('%H')
    formatted = dataheure.strftime('%M')

    if request.method == 'POST':
        couleurz = ["red","blue","yellow","green","orange"]
        import random
        alea = random.randint(0,4)
        print("aleatoore",alea)
        eude = Commantaire.query.all()
       
        redirhd1 = request.form['redirhd1']
        commentairec = request.form['commentairec']
        idclient = useru.id
        idproduit = request.form['idproduit']
        nomclient = useru.first_name + " " + useru.prenom
        datecomman = f"Acheté le {data} à {formatted_time}h{formatted}"
        couleur = couleurz[alea]
        pani = Commantaire(commentairec=commentairec,idclient=idclient,idproduit=idproduit,nomclient=nomclient,datecomman=datecomman,couleur=couleur)
            
        db.session.add(pani)
        db.session.commit()
       
    return redirect(f'/{redirhd1}/{idproduit}')






# @app.route('/receive_data', methods=['POST'])
# def receive_data():
#     data = request.json  # Receives JSON data sent from JavaScript
#     data_from_js = data['data']
    
#     # Now you can use data_from_js as needed in your Python application
#     print('Data received from JavaScript:', data_from_js)
    
#     # Optionally, you can send a response back to JavaScript
#     response = {'message': 'Data received successfully'}
#     return jsonify(response)

@app.route('/deconnexion')
def deconnexion():
    session.pop('utilisateur_id', None)
    return redirect('/pre/acceuilconnect')


@app.route('/designmail/<int:id>')
def designmail(id):
    
    comens = Commande.query.all()
    panier = Panieruser.query.all()
    pmse = []
    
    for i in comens :
        
        datez = i.livrer
        commen = i.comnumid
        prenom = i.prenom
        nom =i.nom

    for i in panier :
        if int(i.identifiant) == int(id):
            pmse.append(i)

    
    lenhsfd = len(pmse)

    

    return render_template("maiql.html",lenhsfd=lenhsfd,pmse=pmse,prenom=prenom,commen=commen,nom=nom,datez=datez)




@app.route('/validedesignmail/<int:id>')
def validedesignmail(id):
    
    comens = Commande.query.all()
    panier = Panieruser.query.all()
    pmse = []
    
    for i in comens :
        
        datez = i.livrer
        commen = i.comnumid
        prenom = i.prenom
        nom =i.nom

    for i in panier :
        if int(i.identifiant) == int(id):
            pmse.append(i)

    
    lenhsfd = len(pmse)

    

    return render_template("validedesignmail.html",lenhsfd=lenhsfd,pmse=pmse,prenom=prenom,commen=commen,nom=nom,datez=datez)







# @app.route('/envoyer-email')
# def envoyer_email():
#     try:
#         msg = Message("Confirmation de votre commande",
#                       sender="votre_email@example.com",
#                       recipients=["client@example.com"])
        
#         # Construire le corps de l'email avec l'encodage utf-8
#         msg.body = "Nous avons bien reçu votre commande et elle vous sera livrée dans deux jours.".encode('utf-8')
        
#         # Ou pour un message HTML
#         msg.html = render_template('email_template.html', some_variable='value').encode('utf-8')
        
#         mail.send(msg)
#         return "Email envoyé avec succès !"
    
#     except Exception as e:
#         return f"Erreur lors de l'envoi de l'e-mail : {str(e)}"





# @app.route('/')
# def index():
#     return render_template('index.html')


# jecpren = Ajouter.query.all()
# for i in jecpren:
#     if int(i.quantit) == 0 :
#         i.stat = "faux" 
#         db.session.commit()



if __name__ == '__main__' :
    app.run(debug=True,port=5005)
