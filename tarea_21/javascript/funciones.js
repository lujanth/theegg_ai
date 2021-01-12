var numeroComp = null;
var numeradorCalc= null;
var denominadorCalc = null;
var esFraccionIrreducible = false; // Vble que indicará cuando se ha llegado a una fraccion irreducible

/*
Funcion de comienzo del programa completo
    Primero comprobamos si el numero a calcular, es correcto(esta entre los limites permitidos)
    Si el numero es correcto, calculamos su fraccion irreducible
*/
function comprobarCalcular(){
    document.getElementById("fraccionRdo").value="";
    if (comprobarNumero())
        calcularFraccionIrreducible()
}


/*
Funcion que comprueba si el numero introducido esté dentro del rango permitido
0.0001 - 0.9999
*/
function comprobarNumero(){
    // Recogemos el numero indicado en el form, en una variable global que utilizaremos mas adelante
    numeroComp = document.getElementById("numero").value;
    if(numeroComp >= 0.0001 && numeroComp <= 0.9999){
        return true;
    } else {
        window.alert("El numero indicado no es correcto, introduzca un valor comprendido entre 0.0001 y 0.9999");
    }
}


/*
Funcion que calcula la fraccion irreducible del numero indicado en el form
*/
function calcularFraccionIrreducible(){
    // Inicializamos las variables en cada comprobacion
    var numerador= null; 
    var denominador = null;
    numeradorCalc= null;
    denominadorCalc = null;
    esFraccionIrreducible = false;

    // como el numero en el form se recoge en formato texto, localizamos el punto y lo partimos en 2
    numeroEnForm = numeroComp.split(".");
    // metemos en una variable, la parte entera del numero del form y en otra la parte decimal
    parteEntera = numeroEnForm[0];
    parteDecimal = numeroEnForm[1];

    // Pasamos a numero la parte decimal, que será el numerador inicial de la fraccion
    numerador=parseInt(parteDecimal);
    
    // Calculamos el denominador de la fraccion en base a la longitud de la parte decimal
    longitudDenominador = parteDecimal.length;
    // Damos al demonimador el valor correspondiente
    switch( longitudDenominador ) {
        case 1: 
            denominador = 10;
            break;
        case 2:
            denominador = 100;
            break;
        case 3: 
            denominador = 1000;
            break;
        default: // damos por hecho que si no se trata de los casos anteriores es de long=4, porque hemos hecho la comprobacion previa del numero
            denominador = 10000;
      }

    // Inicalizamos con los valores anteriores, las variables con las que trabajaremos en el bucle que calculará la fraccion irreducible
    numeradorCalc = numerador
    denominadorCalc = denominador
    
    // bucle para calcular la fraccion irreducible
    do{
        buscarFraccionIrreducible()
    } while(!esFraccionIrreducible )
    alert('La fraccion IRREDUCIBLE calculada es: ' + numeradorCalc + '/' + denominadorCalc);
    document.getElementById("labelFracciónRdo").hidden=false;
    document.getElementById("fraccionRdo").hidden=false;
    document.getElementById("fraccionRdo").value = numeradorCalc + ' / ' + denominadorCalc;
    



}

/*
Funcion para comprobar si numerador y denominador, son divisibles por 2
Estas 3 funciones se pueden unificar en una, donde se pase como argumento el numero por el que se quiere dividir.
Se decide dejar en 3, por facilitar la comprension del codigo
*/
function sonDivisiblesPorDos(){
    if ( (numeradorCalc % 2 == 0) && (denominadorCalc % 2 == 0)){
        numeradorCalc = numeradorCalc/2;
        denominadorCalc = denominadorCalc/2;
        return true;
    }else{
        return false;
    }
}


/*
Funcion para comprobar si numerador y denominador, son divisibles por 3
*/
function sonDivisiblesPorTres(){
    if ( (numeradorCalc % 3 == 0) && (denominadorCalc % 3 == 0)){
        numeradorCalc = numeradorCalc/3;
        denominadorCalc = denominadorCalc/3;
        return true;
    }else{
        return false;
    }
}


/*
Funcion para comprobar si numerador y denominador, son divisibles por 5
*/
function sonDivisiblesPorCinco(){
    if ( (numeradorCalc % 5 == 0) && (denominadorCalc % 5 == 0)){
        numeradorCalc = numeradorCalc/5;
        denominadorCalc = denominadorCalc/5;
        return true
    }else{
        return false;
    }
}

/*
Funcion que va comprobando si numerador y denominador son todavia divisibles
 - va mostrando por pantalla las fracciones intermedias que se van calculando hasta llegar a la irreducible
 - cuando detecta que ya no son divisibles, marca a true la vlble que controla el fin del bucle
*/
function buscarFraccionIrreducible(){
    if (sonDivisiblesPorDos()){
        alert('Fracción intermedia => ' + numeradorCalc + '/' + denominadorCalc);
    }else if (sonDivisiblesPorTres()){
        alert('Fracción intermedia => ' + numeradorCalc + '/' + denominadorCalc);
    }else if(sonDivisiblesPorCinco()){
        alert('Fracción intermedia => ' + numeradorCalc + '/' + denominadorCalc);
    }else{
        esFraccionIrreducible=true
    }

}


function cerrarPagina(){
    document.getElementById("numero").value=null
    document.getElementById("labelFracciónRdo").hidden=true
    document.getElementById("fraccionRdo").hidden=true
    document.getElementById("fraccionRdo").value=""
    window.open("end.html","_self")
}