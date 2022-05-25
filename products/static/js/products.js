function getTypeIds() {
    types = document.body.querySelectorAll(".type-selector:checked");
    typeString = "";
    types.forEach((typeId) => (typeString += typeId.name + ","));
    if (typeString.length == 0) {
        typeString = "all";
    }
    return typeString;
}

function refreshTable(queryString) {
    httpRequest = new XMLHttpRequest();
    httpRequest.onload = redrawTable;
    httpRequest.open("GET", "table?" + queryString, true);
    httpRequest.send();
}

function redrawTable(content) {
    document.getElementById("table-content").innerHTML = content.target.response;
}

updateTypes = function () {
    typeIds = getTypeIds();
    refreshTable("types=" + typeIds);
};

updateSort = function (event) {
    ordering = event.target.dataset.sort;
    queryString = "sort=" + ordering;
    refreshTable(queryString);
};

document.body
    .querySelectorAll(".type-selector")
    .forEach((type) => type.addEventListener("click", updateTypes));
document.body
    .querySelectorAll(".valuecolumn")
    .forEach((type) => type.addEventListener("click", updateSort));
