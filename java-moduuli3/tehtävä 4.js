const target = document.getElementById("target");

for (let i = 0; i < students.length; i++) {
    const option = document.createElement("option");

    option.value = students[i].value;
    option.textContent = students[i].name;

    target.appendChild(option);
}