function ncf_submit() {
    console.log("ncf_submit()");
    var form = document.getElementsByClassName("ncf-client-form")[0];
    var xhr = new XMLHttpRequest();
    var url = "http://192.168.137.1:8000/create-client-form/";
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-type", "application/json");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var json = JSON.parse(xhr.responseText);
            console.log(json);
        }
    };
    var data = JSON.stringify({
        "name": form.getElementsByName("client_name"),
        "short_name": form.client_short,
        "uid": form.client_id,
        "code": form.client_code,
        "category": form.client_category,
        "type": form.client_type,
        "level": form.client_level,
        "currency": form.client_currency,
        "tel": form.client_tel,
        "website": form.client_website,
        "parent": form.client_parent,
        "area": form.client_area,
        "employees": form.client_employees,
        "revenue": form.client_revenue,
        "description": form.client_description,
        "owner": form.client_owner
    });
    xhr.send(data);
}