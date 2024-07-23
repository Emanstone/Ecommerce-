
// Frontend communication
$(window).on('load', function () {

    $('#loader').fadeIn('show', function () {
        $('#maincontent').fadeIn('show');
        //delay the excution by  1 sec
        setTimeout(function () {
            $('#loader').hide()

        }, 1500)

    })

})



$(document).ready(function () {
    $("#form").on('submit', function (event) {
        event.preventDefault();
        // $("#loader").show()
        const $forms = $(this);    // get all the instances of the form
        const $spinner = $('#spin');  // spin id by the submit button
        const $btnsubmit = $('#btnsubmit');    // button id
        const $signup = $('#signup');    // button text id
        const $message = $('#message');    // message id
        $btnsubmit.prop('disabled', true)  // button disabled on processing submission data
        $signup.text('processing...')    // button text changes to 'processing..' on submission mode
        $spinner.show()  // display the spinner on submission mode 
        // const csrftoken = $(["name=csrfmiddlewaretoken"])  // commented cos we already have csrf on the form
        // console.log($forms)



        // Now use ajax to communicate with the views
        $.ajax({
            type: 'POST',
            url: '/signup/',
            data: $forms.serialize(),
            datatype: 'json',

            success: function (event) {
                $message
                    .removeClass('alert-danger')
                    .addClass('alert-success')
                    .text(event.verify)
                    .show();
                   setTimeout(function(){
                      window.location = "/verify/"

                   }, 2000)
                
                // console.log(e)    // to log the error on console

            },


            error: function (e) {
                if (e.responseJSON.email) {
                    $message.removeClass('alert-success')
                        .addClass('alert-danger')
                        .text(e.responseJSON.email)
                        .show();
                    $btnsubmit.prop('disabled', false)
                    $spinner.hide()
                    $signup.text('Signup')

                }


                if (e.responseJSON.username) {
                    $message.removeClass('alert-success')
                        .addClass('alert-danger')
                        .text(e.responseJSON.username)
                        .show();
                    $btnsubmit.prop('disabled', false)
                    $spinner.hide()
                    $signup.text('Signup')

                }


                if (e.responseJSON.first_name) {
                    $message.removeClass('alert-success')
                        .addClass('alert-danger')
                        .text(e.responseJSON.first_name)
                        .show();
                    $btnsubmit.prop('disabled', false)
                    $spinner.hide()
                    $signup.text('Signup')

                }


                if (e.responseJSON.lastname) {
                    $message.removeClass('alert-success')
                        .addClass('alert-danger')
                        .text(e.responseJSON.lastname)
                        .show();
                    $btnsubmit.prop('disabled', false)
                    $spinner.hide()
                    $signup.text('Signup')

                }


                if (e.responseJSON.email_exist) {
                    $message.removeClass('alert-success')
                        .addClass('alert-danger')
                        .text(e.responseJSON.email_exist)
                        .show();
                    $btnsubmit.prop('disabled', false)
                    $spinner.hide()
                    $signup.text('Signup')

                }


                if (e.responseJSON.username_exist) {
                    $message.removeClass('alert-success')
                        .addClass('alert-danger')
                        .text(e.responseJSON.username_exist)
                        .show();
                    $btnsubmit.prop('disabled', false)
                    $spinner.hide()
                    $signup.text('Signup')

                }


                if (e.responseJSON.signup) {
                    $message.removeClass('alert-success')
                        .addClass('alert-danger')
                        .text(e.responseJSON.signup)
                        .show();
                    $btnsubmit.prop('disabled', false)
                    $spinner.hide()
                    $signup.text('Signup')

                }

                // console.log(e)  // to log the error on console
                // console.log(e.responseJSON)
            }


        });

    });

})
