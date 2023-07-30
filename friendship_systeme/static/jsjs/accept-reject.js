//$(".btn").removeAttribute("data-user-id");
$(".btn-primary").click(
    function() {

        const usr_id = $(this).data('user-id');


      $.ajax
        (
           {
            url: "accept",
            method : 'POST',
            data : 
            {
                usr_id:usr_id,
                
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
                    //do somthing if we have't an error from the server

                };

            },
           
           }
        )




  } 
  );




$(".btn-danger").click(
function()
{
    const usr_id = $(this).data('user-id');
    

    $.ajax
    (
        {
            url: "reject",
            method: "POST",
            data:
            {
                usr_id:usr_id,
                

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
                    
                };
            
            },

        }
    );
}




);

