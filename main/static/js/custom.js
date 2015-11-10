$('#search').on('keyup', function(e) {
    $.ajax({
        type: "GET",
        url: "/searcher/",
        data: {
            search: $('#search').val(),
        },
        error: function() {console.log("Boo hiss")}, 
        success: function(data) {
            console.log(data.length);
            $('#thestates').html("");
            if (data.length == 0) {
                $('#thestates').append('<h3 style="text-align: center">Sorry, no states found! Try again</h3>');
            } else {
                for (i=0; i< data.length; i++) {
                    $('#thestates').append('<h2 style="text-align: center"><a href="/state_detail/' + data[i]['state_pk'] + '/">' + data[i]['name'] + '</a><br><small><a href="/capital_detail/' + data[i]['cap_pk'] + '/">' + data[i]['capital'] + '</a></small></h2><a href="/state_detail/' + data[i]['state_pk'] + '/" class="btn btn-default btn-lg">More Details</a><hr>') 
                }
            }
        } 

    });
});

// $('#state_list').on('click', function(event) {
//     $('#state_list').append('<li>extra element</li>');
// });
