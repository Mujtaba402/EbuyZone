$(document).ready(function(event){


        $('.reply-btn').click(function() {
          $(this).parent().parent().next('.replied-comments').fadeToggle("slow");
        });

        $(document).on('submit', '.comment-form', function(event){
          event.preventDefault();
          $.ajax({
            type: 'POST',
            url: $(this).attr('action'),
            data: $(this).serialize(),
            dataType: 'json',
            success: function(response){
              $('.main-comment-section').html(response['form']);
              $('textarea').val('');
              $('.reply-btn').click(function() {
              $(this).parent().parent().next('.replied-comments').fadeToggle();
              $('textarea').val('');
              });
            },
            error: function(rs, e){
              console.log(rs.responseText);
            },
          });
        });

        $(document).on('submit', '.reply-form', function(event){
          event.preventDefault();
          $.ajax({
            type: 'POST',
            url: $(this).attr('action'),
            data: $(this).serialize(),
            dataType: 'json',
            success: function(response){
              $('.main-comment-section').html(response['form']);
              $('textarea').val('');
              $('.reply-btn').click(function() {
              $(this).parent().parent().next('.replied-comments').fadeToggle();
              $('textarea').val('');
              });
            },
            error: function(rs, e){
              console.log(rs.responseText);
            },
          });
        });


      $(document).on('click', '#like', function(event){
        event.preventDefault();
        var pk = $(this).attr('value');
        $.ajax({
          type: 'POST',
          url: '{% url "like_post" %}',
          data: {'id':pk, 'csrfmiddlewaretoken': '{{ csrf_token }}'},
          dataType: 'json',
          success: function(response){
            $('#like-section').html(response['form']);
            console.log($('#like-section').html(response['form']));
          },
          error: function(rs, e){
            console.log(rs.responseText);
          },
        });
      });



    });