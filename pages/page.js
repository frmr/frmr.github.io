var mediaIndex = 0

function selectorClick(element) {

    var nodes = Array.prototype.slice.call(element.parentNode.children);
    var container = document.getElementById("project-page-media-container");
    var filename = media[nodes.indexOf(element)];

    container.innerHTML = "";

    if (filename.endsWith("png")) {
        var image = document.createElement("img");
        image.setAttribute("src", filename);
        image.classList.add("project-page-image");
        container.appendChild(image)
    }
    else if (filename.endsWith("mp4")) {
        alert("mp4");
    }

    
}