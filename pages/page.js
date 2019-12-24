var mediaIndex = 0

function selectorClick(element) {

    var nodes = Array.prototype.slice.call(element.parentNode.children);
    mediaIndex = nodes.indexOf(element);

    updateMediaContainer();
}

function updateMediaContainer() {
    var filename = media[mediaIndex];
    var mediaContainer = document.getElementById("project-page-media-container");
    var selectors = document.getElementsByClassName("project-page-selector");

    for (var i = 0; i < selectors.length; ++i) {
        selectors[i].classList.remove("project-page-selector-selected");
    }
    
    selectors[mediaIndex].classList.add("project-page-selector-selected");

    mediaContainer.innerHTML = "";

    if (filename.endsWith("png")) {
        var image = document.createElement("img");
        image.setAttribute("src", filename);
        image.classList.add("project-page-image");
        mediaContainer.appendChild(image)
    }
    else if (filename.endsWith("mp4")) {
        alert("mp4");
    }
}

function previousMedia() {
    if (--mediaIndex == -1) {
        mediaIndex = media.length - 1;
    }

    updateMediaContainer();
}

function nextMedia() {
    if (++mediaIndex == media.length) {
        mediaIndex = 0;
    }

    updateMediaContainer();
}