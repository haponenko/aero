function validate_form(form)
{
	var value_firstname = form.id_firstname.value;
	var value_surname = form.id_surname.value;
	var value_email = form.id_email.value;
	var value_country_out = form.id_country_out.value;
	var value_country_in = form.id_country_in.value;
    var value_state_out = form.id_state_out.value;
	var value_state_in = form.id_state_in.value;
	var value_city_out = form.id_city_out.value;
	var value_city_in = form.id_city_in.value;
    var value_date_out = form.id_date_out.value;
	var value_date_in = form.id_date_in.value;

	if(value_firstname == "")
	{
		alert("Please enter firstname.");
		form.id_firstname.focus();
		return false;
	}

	if(value_surname == "")
	{
		alert("Please enter surname.");
		form.id_surname.focus();
		return false;
	}
	if(value_email == "")
	{
		alert("Please enter email.");
		form.id_email.focus();
		return false;
	}
    if(value_country_out == "")
	{
		alert("Please enter country To whence.");
		form.id_country_out.focus();
		return false;
	}
    if(value_country_in == "")
	{
		alert("Please enter country To where.");
		form.id_country_in.focus();
		return false;
	}
    //------------------------------
    if((value_state_out == "")||(value_state_out == "Select Region"))
	{
		alert("Please enter state To whence.");
		form.id_state_out.focus();
		return false;
	}
    if((value_state_in == "")||(value_state_in == "Select Region"))
	{
		alert("Please enter state To where.");
		form.id_state_in.focus();
		return false;
	}
    //------------------------------
    if((value_city_out == "")||(value_city_out == "Select City"))
	{
		alert("Please enter city in To whence.");
		form.id_city_out.focus();
		return false;
	}
    if((value_city_in == "")||(value_city_in == "Select City"))
	{
		alert("Please enter city in To where.");
		form.id_city_in.focus();
		return false;
	}
    if(value_date_out == "")
	{
		alert("Please enter Leaving date.");
		form.id_date_in.focus();
		return false;
	}
    if(value_date_in == "")
	{
		alert("Please enter Return date.");
		form.id_date_in.focus();
		return false;
	}

	var reg_name = /^([A-Za-z]){1,}$/;
	var reg_email = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;
    var reg_date = /^([0-9]{4})\-(0[1-9]|1[0-2])\-(0[1-9]|[1-2][0-9]|3[0-1])$/;

	if(reg_name.test(value_firstname) == false)
	{
		alert("Please enter a valid firstname.");
		form.id_firstname.focus();
		return false;
	}
    if(reg_name.test(value_surname) == false)
	{
		alert("Please enter a valid surname.");
		form.id_surname.focus();
		return false;
	}
    if(reg_email.test(value_email) == false)
	{
		alert("Please enter a valid email.");
		form.id_email.focus();
		return false;
	}

    if(reg_date.test(value_date_out) == false)
	{
		alert("Please enter a Leaving date.");
		form.id_date_out.focus();
		return false;
	}
    if(reg_date.test(value_date_in) == false)
	{
		alert("Please enter a Return date.");
		form.id_date_in.focus();
		return false;
	}

}



