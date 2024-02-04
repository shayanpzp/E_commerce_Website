


const monthNames = ["Jan","Feb","Mar","April","May","June",
    "July","Aug","Sept","Oct","Nov","Dec"
];

$("#commentForm").submit(function(e){
    e.preventDefault();

    let dt = new Date();
    let time = dt.getDate() + " " + monthNames[dt.getUTCMonth] + ", " + dt.getFullYear()


    $.ajax({
        data : $(this).serialize(),

        method: $(this).attr("method"),

        url: $(this).attr("action"),

        dataType: "json",

        success: function(response){
            console.log("Comment Saved to DB...");

            
            if(response.bool == true){
                $("#review-res").html("نظر شما با موفقیت ثبت شد.")
                $(".hide-comment-form").hide()
                $(".add-review").hide()


                let _html = '<div class="single-comment justify-content-between d-flex mb-30">'
                    _html += '<div class="user justify-content-between d-flex">'
                    _html += '<div class="thumb text-center">'
                    _html += '<img src="https://static.vecteezy.com/system/resources/previews/020/765/399/non_2x/default-profile-account-unknown-icon-black-silhouette-free-vector.jpg" alt="">'
                    _html += '<a href="#" class="font-heading text-brand">'+ response.context.user +'</a>'
                    _html += '</div>'

                    _html += '<div class="desc">'
                    _html += '<div class="d-flex justify-content-between mb-10">'
                    _html += '<div class="d-flex align-items-center">'
                    _html += '<span class="font-xs text-muted">'+ time +'</span>'
                    _html += '</div>'

                    for(let i = 1; i<=response.context.rating; i++){
                        _html += '<i class="fas fa-star text-warning"></i>';
                    }

                    _html += '</div>'
                    _html += '<p class="mb-10">'+ response.context.review +'</p>'

                    _html += '</div>'                 
                    _html += '</div>'              
                    _html += '</div>'

                    $(".comment-list").prepend(_html)
            }

            
        }
    })
})



$(document).ready(function (){
    $(".filter-checkbox").on("click" , function(){
        console.log("A check box has clicked")

        let filter_object = {}

        $(".filter-checkbox").each(function(){
            let filter_value = $(this).val()
            let filter_key = $(this).data("filter")

            console.log("fliter value is:", filter_value);
            console.log("fliter key is:", filter_key);


            filter_object[filter_key] = Array.from(document.querySelectorAll('input[data-filter='+ filter_key +']:checked')).map(function(element){
                return element.value
            })
        })
        console.log("Filter Object is : ", filter_object);
        $.ajax({
            url:'/filter-products',
            data: filter_object,
            dataType:'json',
            beforeSend:function(){
                console.log("Trying to filter product...");
            },
            success:function(response){
                console.log(response);
                console.log("Data filtered successfully...");
                $("#filtered-product").html(response.data)
            }
        })
    })
})