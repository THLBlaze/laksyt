const section = document.querySelector("section");

for (let i = 0; i < picArray.length; i++) {
    const article = document.createElement("article");
    article.classList.add("card");

    const heading = document.createElement("h2");
    heading.textContent = picArray[i].title;

    const figure = document.createElement("figure");

    const img = document.createElement("img");
    img.src = picArray[i].medium_image;
    img.alt = picArray[i].title;

    const figcaption = document.createElement("figcaption");
    figcaption.textContent = picArray[i].caption;

    const paragraph = document.createElement("p");
    paragraph.textContent = picArray[i].description;

    figure.appendChild(img);
    figure.appendChild(figcaption);

    article.appendChild(heading);
    article.appendChild(figure);
    article.appendChild(paragraph);

    section.appendChild(article);
}