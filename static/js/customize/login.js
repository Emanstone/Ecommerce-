// Frontend communication
$(window).on('load', function () {

    $('#loader2').fadeIn('show', function () {
        $('#maincontent').fadeIn('show');
        //delay the excution by  1 sec
        setTimeout(function () {
            $('#loader2').hide()

        }, 1500)

    })

})


// // NORMAL MESSAGE CODE
$(document).ready(function () {
    $("#form-l").on('submit', function (event) {
        event.preventDefault();
        const $forms = $(this);
        const $spinner = $('#spin');
        const $btnsubmit = $('#btnsubmit');
        const $login = $('#login');
        const $message = $('#message');
        $btnsubmit.prop('disabled', true)
        $login.text('processing...')
        $spinner.show()


        // Now use ajax to communicate with the views
        $.ajax({
            type: 'POST',
            url: '/login/',
            data: $forms.serialize(),
            datatype: 'json',


            success: function (event) {
                if (event.home) {          // Check if the response has a "home" property
                  $message
                    .removeClass('alert-danger')
                    .addClass('alert-success')
                    .text(event.home)
                    .show();
                  setTimeout(function(){
                    window.location = "/";
                  }, 3000);
                } 
            },




            error: function (e) {
                if (e.responseJSON.email || e.responseJSON.password) {
                    $message.removeClass('alert-success')
                        .addClass('alert-danger')
                        .text(e.responseJSON.email)
                        .show();
                    $btnsubmit.prop('disabled', false)
                    $spinner.hide()
                    $login.text('Login')

                }


                if (e.responseJSON.password || e.responseJSON.email) {
                    $message.removeClass('alert-success')
                        .addClass('alert-danger')
                        .text(e.responseJSON.password)
                        .show();
                    $btnsubmit.prop('disabled', false)
                    $spinner.hide()
                    $login.text('Login')

                }


                if (e.responseJSON.invalid) {
                    $message.removeClass('alert-success')
                        .addClass('alert-danger')
                        .text(e.responseJSON.invalid)
                        .show();
                    $btnsubmit.prop('disabled', false)
                    $spinner.hide()
                    $login.text('Login')

                }


                if (e.responseJSON.reverify) {
                    $message.removeClass('alert-success')
                        .addClass('alert-danger')
                        .text(e.responseJSON.reverify)
                        .show();
                    setTimeout(function(){
                        window.location = "/reverify/";
                        $btnsubmit.prop('disabled', false)
                        $spinner.hide()
                        $login.text('Login')      
                    }, 3000)

                }


                if (e.responseJSON.signup) {
                    $message.removeClass('alert-success')
                        .addClass('alert-danger')
                        .text(e.responseJSON.signup)
                        .show();
                    setTimeout(function(){
                        window.location = "/signup/";
                        $btnsubmit.prop('disabled', false)
                        $spinner.hide()
                        $login.text('Login')      
                    }, 3000)

                }
                // console.log(e.responseJSON)
            },    

        });    


    });

})







// // DOT ANIME CODE
// $(document).ready(function () {
//     $("#form-l").on('submit', function (event) {
//         event.preventDefault();
//         const $forms = $(this);
//         const $spinner = $('#spin');
//         const $btnsubmit = $('#btnsubmit');
//         const $login = $('#login');
//         const $message = $('#message');
//         $btnsubmit.prop('disabled', true)
//         $login.text('processing...')
//         $spinner.show()


//         // Now use ajax to communicate with the views
//         $.ajax({
//             type: 'POST',
//             url: '/login/',
//             data: $forms.serialize(),
//             dataType: 'json',


//             success: function (event) {
//                 if (event.home) {          // Check if the response has a "home" property
//                     $message
//                         .removeClass('alert-danger')
//                         .addClass('alert-success')
//                         .text(event.home)
//                         .show();

//                     // Start of Dot Anime Here ***
//                     let dots = "";
//                     const intervalId = setInterval(function () {
//                         dots += "●";  
//                         $message.text(event.home + dots.split('').join('\u00A0'));   // ('\u00A0') is for spacing

//                         if (dots.length === 5) {
//                             clearInterval(intervalId);   // End of Dot Anime ***

//                             setTimeout(function () {
//                                 window.location.href = "/";
//                                 // window.location = "/";
//                             }, 1500);
//                         }

//                     }, 800);    // Dot Anime timing interval***      
//                 }
//             },


//             error: function (e) {
//                 if (e.responseJSON.email || e.responseJSON.password) {
//                     $message.removeClass('alert-success')
//                         .addClass('alert-danger')
//                         .text(e.responseJSON.email)
//                         .show();
//                     $btnsubmit.prop('disabled', false)
//                     $spinner.hide()
//                     $login.text('Login')

//                 }


//                 if (e.responseJSON.password || e.responseJSON.email) {
//                     $message.removeClass('alert-success')
//                         .addClass('alert-danger')
//                         .text(e.responseJSON.password)
//                         .show();
//                     $btnsubmit.prop('disabled', false)
//                     $spinner.hide()
//                     $login.text('Login')

//                 }


//                 if (e.responseJSON.invalid) {
//                     $message.removeClass('alert-success')
//                         .addClass('alert-danger')
//                         .text(e.responseJSON.invalid)
//                         .show();
//                     $btnsubmit.prop('disabled', false)
//                     $spinner.hide()
//                     $login.text('Login')

//                 }


//                 if (e.responseJSON.reverify) {
//                     $message.removeClass('alert-success')
//                         .addClass('alert-danger')
//                         .text(e.responseJSON.reverify)
//                         .show();
//                     setTimeout(function () {
//                         window.location = "/reverify/";
//                         $btnsubmit.prop('disabled', false)
//                         $spinner.hide()
//                         $login.text('Login')
//                     }, 3000)

//                 }


//                 if (e.responseJSON.signup) {
//                     $message.removeClass('alert-success')
//                         .addClass('alert-danger')
//                         .text(e.responseJSON.signup)
//                         .show();
//                     // Start of Dot Anime Here ***
//                     let dots = "";
//                     const intervalId = setInterval(function () {
//                         dots += "●";                       
//                         $message.text(e.responseJSON.signup + dots.split('').join('\u00A0')); // ('\u00A0') is for spacing

//                         if (dots.length === 5) {
//                             clearInterval(intervalId);   // End of Dot Anime ***

//                             setTimeout(function () {
//                                 window.location.href = "/signup/";
//                                 $btnsubmit.prop('disabled', false)
//                                 $spinner.hide()
//                                 $login.text('Login')
//                             }, 1500);
//                         }

//                     }, 800);    // Dot Anime timing interval***      
//                 }
//             },

//         });

//     });

// })
