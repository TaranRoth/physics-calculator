function loadHistoryItem(time) {
    $.ajax({
        type: "POST",
        url: window.location.href,
        data: {time:time},
        success: (data) => {
            console.log(JSON.parse(data)["url"]);
            window.location.href = JSON.parse(data)["url"];
        }
    });
}