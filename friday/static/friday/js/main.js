var main = [];

function typing() {
    document.getElementById("search").style.color = "white";
    document.getElementById("search").style.border = "1px solid #00a1e5";
    document.getElementById("search").style.backgroundColor = "#00a1e5";
    document.getElementById("search").setAttribute("class", "white-placeholder");
    document.getElementsByClassName("close-button")[0].style.display = "inline";
}

function closeSearch() {
    document.getElementById("search").style.color = "#00a1e5";
    document.getElementById("search").style.border = "1px solid lightgray";
    document.getElementById("search").style.backgroundColor = "white";
    document.getElementById("search").setAttribute("class", "");
    document.getElementById("search").value = "";
    document.getElementsByClassName("close-button")[0].style.display = "none";
}

function showClose() {
    document.getElementsByClassName("close-button")[0].style.display = "inline";
}

function hideMenuOver() {
    document.getElementsByClassName("hide-menu")[0].innerHTML = "<i class=\"fa fa-arrow-circle-o-left\" aria-hidden=\"true\"></i>";
}

function hideMenuOut() {
    document.getElementsByClassName("hide-menu")[0].innerHTML = "<i class=\"fa fa-bars\" aria-hidden=\"true\"></i>";
}

function caseInputFocus() {
    document.getElementsByClassName("case-search-input")[0].style.width = "240px";
    document.getElementsByClassName("case-search-left")[0].style.borderColor = "#66ccf5";
    document.getElementsByClassName("case-search-input")[0].style.borderColor = "#66ccf5";
    document.getElementsByClassName("case-search-close")[0].style.borderColor = "#66ccf5";
    document.getElementsByClassName("case-search-right")[0].style.borderColor = "#66ccf5";
    document.getElementsByClassName("case-search-input")[0].setAttribute("class", "case-search-input blue-placeholder");
}

function caseInputBlur() {
    document.getElementsByClassName("case-search-input")[0].style.width = "220px";
    if (document.getElementsByClassName("case-search-input")[0].value === "") {
        document.getElementsByClassName("case-search-input")[0].style.width = "240px";
        document.getElementsByClassName("case-search-close")[0].style.display = "none";
        document.getElementsByClassName("case-search-left")[0].style.color = "lightgray";
        document.getElementsByClassName("case-search-left")[0].style.backgroundColor = "white";
        document.getElementsByClassName("case-search-left")[0].style.borderColor = "lightgray";
        document.getElementsByClassName("case-search-input")[0].style.borderColor = "lightgray";
        document.getElementsByClassName("case-search-close")[0].style.borderColor = "lightgray";
        document.getElementsByClassName("case-search-right")[0].style.borderColor = "lightgray";
        document.getElementsByClassName("case-search-input")[0].setAttribute("class", "case-search-input");
    }
}

function caseInputTyping() {
    document.getElementsByClassName("case-search-input")[0].style.width = "220px";
    document.getElementsByClassName("case-search-close")[0].style.display = "inline";
    document.getElementsByClassName("case-search-left")[0].style.color = "white";
    document.getElementsByClassName("case-search-left")[0].style.backgroundColor = "#66ccf5";
}

function caseInputClose() {
    document.getElementsByClassName("case-search-input")[0].value = "";
    document.getElementsByClassName("case-search-close")[0].style.display = "none";
    caseInputFocus();
    document.getElementsByClassName("case-search-input")[0].focus();
}

function searchCase(term) {
    for (var i = 0; i < main.length; i++) {
        if (main[i].indexOf(term.toLowerCase()) === -1 && term !== "") {
            document.getElementsByClassName("case-body")[0].getElementsByClassName("activity-group-tr")[i + 1].style.display = "none";
        }
        else {
            document.getElementsByClassName("case-body")[0].getElementsByClassName("activity-group-tr")[i + 1].style.display = "table";
        }
    }
}

function getMain(name) {
    var xhr = new XMLHttpRequest();
    var url = "http://localhost:8000/case/";
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-type", "application/json");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var json = JSON.parse(xhr.responseText);
            loadMain(json);
        }
    };
    var data = JSON.stringify({'name': name});
    xhr.send(data);
}

function loadMain(response) {
    main = [];
    response = JSON.parse(response);
    console.log(response);
    document.getElementsByClassName("case-header-top-text")[0].innerHTML = "This board is public, visible to all team members.";
    // if (response.public) {
    //     document.getElementsByClassName("case-header-top-text")[0].innerHTML = "This board is public, visible to all team members.";
    // }
    // else {
    //     document.getElementsByClassName("case-header-top-text")[0].innerHTML = "This board is private, visible to limited members.";
    // }
    document.getElementsByClassName("case-name")[0].innerHTML = response.name;
    document.getElementsByClassName("case-description")[0].innerHTML = response.description;
    var body = "        <table class=\"activity-group\">";
    body += "            <tr class=\"activity-group-tr\">";
    body += "                <th class=\"activity-group-th activity-button\"><i class=\"fa fa-chevron-circle-down\" aria-hidden=\"true\"></i></th>";
    body += "                <th class=\"activity-group-th activity-name\">Activities</th>";
    body += "                <th class=\"activity-group-th activity-owner\">Owner</th>";
    body += "                <th class=\"activity-group-th activity-status\">Status</th>";
    body += "                <th class=\"activity-group-th activity-time\">Time Est.</th>";
    body += "                <th class=\"activity-group-th activity-money\">Money</th>";
    body += "            </tr>";
    console.log(response.activities);
    for (var i = 0; i < response.activities.length; i++) {
        main.push(JSON.stringify(response.activities[i]).toLowerCase());
        console.log(response.activities[i]);
        body += "            <tr class=\"activity-group-tr\">";
        body += "                <td class=\"activity-group-td activity-button\"></td>";
        body += "                <td class=\"activity-group-td activity-name\">" + response.activities[i].name + "</td>";
        body += "                <td class=\"activity-group-td activity-owner\">" + response.activities[i].people[0].name + "</td>";
        body += "                <td class=\"activity-group-td activity-status\">" + response.activities[i].status + "</td>";
        body += "                <td class=\"activity-group-td activity-time\">" + response.activities[i].time + "h</td>";
        body += "                <td class=\"activity-group-td activity-money\">" + response.activities[i].money + "</td>";
        body += "            </tr>";
    }
    body += "        </table>";
    console.log(main);
    document.getElementsByClassName("case-body")[0].innerHTML = body;
}