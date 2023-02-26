var updateBtns = document.getElementsByClassName('update-cart')

for(var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click',function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:', productId, 'action:', action)

        console.log('USER:', user,)
        if(user == 'AnonymousUser'){
            console.log('Not Logged in')
        }
        else{
            updateUserOrder(productId, action)
        }
    })
}


function updateUserOrder(productId, action){
    console.log('User is Logged in. Wait..')

    var url = '/update_item/' //this is where data is sent

    fetch(url, {  //sets the url
        method:'POST',
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'productId': productId, 'action':action}) //data sent to the backend
    })

    .then((response) =>{ //get the response
        return response.json()
    })

    .then((data) =>{
        console.log('data',data) //consoling the data from the response
        location.reload()
    })
}