//função para mudar o select de marca ao escolher tipo
    function changeMarca(){

        var select = document.getElementById('tipo-patrimonio');
        var selectSetor = document.getElementById('marca-patrimonio');

        var value = select.options[select.selectedIndex].value;

        //remove itens
        var length = selectSetor.options.length;        
        var i;
        for(i = selectSetor.options.length-1 ; i>=0 ; i--)
        {
            selectSetor.remove(i);
        }


        if(value == 'computadores') {

            var option = document.createElement('option');
            option.value = '1';
            option.text = 'HP';

            var option2 = document.createElement('option');
            option2.value = '2';
            option2.text = 'DELL';

            var option3 = document.createElement('option');
            option3.value = '3';
            option3.text = 'SONNY';


            selectSetor.add(option);
            selectSetor.add(option2);
            selectSetor.add(option3);

        } else if (value == 'impressoras'){

            var option4 = document.createElement('option');
            option4.value = '4';
            option4.text = 'SAMSUNG';

            var option5 = document.createElement('option');
            option5.value = '5';
            option5.text = 'BROTHER';

            selectSetor.add(option4);
            selectSetor.add(option5);

        }   
    }

// end function


// função para alterar modelo ao escolher marca


function changeModelo(){

	var select = document.getElementById('marca-patrimonio');

	var selectModelo = document.getElementById('modelo-patrimonio');

	var value = select.options[select.selectedIndex].value;

	//remove itens

	var length = selectModelo.options.length;
	var i;
	for(i = selectModelo.options.length-1 ; i>=0; i--){
		selectModelo.remove(i);
	}

	if(value == '1'){

		var option6 = document.createElement('option');
		option6.value = '6';
		option6.text = 'i3 - HD 500';

		var option7 = document.createElement('option');
		option7.value = '7';
		option7.text = 'i5 - HD 1TB';

		var option8 = document.createElement('option');
		option8.value = '8';
		option8.text = 'i7 - HD 2TB';

		selectModelo.add(option6);
        selectModelo.add(option7);
        selectModelo.add(option8);


	}

}


function changeTombo(){

	var select = document.getElementById('modelo-patrimonio');

	var selectTombo = document.getElementById('tombo-patrimonio');

	var value = select.options[select.selectedIndex].value;

	//remove itens

	var length = selectTombo.options.length;
	var i;
	for(i = selectTombo.options.length-1 ; i>=0; i--){
		selectTombo.remove(i);
	}


	if(value == '6'){

		var option9 = document.createElement('option');
		option9.value = '9';
		option9.text = '152014';

        selectTombo.add(option9);
	}

	else if(value == '7'){
		var option10 = document.createElement('option');
		option10.value = '10';
		option10.text = '302502';
		selectTombo.add(option10);

	}


}
