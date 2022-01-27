const dataLowercase = "azertyuiopqsdfghjklmwxcvbn";
const dataUppercase = dataLowercase.toUpperCase();
const dataNumbers = "0123456789";
const dataSymbols = "$^*ùm!:;,&é\"'(-è_ç)";

const rangeValue = document.getElementById("password-length");
const passwordOutput = document.getElementById("password-output");
const lowerCase = document.getElementById("lowercase");
const upperCase = document.getElementById("uppercase");
const numbers = document.getElementById("numbers");
const symbols = document.getElementById("symbols");
const generateButton = document.getElementById("generateButton");

function generatePassword(event) {
    let data = [];
    let password = "";

    console.log(event);
    console.log(passwordOutput.value);
    passwordOutput.style.width = "50%";
    passwordOutput.style.background = "red";

    if (lowerCase.checked) data.push(...dataLowercase);
    if (upperCase.checked) data.push(...dataUppercase);
    if (numbers.checked) data.push(...dataNumbers);
    if (symbols.checked) data.push(...dataSymbols);

    if (data.length === 0) {
        alert("Veuillez sélectionner des critères");
        return;
    }

    for (i = 0; i < rangeValue.value; i++) {
        password += data[Math.floor(Math.random() * data.length)];
    }

    passwordOutput.value = password;
}

generateButton.addEventListener("click", generatePassword);
