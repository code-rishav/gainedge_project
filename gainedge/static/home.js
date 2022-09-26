var close = document.getElementById("close");
close.addEventListenser("click",function(event){
    $.ajax({
        type: "POST",
        url: '{{ 'my-ajax-test/' }}'
    });
})

