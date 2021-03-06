function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Sends the data (the transactions) that a user has written in the textarea to the server.
// Then waits for the response and shows the results.
// TODO: What if the request fails?
$(document).ready(function () {
    $("#solve").click(function () {
        const csrftoken = getCookie('csrftoken');
        $.ajax({
            url: "/solve/",
            type: "POST",
            headers: { "X-CSRFToken": csrftoken },
            data: JSON.stringify({
                'transactions': $("#transactions").val()
            }),
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            success: function (result) {
                $("#results").html(result.debts.replace(/(?:\r\n|\r|\n)/g,"<br />"));
            }
        });
    });
});