$(document).ready(function () {
		    let $updateForm= $('.updateform');
            //edit link function that brings data from the table and fill the edit form
			$('.edite_link').click(function (e) {
				e.preventDefault();
				let $this = $(this);
				let $elem = $this.parent().closest('.user_data_section');
				$updateForm.attr('action',$this.attr('href'),'data-id',$elem.attr('data-id'));
				//iterating the table data
				$elem.find('td').not('.ed_object').each(function () {
					let $element = $updateForm.find('[name="'+$(this).attr('data-element')+'"]');
					//check the table data type if it is select then it should be selected with id
					if ($element.is("select")){
					    $element.val($(this).attr('data-select'))
					}else{
					    $element.val($(this).text())
					}
                })
            });
			//update form on submit with ajax
			$updateForm.submit(function (e) {
                e.preventDefault();
                let $this = $(this);
				$.ajax({
			        url: $this.attr('action'),
					data: $this.serialize(),
					type: 'post',
			        dataType: 'json',
			        success: function (data) {
			            //sweetalert function
				        Swal.fire({
						  icon: 'success',
						  title: 'YAY',
						  text: 'Student Has Been Updated',
						});
				        //returning the data from the backend and replace the old data with the new one
				        let $elemData = eval(data.data)[0];
				        let $elem = $('.user_data_section[data-id="'+$elemData.pk+'"]');
				        $.each($elemData.fields, function(key,valueObj){
				            if(key !=="speciality"){
				                $elem.find('[data-element="'+key+'"]').html(valueObj);
                            }else{
				                $elem.find('[data-element="'+key+'"]').attr('data-select',valueObj).html(data.sepciality)
                            }
                        });
			        },error:function (data) {
			            //sweetalert error message
						Swal.fire({
						  icon: 'error',
						  title: 'OOH!',
						  text: 'sorry an error occured try again later',
						});
                    }
				});
            });

			//delete link with ajax
			$('.delete_link').click(function (e) {
				e.preventDefault();
				let $this = $(this);
				$.ajax({
			        url: $this.attr('href'),
					data: '',
					type: 'post',
			        dataType: 'json',
			        success: function (data) {
			          //removing element from the DOM so it can no longer be visible to the user
			          $this.parent().closest('.user_data_section').remove();
				        Swal.fire({
						  icon: 'success',
						  title: 'YAY',
						  text: 'Student Has Been Deleted',
						})
			        },error:function (data) {
						//sweetalert error message
						Swal.fire({
						  icon: 'error',
						  title: 'OOH!',
						  text: 'sorry an error occured try again later',
						});
                    }
				});
            });

});
