function download(filename, text) {
    var current_date = new Date();
    var current_time = current_date.getTime();
    var element = document.createElement('a');
    element.setAttribute('href', 'data:text/csv;charset=utf-8,' + encodeURIComponent(text));
    element.setAttribute('download', current_time + '_' + filename);

    element.style.display = 'none';
    document.body.appendChild(element);

    element.click();

    document.body.removeChild(element);
}

function ShowLoading(disable_input=false) {
    if (disable_input) {
        var file_file = document.querySelector('#formFile');
        file_file.setAttribute('disabled', 'disabled');
    }

    var submit_btn = document.querySelector('#CrawlBtn');
    submit_btn.setAttribute('disabled', 'disabled');
    submit_btn.value = "Crawling...";
}

function RemoveLoading() {
    var submit_btn = document.querySelector('#CrawlBtn');
    var file_file = document.querySelector('#formFile');
    file_file.removeAttribute('disabled');
    submit_btn.removeAttribute('disabled');
    submit_btn.value = "Start Crawling";
}

async function fetchCards(api_url) {
    const response = await fetch(api_url);
    var data = await response.json();
    if (data.cards_datatable !== null) {
        clearInterval(interval);
        var changeList = document.getElementById("changelist");
        changeList.innerHTML = data.cards_datatable;

        RemoveLoading();

        var ext_btn = document.getElementById("Extract");

        if (ext_btn) {
            ext_btn.addEventListener("click", function () {
                var cards_info = document.querySelectorAll('tr.card_info');
                var gift_cards = "";
                cards_info.forEach(function (card_info) {
                    gift_cards += '="' + card_info.querySelector('.card_number').textContent + '"';
                    gift_cards += ',="' + card_info.querySelector('.serial_number').textContent + '"';
                    gift_cards += "\n";
                });
                var filename = "cards.csv";
                download(filename, gift_cards);
            }, false);
        }
    }
}