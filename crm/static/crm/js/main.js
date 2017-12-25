function client() {
    console.log("client()");
    var xhr = new XMLHttpRequest();
    var url = "http://localhost:8000/";
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-type", "application/json");
    var data = JSON.stringify({
        "page": "client"
    });
    xhr.send(data);
}