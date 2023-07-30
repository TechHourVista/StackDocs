$( ".btn-primary" ).click(
    function() {

      const usr_id = $(this).data('user-id');
      const usr_name = $(this).data('user-name');

      $.ajax
        (
           {
            url: "add_friend",
            method : 'POST',
            data : 
            {
                usr_id:usr_id,
                usr_name :usr_name
            },

            success:function (respons)
            {
              if(respons.Error == true)
                {
                    console.log(respons.messge);
                    //do somthing if we have an error
                    //window.location.reload();

                }
                else
                {
                    //do somthing if we have't an error
                    // Find the button with the matching user ID and remove it
                    
                };
            },
           
           }
        )




  } 
  );


  $( ".btn-primary" ).click(
    function() {

      const usr_id = $(this).data('user-id');
      const usr_name = $(this).data('user-name');

      $.ajax
        (
           {
            url: "add_friend",
            method : 'POST',
            data : 
            {
                usr_id:usr_id,
                usr_name :usr_name
            },

            success:function (respons)
            {
              console.log(respons)
            },
           
           }
        )




  } 
  );




