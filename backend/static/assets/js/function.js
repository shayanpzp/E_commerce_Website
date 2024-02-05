


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
    $(".filter-checkbox, #price-filter-btn").on("click" , function(){
        console.log("A check box has clicked")

        let filter_object = {}

        let min_price = $("#max_price").attr("min")
        let max_price = $("#max_price").val()

        filter_object.min_price = min_price;
        filter_object.max_price = max_price;

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
    $("#max_price").on("blur", function(){
        let min_price = $(this).attr("min")
        let max_price = $(this).attr("max")
        let current_price = $(this).val()

        console.log("Current Price is:" , current_price);
        console.log("Max Price is:" , max_price);
        console.log("min Price is:" , min_price);


        if(current_price < parseInt(min_price) || current_price > parseInt(max_price)){
            console.log("Price Error");
            min_price = Math.round(min_price * 100) / 100
            max_price = Math.round(max_price * 100) / 100


            console.log("##################################")
            console.log("min price is : ", min_price);
            console.log("Max price is : ", max_price);


            alert("قیمت باید بین: " + min_price + "  و  " + max_price)
            $(this).val(min_price)
            $('#range').val(min_price)
            $(this).focus()
            

            return false
        }
    })
})



$("#add-to-cart-btn").on("click",function(){

    let this_val = $(this)
    let index = this_val.attr("data-index")

    let quantity = $("#product-quantity-" + index).val()
    let product_title = $(".product-title-" + index).val()
    let product_id = $(".product-id-" + index).val()
    let prodcut_price = $("#current-product-price-" + index).text()
    let prodcut_pid = $("#product-pid-" + index).val()
    let prodcut_image = $("#product-image-" + index).val()
    


    $.ajax({
        url:'/add-to-cart',
        data: {
            'id' : product_id,
            'pid' : product_pid,
            'image' : prodcut_image,
            'qty':quantity,
            'title':product_title,
            'price' : prodcut_price,
        },
        dataType:'json',
        beforeSend:function(){
            console.log("Adding product to cart...");
        },
        success:function(response){
            this_val.html("Item added to cart")
            console.log("Added product to cart ! ");
            $(".cart-items-count").text(response.totalcartitems)
        }
    })
})






// $("#add-to-cart-btn").on("click",function(){
//     let quantity = $("#product-quantity").val()
//     let product_title = $(".product-title").val()
//     let product_id = $(".product-id").val()
//     let prodcut_price = $("#current-product-price").text()
//     let this_val = $(this)


//     $.ajax({
//         url:'/add-to-cart',
//         data: {
//             'id' : product_id,
//             'qty':quantity,
//             'title':product_title,
//             'price' : prodcut_price,
//         },
//         dataType:'json',
//         beforeSend:function(){
//             console.log("Adding product to cart...");
//         },
//         success:function(response){
//             this_val.html("Item added to cart")
//             console.log("Added product to cart ! ");
//             $(".cart-items-count").text(response.totalcartitems)
//         }
//     })
// })