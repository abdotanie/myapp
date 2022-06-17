$('#add_con').click(function(){
       const city1 =document.getElementById('city1').value
       const city2 =document.getElementById('city2').value
       const connect =document.getElementById('connect').value
        console.log('click')
        
        $.ajax({
            url:'',
            type:'get',
            data:{
                'add_con':'add_con',
                'city1': city1,
                'city2': city2
               ,'connect':connect
            },
             success:function(response){ 
               console.log(response)
            }
        }
        )   
        document.getElementById('city1').value=''
        document.getElementById('city2').value=''
        document.getElementById('connect').value='' 
        document.getElementById('add_con_out').value='Connect Added'
    }
    );
$('#add_inf').click(function(){
        console.log('add_inf save')
        const city_inf =document.getElementById('city_inf').value
        const Inference =document.getElementById('Inference').value
        $.ajax({
            url:'',
            type:'get',
            data:{
                'add_inf' :'add_inf',
                 'city_inf': city_inf,
                 'Inference': Inference

            },
             success:function(response){
                console.log(response)
            }
        }
        )
        document.getElementById('city_inf').value=''
        document.getElementById('Inference').value='' 
        document.getElementById('add_inf_out').value='Inference Added'
    }
    );
$('#showbtn').click(function(){
        console.log('add_inf save')
        console.log('ho ho ho')
        const start =document.getElementById('start').value
        const end =document.getElementById('end').value
        $.ajax({
            url:'',
            type:'get',
            data:{
                'showbtn' :'showbtn',
                 'start': start,
                 'end': end
            },
             success:function(response){
                document.getElementById('path_out').value=response.result
            }
        }
        )
        document.getElementById('start').value=''
        document.getElementById('end').value='' 
    }
    ); 
